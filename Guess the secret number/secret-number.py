secret = 7

guess = int(input("Hello! Try to guess the secret number: "))

if guess == 7:
    print("Congratulations! You correctly guessed the secret number.")
else:
    print("Sorry, unfortunately " + str(guess) + " is not the secret number.")
