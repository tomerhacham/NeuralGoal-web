from datetime import datetime


class BetForm:
    def __init__(self,receiptID,bet_value,bet_odd,bets_list):
        '''
        @param receiptID:string, receipt ID which Winner issue
        @param bet_value:float, amount of money that place on the bet
        @param bet_odd:float, the odds that the bets holds, given by Winner
        @param bets_list:list of tuples that each tuple hold Match object and result e.g (Match,result)
        '''
        self.date=datetime.date()
        self.receiptID=receiptID
        self.bet_value=bet_value
        self.bet_odd=bet_odd
        self.isWin=False
        self.profitExpectation=(self.bet_odd*self.bet_value)-1
        self.bets=bets_list
