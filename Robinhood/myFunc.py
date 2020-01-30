import statistics

def get_Prices(prices):
    low = 99999999;
    high = 0;
    medianArr = []

    for price in prices:
        open_price = float(price['open_price'])
        close_price = float(price['close_price'])
        high_price = float(price['high_price'])
        low_price = float(price['low_price'])
        if(open_price < low):
            low = open_price
        if(open_price > high):
            high = open_price
        if(close_price < low):
            low = close_price
        if(close_price > high):
            high = close_price
        if(high_price < low):
            low = high_price
        if(high_price > high):
            high = high_price
        if(low_price < low):
            low = low_price
        if(low_price > high):
            high = low_price
        medianArr.insert(len(medianArr),open_price)
        medianArr.insert(len(medianArr),close_price)
        medianArr.insert(len(medianArr),high_price)
        medianArr.insert(len(medianArr),low_price)

    print("********************** Company **************************")
    print(symbol)
    print("************************ LOW ****************************")
    print(low)
    print("*********************** High ****************************")
    print(high)
    print("*********************** median **************************")
    print(statistics.median(medianArr))
