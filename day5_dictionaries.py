customer = {
    "name" : "satvik",
    "age" : 24,
    "is_verified" : "True"
}

print(customer.get("name")) #returns none if we provide any key that does not exists
print(customer.get("designation","Software")) # we can set a default value 
customer["name"] = 'Shiva' ## we can set a value
print(customer["name"])
customer["designation"] = 'Software' # we can add a new key value pair
print(customer["designation"])

#exercise , take input as numbers 1234 return output as one two three four
# as we need to create a mapping between these we need to use a dictionary
input_num = input("Enter a number : ")
number_mapping = {
"1" : "One",
"2" : "Two",
"3" : "Three",
"4" : "Four"
}
final_word = ""
for ch in input_num :
    final_word += number_mapping.get(ch,"!") + " "

print(final_word)
#%%
#other dictionaries methods
employee = {
"name" : "explorer",
"age" : 23,
"city" : "Hyderabad",
"Company" : "Oracle"
}

print(employee.keys())
print(employee.values())
print(employee.items())

# using for loops in dictionaris

scores = {"SQL": 90, "Python": 75, "Excel": 60}
for subject, score in scores.items():
    if score >= 80:
        print(f'{subject} : Pass')
    else:
        print(f'{subject} : Fail')

#exercise
employee = {
    "name":"satvik",
    "dept" : "Integrations",
    "salary": 55000,
    "location" : "Hyderabad"
}

for field,value in employee.items() :
    print("key :" + field + " , Value :" + str(value))
employee["experience"]="3"
#print(employee["experience"])
employee["salary"] = 70000
print(employee.get("bonus","No bonus assigned"))
print(employee.items())