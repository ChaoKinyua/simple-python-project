# 🎲 Name Guessing Game (Python)

A simple command-line game written in Python where the program randomly selects a name from a list, and the player tries to guess it.

---

## 🚀 How It Works
1. The game randomly picks one name from a predefined list.  
2. The player is asked to guess the name.  
3. Hints are provided:
   - The first letter of the name  
   - The total number of letters  
4. The game continues until the player guesses correctly.  

---

## 📜 Features
- Randomly selects a name each run  
- Cleans user input (ignores extra spaces, fixes capitalization)  
- Provides hints (first letter & length)  
- Loops until the correct guess is made  

---

## 🖥️ How to Run
1. Make sure you have **Python 3** installed.  
2. Save the game file as `name_guessing_game.py`.  
3. Open a terminal or Git Bash in the file’s folder.  
4. Run the game:

```bash
python name_guessing_game.py
🎲 Welcome to the Name Guessing Game!
I have chosen a random name. Can you guess it?
Hint: The name starts with 'G' and has 5 letters.
Enter your guess: Grace
🎉 Correct! The name was Grace. You win!
**File structure**
name_guessing_game.py   # main game file
README.md               # documentation

