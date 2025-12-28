import pandas as pd
example = pd.Series(["Islamia College Peshawar",100,5.8,True])
x = example[0] 
y = pd.Series([sum,print,len,max,min,type])
print("simple series is printed here: ")
print(example)
print("type of series is: ")
print(type(example))
print("accessing first index of series: ")
print(x)
print("type of first element is: ")
print(type(x))
print("showing all elements of second series object: ")
print(y)
