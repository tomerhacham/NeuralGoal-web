from Server.BetsFinancial.BetForm import BetForm
from enum import Enum
class Result(Enum):
    Home=1
    Away=2
    Draw=3

class Match:
    def __init__(self,matchID,league,date,home_team,away_team,result=None):
        '''
        @param MatchID:string,ID of the match
        @param league:string, name of the league
        @param date:datetime, the date that the game is occurring
        @param home_team:string, name of the home team
        @param away_team:string, name of the away team
        @param result:Result enum
        '''
        self._associateBets=[]
        self._matchID=matchID
        self._league=league
        self._date=date
        self._home_team=home_team
        self._away_team=away_team
        self._result=result

    def homeWin(self):
        self._result=Result.Home
    def awayWin(self):
        self._result=Result.Away
    def draw(self):
        self._result=Result.Draw
    def registerBetForm(self,form):
        self._associateBets.append(form)
    def notifyAll(self):
        for form in self._associateBets: form.checkWin()