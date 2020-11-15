from setuptools import setup
from cryptomon.metadata import Metadata

metadata = Metadata()


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list

long_description = """"
🐍 Python Port 🐍 Based on `COINMON`_

    💰 Cryptocurrency price ticker CLI.

Check cryptocurrencies’ prices, changes on your console. Best CLI tool
for those who are both **Crypto investors** and **Engineers**.

All data comes from `coinmarketcap.com`_ APIs.

Installation
------------

You can install or upgrade cryptomon with:

``$ pip install cryptomon --upgrade``

Or you can install from source with:

::

    $ git clone https://github.com/RDCH106/cryptomon.git --recursive
    $ cd cryptomon
    $ pip install .

Usage
-----

To check the top 10 cryptocurrencies ranked by their market cap, simply
execute

::

    $ cryptomon

Options
~~~~~~~

You can use the ``-c`` (or ``--convert``) with the fiat currency symbol
to find in terms of another currency. The default currency is USD and it
supports AUD, BRL, CAD, CHF, CLP, CNY, CZK, DKK, EUR, GBP, HKD, HUF,
IDR, ILS, INR, JPY, KRW, MXN, MYR, NOK, NZD, PHP, PKR, PLN, RUB, SEK,
SGD, THB, TRY, TWD, ZAR.

::

    $ cryptomon -c eur // convert prices to Euro
    $ cryptomon -c jpy // convert prices to Yen

You can use the ``-f`` (or ``--find``) with coin symbol to search
cryptocurrencies. You can add symbols seperated by space.

::

    $ cryptomon -f btc // search coins included keyword btc
    $ cryptomon -f btc eth // search coins included keyword btc or eth

You can use the ``-l`` (or ``--layout``) with template name to print the
table with different style. The default layout template is grid and it
supports plain, simple, fancy_grid, pipe, orgtbl, ‘presto’, ‘psql’,
‘rst’.

::

    $ cryptomon -l plain // show table with plain style
    $ cryptomon -l fancy_grid // show table with fancy_grid style

You can use the ``-t`` (or ``--top``) with the index to find the top n
cryptocurrencies ranked by their market cap.

::

    $ cryptomon -t 50 // find top 50
    $ cryptomon -t 1000 // find top 1000

You can use the ``-u`` (or ``--update``) with the refresh frequency in
seconds. The value must be bigger than 0.

::

    $ cryptomon -u 10 // update data each 10 seconds

You can use the ``-H`` (or ``--humanize``) to display market cap in
humanized format.

::

    $ cryptomon -H // show market cap in humanized format like 58.9 billion

You can use the ``-h`` (or ``--help``) to find all valid options of
cryptomon.

::

    $ cryptomon -h

You can use the ``--debug`` to show debug info when an error occurred.

::

    $ cryptomon --debug

Screenshot
----------

.. figure:: https://raw.githubusercontent.com/RDCH106/cryptomon/master/cryptomon.png
   :alt: cryptomon screenshot

.. _COINMON: https://github.com/bichenkk/coinmon
.. _coinmarketcap.com: https://coinmarketcap.com/
    """


setup(
    name = 'cryptomon',
    packages = ['cryptomon'],
    install_requires = requirements(),
    version = metadata.get_version(),
    license = 'MIT',
    description = 'The cryptocurrency price tool on CLI',
    long_description= long_description,
    author = metadata.get_author(),
    author_email = 'contact@rdch106.hol.es',
    url = 'https://github.com/RDCH106/cryptomon',
    download_url = 'https://github.com/RDCH106/cryptomon/archive/v'+metadata.get_version()+'.tar.gz',
    entry_points={
        'console_scripts': ['cryptomon=cryptomon.main:main'],
    },
    keywords = 'bitcoin criptocurrency crypto ticker python cli price-tracker command-line',
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8'],
)
