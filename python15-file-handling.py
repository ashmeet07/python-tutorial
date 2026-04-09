import json as j

with open("data.json","r") as file:
    data =j.load(file)

print(data)
print(data["name"])



#dumping data
import json

data = {
    "name": "Rohan Chaturvedi",
    "age": 22,
    "skills": ["Python", "AI"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)



#CSV's
import csv

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["age"])



import csv

fields = ["name", "age", "city"]

with open("data.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerow({"name": "Ashmeet", "age": 22, "city": "Indore"})
