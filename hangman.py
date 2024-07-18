import random

#adding r before a string will make the string a "raw string". So \n and other things will not be considered

def print_hangman(tries):
    """Prints the hangman based on the number of incorrect tries."""

    stages = [# initial empty state, mistake = 0
                r"""
                   --------
                   |      
                   |    
                   |    
                   |      
                   |     
                   -
                """,
                # head, mistake = 1``
                r"""
                   --------
                   |      
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # head and torso, mistake = 2
                r"""
                   --------
                   |      
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head, torso, and one arm, mistake = 3
                r"""
                   --------
                   |      
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head, torso, and both arms, mistake = 4
                r"""
                   --------
                   |      
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, torso, both arms, and one leg, mistake = 5
                r"""
                   --------
                   |      
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # final state: head, torso, both arms, and both legs, mistake = 6
                r"""
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """
    ]
    print(stages[tries])

def game_start(guess):
    print("THE GAME STARTS!!!")
    print("guess the movie:")
    
    unknown = []
    for i in range(len(guess)):
        if guess[i] == " ":
            unknown.append(" ")
        
        else:
            unknown.append("_")
    mistakes = 0
    life = 6
    alphabets = set()
    
    while "_" in unknown and mistakes < 6:
        check = False #Flag variable
        print("Spelling HINT:",(" ").join(unknown))
        user_input = input("guess one letter:").upper()
    
        if user_input in alphabets:
            print("You have already entered that letter, choose different one")
            print()

        else:
            alphabets.add(user_input)
            
            for i in range(0,len(guess)):
                if guess[i] == " ":
                    continue

                elif guess[i] == user_input:
                    unknown[i] = user_input
                    check = True    
                
            if check == True:
                print("You have guessed correct")
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
            print("YOU HAVE GUESSED THE CORRECT MOVIE NAME:",guess.upper())
            print("---------------CONGRAGULATIONS, YOU HAVE WON THE GAME-----------------")

        if mistakes == 6:
            print("---------------GAME OVER---------------")   

movies = ["DOCTOR STRANGE","LA LA LAND","BLACK PANTHER","MURDER ON THE ORIENT EXPRESS","LORD OF THE RINGS", "AVENGERS", "THE NUN", "MISSION IMPOSSIBLE", "BIG HERO 6"
          "HARRY POTTER", "THE HOBBIT", "HANGOVER"]

guess = random.choice(movies)

game_start(guess)