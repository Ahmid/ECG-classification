import numpy
import pandas
import keras
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

seed = 7
numpy.random.seed(seed)

# load dataset
dataframe = pandas.read_csv("training.csv", header=None)
dataset = dataframe.values
X = dataset[:,0:18286]
Y = dataset[:,18286]


model = Sequential()
model.add(Dense(40, input_dim=18286, activation="relu", kernel_initializer='random_uniform'))
model.add(Dense(40, activation="relu", kernel_initializer='random_uniform'))
model.add(Dense(10, activation="relu", kernel_initializer='random_uniform'))
model.add(Dense(4, activation="softmax", kernel_initializer='random_uniform'))

# Compile model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(X, Y, epochs=70, batch_size=10, verbose=1)

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")


#Plot
# summarize history for accuracy
plt.plot(history.history['acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()