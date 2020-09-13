from Server.DataAccess.DTOs import match
from Server.DataAccess.MongoDBConnection import MongoDBConnection
import pandas as pd

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


#allData = getAllData(as_dataframe=True)
#for game in allData:
#  print(game)
#  m=match(**game)
#  print(m)
