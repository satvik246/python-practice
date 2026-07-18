import csv
employees = [{"name":"satvik","department":"Integrations","salary":50000},
             {"name":"shiva","department":"Integrations","salary":60000},
             {"name":"kunala","department":"Integrations","salary":50000}]
with open("practice.csv","w") as file :
    fieldnames = ["name","department","salary"]
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    for row in employees :
        writer.writerow(row)