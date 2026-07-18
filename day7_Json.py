#modules are files which contain pre-build functions
#importing whole module
import math
print(math.sqrt(25))
print(math.pi)

#importing specific function
from math import sqrt
print(sqrt(25))

#Importing with an alias
import math as m
print(m.sqrt(25))

#python in-built json functions
#json.dumps()  --> Dictionary to Json String
#json.loads()  --> JSON String to Dictionary
#json.dump()  --> Dictionary to Json File
#json.load()  --> JSON File to Dictionary

#Converting dictionary to  JSON String
import json
employee = {"name":"Satvik",
            "department":"Integrations",
            "Salary":"60000",
            "skills":["OIC","SQL","PL/SQL","API's"]}
json_string = json.dumps(employee,indent=4)
print(json_string)
print(type(json_string))

#Converting json to dictionary
import json
employee = '{"name": "Satvik","department": "Integrations","Salary": "60000","skills": ["OIC","SQL","PL/SQL","APIs"]}'
dict_string = json.loads(employee)
print(dict_string["name"])
print(type(dict_string))

#writing json to a file
import json
employees = [
    {"name": "satvik", "department": "Integrations", "salary": 55000},
    {"name": "shiva", "department": "Integrations", "salary": 60000},
    {"name": "kunala", "department": "Integrations", "salary": 50000}
]
with open("employees.json","w") as file:
    json.dump(employees,file,indent=4)

print("json file created")

#Reading json from a file
import json
with open("employees.json","r") as file :
    data = json.load(file)

for emp in data :
    print(f"Name : {emp['name']}")


# reading json
import json
response = '{"employeeId": "E001", "name": "satvik", "department": "Integrations", "salary": 55000}'
data = json.loads(response)
print(f"Name : {data['name']}")

#Exercise 
#Creates a list of 3 employee dictionaries — each with name, department, salary, and a list of skills
import json
employee=[{"name":"satvik","department":"Integrations","salary":"60000","skills":["SQL","PLSQL","APIs"]},
          {"name":"shiva","department":"Integrations","salary":"60000","skills":["REST","SOAP","ODI"]},
          {"name":"kunala","department":"Integrations","salary":"60000","skills":["FIN","SCM","PPM"]}]
#Writes them to team.json
with open("team.json","w") as file :
    json.dump(employee,file,indent=4)
#Reads team.json back
with open("team.json","r") as file :
    json_data = json.load(file)
for emp in json_data :
    print(f"Name : {emp['name']} | Department : {emp['department']} | Salary : {emp['salary']}")
    skills = emp['skills']
    print(f"Skills : {', '.join(skills)}")
        