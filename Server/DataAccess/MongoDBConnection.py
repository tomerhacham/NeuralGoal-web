import pymongo as pymongo

class MongoDBConnection:
    def __init__(self):
        client = pymongo.MongoClient(
            "mongodb+srv://Admin:NeuralGoalAdmin@neuralgoal.ewocw.mongodb.net/NeuralGoalDB?retryWrites=true&w=majority")

        # Development DB
        DevCollection = client["NeuralGoalDB-Development"]
        DevDBMainTable = DevCollection["MainTable"]
        DevDBUpcomingGames = DevCollection["UpcomingGames"]
        DevDBBetForms = DevCollection["BetForms"]
        DevDBFundStatus = DevCollection["FundStatus"]
        DevDBMatches = DevCollection["Matches"]
        DevDBTransaction = DevCollection["Transaction"]

        # Production DB
        ProductionCollection = client["NeuralGoalDB"]
        ProductionDBMainTable = ProductionCollection["MainTable"]
        ProductionDBUpcomingGames = ProductionCollection["Upcoming_Games"]

        self.DevDBMainTable = DevDBMainTable
        self.DevDBUpcomingGames=DevDBUpcomingGames
        self.DevDBBetForms=DevDBBetForms
        self.DevDBFundStatus=DevDBFundStatus
        self.DevDBMatches=DevDBMatches
        self.DevDBTransaction=DevDBTransaction
        self.ProductionDBMainTable = ProductionDBMainTable
        self.ProductionDBUpcomingGames = ProductionDBUpcomingGames

    def clearDB(self):
        self.ProductionDBMainTable.remove({})
        self.ProductionDBUpcomingGames.remove({})

