import re
import pandas as pd

log_file_path = ""C:\Users\Manan\Downloads\Unstructured_SSH_logfile.log""
output_csv_path = "structured_logs.csv"

pattern = re.compile(
    r'(?P<Month>\w{3})\s+'            
    r'(?P<Date>\d{1,2})\s+'           
    r'(?P<Time>\d{2}:\d{2}:\d{2})\s+' 
    r'(?P<Host>\S+)\s+'               
    r'(?P<ComponentName>\w+)\[(?P<PID>\d+)\]:\s+'  
    r'(?P<Content>.*)'                
)

rows = []
with open(log_file_path, 'r') as f:
    for line in f:
        m = pattern.match(line)
        if not m:
            continue
        data = m.groupdict()

        
        content = data['Content']
        sub_match = re.search(r'(\w+)\(', content)
        subcomponent = sub_match.group(1) if sub_match else data['ComponentName']
        data['Component'] = f"{data['ComponentName']}({subcomponent})"

        # Static Level column
        data['Level'] = 'combo'
        rows.append(data)

df = pd.DataFrame(rows)

df.insert(0, 'LineId', range(1, len(df) + 1))

unique_contents = df['Content'].unique()
event_id_map = {content: f"E{idx+1:03d}" for idx, content in enumerate(unique_contents)}
df['EventId'] = df['Content'].map(event_id_map)

df['EventTemplate'] = df['Content']

df_structured = df[['LineId', 'Month', 'Date', 'Time', 'Level',
                    'Component', 'PID', 'Content', 'EventId', 'EventTemplate']]

df_structured.to_csv(output_csv_path, index=False)

print(f"Structured logs written to {output_csv_path}")
