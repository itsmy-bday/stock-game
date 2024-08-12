import yfinance as yf
#stockmarket goes from 9:30AM to 4PM


# create a list of ticker symbols
real_symbols = ['DOGE-CAD', 'SBUX', 'AAPL', 'TSLA', 'AMZN', 'MSFT', 'NVDA', 'META', 'NFLX', "ISRG", 'BA', 'ADBE', 'MA', 'RML.NS', 'ZC=F', 'EQIX', 'REGN', 'MELI', 'MKL', 'MTD', 'CMG', '^RUT', 'TPL', "ALI=F", 'AZO', 'BKNG', 'SEB', 'NVR', 'NXT.L', 'LDSVF', 'LISP.SW', 'BTC-CAD', 'LISN.SW', '0QKN.L', 'BRK-A']

# loop through the list and print out the information
def printsymbolpricesandstuff():  
  for symbol in real_symbols:
      ticker = yf.Ticker(symbol)
      print(f"Symbol: {symbol}")

      try:
        #price
        regularmatketprice = ticker.info['regularMarketPrice']
        formatted_mrketprice = '{:,.2f}'.format(regularmatketprice)

        print(f"Current price: ${formatted_mrketprice}")

      except KeyError:
        regularmatketopen = ticker.info['regularMarketOpen']
        formatted_open = '{:,.2f}'.format(regularmatketopen)

        print(f"Open price: ${formatted_open}")

      try:
        #cap
        regularmarketcap = ticker.info['marketCap']
        formatted_mrketcap = '{:,.1f}'.format(regularmarketcap)

        market_cap = ticker.info['marketCap']

        rounded_market_cap = round(market_cap / 1_000_000_000, 2)
        print(f"Market cap: ${formatted_mrketcap}") 
        print(f"Rounded market cap: {rounded_market_cap} B") 
      except KeyError:
        print("Market cap: Not Avalible.")

      try:
        #forwardPE
        forward_pe = ticker.info['forwardPE']
        print(f"Forward P/E ratio: {forward_pe}")
      except KeyError:
        print("Forward P/E ratio: Not Avalible.")
      print("------------")


def stonke(key, value):
  ticker = yf.Ticker(key)

  try:
    mketofstuf = ticker.info['regularMarketPrice']
  except KeyError:
    mketofstuf = ticker.info['regularMarketOpen']


  value = mketofstuf

  key = key.upper()

  return key, value