import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
COLUMNS_NAMES=['away_att','away_def','away_mid','away_odds_n',
               'away_team_rank','away_team_received',
               'away_team_scored','draw_odds_n','home_att',
               'home_def','home_mid','home_odds_n','home_team_rank','home_team_received','home_team_scored','result']
#TODO: needs to fix for pulling data from mongoDB
def train_preprocess(df, test_and_split=False):
    x = df.loc[:, 'home_team_rank':'away_odds_n']
    y = df.loc[:, 'result':]
    labelencoder = LabelEncoder()
    y['result'] = labelencoder.fit_transform(y['result'])  # X:2 ,2:1, 1:0
    print('#result label Encoding')
    le_name_mapping = dict(zip(labelencoder.classes_, labelencoder.transform(labelencoder.classes_)))
    print(le_name_mapping)
    y = pd.get_dummies(y['result'], prefix="result")

    if test_and_split:
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2, shuffle=False)
        return x_train, x_test, y_train, y_test
    else:
        return x,y

def prediction_preprocess(upcoming_df):
    return upcoming_df.loc[:, 'home_team_rank':'away_odds_n']
