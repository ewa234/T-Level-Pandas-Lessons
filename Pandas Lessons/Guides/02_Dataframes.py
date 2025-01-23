#demo

import pandas as pd

myData = {"two" : pd.Series([1.,2.,3.,4.])}
df = pd.DataFrame(myData)

df["three"] = df["two"] * 2
df["four"] = "four"
df["five"] = df["four"][:2]

print(df)
print("#"*10)
input()

print("you can make a copy of a dataframe")
newDf = df.copy()
print(newDf)
print("#"*10)
input()

print("you can change the copy and it won't change the original")
newDf["five"] = "5000"
print("copy: ")
print(newDf)
print("original: ")
print(df)
print("#"*10)
input()

print("you can change the data type of a column by using its name")
print(df.two.astype(int))
print(df.three.astype(int))
print("#"*10)
input()

print("you can transpose the dataframe using .T")
print("this swaps the rows and columns")
print(df.T)
print("#"*10)
input()

print("you can get the rows of a dataframe starting from the")
print("top using .head()")
print("the number in the brackets decides how many rows to show")
print(df.head(2))
print("#"*10)
input()

print("you can print all of the information about the dataFrame using .info()")
print(df.info())
print("#"*10)
input()

print("you can print a description of every column in the dataFrame using .describe()")
print(df.describe(include="all"))
print("#"*10)
input()

print("you can add columns to a dataFrame using iteration")
for i in range(20):
    df[f"column {i}"] = i
print(df)
print("#"*10)
input()

print("when you have this many columns, transposing can help you")
print("view them all in the console")
print(df.T)
print("#"*10)
input()


#This section no longer works! VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV


# print("########################")
# print("#indexing and selecting#")
# print("########################")

# print("we are just using this library to get a sample dataset")
# import os
# os.system("pip install seaborn")
# import seaborn as sns

# print("you can load a dataFrame from a dataset contained withing this library")
# tips = sns.load_dataset("tips")
# print("this will only print the first 3 rows")
# print(tips.head(3))
# print("#"*10)
# input()

# print("you can make a new dataFrame that only contains the columns")
# print("you want to look at")
# totalBillsAndTips = tips[["total_bill","tip"]]
# print(totalBillsAndTips.head())
# print("#"*10)
# input()

# print("you can make a new dataFrame that only contains certain rows")
# someTips = tips[3:5]
# print(someTips)
# print("#"*10)
# input()

# print("you can make a new dataFrame that contains all the rows in a")
# print("range (from row 2 to row 4) and every column between two specific columns")
# someTips = tips.loc[2:4, "tip":"day"]
# print(someTips)
# print("#"*10)
# input()

# print("you can make use 'iloc' instead of 'loc' if you only want to")
# print("use integer indexes instead of names")
# someTips = tips.iloc[2:4,1:5]
# print(someTips)
# print("#"*10)
# input()

# print("you can make a new dataFrame using a series of boolean values")
# test = tips["tip"] > 3
# print(test)
# print("#"*10)
# input()
# someTips = tips[moreThanThree]
# print(someTips)
# print("#"*10)
# input()