#!/usr/bin/env python

import random

def main():
    """Start a music genre guessing game."""
    print("Guess the genre!")

    genre = [
        "rock",
        "hip hop",
        "classic",
        "blues",
        "musical theatre",
        "world music",
        "funk",
        "nasheed",
        "dance music",
        "drill 'n' bass",
        "vocal music",
        "instrumental"
        ]

    x = random.choice(genre)
    guess = None
    
    while x != guess:

        guess = str(input("what genre that am i thinking of?:"))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))
            
            
 
main()