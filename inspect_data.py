import csv
with open("ibmetrophc.csv", encoding="utf-8-sig") as f:
    rows = list (csv.DictReader(f))
values = []
for row in rows: 
    value = float(row["Latitude"])
    values.append(value)
print ("smallest:", min(values))
print ("largest:", max(values))
print ("count:", len(rows)) 

