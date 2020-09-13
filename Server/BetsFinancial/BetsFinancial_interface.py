#Interface of the Bets and Financials module

def addMatch(league ,date ,home_team, away_team) :
    '''
    @param league:string , the league that the match took place.
    @param date:datetime object, the date that the match took place.
    @param home_team:string, name of the home team.
    @param away_team:string, name of the way team.
    @return Match object that represent the match
    '''
    return None

def addMatch(league ,date ,home_team, away_team,result) :
    '''
    @param league:string , the league that the match took place.
    @param date:datetime object, the date that the match took place.
    @param home_team:string, name of the home team.
    @param away_team:string, name of the way team.
    @param result:string, the result of the match ('1','X','2')
    @return: Match object that represent the match
    '''
    return None

def setMatchResult(matchID,result):
    '''
    @param matchID:string, the ID of the match
    @param result:string, the result of the match ('1','X','2')
    @return: Match object that represent the match
    '''
    return None

def setSingleBet(receiptID, bet_value,bet_odd,matchID,result):
    '''
    @param receiptID:string, receipt ID which Winner issue
    @param bet_value:float, amount of money that place on the bet
    @param bet_odd:float, the odds that the bets holds, given by Winner
    @param matchID:string, the ID of the match that the bet place on
    @param result:string, the outcome of the match we expect ('1','X','2')
    @return:None
    '''
    return None

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
    return None

def depositFunds(name,amount):
    '''
    @param name:string, by who the deposit was made
    @param amount:float, how much money has been deposited
    @return:None
    '''
    return None

def withdraw(amount):
    '''
    @param amount:float, how much money has been deposited
    @return:None
    '''
    return None

