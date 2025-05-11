import csv
input_path  = "/tmp/covid_worldwide.csv"
output_path = "/tmp/covid_worldwide_clean.csv"

with open(input_path, "r") as infile, open(output_path, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow(header)

    for row in reader:
        cleaned = []
        for cell in row:
            cell = cell.strip()
            if cell.upper() == "N/A" or cell == "":
                cleaned.append("")
            elif cell.replace(",", "").replace(".", "").isdigit():
                cleaned.append(cell.replace(",", ""))
            else:
                cleaned.append(cell)
        writer.writerow(cleaned)
