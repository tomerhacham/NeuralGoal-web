import math

import shap
import pandas as pd
from sklearn.preprocessing import LabelEncoder

from Server.NeuralNetwork.neuralnet import NeuralNet
from Optimization.Features.data_preproccesor import train_preprocess
shap.initjs()

COLUMNS_NAMES=['away_att','away_def','away_mid',
               'away_team_rank','away_team_received',
               'away_team_scored','home_att',
               'home_def','home_mid','home_team_rank','home_team_received','home_team_scored','result']
FEATURES_NAME=['away_att','away_def','away_mid',
               'away_team_rank','away_team_received',
               'away_team_scored','home_att',
               'home_def','home_mid','home_team_rank','home_team_received','home_team_scored']
Label_to_value_dict={'X':0,
                     '1':1,
                     '2':2}
value_to_label_dict={0:'X',1:'1',2:'2'}
data = pd.read_csv("mainTableCSV.csv")[COLUMNS_NAMES]
X=data.loc[:,FEATURES_NAME]
Y=data.loc[:,'result':'result']

Y['result']=Y['result'].map(Label_to_value_dict)
Y = pd.get_dummies(Y,columns=['result'], prefix='result')

Y.rename(columns={'result_0':'X','result_1':'1','result_2':'2'},inplace=True)

Split_point=math.ceil(data.shape[0]*0.8)
x_train=X[0:Split_point]
y_train=Y[0:Split_point]

x_test=X[Split_point:]
y_test=Y[Split_point:]

feature_names=FEATURES_NAME
class_names=['X','1','2']
ann=NeuralNet(x_train.shape[1])
ann.train(x_train,y_train,1)

explainer = shap.DeepExplainer(ann.model,x_train.sample(1000).to_numpy())

##FIRST GRAPH

number_of_samples = 1
# the sample should change to the match's feature to be explained
sample = x_test.sample(number_of_samples)
result=y_test.loc[sample.index]
np=ann.predict(sample)
#npp=pd.DataFrame(data=np)
#npp.set_index(sample.index,inplace=True)
#npp.rename(columns={0:'pred_x',1:'pred_1',2:'pred_2'},inplace=True)

prediction=pd.DataFrame(data=np,index=sample.index,columns=['pred_X','pred_1','pred_2'])

to_explain = sample.to_numpy()
shap_values = explainer.shap_values(X=to_explain, check_additivity=False)
features = to_explain
feature_names = FEATURES_NAME

shap.summary_plot
##END FIRST GRAPH