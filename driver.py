__author__ = 'laurabush'

#pull the matrix of letters from a single crossword json file and print the array

import json
import numpy as np
from freqs import LetterFrequency
from pprint import pprint

json_data=open('7-7-14.json')
data = json.load(json_data)
json_data.close()

data["grid"]
print(data["grid"])

#construct a 15 x 15 matrix from the array (data["grid"])

gridarray = np.asarray(data["grid"])
a = gridarray.reshape((15,15))
print a

#construct the matrix to store frequencies of each letter at each location in the matrix

