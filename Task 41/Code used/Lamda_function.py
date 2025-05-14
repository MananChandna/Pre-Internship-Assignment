import json
import os
import urllib.request
from datetime import datetime, timedelta
import boto3

NEWS_API_KEY = os.environ['NEWS_API_KEY']
FIREHOSE_STREAM_NAME = os.environ['FIREHOSE_STREAM_NAME']

def lambda_handler(event, context):

    today = datetime.utcnow().strftime('%Y-%m-%d')
    seven_days_ago = (datetime.utcnow() - timedelta(days=7)).strftime('%Y-%m-%d')

    NEWS_ENDPOINT = (
        f"https://newsapi.org/v2/everything?"
        f"q=Apple&"
        f"from={seven_days_ago}&"
        f"to={today}&"
        f"sortBy=popularity&"
        f"language=en&"
        f"pageSize=10"
    )

    req = urllib.request.Request(NEWS_ENDPOINT)
    req.add_header("Authorization", NEWS_API_KEY)

    try:
        with urllib.request.urlopen(req) as response:
            raw_data = response.read().decode("utf-8")
            print(f"API Raw Response: {raw_data}")
            data = json.loads(raw_data)
    except Exception as e:
        print(f"API call failed: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'status': 'error', 'message': 'API request failed'})
        }

    articles = data.get("articles", [])
    if not articles:
        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'ok', 'message': 'No articles found'})
        }

    firehose = boto3.client('firehose')

    for article in articles:
        payload = {
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url"),
            "publishedAt": article.get("publishedAt"),
            "source": article.get("source", {}).get("name")
        }

        firehose.put_record(
            DeliveryStreamName=FIREHOSE_STREAM_NAME,
            Record={'Data': json.dumps(payload) + '\n'}
        )

    return {
        'statusCode': 200,
        'body': json.dumps({'status': 'success', 'articles_sent': len(articles)})
    }
