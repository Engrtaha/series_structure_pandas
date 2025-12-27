import pandas as pd
x = pd.Series([10,20,30,40,50])
list_data = [2,4,6,8,10]
lisy_index = ["a","b","c","d","e"]
y =pd.Series(data=list_data,index=lisy_index, dtype="float")
print("series printing simply: ")
print(x)
print("giving values to indexes as well of the series: ")
print(y)

