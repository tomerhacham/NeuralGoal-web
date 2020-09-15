import Server.DataAccess.DBController as DBController

def depositFunds(name,amount):
    '''
    @param name:string, by who the deposit was made
    @param amount:float, how much money has been deposited
    @return:None
    '''
    updateFund(name,amount)
    return True

def withdraw(amount):
    '''
    @param amount:float, how much money to withdraw
    @return:None
    '''
    updateFund('withdraw',-amount)
    return None

def addWinningMoney(amount):
    '''
    @param amount:float, the amount of money that the bet has ben yield
    @return:None
    '''
    updateFund('winningForm',amount)
    return None

def updateFund(name,amount):
    '''
    @permission private function to generalize the changes in the funds and the connection with the DB
    @param name:string, by who the action has been made
    @param amount:float
    @return:
    '''
    currentStatus=DBController.getLastFundStatus()
    DBController.updateFundStatus(currentStatus+amount)
    DBController.saveTransaction(name, amount)
    return