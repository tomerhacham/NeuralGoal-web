from datetime import datetime,timedelta
from typing import Tuple
import argparse
import pandas as pd
import numpy as np
import sys; sys.path.insert(0, '../../..')
from Server.NeuralNetwork.neuralnet import NeuralNet
from Server.NeuralNetwork.data_preproccesor import train_preprocess,prediction_preprocess

#Constant
DATE_FORMAT='%d/%m/%Y'
COLUMNS=['league', 'date', 'home_team_name','away_team_name','home_odds_nn', 'draw_odds_nn', 'away_odds_nn', 'pred_X','pred_1','pred_2','result']
EPOCHS=100
AVG=30

Label_to_value_dict={'X':0,
                     '1':1,
                     '2':2}

value_to_label_dict={0:'X',
                     1:'1',
                     2:'2'}


def get_next_upcoming_batch(df, simulated_date):
    DAYS=5
    to_return=None
    while to_return is None or to_return.empty:
        to_return = df.loc[(df['date'] > simulated_date) & (df['date'] <= (simulated_date + timedelta(days=DAYS)))]
        DAYS=DAYS+1
    return to_return

def get_available_data(general_Dataframe:pd.DataFrame, date:datetime.date)-> Tuple[pd.DataFrame, pd.DataFrame]:
    '''
    Return the data for learning available until date (exclude) and the upcoming games batch
    @param date: datetime.date object [%d%m%y]
    @return: Tuple[(]training_data,upcoming_games_batch]
    '''
    data=general_Dataframe.loc[(general_Dataframe['date']<date) & (general_Dataframe['home_avg_scored']>-1)]
    upcoming_batch=get_next_upcoming_batch(general_Dataframe.copy(), data['date'].max())
    return data,upcoming_batch

def date_parser(dataframe:pd.DataFrame)->pd.DataFrame:
    '''
    Utility function for prasing and replace date string to datetime object inside pandas Dataframe
    @param dataframe:pd.DataFrame
    @return:pd.DataFrame
    '''
    for index,row in dataframe.iterrows():
       dataframe['date'][index]=datetime.strptime(row['date'], DATE_FORMAT).date()
    return dataframe

def simulate_week(data:pd.DataFrame,upcoming_batch:pd.DataFrame)->pd.DataFrame:
    '''
    Simulate a prediction for given week. The function will get the available data
     that could be found previously to this week and predict the games that has been occurred during that week
    @param data:pd.DataFrame
    @param upcoming_batch:pd.DataFrame
    @return:pd.DataFrame, all the details of the match including the prediction and the actual result
    '''
    X,Y=train_preprocess(data)
    upcoming_batch_=prediction_preprocess(upcoming_batch)
    predictions=[]
    for i in range(AVG):
        max_acc=0
        while max_acc <0.5:
            ann=NeuralNet(X.shape[1])
            HistoryObject=ann.train(x=X,y=Y,epochs=EPOCHS,use_multiprocessing=True)
            max_acc=max(HistoryObject.history['accuracy'])

        predictions.append(ann.predict(upcoming_batch_))
    pred_stack=np.stack(predictions,axis=0)
    pred_stack=np.average(pred_stack,axis=0)
    predictipn_df=pd.DataFrame(data=pred_stack,index=upcoming_batch_.index,columns=['pred_X','pred_1','pred_2'])
    column=list(filter(lambda c: 'Unnamed' not in c ,set(COLUMNS).union(predictipn_df.columns))) #clearing out unwanted columns
    return upcoming_batch.join(other=predictipn_df,how='inner',sort=False)[column]

def make_partition(before,after,upcoming_batch)->pd.DataFrame:
    before= pd.concat([before,upcoming_batch])
    after=pd.concat([after,upcoming_batch]).drop_duplicates(keep=False)
    return before,after

def execute():
    args=parse_arguments()
    print(args)
    start_year=args.year
    general_Dataframe=pd.read_csv(args.i)
    general_Dataframe['date']=pd.to_datetime(general_Dataframe['date'],format=DATE_FORMAT)
    general_Dataframe=general_Dataframe.loc[(general_Dataframe['home_avg_scored']>float(-1)) & (general_Dataframe['away_avg_scored']>float(-1))]

    before=general_Dataframe.loc[general_Dataframe['date']<datetime(start_year, 7, 1)]
    after=pd.concat([general_Dataframe,before]).drop_duplicates(keep=False)
    formated_predictions=pd.DataFrame()
    Counter=1
    while not after.empty :
        upcoming_batch=get_next_upcoming_batch(df=after.copy(),simulated_date=before['date'].max())
        week_prediction = simulate_week(before, upcoming_batch).reindex(columns=COLUMNS)
        week_prediction.to_csv(f'prediction-{Counter}.csv')
        formated_predictions=formated_predictions.append(week_prediction,verify_integrity=True,sort=False)
        Counter=Counter+1
        print(formated_predictions.to_markdown())
        before,after=make_partition(before,after,upcoming_batch)
    formated_predictions.to_csv('final-pred.csv')


def parse_arguments():
    #Parsing arguments
    parser = argparse.ArgumentParser(description='Simulator for a given year')
    parser.add_argument('-year',type=int,action='store',required=True,help='the year to simulate')
    parser.add_argument('-i',type=str,action='store',required=True,help='input file')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    execute()