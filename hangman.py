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
                # head, mistake = 1, life = 7
                r"""
                   --------
                   |      
                   |      O
                   |    
                   |      
                   |     
                   -     ===
                """,
                # head and torso, mistake = 2, life = 6
                r"""
                   --------
                   |      
                   |      O
                   |      |
                   |      |
                   |     
                   -     ===
                """,
                # head, torso, and one arm, mistake = 3, life = 5
                r"""
                   --------
                   |      
                   |      O
                   |     \|
                   |      |
                   |     
                   -     ===
                """,
                # head, torso, and both arms, mistake = 4, life = 4
                r"""
                   --------
                   |      
                   |      O
                   |     \|/
                   |      |
                   |      
                   -     ===
                """,
                # head, torso, both arms, and one leg, mistake = 5, life = 3
                r"""
                   --------
                   |      
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -     ===
                """,
                # final state: head, torso, both arms, and both legs, mistake = 6, life = 2
                r"""
                   --------
                   |      
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -     ===
                """,
                # last life , mistakes=7, life = 1
                r"""
                   --------
                   |      |
                   |     /O\
                   |     \|/
                   |      |
                   |     / \
                   -     ===
                """,
                # dead mistake = 8, life= 0
                r"""
                   -----------
                   | DEAD  DEAD
                   | DEAD  DEAD
                   | DEAD  DEAD
                   | DEAD  DEAD
                   | DEAD  DEAD
                   -     
                """
    ]
    print(stages[tries])

def game_start(guess):
    print("THE GAME STARTS!!!")
    print("GUESS THE MOVIE:")
    
    unknown = []
    for i in range(len(guess)):
        if guess[i] == " ":
            unknown.append(" ")
        
        else:
            unknown.append("_")
    mistakes = 0
    life = 8
    alphabets = set()
    eng = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    while "_" in unknown and mistakes < 8:
        check = False #Flag variable
        print("SPELLING HINT:",(" ").join(unknown))
        print("REMAINING LETTERS:")
        print((" ").join(eng))
        print()
        user_input = input("GUESS ONE LETTER:").upper()[0]

        if user_input in alphabets:
            print("YOU HAVE ALREADY ENTERED THAT LETTER, CHOOSE ANOTHER:")
            print()

        else:
            alphabets.add(user_input)
            eng.remove(user_input)

            for i in range(0,len(guess)):
                if guess[i] == " ":
                    continue

                elif guess[i] == user_input:
                    unknown[i] = user_input
                    check = True    
                
            if check == True:
                print()
                print("YOU HAVE GUESSED CORRECT")
                print("REMAINING LIVES:",life)
                print()

            else:
                print("YOU HAVE GUESSED WRONG")
                print("YOU HAVE LOST A LIFE")
                mistakes += 1
                life -= 1
                print("REMAINING LIVES:",life)
                print_hangman(mistakes)
                print()
        
        if "_" not in unknown:
            print("YOU HAVE GUESSED THE CORRECT MOVIE NAME:",guess.upper())
            print("---------------CONGRAGULATIONS, YOU HAVE WON THE GAME-----------------")

        if mistakes == 8:
            print("---------------GAME OVER---------------")   

f = open("movies.txt","r")
movies = []

for i in f:
    movies.append(i.upper().strip())

guess = random.choice(movies)
game_start(guess)
f.close()