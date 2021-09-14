# report.py
import csv
def read_porfolio(filename):
    '''

    :param filename:
    :return: composite list with nested tuple
    '''
    portfolio = []
    TARGET_FILE = "../Data/"+ filename
    with open(TARGET_FILE, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            holdings = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holdings)
    return portfolio

# process
portfolio = read_porfolio("portfolio.csv")
print(portfolio)

# Total Cost
total_cost = 0.0
for row in portfolio:
    total_cost += int(row[1]) * float(row[2])
print(f"{total_cost:.2f}")


# tuple unpacking
total_cost = 0.0
for _, share, price in portfolio:
    total_cost += int(share) * float(price)
print("After tuple unpacking Total Cost : {:.2f}".format(total_cost))