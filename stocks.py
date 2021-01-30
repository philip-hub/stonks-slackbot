import requests
import json

def StockData():
    with open('stock.txt', 'r') as stocks:
    #line = input("Give me a stock symbol")


      stocklist = stocks.readlines() 
      FinalStatment = ""
  

  
    for line in stocklist:
        line=line.rstrip()
        header = {'X-Finnhub-Token':'Your-Finhub-API-Token'}
        r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={line}', headers = header)
        rjson = json.loads(r.content)
        value = rjson['c']
        previousclose = rjson['pc']
        
        percentchange = ((value - previousclose)/previousclose) * 100
        
        
        
        CurrentValueStatement = (" Current Value - $")
        PreviousCloseStatement = (" Previous Close - $")
        PrecentChangeStatement = (" Percent Change - %")
        CurrentValueStatement = str("\n"+line) + CurrentValueStatement + str(value)
        PreviousCloseStatement = PreviousCloseStatement + str(previousclose)
        PrecentChangeStatement = PrecentChangeStatement +str(percentchange)
        FinalStatment = str(FinalStatment + CurrentValueStatement + PreviousCloseStatement + PrecentChangeStatement)

    return FinalStatment
