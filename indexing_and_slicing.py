import pandas as pd 
example = pd.Series(["+92","+93","+94","+95","+96"], index=['Pakistan','turkey','china','usa','iran'])
a = example["Pakistan"]
b = example.iloc[1]
c = example["Pakistan":"china"]
d = example[["iran","usa"]]

e = example.iloc[0:2:1]

print("pandas series nothing applied else: ")
print(example)
print("showing the index value of the pakistan: ")
print(a)
print("showing the index value of the turkey in different way: ")
print(b)
print("showing the index value of the pakistan to china (using slicing): ")
print(c)
print("showing the index value of the iran and usa (using list): ")
print(d)

print("showing the index value of the pakistan and china  (using slicing number): ")
print(e)
