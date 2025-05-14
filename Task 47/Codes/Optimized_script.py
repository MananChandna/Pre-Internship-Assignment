import re, csv
with open('log.txt','r') as fin, open('out.csv','w', newline='') as fout:
    writer = csv.writer(fout)
    writer.writerow(['IP','Timestamp','Request','Status'])
    ip_counts = {}
    for line in fin:
        m = re.match(r'(\S+) - - \[(.*?)\] "(\S+) (.*?) HTTP/\d\.\d" (\d{3}) (\d+)', line)
        if m:
            ip = m.group(1)
            ip_counts[ip] = ip_counts.get(ip,0) + 1
            writer.writerow([ ip, m.group(2), m.group(3)+' '+m.group(4), m.group(5) ])
