# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n = 18
number_of_guesses = 1
print("Number of guesses is limited 9: ")
while (number_of_guesses <= 9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 18:
        print("you have entered a smaller number try a greater number.\n")
    elif guess_number > 18:
        print("you have entered a greater number try a smaller number.\n ")
    else:
        print("Yor got it!!!\n")
        print(f"It took you {number_of_guesses} guess(s) to guess the correct number.")
        break
    print(9 - number_of_guesses, "guesses left")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses > 9):
    print("Game Over")

