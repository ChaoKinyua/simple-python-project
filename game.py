import random

# List of names to guess from
names = ["Alice", "Brian", "Charles", "Diana", "Evelyn", "Francis", "Grace", "Henry"]

# Pick a random name
secret_name = random.choice(names)

print("🎲 Welcome to the Name Guessing Game!")
print("I have chosen a random name. Can you guess it?")
print(f"Hint: The name starts with '{secret_name[0]}' and has {len(secret_name)} letters.")

# Loop until correct guess
while True:
    guess = input("Enter your guess: ").strip().capitalize()

    if guess == secret_name:
        print(f"🎉 Correct! The name was {secret_name}. You win!")
        break
    elif guess not in names:
        print("That name is not in the list. Try again.")
    else:
        print("❌ Wrong guess, try again!")

