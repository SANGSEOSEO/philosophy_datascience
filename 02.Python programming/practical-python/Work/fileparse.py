# fileparse.py
#
# Exercise 3.3
def parse_csv(filename):
    import csv

    with open("Data/"+filename, 'rt') as f:
        rows = csv.reader(f)
        # read the file header
        header = next(rows)
        records = []

        for row in rows:
            if not row:
                continue
            record = dict(zip(header, row))
            records.append((record))
    return records

# 수행
records = parse_csv("portfolio.csv")
print(records)


