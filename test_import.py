# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:08:39 2020

@author: kach
"""

from apriori import apriori

data=[]
with open("./data/DataSet4.txt", "r") as f:
    for line in f:
        T = []
        for word in line.split():
            T.append(word)
        data.append(T)


x=apriori(data,support=20,confidence=50)
x.generate_association_rules()

# #imporvements
# list
# pandas df
# filename (.txt .csv)
# # dictionary (list-list)
# ouput
# variable or 
# dataframe