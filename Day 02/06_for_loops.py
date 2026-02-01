# ==========================================
# PYTHON DAY 02: THE FOR LOOP MASTER 
# ==========================================
# A 'for' loop is used to repeat an action. 
# Instead of writing the same line 10 times, you use a loop!

print("--- 1. The Squad Loop (Iterating Lists) ---")
# This visits every item in a list one by one.
squad = ["Ali", "Hamza", "Zain", "Saad"]

for player in squad:
    print(f"Checking status for: {player}")
    print(f"  {player} is Online! [v]")

print("\n--- 2. Leveling Up with range() ---")
# range(number) tells Python how many times to repeat.
# Note: range(5) goes from 0 to 4 (5 numbers total).
print("Training session started...")
for i in range(5):
    print(f"  Push-up number {i+1} done!")

print("\n--- 3. Custom Range (Start, Stop, Step) ---")
# range(start, stop, step)
print("Counting down the Match Timer:")
for timer in range(5, 0, -1):
    print(f"  T-minus {timer}...")
print("  MATCH STARTED!")

print("\n--- 4. Game Controls: Break and Continue ---")

# CONTINUE - Skip the current turn and go to the next one
print("Looting items (Skipping trash items):")
items = ["Sword", "Trash", "Shield", "Trash", "Potion"]
for item in items:
    if item == "Trash":
        continue # Skips the rest of this loop and moves to the next item
    print(f"  Collected: {item}")

# BREAK - Stop the whole loop immediately
print("\nScanning for Boss (Stop when found):")
enemies = ["Gnome", "Gnome", "BOSS", "Gnome"]
for enemy in enemies:
    print(f"  Checking {enemy}...")
    if enemy == "BOSS":
        print("  ALERT: Boss found! Stopping scan.")
        break # Ends the loop right here

print("\n--- 5. Nested Loops (Chests inside Rooms) ---")
# A loop inside another loop!
rooms = ["Blue Room", "Red Room"]
chests_per_room = ["Chest A", "Chest B"]

for room in rooms:
    print(f"Entering {room}...")
    for chest in chests_per_room:
        print(f"  Opening {chest} in {room}")

# ==========================================
# CONGRATS! You are now the Loop Master! 
# ==========================================
