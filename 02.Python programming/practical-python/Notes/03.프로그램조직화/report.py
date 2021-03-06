import fileparse

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, chage) tuples given a portfolio
    list and prices dictionary
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows
def print_report(reportdata):
    '''
    Print a nicely formated table from a list of(name, shares, price, change) 
    tuple 
    '''
    headers = ('Name','Shares','Price','Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))

    for row in reportdata:
        print('%10s%10s%10.2f%10.2f' % row)
def read_portfolio(portfoliofile):
    '''
    Read a stock portfolio file into a list of dictionary with keys
    name, shares and price
    '''
    return fileparse.parse_csv(portfoliofile, select=['name', 'shares', 'price'], types=[str,int,float])
def read_prices(pricefile):
    '''
    Read a CSV file of price data into a dict mapping names to prices
    '''
    return dict(fileparse.parse_csv(pricefile, types=[str,float], has_headers=False))

def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data files
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    print_report(report)


def main(args):
    '''
    sys.argv추가 
    '''
    TARGET_DIR = "C:\\dataAnalysis\\philosophy_datascience\\02.Python programming\\practical-python\\Work\\Data\\"
    print("첫번째 파라미터 : ", args[0])
    print("두번째 파라미터 : ", args[1])
    print("세번째 파라미터 : ", args[2])

    portfoliofile = args[1]
    pricefile = args[2]
    portfolio_report(TARGET_DIR+portfoliofile, TARGET_DIR+pricefile)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
    main(sys.argv)    