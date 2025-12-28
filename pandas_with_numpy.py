import numpy as np
import pandas as pd
example = np.array([1,3.3,5,7.2,9])
labels = np.array(['a', 'b', 'c', 'd', 'e'])
s = pd.Series(data=example, index=labels)  
print("series created using numpy array: ")
print(s)