import math

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

COLUMNS_NAMES=['home_team_rank', 'away_team_rank', 'home_avg_scored', 'home_avg_received', 'away_avg_scored',
               'away_avg_received', 'home_att', 'away_att', 'home_def', 'away_def', 'home_mid', 'away_mid',
               'home_avg_shots', 'away_avg_shots', 'home_avg_shots_on_target', 'away_avg_shots_on_target',
               'home_avg_corners', 'away_avg_corners', 'home_avg_fouls', 'away_avg_fouls', 'home_avg_yellow_cards',
               'away_avg_yellow_cards', 'home_avg_red_cards', 'away_avg_red_cards', 'home_odds_n', 'draw_odds_n',
               'away_odds_n', 'home_odds_nn', 'draw_odds_nn', 'away_odds_nn', 'result']

FEATURES_NAME=['home_team_rank', 'away_team_rank', 'home_avg_scored', 'home_avg_received', 'away_avg_scored',
               'away_avg_received', 'home_att', 'away_att', 'home_def', 'away_def', 'home_mid', 'away_mid',
               'home_avg_shots', 'away_avg_shots', 'home_avg_shots_on_target', 'away_avg_shots_on_target',
               'home_avg_corners', 'away_avg_corners', 'home_avg_fouls', 'away_avg_fouls', 'home_avg_yellow_cards',
               'away_avg_yellow_cards', 'home_avg_red_cards', 'away_avg_red_cards', 'home_odds_n', 'draw_odds_n',
               'away_odds_n','round']

Label_to_value_dict={'X':0,
                     '1':1,
                     '2':2}

value_to_label_dict={0:'X',
                     1:'1',
                     2:'2'}
columns_convertor={'result_0':'X',
                   'result_1':'1',
                   'result_2':'2'}


#TODO: needs to fix for pulling data from mongoDB
def train_preprocess(df, test_and_split=False):
    X= df.loc[:,FEATURES_NAME]
    Y = df.loc[:,'result':'result']
    # convert categorical to numerical value and encode
    Y['result'] = Y['result'].map(Label_to_value_dict)
    Y = pd.get_dummies(Y, columns=['result'], prefix='result')
    Y.rename(columns=columns_convertor, inplace=True)

    if test_and_split:
        # splitting the data to train-test datasets
        Split_point = math.ceil(df.shape[0] * 0.8)
        x_train = X[0:Split_point]
        y_train = Y[0:Split_point]

        x_test = X[Split_point:]
        y_test = Y[Split_point:]
        return x_train,x_test,y_train,y_test
    else:
        return X,Y

def prediction_preprocess(upcoming_df):
    return upcoming_df.loc[:,FEATURES_NAME]
