from Server.BetsFinancial.BetForm import BetForm
from Server.BetsFinancial.Match import Match
import Server.DataAccess.DBController as DBController
from Server.BetsFinancial.Match import Result

enumDICT = {
    '1':Result.Home,
    '2':Result.Away,
    'X':Result.Draw
}

def addMatch(league ,date ,home_team, away_team,result=None) :
    '''
    @param league:string , the league that the match took place.
    @param date:datetime object, the date that the match took place.
    @param home_team:string, name of the home team.
    @param away_team:string, name of the way team.
    @param result (OPTIONAL):string, the result of the match ('1','X','2')
    @return: Match object that represent the match
    '''
    try:
        matchID=generateMatchID()
        if result!=None:
            _result=enumDICT[result]
        newMatch = Match(matchID=matchID,league=league,date=date,home_team=home_team,away_team=away_team,result=_result)
        DBController.saveMatch(newMatch.toDTO())
        return newMatch
    except KeyError:
        print("Could not find the associate ENUM")
        return False
    except:
        print("An error has been occurred")
        return False

def setMatchResult(matchID,result):
    '''
    @param matchID:string, the ID of the match
    @param result:string, the result of the match ('1','X','2')
    @return: Match object that represent the match
    '''
    try:
        match=DBController.findMatch(matchID)
        result=enumDICT[result]
        match.setResult(result)
        DBController.updateMatch(match.toDTO())
        return match
    except KeyError:
        print("Could not find the associate ENUM")
        return False
    except:
        print("An error has been occurred")
        return False

def setSingleBet(receiptID, bet_value,bet_odd,matchID,result):
    '''
    @param receiptID:string, receipt ID which Winner issue
    @param bet_value:float, amount of money that place on the bet
    @param bet_odd:float, the odds that the bets holds, given by Winner
    @param matchID:string, the ID of the match that the bet place on
    @param result:string, the outcome of the match we expect ('1','X','2')
    @return:None
    '''
    try:
        match=DBController.findMatch(matchID)
        result=enumDICT[result]
        form=BetForm(receiptID, bet_value, bet_odd, [(match,result)])
        DBController.saveBetForm(form.toDTO())
        return True
    except KeyError:
        print("Could not find the associate ENUM")
        return False
    except:
        print("An error has been occurred")
        return False

def setDoubleBet(receiptID, bet_value,bet_odd,match1_ID,match2_ID,result_1,result_2):
    '''
    @param receiptID:string, receipt ID which Winner issue
    @param bet_value:float, amount of money that place on the bet
    @param bet_odd:float, the odds that the bets holds, given by Winner
    @param match1_ID:string, the ID of the first match that the bet place on
    @param match2_ID:string, the ID of the second match that the bet place on
    @param result_1:string, the outcome of the first match we expect ('1','X','2')
    @param result_2:string, the outcome of the second match we expect ('1','X','2')
    @return:None
    '''
    try:
        match1=DBController.findMatch(match1_ID)
        match2=DBController.findMatch(match2_ID)
        result1=enumDICT[result_1]
        result2=enumDICT[result_2]
        form=BetForm(receiptID, bet_value, bet_odd, [(match1,result1),(match2,result2)])
        DBController.saveBetForm(form.toDTO())
        return True
    except KeyError:
        print("Could not find the associate ENUM")
        return False
    except:
        print("An error has been occurred")
        return False

def generateMatchID():
    #TODO: implement
    return
