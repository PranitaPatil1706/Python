# imports
import random

user_c = 0
com_c = 0

user_p = 0
com_p = 0

count = 0

while True:
    if count == 3:
        break
    user_c = 0
    com_c = 0
    user_c = int(input("Enter your choice = "))
    print(user_c)

    com_c = random.choice([0, 2, 1])
    print(com_c)

    if(user_c == 0 and com_c == 2):
        print("your point!")
        user_p += 1
    elif(user_c == 1 and com_c == 0):
        print("your point!")
        user_p += 1
    elif(user_c == 2 and com_c == 1):
        print("your point!")
        user_p += 1
    elif(user_c == com_c):
        print("Tie")
    else:
        print("my point!")
        com_p += 1
    count = count + 1

print()
print(f"your points = {user_p}")
print(f"my points = {com_p}")
print()
if user_p > com_p:
    print("You Won The Game!")
elif user_p < com_p:
    print("I Won The Game!")
else:
    print("Its a Tie")

