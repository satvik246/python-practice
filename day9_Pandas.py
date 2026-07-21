#Different ways to create a dataframe
#1 From csv file
import pandas as pd
df=pd.read_csv("Employee.csv")
print(df)

#2 From Excel File
import pandas as pd
df=pd.read_excel("Employee.xlsx","Sheet1")
print(df)

#3 From Dictionary
import pandas as pd
employee = {
    "name":["satvik","shiva","kunala"],
    "dept" : ["Integrations","TECH","CLOUD"],
    "salary": [55000,60000,70000],
    "location" : ["Hyderabad","Hyderabad","Hyderabad"]
}
df= pd.DataFrame(employee)
print(df)

#If the data contains a list combined with tuples
#each list act as a row of a table and we have to mention the column names
import pandas as pd
employee = [("shiva","Integrations",50000),
            ("satvik","TECH",60000),
            ("Kunala","CLOUD",70000)]
df=pd.DataFrame(employee,columns=["Name","Department","Salary"])
print(df)

#To skip rows while reading
import pandas as pd
df=pd.read_csv("Employee.csv",skiprows=1) # skips the first row
df1=pd.read_csv("Employee.csv",header=1) # considers header as row number 2 , index starts from zero
df2=pd.read_csv("Employee.csv",skiprows=None,names=["Name","Department","Salary"]) # If our file do not have any headers we can read like this , but pandas give default columns as 0,1,2,3,4
#if we want to ready only specific rows
df3=pd.read_csv("Employee.csv",nrows=3)
#if we want to replace null values with NaN
df4=pd.read_csv("Employee.csv",na_values=["Not Available","n.a."])
#na_values can be provided as a dictionary
pd.read_csv("Employee.csv",na_values={'Name':["Not Available","n/a"],
                                      'Gender':["Not available","n/a."]})

#writing to csv
df.to_csv("new.csv",index=False)
#writing specific columns to file
df.to_csv('new.csv',columns=['Location','Gender'])
# to exculde header
df.to_csv("new.csv",header=False)

#Exercise
import pandas as pd
df_small=pd.read_csv("Employee.csv",nrows=100)
print(df_small)

# 2. Read the dataset treating 'male' and 'female' as null values
df_na = pd.read_csv("Employee.csv",na_values=['Male','Female'])
print(df_na[['Education','Gender']])

# 3. How many employees are from each city?
df = pd.read_csv("Employee.csv")
print(df['City'].value_counts())

# 4. How many employees left vs stayed?
print(df['LeaveOrNot'].value_counts())
# 5. Sort employees by Age — oldest first
print(df.sort_values('Age',ascending=False).head(10))
# 6. Are there any missing values in the dataset?
print(df.isnull().sum())

# 7. Write only employees from Bangalore to a new CSV
bangalore = df[df['City'] == 'Bangalore']
bangalore.to_csv("bangalore_employees.csv", index=False)
print("File created")