import argparse
import os
import sys
import numpy as np
import pandas as pd
import tensorflow as tf
from datetime import datetime
from typing import Dict
from tensorflow.keras.layers.experimental import preprocessing
from dataclasses import dataclass
from dataclasses_json import dataclass_json

# Constants
DATE_FORMAT='%Y-%m-%d'
#DATE_FORMAT='%d/%m/%Y'
COLUMNS=['league', 'date', 'round', 'home_team_name',
       'away_team_name', 'home_team_rank', 'away_team_rank', 'home_scored',
       'away_scored', 'result', 'home_shots', 'away_shots',
       'home_shots_on_target', 'away_shots_on_target', 'home_fouls',
       'away_fouls', 'home_corners', 'away_corners', 'home_yellow_cards',
       'away_yellow_cards', 'home_red_cards', 'away_red_cards', 'home_att',
       'away_att', 'home_def', 'away_def', 'home_mid', 'away_mid',
       'home_odds_nn', 'draw_odds_nn', 'away_odds_nn', 'home_odds_n',
       'draw_odds_n', 'away_odds_n']
SIDE=0
MATCH_DETAILS=1
AVG=30
EPOCHS=50
TEAM_RELATED_FEATURES = ['scored',
                         'received',
                         'shots',
                         'shots_on_target',
                         'corners',
                         'fouls',
                         'yellow_cards',
                         'red_cards',]

#region Classes
@dataclass_json
@dataclass
class raw_match:
    '''
    match-related data
    '''
    league:str
    date:datetime
    round:int
    home_team_name:str
    away_team_name:str
    home_team_rank:int
    away_team_rank:int
    home_scored:int
    away_scored:int
    home_att:int
    away_att:int
    home_def:int
    away_def:int
    home_mid:int
    away_mid:int
    home_shots:int
    away_shots:int
    home_shots_on_target:int
    away_shots_on_target:int
    home_corners:int
    away_corners:int
    home_fouls:int
    away_fouls:int
    home_yellow_cards:int
    away_yellow_cards:int
    home_red_cards:int
    away_red_cards:int
    home_odds_n:float
    draw_odds_n:float
    away_odds_n:float
    home_odds_nn:float
    draw_odds_nn:float
    away_odds_nn:float
    result:str
    def shots_ratio_calc(self):
        try:
            self.home_score_shots_ratio=float(self.home_scored/self.home_shots_on_target)*100
        except ZeroDivisionError:
            self.home_score_shots_ratio =0
        try:
            self.away_score_shots_ratio = float(self.away_scored / self.away_shots_on_target)*100
        except ZeroDivisionError:
            self.away_score_shots_ratio =0
    def __post_init__(self):
        #self.shots_ratio_calc()
        pass

class Team:
    def __init__(self,N:int, league: str, name: str):
        self.N=N
        self.league = league
        self.name = name
        self.matches = [] #lsit of tuple (side,match_details)
        # team_related_features
        self.avg_scored = -1
        self.avg_received = -1
        self.avg_shots = -1
        self.avg_shots_on_target = -1
        self.avg_corners = -1
        self.avg_fouls = -1
        self.avg_yellow_cards = -1
        self.avg_red_cards = -1
        self.avg_score_shots_ratio=-1
    def addMatch(self, side:str,match: raw_match):
        '''
        @param side:str {'home'/'away'}
        @param match:raw_match object
        @return:
        '''
        self.matches.append((side,match))
        if self.matches.__len__() < self.N:
            pass
        else:
            n_last_matches = self.matches[-self.N:]
            for feature in TEAM_RELATED_FEATURES:
                _value = 0
                for pair in n_last_matches:
                    attribute=completeStat(pair[SIDE],feature)
                    _value = _value + getattr(pair[MATCH_DETAILS], attribute)
                _value = float(_value / self.N)
                setattr(self,f'avg_{feature}', _value)
