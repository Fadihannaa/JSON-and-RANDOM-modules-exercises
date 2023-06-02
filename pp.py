
#Exercise using json module


import json 


{
"name" : "Jhon Doe",
"age" : "25",
"city" : "New york"


}

 


with open('data.json ') as f:
    json.data = json.load(f)
    
    
print("Name", json_data["name"])
print("Age", json_data["age"])
print("city",json_data["city"])




#Exercise using random mudule


import random 


lower = int(input("Enter the lower bound of the range: "))
upper = int(input("Enter the upper bound of the range: "))
random_number =random.randint(lower,upper)


print("Random number: ",random_number )

