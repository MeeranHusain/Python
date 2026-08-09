import random

n = random.randint(1, 100)
a = -1
guesses = 0

while a != n:
    a = int(input("Guess the number between 1 and 100: "))
    guesses += 1

    if a > n:
        print("Your guess is too high.")
    elif a < n:
        print("Your guess is too low.")

print(f"\n===== You guessed the number {n} correctly in {guesses} attempts =====")

