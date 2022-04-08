one = {'a': 100, 'b': 200, 'c': 300}
two = {'a': 300, 'b': 200, 'd': 400}
three = {}

for i, j in one.items():
    for x, y in two.items():

        if i == x:
            three[i] = (j+y)

print(three)
print("--------------------\nPawan - 20BCS1717")