class Match:
    def __init__(self, home: Team, away: Team, raw_data: raw_match):
        self.home = home
        self.away = away
        self.raw_data = raw_data
        self.home.addMatch(side='home',match=raw_data)
        self.away.addMatch(side='away',match=raw_data)

    def convert(self) -> Dict:
        return {
            'league' : self.home.league,
            'date' : self.raw_data.date,
            'home_team_name' : self.raw_data.home_team_name,
            'away_team_name' : self.raw_data.away_team_name,
            'home_team_rank' : self.raw_data.home_team_rank,
            'away_team_rank' : self.raw_data.away_team_rank,
            'home_avg_scored' : self.home.avg_scored,
            'home_avg_received' : self.home.avg_received,
            'away_avg_scored' : self.away.avg_scored,
            'away_avg_received' : self.away.avg_received,
            'round' : self.raw_data.round,
            'home_att' : self.raw_data.home_att,
            'away_att' : self.raw_data.away_att,
            'home_def' : self.raw_data.home_def,
            'away_def' : self.raw_data.away_def,
            'home_mid' : self.raw_data.home_mid,
            'away_mid' : self.raw_data.away_mid,
            'home_avg_shots' : self.home.avg_shots,
            'away_avg_shots' : self.away.avg_shots,
            'home_avg_shots_on_target' : self.home.avg_shots_on_target,
            'away_avg_shots_on_target' : self.away.avg_shots_on_target,
            'home_avg_corners' : self.home.avg_corners,
            'away_avg_corners' : self.away.avg_corners,
            'home_avg_fouls' : self.home.avg_fouls,
            'away_avg_fouls' : self.away.avg_fouls,
            'home_avg_yellow_cards' : self.home.avg_yellow_cards,
            'away_avg_yellow_cards' : self.away.avg_yellow_cards,
            'home_avg_red_cards' : self.home.avg_red_cards,
            'away_avg_red_cards' : self.away.avg_red_cards,
            'home_odds_n' : self.raw_data.home_odds_n,
            'draw_odds_n' : self.raw_data.draw_odds_n,
            'away_odds_n' : self.raw_data.away_odds_n,
            'home_odds_nn' : self.raw_data.home_odds_nn,
            'draw_odds_nn' : self.raw_data.draw_odds_nn,
            'away_odds_nn' : self.raw_data.away_odds_nn,
            'result' : self.raw_data.result}
#endregion

#region Data Region
def completeStat(side:str, feature:str)->str:
    if side=='home' and feature=='received':
        return 'away_scored'
    elif side=='away' and feature=='received':
        return 'home_scored'
    else: return f'{side}_{feature}'

def parse_dates(dataframe)->pd.DataFrame:
    for index,row in dataframe.iterrows():
        try:
            datetime_obj=datetime.strptime(dataframe['date'][index],DATE_FORMAT)
            dataframe['date'][index]=datetime_obj
        except ValueError:
            try:
                datetime_obj = datetime.strptime(dataframe['date'][index],'%d/%m/%Y')
                dataframe['date'][index] = datetime_obj
            except Exception as e:
                print(e)
                exit(1)
    return dataframe

def unify(args)->pd.DataFrame:
    '''
    Unify all the CSVs file to one Dataframe
    :param args:
    :return:
    '''
    full_DataFrame=pd.DataFrame(columns=COLUMNS)
    for file in filter(lambda file_name: '.csv' in file_name,os.listdir(args.dir)):
        try:
            temp_df=pd.read_csv(f'{args.dir}\\{file}')[COLUMNS]
            full_DataFrame=full_DataFrame.append(temp_df,ignore_index=True,verify_integrity=True,)
        except Exception as e:
            print(f'ERROR at {file}\n {e}',file=sys.stderr)
    #full_DataFrame=parse_dates(full_DataFrame)
    full_DataFrame['date'] = pd.to_datetime(full_DataFrame['date'], format=DATE_FORMAT)
    full_DataFrame.sort_values(by='date',kind='mergesort', inplace=True, ascending=True)
    full_DataFrame.dropna(how='any',inplace=True)
    full_DataFrame.reset_index(inplace=True,drop=True)
    #full_DataFrame.to_csv('united.csv',date_format='%d/%m/%Y',columns=COLUMNS)
    print('Unify -- Done')
    return full_DataFrame

def organize(args,dataframe)->pd.DataFrame:
    '''
    organize the data and calculate all the avg stats
    :param args:
    :param dataframe:Pandas Dataframe which contains al the raw data
    :return: calculates dataframe
    '''
    # Initialize Data
    N=args.n
    calc_dataFrame = pd.DataFrame()
    Teams = {}
    all_teams = dataframe['home_team_name'].unique()
    print(f'Start calculation for avg of {N}')

    # construction Team's dictionary:
    print('Building Teams dictionary')
    for team in all_teams.tolist():
        if team not in Teams:
            filter = dataframe['home_team_name'] == team
            selected_frame = dataframe.where(filter, inplace=False).copy()
            selected_frame=selected_frame.dropna(how='all')
            selected_frame=selected_frame['league']
            league=selected_frame.iloc[0]
            Teams[team] = Team(N=int(N),league=league, name=team)
            print(f'{team} at {league} has been added')
    # sanity check
    if not (all_teams.__len__() == Teams.keys().__len__()) :
        print('WARNING: There is missing team',file=sys.stderr)

    # creating the calculated dataframe
    print('Start processing')
    total_rows=dataframe.shape[0]
    for index,row in dataframe.iterrows():
        a:Dict=row.to_dict()
        _raw:raw_match=raw_match(**a)
        obj_match:Match = Match(home=Teams[_raw.home_team_name], away=Teams[_raw.away_team_name], raw_data=_raw)
        to_insert:Dict = obj_match.convert()
        calc_dataFrame=calc_dataFrame.append(to_insert,ignore_index=True)
        print(f'{index+1}/{total_rows}',end='\r',flush=True)
        break

    calc_dataFrame.to_csv(f'{N}-avg-main-table.csv')
    #TODO: rename the columns for nice order
    print('calculation -- DONE')
    return calc_dataFrame
