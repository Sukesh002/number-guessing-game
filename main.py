import random

def generate_random_num():
    return random.randint(1,50)

num=generate_random_num()
lives=10
while lives>0:
    guess=int(input("Enter your guess between 1 to 50 :"))
    if guess==num:
        print("You guessed it right!")
        break
    elif guess<num:
        print("Too low!")
        lives-=1
    else:
        print("Too high!")
        lives-=1
    print(f"You have {lives} lives left")
    if lives==0:
        print(f"You've run out of lives! The correct number was {num}.")
