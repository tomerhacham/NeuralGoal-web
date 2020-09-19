from Server.DataAccess.DTOs import *
from Server.DataAccess.MongoDBConnection import MongoDBConnection
from Server.BetsFinancial.Match import Match, Result
from Server.BetsFinancial.BetForm import BetForm
import pandas as pd
enumDICT = {
    '1':Result.Home,
    '2':Result.Away,
    'X':Result.Draw
}
Match=0
ExpectedResult=1
DBConnection = MongoDBConnection()

def getAllData(as_dataframe=False):
    '''
    @param as_dataframe: boolean indicate if to return the data as Pandas DataFrame or list of DTOs
    @return: all the match in match table
    '''
    if as_dataframe:
        cursor=DBConnection.ProductionDBMainTable.find({},projection={'_id': False})
        return pd.DataFrame.from_records(cursor)
    return DBConnection.ProductionDBMainTable.find({},projection={'_id': False})

def getUpcomingGames(league,as_dataframe=False):
    '''
    @param league: string of the requested league (can be 'all' in order for all leagues)
    @param as_dataframe:  boolean indicate if to return the data as Pandas DataFrame or list of DTOs
    @return: all the upcoming matches for the requested league
    '''
    if league=='all':
        getAllData()
    myquery = { "league": league }

    if as_dataframe:
        cursor=DBConnection.ProductionDBMainTable.find(myquery,projection={'_id': False})
        return pd.DataFrame.from_records(cursor)

    return DBConnection.ProductionDBMainTable.find(myquery,projection={'_id': False})

def updateUpcomingGameOdds(dto):
    '''
    @param dto: dto of the upcoming game to be update (the dto will store the odds of the match)
    @return: Void
    '''
    return None

def clearDB():
    DBConnection.clearDB()

def updateDB():
    #TODO: implement- scrap all the data
    return None

def saveMatch(newMatch):
    '''
    @param newMatch:DTO.betMatch
    @return:
    '''
    return None

def updateMatch(match):
    '''
    amtch is already DTO
    @param match:DTO.betMatch
    @return:
    '''
    #TODO: implement
    return None

def findMatch(matchID):
    #TODO: implement
    #dto=(**what returns from mongo)
    dto=None
    return Match.constructor(dto)

def saveBetForm(form):
    # TODO: implement
    return None
def findBetForm(receiptID):
    try:
        #dto=(**what returns from mongo)
        dto=None
        bets_list=map(lambda pair: (findMatch(pair[Match]),enumDICT[pair[ExpectedResult]]))
        return BetForm.constructor(dto,bets_list)
    except KeyError:
        print("Could not find the associate ENUM")
        return None
    except:
        print("An error has been occurred")
        return None

def getLastFundStatus():
    '''
    return the current status of the fund
    @return:float
    '''
    return None
def updateFundStatus(amount):
    '''
    save the current status of the fund
    @param amount:float, the current status of the fund
    @return:
    '''
    return None

def saveTransaction(name, amount):
    '''
    save the deposit that has been made
    @param name:string, who has been deposit the money
    @param amount:flaot, the amount of money that has been deposited
    @return:
    '''
    return None

#allData = getAllData(as_dataframe=True)
#for game in allData:
#  print(game)
#  m=match(**game)
#  print(m)
