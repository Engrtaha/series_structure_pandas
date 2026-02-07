import pandas as pd
x = pd.Series([1,2,3,4,5,6,7,8,9,10,11])
a = x.axes
b = x.dtype
c = x.size
d = x.head()
e = x.head(3)
f = x.tail()
g = x.tail(3)
print("showing the rangeindex of the series: ")
print(a)
print("showing the dtype of the series: ")
print(b)
print("showing the size of the series: ")
print(c)
print("showing the first five elements: ")
print(d)
print("showing the first three elements: ")
print(e)
print(" showing the last five elements: ")
print(f)
print("shpwing the last 3 elements: ")
print(g) 