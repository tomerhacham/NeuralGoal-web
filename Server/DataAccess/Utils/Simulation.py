from datetime import datetime,timedelta
import pandas as pd
import numpy as np
from Server.NeuralNetwork.neuralnet import NeuralNet
from Server.NeuralNetwork.data_preproccesor import train_preprocess,prediction_preprocess

#Constant
DATE_FORMAT='%d/%m/%Y'
EPOCHS=10
AVG=2

Label_to_value_dict={'X':0,
                     '1':1,
                     '2':2}

value_to_label_dict={0:'X',
                     1:'1',
                     2:'2'}


def get_upcoming(df,simulated_date):
    ##FOR DEBUG
    DAYS=5
    to_return=None
    while to_return is None or to_return.empty:
        to_return = df.loc[(df['date'] > simulated_date) & (df['date'] <= (simulated_date + timedelta(days=DAYS)))]
        DAYS=DAYS+1
    return to_return

def get_data(general_Dataframe:pd.DataFrame,date:datetime.date):
    '''
    Return the data for learning available until date (exclude) and the upcoming games batch
    @param date: %d%m%y
    @return: Tuple(training_data,upcoming_games_batch)
    '''
    #print(f'type of date{type(date)}')
    #print(f'type of date_date{type(general_Dataframe["date"][0])}')
    data=general_Dataframe.loc[(general_Dataframe['date']<date) & (general_Dataframe['home_avg_scored']>-1)]
    upcoming_batch=get_upcoming(general_Dataframe.copy(),data['date'].max())
    return data,upcoming_batch

def date_parser(dataframe):
    for index,row in dataframe.iterrows():
       dataframe['date'][index]=datetime.strptime(row['date'], DATE_FORMAT).date()
    return dataframe

def simulate_week(data:pd.DataFrame,upcoming_batch:pd.DataFrame)->pd.DataFrame:
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
    return upcoming_batch.join(other=predictipn_df,how='inner',sort=False)


def execute():
    general_Dataframe=pd.read_csv('3-avg-full_dataset.csv')
    general_Dataframe=date_parser(general_Dataframe)
    start_year=2018
    data, upcoming_batch = get_data(general_Dataframe, datetime(start_year,7,1).date())
    formated_predictions=simulate_week(data,upcoming_batch)
    formated_predictions.to_csv('testest.csv')
    print(formated_predictions.to_markdown())

    pass

if __name__ == '__main__':
    execute()