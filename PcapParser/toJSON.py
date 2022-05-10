import json

# Data to be written
dictionary ={
    "name" : "Nisha",
    "rollno" : 420,
    "cgpa" : 10.10,
    "phonenumber" : "1234567890"
}

def toJSON(name, dataList):
    with open(name, "w") as outfile:
        json.dump(dataList, outfile, indent=4)