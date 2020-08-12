from Server.Persistent.DTOs import match
from Server.Persistent.MongoDBConnection import MongoDBConnection

DBConnection = MongoDBConnection()
ListOfKeys=['Game Date','Home Team','Away Team','Home ATT','Away ATT',
            'Home DEF','Away DEF','Home MID','Away MID','Home Win Odds','Draw Odds',
            'Away Win Odds','Winner','Home win Odds not normal','Draw Odds not normal',
            'Away win Odds not normal','Home Team Rank','Away Team Rank','Home Team Scored Goals',
            'Home Team Received Goals','Away Team Scored Goals','Away Team received Goals']
#TODO: inform Andrey missing 'League' attribute on the DB
#TODO: inform Andrey missing the dict should be in the same order and the same names of the keys as the dataclass

def getAllData(as_dataframe=False):
    #TODO:implement
    '''
    @param as_dataframe: boolean indicate if to return the data as Pandas DataFrame or list of DTOs
    @return: all the match in match table
    '''
    x= DBConnection.DevDBGames.find()
    return x
    #return mongoConnection.ProductionDBMainTable.find()

def getUpcomingGames(league,as_dataframe=False):
    #TODO:implement
    '''
    @param league: string of the requested league (can be 'all' in order for all leagues)
    @param as_dataframe:  boolean indicate if to return the data as Pandas DataFrame or list of DTOs
    @return: all the upcoming matches for the requested league
    '''
    if league=='all':
        getAllData()
    myquery = { "league": league }

    return DBConnection.DevDBGames.find(myquery)
    #return mongoConnection.ProductionDBUpcomingGames.find(myquery)

def updateUpcomingGameOdds(dto):
    #TODO: implement
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




allData = getAllData()

for game in allData:
  print(game)
  sliced = {k:game[k] for k in ListOfKeys if k in game}
  print(match(**sliced))