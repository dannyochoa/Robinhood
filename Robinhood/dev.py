import logging as logger
import time 

from Robinhood import Robinhood
from myFunc import get_Prices

logger.basicConfig(filename='../../logs/dev.log', level=logger.DEBUG)
logger.info('Dev Robinhood Bot has started')

my_trader = Robinhood()
try_signin = True
while(try_signin):
    try:
        try_signin = False
        signin = True
        logger.info("successful sign in")

    except:
        logger.error("Could not log in")
        retry = input("Error Logging in! \n Would you like to try Again (y) (n)")
        if(retry == 'n'):
            try_signin = False
            signin = False
            logger.info("Dev Robinhood STOPPED")

if(signin):
    logger.info("Getting histoical data for NIO")
    stock_instrument = my_trader.instruments('NIO')[0]
    week = my_trader.get_historical_quotes('NIO','5minute','week')
    prices = week['results'][0]['historicals']
    result = get_Prices(prices, "NIO")
    print(result)

    #number of peaks per day
    #avegare number of peaks

    currentQuote = my_trader.quote_data("NIO")
    startingLastTradePrice = float(currentQuote['last_trade_price'])
    percentage = 0
    allowance = 100
    numStocks = float(allowance/startingLastTradePrice)
    targetBuyPercent = 1
    targetSellPercent = 1
    stocksBought = 0;
    while(True):
        print("getting current price for NIO")
        logger.info("getting current price for NIO")
        currentQuote = my_trader.quote_data("NIO")
        logInfo = currentQuote['updated_at'] + " " + "Last Trade price: " + currentQuote['last_trade_price'] + " Last extended hour trade price: " + currentQuote['last_extended_hours_trade_price']
        logger.info(logInfo)
        lastTradePrice = float(currentQuote['last_trade_price'])
        priceDiff = startingLastTradePrice - lastTradePrice
        percentDiff = startingLastTradePrice - lastTradePrice
        if(priceDiff < 0):#buy
            if(targetBuyPercent < percentDiff):
                numStocksToPurchace = (pricentDiff * 10) * numStocks
                targetBuyPercent = targetBuyPercent + 1
                moneyNeeded = lastTradePrice * int(numStocksToPurchace)
                stocksBought = stocksBought + int(numStocksToPurchace)
                if(moneyNeeded < allowance):
                    allowance = allowanec - moneyNeeded
                    banner = ("*************** Buying stock **************")
                    symbolP = ("Symbol: " + "NIO")
                    priceP = ("Price: " + lastTradePrice)
                    numP = ("number of stocks: " + int(numStocksToPurchace))
                    moneyP = ("Equity: " + moneyNeeded)
                    allowanceP = ("Allowance: " + allowanceP)

                    print(banner)
                    print(symbolP)
                    print(priceP)
                    print(numP)
                    print(moneyP)
                    print(allowanceP)

                    logger.info(banner)
                    logger.info(symbolP)
                    logger.info(priceP)
                    logger.info(numP)
                    logger.indo(moneyP)
                    logger.info(allowanceP)

                    
        if(priceDiff > 0):#sell
            if(targetSellPercent < percentDiff):
                numStocksToSell = (priceDiff * 10) * stocksBought
                targetSellPercent = targetSellPercent + 1
                moneyReturned = lastTradePrice * int(numStocksToSell)
                allowance = allowance + moneyReturned
                stocksBought = stocksBought - int(numStocksToSell)
                banner = ("******************* Selling Stock *********************")
                symbolP = ("Symbol: " + "NIO")
                priceP = ("Price: " + lastTradePrice)
                numP = ("number of stocks: " + int(numStocksToSell))
                moneyP = ("Money Returned: " + moneyReturned)
                allowanceP = ("Allowance: " + allowanceP)

                print(banner)
                print(symbolP)
                print(priceP)
                print(numP)
                print(moneyP)
                print(allowanceP)

                logger.info(banner)
                logger.info(symbolP)
                logger.info(priceP)
                logger.info(numP)
                logger.info(moneyP)
                logger.indo(allowanceP)
        
        time.sleep(10)
