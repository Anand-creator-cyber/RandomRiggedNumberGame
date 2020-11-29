import random
unknown = random.randint(1,10)
chances = 0

print("Enter your guess")
while chances < 5 :
    guess = int(input("Enter Your Guess"))
    if(guess == unknown) :
        print("Congratulations! You win absolutely nothing")
        break
    elif guess < unknown :
     print("You're too low")

    else : 
        print("You're too high")

    chances = chances+1
if(chances >= 5) :
    print("You're out of guess', game over")
    


