import pandas
from keras.models import model_from_json

from keras.utils.np_utils import to_categorical
import numpy as np

# fix random seed for reproducibility
seed = 4
np.random.seed(seed)

# 1-load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# Predict
data = pandas.read_csv("validation.csv")
i = 800
data_to_predict = data[:i].reset_index(drop = True)
predict_species = data_to_predict['1.110000000000000000e+02.15']
predict_species = np.array(predict_species)
prediction = np.array(data_to_predict.drop(['1.110000000000000000e+02.15'], axis= 1))

X = data.drop(['1.110000000000000000e+02.15'], axis=1)
X = np.array(X)

predictions = loaded_model.predict_classes(prediction)
prediction_ = np.argmax(to_categorical(predictions), axis = 1)

c = 0
for i, j in zip(prediction_ , predict_species):
    print( "{} - the nn predict {}, and the true ECG sample to find is {}".format(c, i, j))
    c+=1
