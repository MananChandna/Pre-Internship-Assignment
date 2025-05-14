import re, csv
def extract_data(logfile):
    data = []
    with open(logfile, 'r') as f:
        for line in f:
            m = re.match(r'(\S+) - - \[(.*?)\] "(\S+) (.*?) HTTP/\d\.\d" (\d{3}) (\d+)', line)
            if m:
                data.append({
                    'IP': m.group(1),
                    'Timestamp': m.group(2),
                    'Request':   m.group(3) + ' ' + m.group(4),
                    'Status':    m.group(5)
                })
    return data
