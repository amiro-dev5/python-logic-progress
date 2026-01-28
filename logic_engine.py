import random

users = ["Admin", "Guest", "Amir", "Dev"]
target = random.randint(1, 50)
chances = 5
running = True

print("SYSTEM START")
for u in users:
    print(f"AUTHORIZED: {u}")

while running:
    print(f"REMAINING: {chances}")
    
    entry = int(input("INPUT: "))
    
    if entry == target:
        print("SUCCESS")
        running = False
    elif entry < target:
        print("INCREASE")
    else:
        print("DECREASE")
        
    chances = chances - 1
    
    if chances == 0 and running != False:
        print("FAILED")
        print(target)
        running = False

print("TERMINATED")