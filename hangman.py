import random

def print_hangman(tries):
    """Prints the hangman based on the number of incorrect tries."""

    stages = [# initial empty state, mistake = 0
                """
                   --------
                   |      
                   |    
                   |    
                   |      
                   |     
                   -
                """,
                # head, mistake = 1``
                """
                   --------
                   |      
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # head and torso, mistake = 2
                """
                   --------
                   |      
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head, torso, and one arm, mistake = 3
                """
                   --------
                   |      
                   |      O
                   |    \\|
                   |      |
                   |     
                   -
                """,
                # head, torso, and both arms, mistake = 4
                """
                   --------
                   |      
                   |      O
                   |    \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, both arms, and one leg, mistake = 5
                """
                   --------
                   |      
                   |      O
                   |    \\|/
                   |      |
                   |     / 
                   -
                """,
                # final state: head, torso, both arms, and both legs, mistake = 6
                """
                   --------
                   |      |
                   |      O
                   |    \\|/
                   |      |
                   |     / \\
                   -
                """
    ]
    print(stages[tries])

def game_start(guess):
    print("THE GAME STARTS!!!")
    print("guess the movie:")
    # print(guess)
    unknown = ["_"]*len(guess)
    mistakes = 0
    life = 6
    alphabets = set()
    
    while "_" in unknown and mistakes < 6:
        check = False #Flag variable
        print("No. of spelling to find:",unknown)
        user_input = input("guess one letter:").lower()
    
        if user_input in alphabets:
            print("You have already entered that letter, choose different one")
            print()

        else:
            alphabets.add(user_input)
            
            for i in range(0,len(guess)):
                if guess[i] == user_input:
                    unknown[i] = user_input
                    check = True
                
            if check == True:
                print("hooray!!, You have guessed correct")
                print("Remaining LIVES:",life)
                print()

            else:
                print("You have guessed wrong... try again")
                print("YOU HAVE LOST A LIFE")
                mistakes += 1
                life -= 1
                print("Remaining LIVES:",life)
                print_hangman(mistakes)
                print()
        
        if "_" not in unknown:
            print("CONGRAGULATIONS, YOU HAVE WON THE GAME....")

        if mistakes == 6:
            print("GAME OVER....")          
        

movies = ["avatar","avengers","titanic","joker","kill"]

guess = random.choice(movies)

game_start(guess)