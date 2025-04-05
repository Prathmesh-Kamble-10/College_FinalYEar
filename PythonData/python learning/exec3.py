# maing a game which hide no 18 and get input from user this no as a suggestion get less than 9 suggestion 
# if no. is less than 18 then increase value and if no more than 18 then decrease value if value is 18 then user won..

"""
i = 18
print("Enter the no which is hide in this game \n")
en =int(input("guess no between 1 to 100: \n"))
guess = 1
game_over = False

while not game_over:
    
    if (i==en):
        print(f"You win!. you guess the no in {guess} guesses") # f in printf indicates f string
        game_over = True

    else: 
        if (i > en):
            guess += 1
            print("You need to add more")
            en = int(input("Guess again : "))
        else: 
            print("You need to add less")
            guess +=1
            en = int(input("Guess again : "))
"""
"""
# another solution of exercise

n = 18
number_of_guess=1
print("Number of guesses is limited to only 9 times\n")
while (number_of_guess<=9):
    guess_number = int(input("Guess the number between 1 to 100: \n"))

    if guess_number<18:
        print(f"You enter less no. plz enter greater number. \n")
    elif guess_number>18: 
        print("You enter grater no. Plz enter small number. \n")
    else: 
        print("You win! \n")
        print(number_of_guess," guesses are used   \n")
        break
    print(9-number_of_guess,"No. of guess left")
    number_of_guess = number_of_guess+1

if number_of_guess<9:
        print("Game over")
"""
"""
# how to add y or n funciton in python
reply = input('Do you want to play it again [Y/N]:')
if reply == 'Y':
    
else:
        print("Thanx for playing")
    """


    