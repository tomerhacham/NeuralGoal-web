import pymongo as pymongo

class MongoDBConnection:
    def __init__(self,mode):
        client = pymongo.MongoClient(
            "mongodb+srv://Admin:NeuralGoalAdmin@neuralgoal.ewocw.mongodb.net/NeuralGoalDB?retryWrites=true&w=majority")
        if mode=='dev':
            # Development DB
            Collections = client["NeuralGoalDB-Development"]
        else:
            # Production DB
            Collections = client["NeuralGoalDB"]

        self.MainTable = Collections["MainTable"]
        self.UpcomingGames = Collections["UpcomingGames"]
        self.BetForms = Collections["BetForms"]
        self.FundStatus = Collections["FundStatus"]
        self.Matches = Collections["Matches"]
        self.Transaction = Collections["Transaction"]

    def clearDB(self):
        self.ProductionDBMainTable.remove({})
        self.ProductionDBUpcomingGames.remove({})

