from datetime import datetime
import pandas as pd
from Server.NeuralNetwork.neuralnet import NeuralNet
from Server.NeuralNetwork.data_preproccesor import train_preprocess,prediction_preprocess

#Constant
DATE_FORMAT='%d/%m/%Y'
EPOCHS=100
AVG=30


def get_upcoming():
    pass

def get_data(general_Dataframe:pd.DataFrame,date:datetime.date):
    '''
    Return the data for learning available until date (exclude) and the upcoming games batch
    @param date: %d%m%y
    @return: Tuple(training_data,upcoming_games_batch)
    '''
    #print(f'type of date{type(date)}')
    #print(f'type of date_date{type(general_Dataframe["date"][0])}')
    data=general_Dataframe.loc[general_Dataframe['date']<date]
    upcoming_batch=get_upcoming()
    return data,upcoming_batch

def date_parser(dataframe):
    for index,row in dataframe.iterrows():
       dataframe['date'][index]=datetime.strptime(row['date'], DATE_FORMAT).date()
    return dataframe

def simulate_week(data:pd.DataFrame,upcoming_batch:pd.DataFrame)->pd.DataFrame:
    X,Y=train_preprocess(data)
    upcoming_batch=prediction_preprocess(upcoming_batch)
    sum_predictions=[0 for x in Y.shape[1]]
    for i in range(AVG):
        ann=NeuralNet(X.shape[0])
        min_acc=0
        while min_acc <0.5:
            HistoryObject=ann.train(x=X,y=Y,epochs=EPOCHS,use_multiprocessing=True)
            min_acc=min(HistoryObject.history['accuracy'])
    prediction=ann.predict(upcoming_batch)
    for i in range(Y.shape[1]):
        sum_predictions[i]= sum_predictions[i]+prediction[i]
    ##FOR DEBUG
    toReturn= map(lambda sum:float(sum/AVG),sum_predictions)
    ##FOR DEBUG

    predictipn_df=pd.DataFrame(data=toReturn,index=upcoming_batch.index,columns=['pred_X','pred_1','pred_2'])
    final_dataframe=upcoming_batch.join(other=predictipn_df,how='inner',sort=False)
    return final_dataframe

def execute():
    general_Dataframe=pd.read_csv('3-avg-full_dataset.csv')
    general_Dataframe=date_parser(general_Dataframe)
    data, upcoming_batch = get_data(general_Dataframe, datetime.now().date())

    pass

if __name__ == '__main__':
    execute()