import random
character = "1234567890abcdefghijklmnopqrstuvwxyz"
character_list = list(character)
password = input("Maak een wachtwoord: ")
guess = ""
while (guess != password):
    guess = random.choices(character_list,k=len(password))
    print(guess)
    guess = "".join(guess)
    print(guess)
print("Jouw wachtwoord is: " + guess)
