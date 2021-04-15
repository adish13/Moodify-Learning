import pandas as pd
import numpy as np
import math

data = pd.read_json('input.json')
weights = [0.25400000000000017, 0.017000000000000008, 0.2460000000000002, -0.01800000000000001, -0.038000000000000034]
data.columns = ['x','y']
def polynomial(x,y,weights):
    sum = 0
    for i in range(5):
        sum += weights[i]*(x**(4-i))*(y**i)
    return sum 
def sigmoid(result):
    return 1/(1+np.exp(-1*result))
    
result = polynomial(data['x'],data['y'],weights)
result = sigmoid(result)

label_list = []   

for i in range(data.shape[0]):
    if result[i]>0.519 :
        label_list.append(1)
    else:
        label_list.append(0)

data['label'] = label_list
data.to_json('result.json')
             
