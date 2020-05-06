HANGMANPICS = ['''
    +---+
  |   |
      |
      |
      |
      |
 =========''', '''
    +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''
 
    +---+
    |   |
    O   |
    |   |
        |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
   /|   |
        |
        |
  =========''', '''
  
    +---+
    |   |
    O   |
   /|\  |
        |
        |
  =========''', '''
 
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
  =========''', '''
  
    +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
  =========''']

def hangman():
    i = 0
    incorrectguess = 0
    correctguess = 0
    whateveriwant = ["person","eliphant","brother","myself"]
    for x in whateveriwant:
        print("Let's play Hangman! There are", len(x), "letters in this word.")
        while i < (7 + len(x)):
            y = input("Guess a letter in a mystery word!")
            i += 1
            print("Your guess is", y, "!")
            if y in x:
                print("Correct")
                correctguess += 1
                print("correctguess=", correctguess)
                if correctguess == len(x):
                    break
                else:
                    continue
            else:
                print("Incorrect")
                print(HANGMANPICS[incorrectguess])
                incorrectguess += 1    
        print("The correct word is", x)
        print("GAME OVER")
        z = input("Do you want to play again? Type yes or no.")
        if z == "yes":
            i = 0
            incorrectguess = 0
            correctguess = 0
            continue
        else:
            break
