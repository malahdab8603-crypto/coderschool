import random

chances = 10
randOM = "sdd"

listOfWords = ['elephant' , 'hat' , 'splash' , 'leather' , 'algebra' , 'computer' ,'mystery' , 'rhythm' , 'code', 'ridwan', 'hamza']

gameStart = False 
while not gameStart:
    is_correct = False
    print("Welcome to the Guessing Word Game")
    print('Press 1 to Start the Game\n\n')
    is_enter = input()
    if is_enter == "1":
        gameStart = True 

word = random.choice(listOfWords)        
word_skeleton = ["_"] * len(word)
found_Indicies = []


# game loop
while gameStart == True:

    print(f'\nfound indices: {found_Indicies}')

    if len(found_Indicies) == len(word):
        print("You won !")
        break

    print(f'You have {chances} chances left\n')

    user_guess = input("enter a letter...\n\n")
    if not isinstance(user_guess, str) or not user_guess.isalpha() or not len(user_guess) == 1:
        print("Invalid. Re enter\n")
        continue

    for i in range(len(word)):
        if i in found_Indicies:
            continue
        if user_guess == word[i]: # This checks for if the user guesses the correct letter
            word_skeleton[i] = user_guess
            found_Indicies.append(i)
            is_correct = True
            print("Correct Guess\n\n")
            break

    if not is_correct:
        print("incorrect\n\n")
        chances -= 1
    is_correct = False
    print(*word_skeleton)
    print('\n\n')



