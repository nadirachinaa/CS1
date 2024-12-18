import random

name = input ("What is your name?")                     #input what is their name
print("Good luck", name)                                # 
words = ['hello', 'world', 'python']
wins = 0
games = 0

while True:                                                                                                                 
    word = random.choice(words)
    display = list(word)
    random.shuffle(display)
    display = "".join(display)
    turns = 5

    while turns > 0:
        guess = input(f"Unscramble {display}: ")

        if guess == word:
            print("You got it!")
            wins += 1
            break

        while True:
            scramble = input("Nope! Would you like to rescramble? y/n: ")

            if scramble == "y":
                display = list(word)
                random.shuffle(display)
                display = "".join(display)
                break
            elif scramble == "n":
                break
            else:
                print("Invalid Response")

        turns -= 1

    print("The word was", word)
    games += 1

    while True:
        play_again = input(f"You have won {wins} out of {games} games. Would you like to play again? y/n: ")

        if play_again == "y":
            break
        elif play_again == "n":
            exit()
        else:
            print("Invalid Response")
        

                

