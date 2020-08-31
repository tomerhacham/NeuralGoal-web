from Server.Persistent.DTOs import match
from Server.Persistent.MongoDBConnection import MongoDBConnection
import pandas as pd

DBConnection = MongoDBConnection()

def getAllData(as_dataframe=False):
    #TODO:implement dataframe return
    '''
    @param as_dataframe: boolean indicate if to return the data as Pandas DataFrame or list of DTOs
    @return: all the match in match table
    '''
    return DBConnection.ProductionDBMainTable.find({},projection={'_id': False})


def getUpcomingGames(league,as_dataframe=False):
    #TODO:implement dataframe return
    '''
    @param league: string of the requested league (can be 'all' in order for all leagues)
    @param as_dataframe:  boolean indicate if to return the data as Pandas DataFrame or list of DTOs
    @return: all the upcoming matches for the requested league
    '''
    if league=='all':
        getAllData()
    myquery = { "league": league }

    return DBConnection.ProductionDBMainTable.find(myquery,projection={'_id': False})

def updateUpcomingGameOdds(dto):
    #TODO: implement dataframe return
    '''
    @param dto: dto of the upcoming game to be update (the dto will store the odds of the match)
    @return: Void
    '''
    return None


def clearDB():
    #TODO:implement-delete all data in the DB
    return None


def updateDB():
    #TODO: implement- scrap all the data
    return None


#allData = getAllData()
#for game in allData:
 # print(game)
 # m=match(**game)
 # print(m)