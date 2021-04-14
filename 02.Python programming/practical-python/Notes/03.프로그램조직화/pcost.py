#pcost.py
import report
def portfolio_cost(filename):
    """
    Computes the total cost(shares * price) of a portfolio file
    """
    portfolio = report.read_portfolio(filename)
    return sum([s['shares'] * s['price'] for s in portfolio])


def main(filename):
    TARGET_DIR = "C:\\dataAnalysis\\philosophy_datascience\\02.Python programming\\practical-python\\Work\\Data\\"
    filedir = TARGET_DIR+filename
    cost = portfolio_cost(filedir)
    print("Total cost : ", cost)    


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        filename  = sys.argv[1]
    else:
        SystemExit(f'Usage: {sys.argv[0]} ' 'pricefile')
    main(filename)


