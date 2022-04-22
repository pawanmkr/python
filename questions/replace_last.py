tup = (1, 2, 3, "not replaced yet!")
lis = []

lastvalue = input()

for i in range(0, len(tup)):

    if i == len(tup)-1:
        lis.append(lastvalue)
    else:
        lis.append(tup[i])


newtup = tuple(lis)
print(newtup)
