import pandas as pd
dictionary =  {"ferrai":334.7,"porche":337.9,"lamborghini":349,"BMW":360,"bugatti":365}
x =  pd.Series(data=dictionary)
y = pd.Series(data=dictionary,index=["porche","toyata","ferrai"])
print("using pandas and dictrionary making series: ")
print(x) 
print("according our indexing the serries is made: ")
print(y)
