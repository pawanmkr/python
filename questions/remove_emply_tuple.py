turtles = (("Pawan Kumar", 21, 1717), (), (1, 2, 3, 4, 5), ("python", "lab", 8), ())
lis = []

for i in range(0, len(turtles)):
    if len(turtles[i]) != 0:
        lis.append(turtles[i])

newtups = tuple(lis)
print(newtups)
