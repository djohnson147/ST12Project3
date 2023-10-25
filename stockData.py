import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=GOOGL&interval=5min&apikey=QNBSQ569PDAHAV41'
r = requests.get(url)
data = r.json()
print(data)