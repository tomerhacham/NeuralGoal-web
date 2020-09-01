import pymongo as pymongo

class MongoDBConnection:
    def __init__(self):
        client = pymongo.MongoClient(
            "mongodb+srv://Admin:NeuralGoalAdmin@neuralgoal.ewocw.mongodb.net/NeuralGoalDB?retryWrites=true&w=majority")

        # Development DB
        DevCollection = client["NeuralGoalDB-Development"]
        DevDBGames = DevCollection["Games"]

        # Production DB
        ProductionCollection = client["NeuralGoalDB"]
        ProductionDBMainTable = ProductionCollection["Main_Table"]
        ProductionDBUpcomingGames = ProductionCollection["Upcoming_Games"]

        self.DevDBGames = DevDBGames
        self.ProductionDBMainTable = ProductionDBMainTable
        self.ProductionDBUpcomingGames = ProductionDBUpcomingGames

    def clearDB(self):
        self.ProductionDBMainTable.remove({})
        self.ProductionDBUpcomingGames.remove({})

