🐍 Python Port 🐍 Based on [COINMON](https://github.com/bichenkk/coinmon)

> 💰 Cryptocurrency price ticker CLI.

Check cryptocurrencies' prices, changes on your console.
Best CLI tool for those who are both **Crypto investors** and **Engineers**.

## Installation

Install from source with:

```
$ git clone https://github.com/S0L1DUS/cryptomon.git --recursive
$ cd cryptomon
$ pip install .
```

## Usage

To check the top 10 cryptocurrencies ranked by their market cap, simply execute
```
$ cryptomon
```

### Options

You can use the `-c` (or `--convert`) with the fiat currency symbol to find in terms of another currency.
The default currency is USD and it supports AUD, BRL, CAD, CHF, CLP, CNY, CZK, DKK, EUR, GBP, HKD, HUF, IDR, ILS, INR, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PKR, PLN, RUB, SEK, SGD, THB, TRY, TWD, ZAR.

```
$ cryptomon -c eur // convert prices to Euro
$ cryptomon -c jpy // convert prices to Yen
```

You can use the `-f` (or `--find`) with coin symbol to search cryptocurrencies. You can add symbols seperated by space.

```
$ cryptomon -f btc // search coins included keyword btc
$ cryptomon -f btc eth // search coins included keyword btc or eth
```

You can use the `-l` (or `--layout`) with template name to print the table with different style.
The default layout template is grid and it supports plain, simple, grid, fancy_grid, pipe, orgtbl, presto, psql, rst.

```
$ cryptomon -l plain // show table with plain style
$ cryptomon -l fancy_grid // show table with fancy_grid style
```

You can use the `-t` (or `--top`) with the index to find the top n cryptocurrencies ranked by their market cap.

```
$ cryptomon -t 50 // find top 50
$ cryptomon -t 1000 // find top 1000
```

You can use the `-u` (or `--update`) with the refresh frequency in seconds. The value must be bigger than 0.

```
$ cryptomon -u 10 // update data each 10 seconds
```

You can use the `-H` (or `--humanize`) to display market cap in humanized format.

```
$ cryptomon -H // show market cap in humanized format like 58.9 billion 
```

You can use the `-h` (or `--help`) to find all valid options of cryptomon.

```
$ cryptomon -h
```

You can use the `--debug` to show debug info when an error occurred.

```
$ cryptomon --debug
```
