import scipy.io
import numpy as np
import os
import pandas as pd

directory = "validation\\TestLoadModel\\"
df = pd.read_excel('validatedData.xlsx')

normal = df['normal'].values.tolist()
af = df['af'].values.tolist()
noisy = df['noisy'].values.tolist()
other = df['other'].values.tolist()
maxSize = 18286


def checkClass (list, type):
    for val in list:
        if record_name == val:
            global npFinalArray
            npFinalArray = np.pad(npPaddedArray, (0, 1), 'constant', constant_values=type)
            return True
    return False


i = 0
for filename in os.listdir(directory):
    if not filename.endswith(".hea"):
        data = scipy.io.loadmat(directory + filename)
        record_name = os.path.splitext(filename)[0]

        npArray = np.array(data['val'])
        size = data['val'].size
        npPaddedArray = np.pad(npArray[0], (0, maxSize-data['val'].size), 'constant', constant_values=0)

        if i == 0:
            print ('In')
            npFinalArray = np.pad(npPaddedArray, (0, 1), 'constant', constant_values='111')
        else:
            if not checkClass(normal, "0"):
                if not checkClass(af, "1"):
                    if not checkClass(other, "2"):
                        npFinalArray = np.pad(npPaddedArray, (0, 1), 'constant', constant_values=3)

        i = i+1
        c = [[1, 2, 3]]
        c[0] = npFinalArray.tolist()

        f = open("validation.csv", 'a')
        np.savetxt(f, c, delimiter=",")


#f.close()

