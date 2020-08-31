from random import randint
def Check(key, guess):
    for i in guess:
        if i in key:
            key.replace(i, " ", 1)
        else:
            return False
    return True
def Fig(attempts):
    if attempts == 9:
        print("-----------------------")
    if attempts == 8:
        print("-----------------------")
        print("         O             ")
    if attempts == 7:
        print("-----------------------")
        print("         O             ")
        print("         |             ")
    if attempts == 6:
        print("-----------------------")
        print("         O             ")
        print("         |             ")
        print("        /              ")
    if attempts == 5:
        print("-----------------------")
        print("         O             ")
        print("         |             ")
        print("        / \            ")
    if attempts == 4:
        print("-----------------------")
        print("       \ O             ")
        print("         |             ")
        print("        / \            ")
    if attempts == 3:
        print("-----------------------")
        print("       \ O /           ")
        print("         |             ")
        print("        / \            ")
    if attempts == 2:
        print("-----------------------")
        print("       \ O /|          ")
        print("         |             ")
        print("        / \            ")
    if attempts == 1:
        print("Loosing breath counting take care!!!")
        print("-----------------------")
        print("       \ O_|/          ")
        print("         |             ")
        print("        / \            ")
    if attempts == 0:
        print("You lost :=(")
        print("Ypu let an innocent die...")
        print("Loosing breath counting take care!!!")
        print("-----------------------")
        print("         O_|           ")
        print("        /|\            ")
        print("        / \            ")



print("Welcome to Hang Man!!\n\tLets see that if you could save yourself.")
name = input("Enter your name: ")
print(f"Hallow {name}, try to guess words within in 10 wrong attempts.")
word = ['avengers', 'hulk', 'tony', 'freedom', 'play']
clues = ["World where a radioactive man fights along with a person from secret but advanced tribe.",
         "A guy who is smart & calm but violent & dum at same time.",
         "A person whose injury made him a hero.",
         "One of the only things for which any method to achieve can be neglected.",
         "Every person loves to do this at the beginning of their life."]
valid = "qwertyuioplkjhgfdsazxcvbnm"
num = randint(0, 4)
key = word[num]
print(clues[num])
guess = ""
attempts = 10
while attempts > 0 and len(guess) != len(key):
    temp = input("Enter your guess: ")
    if (temp in valid) and len(temp) == 1 and Check(key, guess+temp):
        guess += temp
        print(f"Congrats {name} :-) Its a right choice, characters: {guess}")
    else:
        attempts -= 1
        Fig(attempts)
        print("Wrong Guess {name} :-(")
    print(f"\tNo of attempts left: {attempts}")
if len(guess) != len(key):
    Fig(attempts)
else:
    print(f"Congrats {name}! you saved the day, criminal can't touch justice until a smart guy like you are around ;-)")
