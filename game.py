import random

def get_guess():
    num=input("What is your guess?")
    res = [str(x) for x in str(num)] 
    return res

def generate_code():
    
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]
    

def generate_clues(code,userGuess):
    if userGuess == code:
        return "CODE CRACKED"

    clues = []

    # Compare guess to code
    for ind,num in enumerate(userGuess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues

# Run Game
print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")

secretCode = generate_code()
print("Code has been generated, please guess a 3 digit number")

clueReport = []

# Keep asking until the user has gotten it right!
while clueReport != "CODE CRACKED":

    # Ask for guess
    guess = get_guess()

    # Give the clues
    clueReport = generate_clues(guess,secretCode)
    print("Here is the result of your guess:")
    for clue in clueReport:
        print(clue)
