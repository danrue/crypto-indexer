#!/usr/bin/env python3
# CryptoCurrency Asset Allocator

import os
import requests
import sys
import yaml

DATA = requests.get('https://api.coinmarketcap.com/v1/ticker/').json()


def get_price_usd(coin):
    for crypto in DATA:
        if coin == crypto['symbol']:
            return float(crypto['price_usd'])


def get_crypto_cap_by_percent(min_cap_percent=.01):
    crypto_by_cap = {}
    crypto_by_usd = {}
    total_cap = 0
    for crypto in DATA:
        if crypto.get('market_cap_usd'):
            total_cap += float(crypto['market_cap_usd'])
            crypto_by_cap[crypto['symbol']] = crypto['market_cap_usd']
            crypto_by_usd[crypto['symbol']] = crypto['price_usd']

    crypto_cap_by_percent = {}
    for symbol, market_cap_usd in crypto_by_cap.items():
        cap_percent = float(market_cap_usd)/float(total_cap)
        if cap_percent >= min_cap_percent:
            crypto_cap_by_percent[symbol] = cap_percent

    return crypto_cap_by_percent


class coin(object):

    def __init__(self, symbol, amount_owned=0):
        self.symbol = symbol
        self.amount_owned = float(amount_owned)
        self.price_usd = get_price_usd(self.symbol)
        self.value_usd = self.amount_owned*self.price_usd

    def __repr__(self):
        return "{}: {:>5} coins, ${:,.2f}\n".format(
            self.symbol, self.amount_owned, self.value_usd)


class portfolio(object):
    def __init__(self, assets):
        self.coins = {}
        for symbol, amount in assets.items():
            self.coins[symbol] = coin(symbol, amount)
        self.value = self._get_portfolio_value()
        self.crypto_cap_by_percent = get_crypto_cap_by_percent()
        self.my_cap_by_percent = self._get_my_cap_by_percent()

    def _get_portfolio_value(self):
        value = 0
        for symbol, coin in self.coins.items():
            value += coin.value_usd
        return value

    def __repr__(self):
        buf = "Portfolio Positions\n"
        buf += "====================\n"
        lines = []
        for symbol, coin in self.coins.items():
            lines.append(coin.__repr__())
        lines.sort()
        buf += "".join(lines)
        buf += "Portfolio(USD): ${:,.2f}".format(self.value)
        return buf

    def _get_my_cap_by_percent(self):
        crypto_by_percent = {}
        for symbol, coin in self.coins.items():
            crypto_by_percent[symbol] = coin.value_usd/self.value
        return crypto_by_percent

    def rebalance(self):
        buf = "Portfolio Rebalance\n"
        buf += "===================\n"
        lines = []
        for symbol, market_weight in self.crypto_cap_by_percent.items():
            change_percent = market_weight-self.my_cap_by_percent.get(
                symbol, 0)
            change_usd = change_percent*self.value
            lines.append("{:>4}: {:>6.2f}%, ${:,.2f}\n".format(
                symbol, change_percent*100, change_usd))
        lines.sort()
        return buf + "".join(lines)

    def crypto_by_weight(self):
        buf = "\nCurrencies and their relative market weight\n"
        buf += "===========================================\n"
        lines = []
        for symbol, market_weight in self.crypto_cap_by_percent.items():
            lines.append(
                "{:>4}: market: {:>5.2f}% portfolio: {:.2f}%\n".format(
                    symbol, market_weight*100,
                    self.my_cap_by_percent.get(symbol, 0)*100))
        lines.sort()
        return buf + "".join(lines)


def usage():
    return "Usage: {} <portfolio.yaml>".format(sys.argv[0])


if __name__ == "__main__":
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        sys.exit(usage())

    with open(sys.argv[1]) as f:
        holdings = yaml.load(f)['portfolio']

    my_port = portfolio(holdings)
    print(my_port)
    print(my_port.crypto_by_weight())
    print(my_port.rebalance())
