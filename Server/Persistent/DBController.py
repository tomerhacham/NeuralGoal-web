from Server.Persistent.MongoDBConnection import MongoDBConnection

DBConnection = MongoDBConnection()


def getAllData(as_dataframe=False):
    #TODO:implement
    '''
    @param as_dataframe: boolean indicate if to return the data as Pandas DataFrame or list of DTOs
    @return: all the match in match table
    '''
    return DBConnection.DevDBGames.find()
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