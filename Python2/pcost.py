# pcost.py
import sys
import fileparse

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = fileparse.read_portfolio(filename)
    return sum([s['shares'] * s['price'] for s in portfolio])

def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s portfoliofile' % args[0])
    portfoliofile = args[1]
    cost = portfolio_cost(portfoliofile)
    print(f'Total cost: {cost:.2f}')

if __name__ == '__main__':
    main(sys.argv)
