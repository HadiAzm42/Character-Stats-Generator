import random
print("⚔️ Character Stats Generator ⚔️")
  
sides = int(input("How many sides?: "))
playGame = "yes"

def dice(sides):
  

def rollDice(sides):
  print("You rolled ", random.randint(1,sides))
  return rollDice(10)
while playGame == "yes":
    rollDice(sides)
    playGame = input("Roll again?")
