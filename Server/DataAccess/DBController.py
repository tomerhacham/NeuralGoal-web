import pandas as pd
import datetime
from Server.BetsFinancial.BetForm import BetForm
from Server.BetsFinancial.Match import Match, Result
from Server.DataAccess.DTOs import *
from Server.DataAccess.MongoDBConnection import MongoDBConnection

MATCH=0
EXPECTED_RESULT=1
DBConnection = MongoDBConnection(mode='dev')
CURR_TIME_STMP=datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def insertMatchToMainTable(dto):
    '''
    @param dto:matchDTO
    @return:
    '''
    DBConnection.MainTable.insert(convertDateToStr(dto.to_dict()))
    return None

def insertMatchToUpcomingGames(dto):
    '''
    @param dto:matchDTO
    @return:
    '''
    DBConnection.UpcomingGames.insert(convertDateToStr(dto.to_dict()))
    return None

def deleteMatchFromUpcomingGames(date,home_team_name,away_team_name):
    '''
    @param date: str (%d-%m-%Y) format
    @param home_team_name:string
    @param away_team_name:string
    @return:
    '''
    myquery = { "date": date,
                "away_team_name": home_team_name,
                "away_team_name": away_team_name}
    DBConnection.UpcomingGames.delete_one(myquery)
    return None

def getAllData(as_dataframe=False):
    '''
    @param as_dataframe: boolean indicate if to return the data as Pandas DataFrame or list of DTOs
    @return: all the match in match table
    '''
    cursor=DBConnection.MainTable.find({},projection={'_id': False})
    if as_dataframe:
        return pd.DataFrame.from_records(cursor)
    else:
        dtos = map(lambda record: match.from_dict(convertStrtoDate(record)))
    return dtos

def getUpcomingGames(league,as_dataframe=False):
    '''
    @param league: string of the requested league (can be 'all' in order for all leagues)
    @param as_dataframe:  boolean indicate if to return the data as Pandas DataFrame or list of DTOs
    @return: all the upcoming matches for the requested league
    '''
    if league!='all':
        myquery = { "league": league }
    else:
        myquery={}
    cursor=DBConnection.UpcomingGames.find(myquery,projection={'_id': False})
    if as_dataframe:
        return pd.DataFrame.from_records(cursor)
    else:
        dtos = list(map(lambda record: upcoming_match.from_dict(convertStrtoDate(record)), cursor))
    return dtos

def updateUpcomingGameOdds(dto):
    '''
    @param dto: dto of the upcoming game to be update (the dto will store the odds of the match)
    @return: Void
    '''
    DBConnection.UpcomingGames.update_one(convertDateToStr(dto.to_dict()))
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
    DBConnection.Matches.insert(convertDateToStr(newMatch.to_dict()))
    return None

def updateMatch(dto):
    '''
    amtch is already DTO
    @param match:DTO.betMatch
    @return:
    '''
    DBConnection.Matches.update_one(convertDateToStr(dto.to_dict()))
    return None

def findMatch(matchID):
    myquery = {"matchID": matchID}
    dto=betMatch.from_dict(convertStrtoDate(DBConnection.Matches.find_one(myquery,projection={'_id': False})))
    return Match.constructor(dto)

def saveBetForm(form):
    DBConnection.BetForms.insert(convertDateToStr(form.to_dict()))
    return None

def findBetForm(receiptID):
    myquery={"receiptID":receiptID}
    try:
        dto=betForm.from_dict(convertStrtoDate(DBConnection.BetForms.find_one(myquery,projection={'_id': False})))
        #match=findMatch(dto.bets[0][MATCH])
        #res=Result.from_str(dto.bets[0][EXPECTED_RESULT])
        bets_list=list(map(lambda pair: (findMatch(pair[MATCH]), Result.from_str(pair[EXPECTED_RESULT])),dto.bets))
        return BetForm.constructor(dto,bets_list)
    except KeyError:
        print("Could not find the associate ENUM")
        return None
    except Exception as e:
        print(e)
        #print("An error has been occurred")
        return None

def getLastFundStatus():
    '''
    return the current status of the fund
    @return:float
    '''
    last_record= DBConnection.FundStatus.find().sort([('time',-1)]).limit(1).next()
    amount=last_record['amount']
    return amount

def updateFundStatus(amount):
    '''
    save the current status of the fund
    @param amount:float, the current status of the fund
    @return:
    '''
    record={"time":CURR_TIME_STMP,
            "amount":amount}
    DBConnection.FundStatus.insert(record)
    return None

def saveTransaction(name, amount):
    '''
    save the deposit that has been made
    @param name:string, who has been deposit the money
    @param amount:flaot, the amount of money that has been deposited
    @return:
    '''
    record={"time":CURR_TIME_STMP,
            "name":name,
            "amount":amount}
    DBConnection.Transaction.insert(record)
    return None

def convertStrtoDate(dict):
    dict['date']=datetime.datetime.strptime(dict['date'], '%d-%m-%Y').date()
    return dict
def convertDateToStr(dict):
    dict['date']=dict['date'].strftime("%d-%m-%Y")
    return dict

#allData = getAllData(as_dataframe=True)
#for game in allData:
#  print(game)
#  m=match(**game)
#  print(m)

#newMatch =betMatch(matchID='{}_TeamA_TeamB'.format(datetime.date.today()),date=datetime.date.today().__str__(),league='league',home_team='TeamA',away_team='TeamB',result='1',associateBets=[])
#saveMatch(newMatch)
#m=findMatch('19092020_TeamA_TeamB')
#print(m)
#deleteMatchFromUpcoming(date=datetime.date.today().__str__(),home_team='TeamA',away_team='TeamB')