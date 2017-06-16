Crypto Currency Indexer
=======================

Basic portfolio manager for a market-weighted crypto currency portfolio.

Given a portfolio defined in portfolio.yaml (see portfolio.yaml-sample), find
its value, all cryptocurrencies with more than .5% overall market capitalization
weight, and the amount required to rebalance equally across said currencies.

    $ ./aa.py portfolio.yaml-sample

    Currencies and their relative market weight
    ===========================================
              Spot   Market Port   Position Rebalance
     1. BTC   $2,456 38.91% 77.14% $51,591 $-25,569
     2. ETH   $353   31.63% 22.22% $14,862 $6,292
     3. XRP   $0.26   9.62%  0.00% $0      $6,432
     4. XEM   $0.19   1.67%  0.00% $0      $1,120
     5. ETC   $18.03  1.61%  0.00% $0      $1,079
     6. LTC   $30.21  1.51%  0.59% $393    $614
     7. DASH  $163    1.16%  0.00% $0      $776
     8. MIOTA $0.33   0.90%  0.00% $0      $601
     9. BTS   $0.32   0.81%  0.00% $0      $543
    10. STRAT $7.85   0.75%  0.00% $0      $499
    11. XMR   $45.68  0.65%  0.00% $0      $432
    12. ZEC   $384    0.57%  0.00% $0      $381
    18. XLM   $0.04   0.35%  0.05% $31     $200

    Total: $66,877.70

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
