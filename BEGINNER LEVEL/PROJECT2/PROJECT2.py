# #Base Code Alogorithm
import random                                   

def Display_Rules():  #Displays intro
    print("WELCOME TO WORD GUESSING GAME!")
    name=input("Enter your name :")
    print(f"Good luck!, {name}")



def PLay_Game(words):


    chosen=random.choice(words)
    beta=[i for i in chosen]
    char=["_" for i in range(len(chosen))]
    lives=7
    gameover=False
    while not gameover:
        guess=input("Enter your guess:")
        if guess in chosen :
            for i in range(len(chosen)):
                if guess == chosen[i]:
                    char[i] = guess
                    lives=lives-0
                    
        else:
            print(char)
            lives=lives-1
        if lives<=0:
                 gameover=True 
                 print(chosen)
        print(f"you have {lives}lives left {char}")            
                   
        if "_" not in char:
            return "win"
                
    
    return  "Lose"


if __name__=="__main__":
    Display_Rules()
    words=["apple","banana","cherry"]
    print(PLay_Game(words))

