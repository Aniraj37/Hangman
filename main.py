#! === HangMan ===


import random
import os
from hangman import riddle_list
from hangman_art import stages, logo

clear = lambda: os.system('cls')

chosen_word=random.choice(list(riddle_list.keys()))

print(logo, "\n")

words_length=len(chosen_word)
display=[]
for each in range(words_length):
    display.append("_")

lives=6


end_of_game=False
while not end_of_game:
    print(f"Hint: {riddle_list[chosen_word]}\n")
    guessed_letter=input("Guess a Letter: ").lower()
    
    clear()

    if guessed_letter in display:
        print(f"you have already guessed this letter {guessed_letter}.")

    for i in range(0,words_length):
        if chosen_word[i]==guessed_letter:
            display[i]=guessed_letter
    

    if guessed_letter not in chosen_word:
        print(f"You guessed the letter {guessed_letter}, that's not in the word. You loose a life.\n")
        lives-=1
        if lives == 0:
            end_of_game=True
            print("Game Over!!")
        
    print(stages[lives])
            
    print("\n","".join(display), "\n")
    
    if "_" not in display:
        end_of_game=True

        print("You WIN!!!")






