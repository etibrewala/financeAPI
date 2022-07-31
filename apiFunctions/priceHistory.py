from operator import index
import requests
from accessData.authData import apikey
from accessData.url import priceHistoryURL

def set_symbol():
    userSymbol=str(input("What stock do you want price history for(enter the symbol)?: ")).upper()
    return userSymbol

def set_periodType(): 
    userPeriodType=str(input("What period would you like to see(DAY, MONTH, YEAR, YTD)? ")).lower()

    return userPeriodType

def set_peirodLength(periodType):
    if(periodType=="day"):
        userPL=int(input("Enter the number of periods to show(1, 2, 3, 4, 5, or 10): "))
    if(periodType=="month"):
        userPL=int(input("Enter the number of periods to show(1,2,3,6): "))
    if(periodType=="year"):
        userPL=int(input("Enter the number of periods to show(1,2,3,5,10,15,20): "))
    if(periodType=="ytd"):
        userPL=1

    return userPL

def set_frequencyType(periodType):
    if(periodType=="day"):
        userFT="minute"
    if(periodType=="month" or periodType=="ytd"):
        userFT=str(input("Enter the frequency type you want to see(DAILY or WEEKLY): ")).lower()
    if(periodType=="year"):
        userFT=str(input("Enter the frequency type you want to see(DAILY, WEEKLY or MONTHLY): ")).lower()
    return userFT

def set_Frequency(userFrequencyType):
    if(userFrequencyType=="minute"):
        userFrequency=int(input("Enter the frequency intervals you want to see(1,5,10,15,30): "))
    else:
        userFrequency=1

    return userFrequency

def get_extendedHours():
    userHours=str(input("Do you want extended hours data(Y/N)? ")).lower()
    if(userHours=="y"):
        return "true"
    if(userHours=="n"):
        return "false"

    
def set_Parameters():
    periodType=set_periodType()
    periodLength=set_peirodLength(periodType)
    frequencyType=set_frequencyType(periodType)
    frequency=set_Frequency(frequencyType)
    extendedHours=get_extendedHours()

    parameters={"apikey":apikey,
                "periodType":periodType,
                "period":periodLength,
                "frequencyType":frequencyType,
                "frequency":frequency,
                "needExtendedHoursData":extendedHours}

    return parameters

def get_priceHistory():
    symbol=set_symbol()
    parameters=set_Parameters()
    phURL=priceHistoryURL.format(index=symbol)
    response=requests.get(phURL,params=parameters)
    return response.json()
