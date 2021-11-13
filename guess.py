# A basic python guessing game

secret_word = "apple"
guess = ""
guess_count = 0
guess_max = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count != guess_max:
        guess = print(input("What is the secret word: "))
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You're out of guesses")
elif guess == secret_word:
    print("Congratulation")
