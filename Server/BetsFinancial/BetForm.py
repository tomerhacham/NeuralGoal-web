from datetime import datetime
from functools import reduce
import Server.BetsFinancial.FundsController as funds


class BetForm:
    def __init__(self, receiptID, bet_value, bet_odd, bets_list):
        '''
        @param receiptID:string, receipt ID which Winner issue
        @param bet_value:float, amount of money that place on the bet
        @param bet_odd:float, the odds that the bets holds, given by Winner
        @param bets_list:list of tuples that each tuple hold Match object and result e.g (Match,result)
        '''
        self._date = datetime.date()
        self._receiptID = receiptID
        self._bet_value = bet_value
        self._bet_odd = bet_odd
        self._isWin = False
        self._profitExpectation = (self._bet_odd * self._bet_value) - 1
        self._bets = bets_list

    def checkWin(self):
        '''
        Iterate all over the bets with MAP func and return boolean if
        the the expected result is the outcome of the match.
        Using reduce to check if all the bets were corrects, if so update the funds with the reward
        @return:boolean
        '''
        m = map(lambda bet: bet[0].result == bet[1], self._bets)
        if reduce(lambda prev, curr: prev and curr, m):
            self.notifyWin()  # notify the fundsController and update the fund with the winning amount
            return True
        return False

    def notifyWin(self):
        funds.addWinningMoney(self._bet_odd * self._bet_value)
