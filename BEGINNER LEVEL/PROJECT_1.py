# Base Code Algorithm

import random

print("Welcome to Number Guessing Game")
target=random.randint(1,100)
print("I have selected a number between 1 and 100 \n You have  7 attempts to guess it")

count=1
while count <=7:

    b=(input(f" attempt {count}/7-- Enter your guess :"))
    try:
        a=int(b)
    
    except ValueError:
        print("Please enter a valid number.\n")
        continue
    if not (1<=a<=100):
        print("Please enter a  number, between 1 and 100.\n")
        continue
    

    if a==target:
        
        print(f"Congratulations! you guessed the correct number \n you have guessed in {count} attempt(s)")
        break
    elif a>target:
        
        print("Too High -- try a lower number!")
    else:
        print(f"\nToo Low -- try a higher number!")
    count+=1
else:
    print(f"Better luck next time the correct value is  {target} ")






