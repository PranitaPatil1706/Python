import random
print("Welcome To Snake Ladder Game!...")
user = 0
status = True
dice_roll = 1

ladder={1:38,4:14,9:31,28:84,21:42,51:67,72:91,80:99}
snake={17:7,62:18,54:34,64:60,87:36,93:73,95:75,98:79}

def dice():
    return (random.choice([1, 2, 3, 4, 5, 6]))


while status:
    if user == 100:
        break

    input("Hit enter to roll dice")
    dice_roll=dice()
    print(f"dice {dice_roll}")
    temp = user + dice_roll
    if temp >  100:
        pass
    elif user==100:
        break   
    else:
        user += dice_roll
        print(f"position {user}")
        if user in snake:
            user = snake[user]
            print("snake")
            print(user)

        elif user in ladder:
            user = ladder[user]
            print("ladder")
            print(user)

    print()
    
            

    

    



    
    
