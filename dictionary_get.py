a = {
    "name": "Rajat",
    "age": 30,
    "city": "Bangalore",
    "data_1": { 
        "roll.no" : 21,
        "data_2": [ 1, 2, 3, 4, 5, { "data_3": "hello" } ]
    }
}

print(a.get("name") )
# print( a.get("data_1").get("data_2")[-1].get("data_3") )
