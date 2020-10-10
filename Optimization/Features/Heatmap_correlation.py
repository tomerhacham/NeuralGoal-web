import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
COLUMNS_NAMES=['away_att','away_def','away_mid','away_odds_n',
               'away_team_rank','away_team_received',
               'away_team_scored','draw_odds_n','home_att',
               'home_def','home_mid','home_odds_n','home_team_rank','home_team_received','home_team_scored','result']
data = pd.read_csv("mainTableCSV.csv")[COLUMNS_NAMES]
labelencoder = LabelEncoder()
data['result'] = labelencoder.fit_transform(data['result'])  # X:2 ,2:1, 1:0
print('#result label Encoding')
le_name_mapping = dict(zip(labelencoder.classes_, labelencoder.transform(labelencoder.classes_)))
print(le_name_mapping)
corrmat = data.corr()
#top_corr_features = corrmat.index

plt.figure(figsize=(20,20))
#plot heat map
#g=sns.heatmap(data[top_corr_features].corr(),annot=True,cmap="RdYlGn")
g=sns.heatmap(data.corr(),annot=True,cmap="RdYlGn")
plt.savefig('heatmap.png')
plt.show()