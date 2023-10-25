import requests

key = "QNBSQ569PDAHAV41"
print("Stock Data Visualizer")
print("__________________________")

def get_Symbol():
    global userSymbol 
    userSymbol = input("Enter the stock symbol you are looking for: ")
    print("")
    #if (userSymbol == "GOOGL"):
    #    print("Works")
    #else:
    #    print("Doesn't Work")

def get_Time():
    global timeSeries
    print("Select the Time Series of the chart you want to Generate ")
    print("________________________________________________________________")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly")

    userTime = input("Enter time series option (1, 2, 3, 4): ")
    if (userTime == "1"):
        timeSeries = "TIME_SERIES_INTRADAY"
        #print (timeSeries)
    elif (userTime == "2"):
        timeSeries = "TIME_SERIES_DAILY"
        #print (timeSeries)
    elif (userTime == "3"):
        timeSeries = "TIME_SERIES_WEEKLY"
        #print (timeSeries)
    elif (userTime == "4"):
        timeSeries = "TIME_SERIES_MONTHLY"
        #print (timeSeries)
    else:
        print(" ")
        print("Please be sure to input 1, 2, 3, or 4. Try again.")
        print(" ")
        get_Time()





def main():
    get_Symbol()
    get_Time()
    getData()


def getData():
    url = 'https://www.alphavantage.co/query?function='+ timeSeries + '&symbol=' + userSymbol + '&interval=5min&apikey=' + key
    r = requests.get(url)
    data = r.json()
    print(data)


main()