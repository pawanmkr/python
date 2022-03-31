def flyin():
    print("jarvis let's ready to fly and help this guy")

def time_travel():
    print("jarvis let's go back to past for there help and solve the problem of this guy")

def healing_people():

    print("jarvis let's heal this people and make their life happy and helthy with our power")

print("wahat can you see in front of you right know my jarvis")
condition = input()

if  condition =="your friend was beaten by tom & he has multiple injuries on body, you have to heal him":
     healing_people()
elif  condition== "while evening walk you saw a person down hit by a heavy driver, but you are not able to help him since you dont have healing medicine with you.":
    flyin()

elif condition =="there was another person who died in front of your eyes-you felt said that you dont got time to save him.":
    time_travel()

else:
    print("sorry i am not able to help you!!")
