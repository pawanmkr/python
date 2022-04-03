first = int(input("enter first no:"))
operator = input("enter operator (+,-,%,/,*):")
second = int(input("enter 2nd no:"))

if operator == "+" :
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first *second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)

else:
    print("invalid operator")