#endregion

#region Classification region
#region preprocess-Utils
# A utility method to create a tf.data dataset from a Pandas Dataframe
def df_to_dataset(dataframe,Label_to_value_dict,columns_convertor,shuffle=False, batch_size=32):
  dataframe = dataframe.copy()
  labels = dataframe.pop('result')
  labels=labels.map(Label_to_value_dict)
  labels = pd.get_dummies(labels, prefix='result')
  labels.rename(columns=columns_convertor,inplace=True)
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  ds = ds.prefetch(batch_size)
  return ds

def make_ds(dataframe,batch_size=32):
  dataframe = dataframe.copy()
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe)))
  ds = ds.batch(batch_size)
  ds = ds.prefetch(batch_size)
  return ds

def get_normalization_layer(name, dataset):
  # Create a Normalization layer for our feature.
  normalizer = preprocessing.Normalization()
  # Prepare a Dataset that only yields our feature.
  feature_ds = dataset.map(lambda x, y: x[name])
  # Learn the statistics of the data.
  normalizer.adapt(feature_ds)
  return normalizer

def get_category_encoding_layer(name, dataset, dtype, max_tokens=None):
  # Create a StringLookup layer which will turn strings into integer indices
  if dtype == 'string':
    index = preprocessing.StringLookup(max_tokens=max_tokens)
  else:
    index = preprocessing.IntegerLookup(max_values=max_tokens)
  # Prepare a Dataset that only yields our feature
  feature_ds = dataset.map(lambda x, y: x[name])
  # Learn the set of possible values and assign them a fixed integer index.
  index.adapt(feature_ds)
  # Create a Discretization for our integer indices.
  encoder = preprocessing.CategoryEncoding(max_tokens=index.vocab_size())
  # Prepare a Dataset that only yields our feature.
  feature_ds = feature_ds.map(index)
  # Learn the space of possible indices.
  encoder.adapt(feature_ds)
  # Apply one-hot encoding to our indices. The lambda function captures the
  # layer so we can use them, or include them in the functional model later.
  return lambda feature: encoder(index(feature))
#endregion

def preprocessData(dataframe):
    '''
    preprocess the data and return the pre-fetch datasets
    :param dataframe:
    :return:
    '''
    dataframe=dataframe.copy()
    batch_size = 32
    Label_to_value_dict = {'X': 0,
                           '1': 1,
                           '2': 2}
    value_to_label_dict = {0: 'X',
                           1: '1',
                           2: '2'}
    columns_convertor = {'result_0': 'X',
                         'result_1': '1',
                         'result_2': '2'}
    dataframe = dataframe.loc[(dataframe['home_avg_scored'] > -1) & (dataframe['away_avg_scored'] > -1)]
    dataframe.drop(inplace=True, columns=[ 'date', 'round', 'home_odds_nn','draw_odds_nn', 'away_odds_nn'])

    train=dataframe
    train = balance_dataset(train)
    train_ds = df_to_dataset(train,Label_to_value_dict ,value_to_label_dict ,shuffle=True, batch_size=batch_size)
    #val_ds = df_to_dataset(val, shuffle=False, batch_size=batch_size)
    #test_ds = df_to_dataset(test, shuffle=False, batch_size=batch_size)
    print('Processing data -- DONE')
    return train_ds


def balance_dataset(train):
    twos = train.loc[train['result'] == '2']
    xs = train.loc[train['result'] == 'X']
    oversampling = train.append(twos.sample(train.result.value_counts()['1'] - train.result.value_counts()['2']),
                                ignore_index=True, verify_integrity=True)
    oversampling = oversampling.append(xs.sample(train.result.value_counts()['1'] - train.result.value_counts()['X']),
                                       ignore_index=True, verify_integrity=True)
    print(oversampling.result.value_counts())
    if ((oversampling.result.value_counts()['1'] - oversampling.result.value_counts()['2']) != 0) or (
            (oversampling.result.value_counts()['1'] - oversampling.result.value_counts()['X']) != 0):
        print("Imbalance dataset")
    return oversampling


