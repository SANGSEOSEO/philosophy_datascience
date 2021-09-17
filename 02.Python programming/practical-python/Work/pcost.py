# pcost.py

import csv
def portfolio_cost(filename):
    """
    compute the total cost(shares * price)
    :param filename:
    :return: total_cost
    """
    total_cost = 0.0

    with open("../Data/"+ filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost = nshares * price
    return total_cost

# process
total_cost = portfolio_cost("portfolio.csv")
print(f"Total Cost : {total_cost: .2f}")

# Excercise 2-15
def portfolio_cost(filename):
    '''
    :param filename:
    :return: toal_cost
    '''
    total_cost = 0.0
    TARGET_FILE ="../Data/"+ filename
    with open(TARGET_FILE, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows, start=1):
            try:
                nshares = int(row[1])
                price = float(row[2])
                total_cost  += nshares * price
            except ValueError:
                print(f"Row {i} : Couldn't convert : {row}")
        total_cost += nshares * price
    return total_cost

# 수행
#total_cost = portfolio_cost("missing.csv")
#print("총 주식사기 위한 비용 %10.2f" %total_cost)

def portfolio_cost(filename):
    """
    :파일을 읽어서 주식구매 비용 리턴
    :param filename:
    :return: total_cost
    """
    total_cost = 0.0
    TARGET_FILE = "../Data/"+ filename
    with open(TARGET_FILE, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f"Row {rowno} : Couldn't convert : {row}")
    return total_cost

# 수행
import sys

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input("Enter a fileName : ")

cost = portfolio_cost(filename)
print(f"Total Cost : {cost}")

total_cost = portfolio_cost("portfoliodate.csv")

# Excercise 2-17
prices = {
        'GOOG' : 490.1,
        'AA' : 23.45,
        'IBM' : 91.1,
        'MSFT' : 34.23
    }

print(prices.items())

prices_list = list(dict(zip(prices.values(), prices.keys())))
print(prices_list)

print(f'최소값 : {min(prices_list)}, 최대값 : {max(prices_list)}')
print(sorted(prices_list))

a = [1,2,3,4]
b = ['w', 'x', 'y', 'z']
c = [0.2, 0.4, 0.6, 0.8]
print(list(zip(a, b, c)))
