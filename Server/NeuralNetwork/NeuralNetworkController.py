import numpy as np
import pandas as pd
import Server.NeuralNetwork.data_preproccesor as data_preprocessor
from Server.NeuralNetwork.neuralnet import NueralNet
from Server.Persistent import DBController

AVG = 30
EPOC = 30

def predict(league):
    """
    @param league: string that represent the league
    @return: Pandas DataFrame of all the necessary information after the prediction
    """
    predictions = []
    #region Data
    all_data=DBController.getAllData()
    upcoming_games=DBController.getUpcomingGames(league)
    x,y = data_preprocessor.train_preprocess(all_data)
    to_predict = data_preprocessor.prediction_preprocess(upcoming_games)
    #endregion
    #region ANN
    for i in range(0, AVG):
        ann = NueralNet(x.shape[1])
        ann.train(x, y, EPOC)
        predictions.append(ann.predict(to_predict))
    #endregion
    #region Calculate avg of predictions
    lines = predictions[0].shape[0]
    columns = predictions[0].shape[1]
    avgPrediction = np.zeros((lines, columns))
    for line in range(lines):
        for cell in range(columns):
            sum = 0
            for prediction in predictions:
                sum = sum + prediction[line, cell]
            avgPrediction[line, cell] = sum/AVG
    #endregion
    #region Converting avgPrediction to pandas DataFrame
    y_pred, indexes =apply_indexes(avgPrediction,upcoming_games)
    details=upcoming_games.iloc[indexes]
    details=details[['league','date','home_team_name','away_team_name','home_odds_nn','draw_odds_nn','away_odds_nn']]
    final = pd.concat([details,y_pred],axis=1,sort=False)

    #slashDirection = "\\"
    #if platform.system() == "Darwin":
    #    slashDirection = "//"
    #pathToSave = 'outputs{}predictions-Week-{}.csv'.format(slashDirection,_round)
    #final.to_csv(pathToSave,index=False)
    #endregion
    return final

def apply_indexes(y_pred, y_test):
    """
    @param y_pred: Numpy array
    @param  y_test: Pandas DataFrame
    @return: y_pred as Pandas DataFrame with indexes
    """
    indexes = list(y_test.index.values.tolist())
    y_pred_df = pd.DataFrame(data=y_pred, index=indexes, columns=['pred_1','pred_2','pred_X'])
    return y_pred_df,indexes