from Server.DataAccess.DTOs import betMatch as dto
from enum import Enum
class Result(Enum):
    Home='1'
    Away='2'
    Draw='X'

    @classmethod
    def from_str(cls, str):
        x= cls._value2member_map_
        value = cls._value2member_map_[str]
        if value==None:
            raise NotImplementedError
        else:
            return value
#        print(x)
        #else:
        #    raise NotImplementedError

class Match:
    def __init__(self,matchID,league,date,home_team,away_team,result=None):
        '''
        @param MatchID:string,ID of the match
        @param league:string, name of the league
        @param date:datetime, the date that the game is occurring
        @param home_team:string, name of the home team
        @param away_team:string, name of the away team
        @param result (OPTIONAL):Result enum or None
        '''
        self._associateBets=[]
        self._matchID=matchID
        self._league=league
        self._date=date
        self._home_team=home_team
        self._away_team=away_team
        self._result=result

    def setResult(self,result):
        '''
        @param result:Enum
        @return:
        '''
        self._result=result
        self.notifyAll()

    def associateBetForm(self,receiptID):
        self._associateBets.append(receiptID)

    def toDTO(self):
        return dto(self._matchID,self._date,self._league,self._home_team,self._away_team,self._result.value,self._associateBets)

    def __repr__(self):
        return 'Match(matchID:{}, league:{}, date:{}, home_team_name:{}, away_team_name:{}, result:{})'.format(self._matchID,self._league,self._date,self._home_team,self._away_team,self._result)
    def __eq__(self, other):
        return (isinstance(other,Match) and
                self._matchID==other._matchID and
                self._league==other._league and
                 self._date==other._date and
                 self._home_team==other._home_team and
                 self._away_team==other._away_team and
                 self._result==other._result)

    @staticmethod
    def constructor(dto:dto):
        return Match(dto.matchID,dto.league,dto.date,dto.home_team_name,dto.away_team_name,Result.from_str(dto.result))