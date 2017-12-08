Crypto Currency Indexer
=======================

Basic portfolio manager for a market-weighted crypto currency portfolio.

Given a portfolio defined in portfolio.yaml (see portfolio.yaml-sample), find
its value, all cryptocurrencies with more than .5% overall market capitalization
weight, and the amount required to rebalance equally across said currencies.

    $ ./aa.py portfolio.yaml-sample
        | Coin   | Spot       | Market   | Port   | Position   | Rebalance
    ----+--------+------------+----------+--------+------------+-------------
      1 | BTC    | $17,370.70 | 66.58%   | 62.68% | $86,853.50 | $5,401.60
      2 | ETH    | $429.68    | 9.47%    | 31.01% | $42,968.40 | -$29,843.82
      3 | BCH    | $1,554.17  | 6.00%    | 5.61%  | $7,770.85  | $540.48
      4 | MIOTA  | $3.80      | 2.42%    | 0.00%  | $0.00      | $3,356.06
      5 | XRP    | $0.26      | 2.31%    | 0.00%  | $0.00      | $3,203.77
      6 | DASH   | $692.33    | 1.23%    | 0.00%  | $0.00      | $1,701.36
      7 | LTC    | $98.02     | 1.22%    | 0.71%  | $980.20    | $706.24
      8 | BTG    | $270.88    | 1.04%    | 0.00%  | $0.00      | $1,435.79
      9 | XMR    | $279.59    | 0.99%    | 0.00%  | $0.00      | $1,371.46
     10 | ADA    | $0.11      | 0.68%    | 0.00%  | $0.00      | $946.26
     11 | ETC    | $27.29     | 0.61%    | 0.00%  | $0.00      | $850.85
     12 | XLM    | $0.14      | 0.56%    | 0.00%  | $0.00      | $782.41
     13 | XEM    | $0.25      | 0.51%    | 0.00%  | $0.00      | $712.23
     14 | NEO    | $34.27     | 0.51%    | 0.00%  | $0.00      | $707.16
    Total: $138,572.95

Usage
-----

Copy portfolio.yaml-sample to portfolio.yaml and edit it according to your
actual holdings. Run `./aa.py portfolio.yaml`.

Requirements
------------

- python3
- python3 libraries: requests, tabulate (`pip3 install --user requests tabulate`)

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