def build_train_model(train_ds):
    '''
    build the model and preprocess layers by the train dataset
    :param train_ds: pre-fetch dataset
    :return: fully build model
    '''
    encoded_features = []
    all_inputs = []
    encoding_layer = get_category_encoding_layer('home_team_rank', train_ds, dtype='int64')
    for column in ['home_team_rank', 'away_team_rank']:
        _input = tf.keras.Input(shape=(1,), name=column, dtype='int64')
        encoded_features.append(encoding_layer(_input))
        all_inputs.append(_input)

    league_col = tf.keras.Input(shape=(1,), name='league', dtype='string')
    encoding_layer = get_category_encoding_layer('league', train_ds, dtype='string')
    encoded_features.append(encoding_layer(league_col))
    all_inputs.append(league_col)

    encoding_layer = get_category_encoding_layer('home_team_name', train_ds, dtype='string')
    for column in ['home_team_name', 'away_team_name']:
        _input = tf.keras.Input(shape=(1,), name=column, dtype='string')
        encoded_features.append(encoding_layer(_input))
        all_inputs.append(_input)

    for attribute in ['att', 'mid', 'def']:
        encoding_layer = get_normalization_layer(f'home_{attribute}', train_ds)
        for team in ['home', 'away']:
            _input = tf.keras.Input(shape=(1,), name=f'{team}_{attribute}')
            encoded_features.append(encoding_layer(_input))
            all_inputs.append(_input)

    #for attribute in ['scored', 'received', 'shots_on_target', 'shots']:
    for attribute in ['scored', 'received']:
        encoding_layer = get_normalization_layer(f'home_avg_{attribute}', train_ds)
        for team in ['home', 'away']:
            _input = tf.keras.Input(shape=(1,), name=f'{team}_avg_{attribute}')
            encoded_features.append(encoding_layer(_input))
            all_inputs.append(_input)

    all_features = tf.keras.layers.concatenate(encoded_features)
    x = tf.keras.layers.Dense(128, activation="relu")(all_features)
    x = tf.keras.layers.Dropout(0.5)(x)
    x = tf.keras.layers.Dense(32, activation="relu")(x)
    x = tf.keras.layers.Dropout(0.5)(x)
    output = tf.keras.layers.Dense(3, activation=tf.nn.softmax)(x)
    model = tf.keras.Model(all_inputs, output)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
        metrics=['categorical_crossentropy',"categorical_accuracy",'accuracy'])

    print('Building and compiling model -- DONE')
    return model

def predict(calc_dataframe,upcoming_dataframe):
    train_ds=preprocessData(calc_dataframe)
    upcoming_ds = make_ds(upcoming_dataset)
    predictions=[]
    print('Start predictions')
    for i in range(AVG):
        max_acc=0
        while max_acc <0.5:
            model=build_train_model(train_ds)
            HistoryObject=model.fit(train_ds,epochs=EPOCHS,use_multiprocessing=True)
            max_acc=max(HistoryObject.history['accuracy'])

        predictions.append(model.predict(upcoming_ds))
        print(f'{i+1}/{AVG}',end='\r',flush=True)
    pred_stack=np.stack(predictions,axis=0)
    pred_stack=np.average(pred_stack,axis=0)
    predictipn_df=pd.DataFrame(data=pred_stack,index=upcoming_dataframe.index,columns=['pred_X','pred_1','pred_2'])
    columns=list(filter(lambda c: 'Unnamed' not in c ,upcoming_dataframe.columns.append(predictipn_df.columns))) #clearing out unwanted columns
    print('Predictions -- Done')
    return upcoming_dataframe.join(other=predictipn_df,how='inner',sort=False)[columns]

#endregion

def args_parsing():
    #Parsing arguments
    parser = argparse.ArgumentParser(description='full prediction suit')
    parser.add_argument('-dir',type=str,action="store",required=True,help='path for the CSVs files to be unify')
    parser.add_argument('-n',type=int,action="store",required=True,help='N to run the average tool')
    parser.add_argument('-upcoming',type=str,action="store",required=True,help='path to the upcoming CSV file')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args=args_parsing()
    #raw_dataframe=unify(args)
    #calc_dataframe=organize(args,raw_dataframe)
    calc_dataframe = pd.read_csv('3-avg-full_dataset.csv')
    calc_dataframe['date'] = pd.to_datetime(calc_dataframe['date'], format='%d/%m/%Y')
    upcoming_dataset=pd.read_csv(args.upcoming)
    predictions=predict(calc_dataframe,upcoming_dataset)
    predictions.to_csv('predictions.csv')

