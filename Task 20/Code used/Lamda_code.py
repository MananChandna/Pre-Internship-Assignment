import boto3
import pandas as pd
import io

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']
    destination_bucket = source_bucket
    destination_key = f"cleaned/{source_key.split('/')[-1]}"

    try:
        
        response = s3.get_object(Bucket=source_bucket, Key=source_key)
        df = pd.read_csv(io.BytesIO(response['Body'].read()))
        df.drop_duplicates(inplace=True)
        df.dropna(how='all', inplace=True)
        df.fillna(method='ffill', inplace=True)
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        buffer = io.StringIO()
        df.to_csv(buffer, index=False)
        buffer.seek(0)
        s3.put_object(Bucket=destination_bucket, Key=destination_key, Body=buffer.getvalue())

        return {
            'statusCode': 200,
            'body': f'Successfully cleaned and uploaded to {destination_key}'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error processing file: {str(e)}'
        }
