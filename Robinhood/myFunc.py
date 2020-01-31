import statistics
import logging as logger

def get_Prices(prices, company):
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

    median = statistics.median(medianArr)
    logger.info("*********************** COMPANY *************************")
    logger.info(company)
    logger.info("************************ LOW ****************************")
    logger.info(low)
    logger.info("*********************** High ****************************")
    logger.info(high)
    logger.info("*********************** median **************************")
    logger.info(median)

    return {"company" : company, "low" : low, "high" : high, "median" : median}
