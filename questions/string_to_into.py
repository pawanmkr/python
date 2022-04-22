def tupintstr(tupstr):
    result = tuple((int(x[0]), int(x[1])) for x in tupstr)
    return result


tupstr = (('333', '33'), ('1416', '55'))
print(tupstr)
print("string to int tuple:", tupintstr(tupstr))
