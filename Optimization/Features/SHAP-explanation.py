import shap
import pandas as pd
from Server.NeuralNetwork.neuralnet import NeuralNet
from Optimization.Features.data_preproccesor import train_preprocess
shap.initjs()

data = pd.read_csv("../mainTableCSV.csv")
X,Y= train_preprocess(data)
#X,Y=select_columns()
#feature_names=list(X.columns)
#class_names=Y['result'].unique()
#class_names=['result_0','result_1','result_2']
#x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0, shuffle=False)
ann=NeuralNet(X.shape[1])
ann.train(X,Y,1)
prediction=ann.predict(X)
print(prediction)




# we use the first 100 training examples as our background dataset to integrate over
#explainer = shap.DeepExplainer(ann.model,np.array(x_train[:1000].values))
# explain the first 10 predictions
# explaining each prediction requires 2 * background dataset size runs
#to_explain=np.array(x_test[:10].values)
#shap_values = explainer.shap_values(X=to_explain)
#base_values=explainer.expected_value[0].numpy()

#shap.force_plot(base_value=base_values ,
 #               shap_values= shap_values[0],
 #               features=to_explain,
 #               feature_names=list(x_test.columns)
                        #)
#shap.summary_plot(shap_values=shap_values,features=x_test,feature_names=list(x_test.columns),class_names=['Home','Away','Draw'])