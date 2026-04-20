import random
ComNumber=random.randint(1,100)
userInput=int(input("Enter a number between 1 and 100:"))
if userInput>ComNumber:
    print("Too high! Try again.")
elif userInput<ComNumber:
    print("Too low! Try again.")
else:
    print("Congratulatiions!! you are guessed the number correctly!!")