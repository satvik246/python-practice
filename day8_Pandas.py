import pandas as pd
df = pd.read_csv("Employee.csv")
print(df.head())
# A data frame is simply a table (rows and columns)
print(df.shape) # return a tuple
rows,columns = df.shape
print(rows)
#to return only specific rows 
print(df.head(2))
#to print last rows
print(df.tail())
#to specify rownum's
print(df[2:5]) #includes 2 and excludes 5
#to print colunms
print(df.columns)
#to access specified column
print(df['Education'])


import pandas as pd
df=pd.read_csv("Employee.csv")
print(df.Education)
#to print specific columns
print(df[['Education','JoiningYear']])

import pandas as pd
df=pd.read_csv("Employee.csv")
print(df['Age'].max())
print(df['Age'].min())
print(df.describe())

#conditionally selecting the data
import pandas as pd
df=pd.read_csv("Employee.csv")
print(df.loc[df['Age']==41,['JoiningYear','Gender']])
print(df[['Age','Gender']][df.Age==df.Age.max()])
print(df.Age==df.Age.max())

# To Set Index
import pandas as pd
df=pd.read_csv("Employee.csv")
df.set_index('JoiningYear',inplace=True) #Inplace true modifies the current data set
print(df.loc[2017,['Education','City']])
df.reset_index(inplace=True)

#practice
import pandas as pd
df=pd.read_csv("Employee.csv")
print(df[['JoiningYear','Education']])

#Exercise
import pandas as pd
df = pd.read_csv("Employee.csv")

# 1. How many rows and columns does the dataset have?
print(df.shape)
#returned (4653, 9)
# 2. Show the first 10 rows
print(df[1:11])

# 3. What are all the column names?
print(df.columns)
#Index(['Education', 'JoiningYear', 'City', 'PaymentTier', 'Age', 'Gender',
    #    'EverBenched', 'ExperienceInCurrentDomain', 'LeaveOrNot'],
    #   dtype='object')
# 4. Show only employees where salary > 50000
#    (use whatever salary column exists in your dataset)
#salary column is not present in data set so replaced it with age 
print(df['Age']>30)
# 5. Show only the name and department columns for those employees
#name and department are not there in data set , used other two columns
print(df[['Age','JoiningYear']][df.Age>30])
# 6. What is the maximum, minimum and average salary?
print(df.Age.max())
print(df.Age.min())
print(df.Age.mean())
# 7. Set a meaningful column as index and display first 5 rows
df.set_index('Age',inplace=True)