Crypto Currency Indexer
=======================

Basic portfolio manager for a market-weighted crypto currency portfolio.

Given a portfolio defined in portfolio.yaml (see portfolio.yaml-sample), find
its value, all cryptocurrencies with more than 1% overall market capitalization
weight, and the amount required to rebalance equally across said currencies.

	$ ./aa.py portfolio.yaml
	Portfolio Positions
	====================
	BTC:  21.0 coins, $55,944.42
	ETH:  42.0 coins, $17,044.99
	LTC:  13.0 coins, $387.00
	Portfolio(USD): $73,376.41

	Currencies and their relative market weight
	===========================================
	 BTC: market: 39.32% portfolio: 76.24%
	 ETC: market:  1.71% portfolio: 0.00%
	 ETH: market: 33.79% portfolio: 23.23%
	 LTC: market:  1.38% portfolio: 0.53%
	 XEM: market:  1.61% portfolio: 0.00%
	 XRP: market:  8.76% portfolio: 0.00%
	DASH: market:  1.16% portfolio: 0.00%

	Portfolio Rebalance
	===================
	 BTC: -36.92%, $-27,091.08
	 ETC:   1.71%, $1,255.44
	 ETH:  10.56%, $7,747.57
	 LTC:   0.85%, $626.66
	 XEM:   1.61%, $1,183.51
	 XRP:   8.76%, $6,427.06
	DASH:   1.16%, $851.05

Usage
-----

Copy portfolio.yaml-sample to portfolio.yaml and edit it according to your
actual holdings. Run `./aa.py portfolio.yaml`.

Requirements
------------

- python3
- python3 requests library (`sudo pip3 install requests`)

Background and personal opinions...
-----------------------------------

The crypto currency market is competitive and dynamic. Instead of trying to
predict which coins will "win", or trying to time the market,
[indexing](https://www.bogleheads.org/wiki/Indexing) is a strategy that invests
across an entire market equally based on the relative market weight of the
underlying securities.

Remember that at this point, investing in cryptocurrencies is closer to
gambling than investing. By diversifying across many currencies, as long as the
blockchain based currencies concept holds (and evidence suggests it will), the
crypto market, as a whole, will increase in value over time.

Investing in crypto currencies should not take the place of traditional
investments, but rather supplement a well diversified low cost index portfolio.
For more information on index investing, visit
[bogleheads.org](https://www.bogleheads.org).
