import pymongo as pymongo

class MongoDBConnection:
    def __init__(self,mode):
        '''
        @param mode:str ['dev','production','explore']
        '''
        client = pymongo.MongoClient(
            "mongodb+srv://Admin:NeuralGoalAdmin@neuralgoal.ewocw.mongodb.net/NeuralGoalDB?retryWrites=true&w=majority")
        if mode=='dev' or mode=='production':
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
        else:
            #mode=='explore'
            Collections = client["NeuralGoalDB-Feature_Engineering"]
            self.RawData=Collections["RawData"]
            self.MainTable = Collections["MainTable"]

    def clearDB(self):
        self.ProductionDBMainTable.remove({})
        self.ProductionDBUpcomingGames.remove({})

