#heading
print("Welcome to the best Number Guessing Game")

#asking user for difficulty and setting it 
while True:
    difficulty = input("Choose difficulty of guess (Easy/Medium/Hard/Impossible/Custom):")
    if difficulty == "easy" or difficulty == "Easy" or difficulty == "EASY":
        min = 1
        max = 10
        break
    elif difficulty == "medium" or difficulty == "Medium" or difficulty == "MEDIUM":
        min = 1 
        max = 25
        break
    elif difficulty == "hard" or difficulty == "Hard" or difficulty == "HARD":
        min = 1
        max = 50
        break
    elif difficulty == "impossible" or difficulty == "Impossible" or difficulty == "IMPOSSIBLE":
        min = 1
        max = 200
        break
    elif difficulty == "custom" or difficulty == "Custom" or difficulty == "CUSTOM":
        min = int(input("What do you want the minimum number possible to be: "))
        max = int(input("What do you want the maximum number possible to be: "))
        break
    else: print("Wrong input, try again!")


#making the random number
import random
number = random.randint(min, max)

#checking if the guess is correct
while True:
    #shows the bounds of the number and asks for guess
    print("A number from ", min, " to ", max, " has been generated.")
    guess = input("Guess the number: ")
    #allows only ints to be entered
    if guess.isdecimal() :
        guess = int(guess)
    else:
        continue
    
    #checks if correct and if wrong gives tips
    if guess == number :
        print("You guessed correctly!")
        break
    else:
        if guess > max or guess < min:
            print("You are out of minimum and maximum bounds you dummy")
            continue
        elif guess > number:
            print("Guess Lower")
        elif guess < number:
            print("Guess Higher")
        

#thanks for playing 
#made by @miljkovicjovan on GitHub
#        @miljkovicjovan on Instagram
#        @miljkovicjovann on Twitter
