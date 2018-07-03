
import pandas
import numpy

"""
df = pandas.DataFrame([('falcon', 'bird',    389.0),
                    ('parrot', 'bird',     24.0),
                    ('lion',   'mammal',   80.5),
                    ('monkey', 'mammal', numpy.nan)],
                   columns=('name', 'class', 'max_speed'))
				   
print(df)

nf = df

nf.pop('class')

print(df)

mypath = "users/name/desktop/"

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


import os

for root, dirs, files in os.walk("."):  
    for filename in files:
        print(filename)

		
from sklearn.modelselection import train_test_split
train, test = train_test_split(df, test_size=0.2)		
		
for index, row in df.iterrows():
    print (row["name"], row["age"])

	
"""

"""
df = pandas.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                   index=[4, 5, 6], columns=['A', 'B', 'C'])
				   
				   
print(df.at[4, 'B'])

#print(df.at[4, 'D']) # KeyError

df['Name'] = 0.0 #gives a new column filled with 0.0

print(df)

df = pandas.DataFrame(columns=['A', 'B', 'C'])

print(df)

df['Name'] = [] # Gives a new column without rows

print(df)
"""


dt = pandas.DataFrame({'month': [1, 4, 7, 10],
                    'year': [2012, 2014, 2013, 2014],
                    'sale':[55, 40, 84, 31],
					'sum':[55, 40, 84, 31]})
					

sum = 'sum'
dt[sum] = 0

print(dt)

sales = dt.pop('sale')

print(dt)

dt['sale'] = sales
					
dt = dt.set_index(['month', 'year'])

print(dt)


"""
#print(dt.loc[(1, 2012), :].at['sale'])

#df.ix[(dt.datetime(2013,2,3,9,0,2),0),:] = 5

month = 5
date = '2018-06-30'

dt.ix[(month,date),:] = 11 # Inserts a row with default 11

print(dt)

#dt.pop('year')
#dt.pop('month')
#dt.reindex()
dt = dt.reset_index() # gives a new dataframe with old indexes removed and new default index inserted

print(dt)

column = dt.pop('year')

print(column) # a column as Series

print('hej')

dt = pandas.DataFrame(column) # a dataframe from Series

print(dt)

"""

# mapping strings to integers
# l = ['apple','bat','apple','car','pet','bat']
# d = dict([(y,x+1) for x,y in enumerate(sorted(set(l)))])
#print [d[x] for x in l]
# [1, 2, 1, 3, 4, 2]









