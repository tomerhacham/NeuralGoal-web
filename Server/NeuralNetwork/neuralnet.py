import keras, math,os,logging
import time
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import TensorBoard
from Server.NeuralNetwork import batch_size_calc

LOGGIN_NAME ="ann-{}".format((int)(time.time()))
tensorboard = TensorBoard(log_dir='logs\\{}'.format(LOGGIN_NAME))

class NeuralNet ():
    model = None
    input=0
    output=0

    def __init__(self,input_dim,tf_verbose=3):
        self.input=input_dim
        self.output=int(3)
        self.build()
        set_tf_loglevel(tf_verbose)

    #region Model Essence
    def build(self):
        self.model=Sequential()
        self.model.add(Dense(units=CalculateNodesInFirstLayer(self.input,self.output),input_dim=self.input, activation='relu'))
        self.model.add(Dense(units=CalculateNodesInSecondLayer(self.input,self.output),activation='relu'))
        self.model.add(Dense(units=3, activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    def train(self,x,y,_epochs):
        self.model.fit(x,y, batch_size=batch_size_calc.FindBatchSize(self.model), epochs=_epochs)

    def predict(self,x): #return array of prediction per the features
        prediction=self.model.predict_proba(x)
        return prediction
    #endregion

    #region Evaluate
    def metrics_evaluate(self, x_test, y_test):  # prediction for test phase
        # print("# Make Prediction in Training mode")
        import pandas as pd
        from sklearn.metrics import accuracy_score, confusion_matrix
        prediction = self.model.predict_proba(x_test)
        y_pred = pd.DataFrame(prediction)
        columns_names = y_test.columns
        y_pred.columns = columns_names
        conf_metrics = confusion_matrix(y_test.idxmax(axis=1),y_pred.idxmax(axis=1))
        accuracy = accuracy_score(y_test.idxmax(axis=1), y_pred.idxmax(axis=1))
        return conf_metrics,accuracy
    #endregion


#region Old utilities
def set_tf_loglevel(level):
    if level >= logging.FATAL:
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    if level >= logging.ERROR:
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    if level >= logging.WARNING:
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
    else:
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
    logging.getLogger('tensorflow').setLevel(level)

def print_plot(history):
    import matplotlib.pyplot as plt
    # list all data in history
    print(history.history.keys())
    # summarize history for accuracy
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()

def prediction_to_excel(prediction,path):
    import pandas as pd
    from datetime import date
    df = pd.DataFrame(prediction)
    file = path+'prediction_'+'_"+str(date.today())+'.xlsx
    df.to_excel(file, index=False)

#region Calculationg number of nodes in layers
def CalculateNodesInFirstLayer(n,m):
    return math.ceil(math.sqrt(n*(m+2)) + 2*math.sqrt(n/(m+2))-1)

def CalculateNodesInSecondLayer(n,m):
    return math.ceil(m*math.sqrt(n/(m+2))-1)
#endregion

#endregion