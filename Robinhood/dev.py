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
    print(currentQuote)
    startingLastTradePrice = float(currentQuote['last_trade_price'])
    allowance = 100
    numStocks = float(allowance/startingLastTradePrice)
    targetBuyPercent = 1
    targetSellPercent = 1
    stocksBought = 0;

    startingMedianPrice = float(result['median'])
    allowance2 = 100
    numStocks2 = float(allowance/startingMedianPrice)
    targetBuyPercent2 = 1
    targetSellPercent2 = 1
    stocksBought2 = 0;
    while(True):
        print("getting current price for NIO")
        logger.info("getting current price for NIO")
        currentQuote = my_trader.quote_data("NIO")
        logInfo = str(currentQuote['updated_at']) + " " + "Last Trade price: " + str(currentQuote['last_trade_price']) + " Last extended hour trade price: " + str(currentQuote['last_extended_hours_trade_price'])
        logger.info(logInfo)
        lastTradePrice = float(currentQuote['last_trade_price'])
        priceDiff = lastTradePrice - startingLastTradePrice 
        percentDiff = lastTradePrice - startingLastTradePrice 

        if(priceDiff < 0):#buy startingLastTradePrice
            b = ("********************** Trying buy starting last ***************")
            logger.info(b)
            print(b)
            print(str(targetBuyPercent/100) + " < " + str(-1 * percentDiff))
            if(targetBuyPercent/100 < -1* percentDiff):
                numStocksToPurchace = (-1 * percentDiff * 10) * numStocks
                targetBuyPercent = targetBuyPercent + 1
                moneyNeeded = lastTradePrice * int(numStocksToPurchace)
                stocksBought = stocksBought + int(numStocksToPurchace)
                print("have money")
                if(moneyNeeded < allowance):
                    allowance = allowance - moneyNeeded
                    banner = ("*************** Buying stock LAST**************")
                    symbolP = ("Symbol: " + "NIO")
                    priceP = ("Price: " + str(lastTradePrice))
                    numP = ("number of stocks: " + str(int(numStocksToPurchace)))
                    moneyP = ("Equity: " + str(moneyNeeded))
                    allowanceP = ("Allowance: " + str(allowanceP))
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


        if(priceDiff > 0 and stocksBought > 0):#sell
            b = ("********************* trying to sell starting last *************")
            logger.info(b)
            print(b)
            print(str(targetSellPercent) + " < " + str(percentDiff))
            if(targetSellPercent < percentDiff):
                numStocksToSell = (percentDiff * 10) * stocksBought
                targetSellPercent = targetSellPercent + 1
                moneyReturned = lastTradePrice * int(numStocksToSell)
                allowance = allowance + moneyReturned
                stocksBought = stocksBought - int(numStocksToSell)
                banner = ("******************* Selling Stock LAST*********************")
                symbolP = ("Symbol: " + "NIO")
                priceP = ("Price: " + str(lastTradePrice))
                numP = ("number of stocks: " + str(int(numStocksToSell)))
                moneyP = ("Money Returned: " + str(moneyReturned))
                allowanceP = ("Allowance: " + str(allowance))
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

        priceDiff2 = lastTradePrice - startingMedianPrice
        percentDiff2 = lastTradePrice - startingMedianPrice
        if(priceDiff2 < 0):#buy startingLastTradePrice
            b = ("******************* trying to buy median ***************")
            logger.info(b)
            print(b)
            print(str(targetBuyPercent2/100) + " < " + str(-1 * percentDiff2))
            if(targetBuyPercent2/100 < -1 * percentDiff2):
                numStocksToPurchace = (-1 * percentDiff2 * 10) * numStocks2
                targetBuyPercent2 = targetBuyPercent2 + 1
                moneyNeeded = lastTradePrice * int(numStocksToPurchace)
                stocksBought2 = stocksBought2 + int(numStocksToPurchace)
                if(moneyNeeded < allowance2):
                    allowance2 = allowance2 - moneyNeeded
                    banner = ("*************** Buying stock MEDIAN**************")
                    symbolP = ("Symbol: " + "NIO")
                    priceP = ("Price: " + str(lastTradePrice))
                    numP = ("number of stocks: " + str(int(numStocksToPurchace)))
                    moneyP = ("Equity: " + str(moneyNeeded))
                    allowanceP = ("Allowance: " + str(allowance))
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


        if(priceDiff2 > 0 and stocksBought2 > 0):#sell
            b = ("********************* trying to sell median ********************")
            logger.info(b)
            print(b)
            print(str(targetSellPercent2) + " < " + str(percentDiff2))
            if(targetSellPercent2 < percentDiff2):
                numStocksToSell = (percentDiff2 * 10) * stocksBought2
                targetSellPercent2 = targetSellPercent2 + 1
                moneyReturned = lastTradePrice * int(numStocksToSell)
                allowance = allowance + moneyReturned
                stocksBought2 = stocksBought2 - int(numStocksToSell)
                banner = ("******************* Selling Stock MEDIAN*********************")
                symbolP = ("Symbol: " + "NIO")
                priceP = ("Price: " + str(lastTradePrice))
                numP = ("number of stocks: " + str(int(numStocksToSell)))
                moneyP = ("Money Returned: " + str(moneyReturned))
                allowanceP = ("Allowance: " + str(allowanceP))
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
