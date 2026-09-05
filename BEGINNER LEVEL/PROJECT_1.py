# Base Code Algorithm
# Intro
# Selecting a random number
# Start
# Attempt no
# Guess checking
#  inform  result
import random

print("Welcome to Number Guessing Game")
target=random.randint(1,100)
print("I have selected a number between 1 and 100 \n You have  7 attempts to guess it")

count=1
while count <=7:

    a=int(input(f" attempt {count}/7-- Enter your guess :"))
    if a==target:
        
        print(f"Congratulations! you guessed the correct number \n you have guessed in {count} attempt(s)")
        break
    elif a>target:
        
        print("Too High -- try a lower number!")
    else:
        print(f"\nToo Low -- try a higher number!")
    count+=1
if count+1 >8:
    print(f"Better luck next time the correct value is  {target} ")






