
one = int(input('first number: '))
operator = input(' what you want to do: ')
two = int(input('second number: '))

def operation(one, operator, two):
    switcher = {
         operator == '+': print(one.__add__(two)),
         operator == '-': print(one.__sub__(two)),
         operator: print(one.__mul__(two)),
         operator: print(one.__divmod__(two))
    }

operation(one, operator, two)