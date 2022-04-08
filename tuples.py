tup = ("computer science", "mechanical", "bca", 60, "pawan", 1000, "nothing")

for i in range(0, len(tup)):
    print(tup[i])

# print from 0, then index 3(skipping 1 and 2)
print(tup[0::3])

# print from index 1
print(tup[1:])

# indexing from back to how much
print(tup[-6: -3])

# indexing from back
print(tup[-3])

# checking type
print(type(tup))
