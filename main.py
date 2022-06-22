import random

computerOptions = ["Rock", "Paper", "Scissors"]
computerChoice = computerOptions[random.randint(0,2)]

print("Welcome to Rock, Paper, Scissors!")

userChoice = input("What is your weapon of choice?: ")

if(computerChoice == "Rock" and userChoice == "Paper"):
  print("basura (rock)")
elif(computerChoice == "Rock" and userChoice == "Scissors"):
  print("You won!!")
elif(computerChoice == "Rock" and userChoice == "Rock"):
  print("You tied! Try again!")
elif(computerChoice == "Scissors" and userChoice == "Paper"):
  print("You won!!")
elif(computerChoice == "Scissors" and userChoice == "Rock"):
  print("basura (scissors)")
elif(computerChoice == "Scissors" and userChoice == "Scissors"):
  print("You tied! Try again!")
elif(computerChoice == "Paper" and userChoice == "Rock"):
  print("You won!!")
elif(computerChoice == "Paper" and userChoice == "Scissors"):
  print("basura(paper)")
elif(computerChoice == "Paper" and userChoice == "Paper"):
  print("You tied! Try again!")
else:
  print("invalid option") 
done