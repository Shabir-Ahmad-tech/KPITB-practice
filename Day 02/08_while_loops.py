# ==========================================
# PYTHON DAY 02: SURVIVAL MODE (WHILE LOOPS) 🛡️
# ==========================================
# A 'while' loop runs AS LONG AS a condition is True.
# Use it when you don't know exactly how many times you need to loop!

print("--- 1. The Basic While Loop (The Health Bar) ---")
# This loop runs until the player's HP reaches 0.

hp = 50
while hp > 0:
    print(f"  [STATUS] Still alive! HP: {hp}")
    hp -= 10  # This is the most important part! If we don't decrease HP, the loop never stops.

print("  [!] Game Over. HP reached 0.")

print("\n--- 2. Using a Flag (The Game Loop) ---")
# A 'Flag' is a boolean variable that controls the loop.

game_active = True
rounds = 1

while game_active:
    print(f"  [ROUND {rounds}] Exploring the dungeon...")
    rounds += 1
    
    if rounds > 3:
        print("  [SYSTEM] Maximum rounds reached. Shutting down.")
        game_active = False # Flipping the flag stops the loop on the next check.

print("\n--- 3. While with Break (Emergency Exit) ---")
# You can use 'break' to jump out of a while loop instantly.

energy = 100
while True: # This is a 'Forever' loop...
    print(f"  Searching for Loot... Energy: {energy}")
    energy -= 20
    
    if energy <= 20:
        print("  [!] LOW ENERGY! Forced to stop looting.")
        break # ...until we hit this BREAK!

print("\n--- 4. The Infinite Loop WARNING ---")
# If you forget to update your variable (like hp -= 10), 
# your computer will be stuck looping FOREVER!
# If that happens, press CTRL + C to kill the script.

print("\n--- Summary: How to Build a While Loop ---")
print("1. Start your variable (e.g., hp = 50)")
print("2. Set the condition (e.g., while hp > 0)")
print("3. CHANGE the variable inside (e.g., hp -= 10)")

# ==========================================
# CONGRATS! You survived the While Loop! 🏆
# ==========================================
