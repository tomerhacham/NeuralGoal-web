import pandas as pd
COLUMNS_NAMES=['away_att','away_def','away_mid','away_odds_n',
               'away_team_rank','away_team_received',
               'away_team_scored','draw_odds_n','home_att',
               'home_def','home_mid','home_odds_n','home_team_rank','home_team_received','home_team_scored','result']
def fix_strings():
    data = pd.read_csv("mainTableCSV.csv")
    for i,row in data.iterrows():
        if data.loc[i,'result']=='TRUE' or data.loc[i,'result']=='true' :
            data.loc[i,'result']='1'
    data.to_csv('mainTableCSV.csv')
def select_columns():
    from sklearn.preprocessing import LabelEncoder
    data = pd.read_csv("mainTableCSV.csv")[COLUMNS_NAMES]
    x = data.loc[:, 'away_att':'home_team_scored']
    y = data.loc[:, 'result':]
    labelencoder = LabelEncoder()
    y['result'] = labelencoder.fit_transform(y['result'])  # X:2 ,2:1, 1:0
    print('#result label Encoding')
    le_name_mapping = dict(zip(labelencoder.classes_, labelencoder.transform(labelencoder.classes_)))
    print(le_name_mapping)
    y = pd.get_dummies(y['result'], prefix="result")
    return x,y

fix_strings()