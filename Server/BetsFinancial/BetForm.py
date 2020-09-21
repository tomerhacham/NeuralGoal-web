from datetime import date
from functools import reduce
from typing import List, Tuple,TypeVar
from Server.DataAccess.DTOs import betForm as dto

_MATCH=0
_EXPECTEDRESULT=1
T1= TypeVar('T1')
T2= TypeVar('T2')


class BetForm:
    def __init__(self,receiptID ,bet_value, bet_odd, bets_list,date=date.today(),isWin=False):
        '''
        @param receiptID:string, receipt ID which Winner issue
        @param bet_value:float, amount of money that place on the bet
        @param bet_odd:float, the odds that the bets holds, given by Winner
        @param bets_list:list of tuples that each tuple hold Match object and result e.g (Match,resultENUM)
        '''
        self._date = date
        self._receiptID = receiptID
        self._bet_value = bet_value
        self._bet_odd = bet_odd
        self._isWin = isWin
        self._profitExpectation = (self._bet_odd * self._bet_value) - 1
        self._bets = bets_list

    def checkWin(self):
        '''
        Iterate all over the bets with MAP func and return boolean if
        the the expected result is the outcome of the match.
        Using reduce to check if all the bets were corrects, if so update the funds with the reward
        @return:boolean
        '''
        if not self._isWin:
            m = list(map(lambda bet: bet[_MATCH].result is bet[_EXPECTEDRESULT], self._bets))
            if reduce(lambda prev, curr: prev and curr, m):
                self._isWin=True
                self.notifyWin()  # notify the fundsController and update the fund with the winning amount
                return True
        return False
    def notifyWin(self):
        import Server.BetsFinancial.FundsController as funds
        funds.addWinningMoney(self._bet_odd * self._bet_value)
    def toDTO(self):
        flatBets=list(map(lambda pair:(pair[_MATCH]._matchID,pair[_EXPECTEDRESULT].value),self._bets))
        return dto(self._receiptID,self._date,self._bet_value,self._bet_odd,self._isWin,self._profitExpectation,flatBets)
    def __repr__(self):
        return 'BetForm(receiptID:{}, date:{},bet_value:{}, bet_odd:{}, bets_list:{}, isWin:{}, profitExpectation:{}, bets:{})'\
            .format(self._receiptID,self._date,self._date,self._bet_value,self._bet_odd,self._isWin,self._profitExpectation,
                    list(map(lambda pair:'({},{})'.format(pair[_MATCH],pair[_EXPECTEDRESULT]),self._bets)))

    def __eq__(self, other):
        x= (isinstance(other, BetForm) and
         self._date == other._date and
         self._receiptID == other._receiptID and
         self._bet_value == other._bet_value and
         self._bet_odd == other._bet_odd and
         self._isWin == other._isWin and
         self._profitExpectation == other._profitExpectation)
        return x

    @staticmethod
    def constructor(dto:dto,bets_list:List[Tuple[T1,T2]]):
        return BetForm(receiptID=dto.receiptID,date=dto.date ,bet_value= dto.bet_value,bet_odd= dto.bet_odd,bets_list= bets_list,isWin=dto.isWin)
