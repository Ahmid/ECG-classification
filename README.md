# ECG-classification
A neural network that classifies the ECG Beat as normal, abnormal (Arrhythmias), noisy or other.

# Tools used
* Python
* Tensorflow
* Keras

# Algorithms used
* Sequential neural network data model (Multilayer Perceptron)
* (Relu, Softmax) algorithms for activation
* (random_uniform) algorithm for initializing
* (sparse_categorical_crossentropy) algorithm for loss calculation
* (adam) algorithm for the optimizer

# Steps
1. Download [ECH beats training dataset](https://physionet.org/pn3/challenge/2017/training/) 
2. Create a new Excel file named `classifiedData.xlsx`, then group the records found in the above link inside the excel sheet and remove `*/` (you can use Find and Replace with the following regex: `*/`) so the columns contain only the ECG signal name as shown below:
![classified data in excel sheet](https://github.com/Ahmid/ECG-classification/blob/master/RawImages/Capture.JPG)
3. Run `groupdata.py`, this will create a big size csv sheet named `training.xlsx` containing all the signal points ended with a classification column (whether it is normal, noisy, abnormal or other).
4. Run `saveModel.py`, this will create a deep neural network and will train it on the classified ECG signals.
5. Download [ECG beats validation dataset](https://physionet.org/pn3/challenge/2017/validation/)
6. Redo step-2 with a file named `validatedData.xlsx`
7. Run `groupDataForLoadedModel.py`, this will create a new sheet named `validation.xlsx` for testing the neural network.
8. Run `LoadModel.py` and check the neural network results.

# Results
1. Accuracy reached about 90% as number of epochs increases with time:
![Accuracy](https://github.com/Ahmid/ECG-classification/blob/master/RawImages/acc.jpg)

2. Loss decreases to 0.4 as time increases:
![Loss](https://github.com/Ahmid/ECG-classification/blob/master/RawImages/loss.jpg)

3. Snippet from Python Pycharm showing the accuracy:
![Snippet from PyCharm](https://github.com/Ahmid/ECG-classification/blob/master/RawImages/snippet.jpg)

4. And finally some predictions on new unseen data:
![Predictions](https://github.com/Ahmid/ECG-classification/blob/master/RawImages/predictions.png)




