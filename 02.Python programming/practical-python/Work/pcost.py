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