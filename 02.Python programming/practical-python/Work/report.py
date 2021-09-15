# report.py
import csv
def read_porfolio(filename):
    '''
    Excercise 2-4
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


def read_portfolio(filename:str):
    '''
    Excercise 2-5
    :param fiename:
    :return List with dictionary collections.
    '''
    portfolio = []
    TARGET_FILE = "../Data/"+filename

    key_cols = []
    with open(TARGET_FILE, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        key_cols = header

        result_list = []
        for row in rows:
            result = dict()
            #print(row, type(row))

            result[key_cols[0]] = row[0].replace('"', '')
            result[key_cols[1]] = int(row[1])
            result[key_cols[2]] = float(row[2])
            result_list.append(result)
    return result_list

# 수행
portfolio = read_portfolio("portfolio.csv")
print(portfolio[0])
print(portfolio[1])
print("Shares : ", portfolio[1]['shares'])

total = 0.0
for s in portfolio:
    total += int(s["shares"]) * float(s["price"])
print(f"{total:.2f}")

from pprint import pprint
pprint(portfolio)

f = open("../Data/prices.csv", "rt")
rows = csv.reader(f)
for row in rows:
    print(row)

def read_prices(filename: str):
    '''
    Excercies 2-6
    :param filename:
    :return:
    '''
    TARGET_DIR = "../Data/"+filename
    with open(TARGET_DIR, "rt") as f:
        pricesList = csv.reader(f)

        prices = {}
        for lst in pricesList:
            try:
                prices[lst[0]] = lst[1]
            except IndexError:
                pass
    return prices

# 수행
prices = read_prices("prices.csv")
print(prices["IBM"])
print(prices["MSFT"])

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += int(s["shares"]) * float(prices[s["name"]])

print(f" total value : {total_value: .2f}")