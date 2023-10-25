import requests

key = "QNBSQ569PDAHAV41"

def get_Symbol():
    global userSymbol 
    userSymbol = input("Enter the stock symbol you are looking for: ")
    #if (userSymbol == "GOOGL"):
    #    print("Works")
    #else:
    #    print("Doesn't Work")



def main():
    get_Symbol()
    getData()

def getData():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + userSymbol + '&interval=5min&apikey=' + key
    r = requests.get(url)
    data = r.json()
    print(data)


main()