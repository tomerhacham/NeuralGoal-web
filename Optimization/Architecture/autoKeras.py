import math
import sys
import time
import autokeras as ak
import pandas as pd
from contextlib import redirect_stdout


COLUMNS_NAMES=['away_att','away_def','away_mid',
               'away_team_rank','away_team_received',
               'away_team_scored','home_att',
               'home_def','home_mid','home_team_rank','home_team_received','home_team_scored','result']
FEATURES_NAME=['away_att','away_def','away_mid',
               'away_team_rank','away_team_received',
               'away_team_scored','home_att',
               'home_def','home_mid','home_team_rank','home_team_received','home_team_scored']
data = pd.read_csv("../mainTableCSV.csv")[COLUMNS_NAMES]

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

data = pd.read_csv("../mainTableCSV.csv")[COLUMNS_NAMES]
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

# Initialize the structured data classifier.
clf = ak.StructuredDataClassifier(column_names=FEATURES_NAME,num_classes=3,multi_label=True,overwrite=True,max_trials=30)
# Feed the structured data classifier with training data.
clf.fit(x=x_train,y=y_train,epochs=30,shuffle=False)

model=clf.export_model()
with open('model-summary-{}.txt'.format((int)(time.time())), 'w+') as f:
    with redirect_stdout(f):
        model.summary()
    with redirect_stdout(sys.stdout):
        model.summary()

print(type(model))  # <class 'tensorflow.python.keras.engine.training.Model'>
try:
    model.save("model_autokeras", save_format="tf")
except:
    model.save("model_autokeras.h5")
