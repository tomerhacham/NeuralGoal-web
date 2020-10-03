import math
import autokeras as ak
import pandas as pd
from sklearn.preprocessing import LabelEncoder

COLUMNS_NAMES=['away_att','away_def','away_mid',
               'away_team_rank','away_team_received',
               'away_team_scored','home_att',
               'home_def','home_mid','home_team_rank','home_team_received','home_team_scored','result']
FEATURES_NAME=['away_att','away_def','away_mid',
               'away_team_rank','away_team_received',
               'away_team_scored','home_att',
               'home_def','home_mid','home_team_rank','home_team_received','home_team_scored']
data = pd.read_csv("../mainTableCSV.csv")[COLUMNS_NAMES]
Split_point=math.ceil(data.shape[0]*0.8)
train_set=data[0:Split_point]
test_set=data[Split_point:]
x_train=train_set.loc[:, FEATURES_NAME]
y_train=train_set.loc[:, 'result':'result']
x_test=test_set.loc[:, FEATURES_NAME]
y_test=test_set.loc[:, 'result':'result']
labelencoder = LabelEncoder()
y_train = labelencoder.fit_transform(y_train['result'])  # X:2 ,2:1, 1:0
y_test = labelencoder.fit_transform(y_test['result'])  # X:2 ,2:1, 1:0
print('#result label Encoding')
le_name_mapping = dict(zip(labelencoder.classes_, labelencoder.transform(labelencoder.classes_)))
print(le_name_mapping)
y_train = pd.get_dummies(y_train, prefix="result")
y_test = pd.get_dummies(y_test, prefix="result")

# Initialize the structured data classifier.
clf = ak.StructuredDataClassifier(column_names=FEATURES_NAME,multi_label=True,overwrite=True,max_trials=10)
# Feed the structured data classifier with training data.
clf.fit(x=x_train,y=y_train,epochs=25)

# Predict with the best model.
#predicted_y = clf.predict(x_test)
#df=pd.DataFrame(clf.predict(x_test))
#print(df.to_markdown())
# Evaluate the best model with testing data.
#print(clf.evaluate(x_test,y_test))
model=clf.export_model()
model.summary()

print(type(model))  # <class 'tensorflow.python.keras.engine.training.Model'>
try:
    model.save("model_autokeras", save_format="tf")
except:
    model.save("model_autokeras.h5")