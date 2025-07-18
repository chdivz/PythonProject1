import random
def roll_dice():
    return random.randint(1, 6)

print("Rolling Dice")
print(f"You rolled a {roll_dice()}")