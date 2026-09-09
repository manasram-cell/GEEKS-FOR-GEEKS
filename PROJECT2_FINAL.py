""" A simple commandline WORD GUESSING GAME"""

import random

Lives=7
Word_list:list[str]=["apple","banana","cherry"]

def Display_Rules()->str:
    """Print the welcome message and return the player's name."""
    print("Welcome TO Word Guessing Game!")
    name=input("Enter your name: ").strip()
    print(f"Good Luck ,{name}!")
    return name
class WordGuessingGame:
    """Encapusulating the state and rules of a single game round."""
    def __init__(self,word:str,lives:int=Lives)->None:
        self.word=word.lower()
        self.revealed:list[str]=["_"]*len(self.word)
        self.guessed_letters:set[str]=set()
        self.lives=lives
    @property
    def is_won(self)->bool:
        """True once every letter in the word has beem reveaed."""
        return "_" not in self.revealed
    @property 
    def is_lost(self)->bool:
        """True once player has run out of liveas."""
        return self.lives<=0
    def guess(self,letter:str)->bool:
        """Apply a validated,lower case,unguessed letter.return true if correct"""
        self.guessed_letters.add(letter)
        if letter in self.word:
            for i,ch in  enumerate(self.word):
                if ch==letter:
                    self.revealed[i]=letter
            return True
        self.lives-=1
        return False
    def display_state(self)->None:
        """Print the current word progress ,lives,and guessed letters."""
        print(f"\n Word: {''.join(self.revealed)}")
        print(f"Lives remaining : {self.lives}")
        guessed=",".join(sorted(self.guessed_letters)) or "None"
        print(f"Guessed letters:{guessed}")
def get_valid_guess(guessed_letters:set[str])->str:
    """Prompt until the player enters a single ,unguessed letter"""
    while True:
        guess=input("Enter your guess(a single letter): ").strip().lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Please enter exaclty one alphabetical letter")
            continue
        if guess in guessed_letters:
            print(f"You have already guessed '{guess}'. Try a different letter.")
            continue
        return guess
def play_game(word_list:list[str],lives:int=Lives):
    """Run one round of the game and return 'win' or 'lose'"""
    chosen_word=random.choice(word_list)
    game=WordGuessingGame(chosen_word,lives)
    while not game.is_won and not game.is_lost:
        game.display_state()
        letter=get_valid_guess(game.guessed_letters)
        game.guess(letter)
    game.display_state()
    if game.is_won:
        print(f"you won! the word was '{game.word}'")
        return 'win'
    print(f"you won! the word was '{game.word}'")
    return "lose"
def main()->None:
    """Entry point :show rules ,run game,report the result"""
    Display_Rules()
    result=play_game(Word_list)
    print(f"\nGame result: {result}")
if __name__=="__main__":
    main()