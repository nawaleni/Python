import pandas as pd

# Q1 import file as dataframe
file = "/users/nirmalanawale/downloads/UIC2016Basketball.csv"
data = pd.read_csv(file, sep = ",")
df2016 = pd.DataFrame(data)

#Q2 Assign column names
df2016.columns =['Date','Opponent','UIC Score','Opp Score', 'UIC Field Goal Percentage', 'Opp Field Goal Percentage', 'UIC 3 point Field Goal Percentage', 'Opp 3 point Field Goal Percentage', 'UIC Rebound', 'Opp Rebound', 'UIC Assists', 'Opp Assists']

# Q3 Missing data
df2016.fillna('-', inplace=True)

# Q4 data types
df2016.dtypes
"""Date                                 object
Opponent                             object
UIC Score                             int64
Opp Score                             int64
UIC Field Goal Percentage            object
Opp Field Goal Percentage             int64
UIC 3 point Field Goal Percentage    object
Opp 3 point Field Goal Percentage    object
UIC Rebound                           int64
Opp Rebound                          object
UIC Assists                          object
Opp Assists                           int64 """

#Q5 
# convert data type of 'Date' column to DateTime type
df2016["Date"] = pd.to_datetime(df2016["Date"])
# extract year and store in separate column
df2016["Date_Year"] = df2016["Date"].dt.year
#cal length of df where year == 2016
print("Games played in 2016:",len(df2016.loc[df2016["Date_Year"] == 2016]))
# 19 school opponents played Men’s Soccer in 2016


#Q6
df2016.loc[df2016["UIC Score"] > 65]
# There were 15 such games played as below

"""
0	2015-11-13	San Francisco	
2	2015-11-24	Roosevelt	
6	2015-12-12	Illinois
9	2015-12-22	Purdue Calumet
12	2016-01-08	Detroit
14	2016-01-14	Green Bay
17	2016-01-22	Northern Kentucky	
18	2016-01-24	Wright State	
19	2016-01-28	Youngstown State	
20	2016-01-30	Cleveland State	
23	2016-02-13	Northern Kentucky	
24	2016-02-16	Youngstown State	
25	2016-02-19	Detroit
27	2016-02-26	Green Bay	
28	2016-02-28	Milwaukee   
"""	

# Q7 Win-Los-Tie
df2016["Result"] = df2016["UIC Score"] - df2016["Opp Score"]
def f(x):
    if x > 0:
        return "Win"
    elif x < 0:
        return "Loss"
    else:
        return "Tie"
df2016["Win/Loss"] = df2016["Result"].map(f)
# number of wins = 5:
print("Number of Wins:",len(df2016.loc[df2016["Win/Loss"] == "Win"]))
# number of Losses = 25
print("Number of Losses:",len(df2016.loc[df2016["Win/Loss"] == "Loss"]))
# Number of Ties = 0
print("Number of Ties:",len(df2016.loc[df2016["Win/Loss"] == "Tie"]))