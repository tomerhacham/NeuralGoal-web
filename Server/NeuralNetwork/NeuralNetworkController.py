import numpy as np
import pandas as pd
import Server.NeuralNetwork.data_preproccesor as data_preprocessor
from Server.NeuralNetwork.neuralnet import NeuralNet
from Server.Persistent import DBController
from Server.Persistent.DTOs import prediction as Prediction

AVG = 30
EPOC = 30

def predict(league):
    """
    @param league: string that represent the league (can be 'all')
    @return: list of predictions DTOs
    """
    predictions = []
    #region Data
    all_data=DBController.getAllData(as_dataframe=True)
    upcoming_games=DBController.getUpcomingGames(league,as_dataframe=True)
    x,y = data_preprocessor.train_preprocess(all_data)
    to_predict = data_preprocessor.prediction_preprocess(upcoming_games)
    #endregion
    #region ANN
    for i in range(0, AVG):
        ann = NeuralNet(x.shape[1])
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

    prediction_dtos=[]
    for row in final.shape[0]:
        prediction_dtos.append(Prediction(final.loc[row,'leauge'],final.loc[row,'date'],final.loc[row,'home_team_name'],
                               final.loc[row,'away_team_name'],final.loc[row,'home_odds_nn'],final.loc[row,'draw_odds_nn'],
                               final.loc[row,'away_odds_nn'],final.loc[row,'pred_1'],final.loc[row,'pred_2'],
                               final.loc[row,'pred_x'],calc_exp(predictions=[final.loc[row,'pred_1'],
                                                                             final.loc[row,'pred_x'],
                                                                             final.loc[row,'pred_2']],
                                                                odds=[final.loc[row,'home_odds_nn'],
                                                                      final.loc[row,'draw_odds_nn'],
                                                                      final.loc[row, 'away_odds_nn']]),final.loc[row,'result']))
    return prediction_dtos

def apply_indexes(y_pred, y_test):
    """
    @param y_pred: Numpy array
    @param  y_test: Pandas DataFrame
    @return: y_pred as Pandas DataFrame with indexes
    """
    indexes = list(y_test.index.values.tolist())
    y_pred_df = pd.DataFrame(data=y_pred, index=indexes, columns=['pred_1','pred_2','pred_X'])
    return y_pred_df,indexes

def calc_exp(predictions,odds):
    '''
    @param predictions: array of 3 possibilities
    @param odds: array of 3 odds
    @return: expected value
     '''
    predictions=np.array(predictions)
    maxElement=np.amax(predictions)
    return odds[maxElement]*predictions[maxElement]