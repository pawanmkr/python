dict = {
    "name" : "pawan",
    "age" : 21,
    "course" : "cse",
    1717 : "UID"
}

print(dict.get(1717))
print(dict["course"])
print(dict.__len__())

print(dict.keys())

dict.update({ "lab" : "106B"} )

print(dict)

take = dict.get("age")

print(take)