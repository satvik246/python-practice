with open("employees.txt","r") as file:
    #content = file.read()
    #print(content)
    for line in file :
        print(line.strip())

with open("employees.txt","r") as file :
    for line in file :
        print(line)

#two options in printing contents of a file 
#1 : with help of loop and printing loop variable
with open("employees.txt","r") as file:
    for line in file :
        print(line.strip()) #strip removes extra line after every line
#2 : with help of read method
with open("employees.txt","r") as file:
    content=file.read()
    print(content)

#Writing to a file
#creates a new file if it does not exist and overwrites if exists
with open("output.txt","w") as file :
    file.write("Hello from Python\n")
    file.write("This is file handling\n")

#append contents to a file
with open("output.txt","a") as file :
    file.write("This line is newly added\n")

#reading csv file (employees.csv)
#dict reader reads each row as dictionary
import csv

with open("employees.txt","r") as file :
   reader = csv.DictReader(file)
   for row in reader :
       print(f"Name : {row['name']} | Department : {row['department']} | Salary : {row['salary']} | Location  {row['location']}")

#writing to a csv file
import csv
employees = [
    {"name": "satvik", "department": "Integrations", "salary": 55000},
    {"name": "john", "department": "Finance", "salary": 60000},
    {"name": "priya", "department": "HR", "salary": 52000}
]

with open("output.csv","w") as file :
    fieldnames = ["name","department","salary"]
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    for employee in employees :
        writer.writerow(employee)

print("csv file created successfully")

#exercise
#Creates a list of 4 dictionaries — each representing an employee with name, department, salary
import csv
emp_cnt = 0
employees = [{"name":"satvik","department":"Integrations","salary":50000},
             {"name":"shiva","department":"Integrations","salary":60000},
             {"name":"kunala","department":"Integrations","salary":50000}]
#Writes them to a CSV file called team.csv
with open("team.csv","w") as file :
    fieldnames=["name","department","salary"]
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    for row in employees :
        writer.writerow(row)
#Reads team.csv back
with open("team.csv","r") as file :
    reader = csv.DictReader(file)
    for row in reader :
        #Prints only employees whose salary is above 55000
        if int(row['salary']) > 55000 :
            emp_cnt+=1
            print(f"Name : {row['name']} | Department : {row['department']} | Salary : {row['salary']}")
print(f"Count : {emp_cnt}")
    