# ==========================================
# PYTHON DAY 02: HACK THE LOOP 🛠️
# ==========================================
# Sometimes you need to change how a loop behaves while it's running.
# We call these 'Loop Control' statements.

print("--- 1. The BREAK Statement (The Emergency Exit) ---")
# Use 'break' to stop a loop completely, even if it's not finished.

print("Scenario: Scanning for a Exit Door in a dungeon...")
rooms = ["Room 1", "Room 2", "EXIT DOOR", "Room 4", "Room 5"]

for room in rooms:
    print(f"  Entering {room}...")
    if room == "EXIT DOOR":
        print("  [!] Exit Found! Stopping the search immediately.")
        break  # This kills the loop right here. room 4 and 5 are never visited.

print("\n--- 2. The CONTINUE Statement (The Skip Turn) ---")
# Use 'continue' to skip the rest of the current turn and jump to the next one.

print("Scenario: Collecting Loot (But skipping the heavy rocks)...")
found_items = ["Health Potion", "Heavy Rock", "Silver Sword", "Heavy Rock", "Mana Crystal"]

for item in found_items:
    if item == "Heavy Rock":
        print("  [X] Skipping heavy rock... too heavy to carry!")
        continue  # Skips the print line below and jumps to the next item in the list.
    print(f"  [+] Looted: {item}")

print("\n--- 3. The PASS Statement (The Placeholder) ---")
# 'pass' does NOTHING. 
# We use it when Python requires code but we haven't written it yet.
# Think of it as a "Place Your Feature Here" sign.

level = 10
if level == 10:
    # We want to give a special achievement but haven't decided what yet.
    # Without 'pass', Python would crash because it expects something here.
    pass 
    print("  Achievement logic will be added here later (using 'pass' for now).")

print("\n--- Summary: Cheat Sheet ---")
print("- break: 'Kills' the loop and leaves.")
print("- continue: 'Skips' the rest of this turn.")
print("- pass: 'Wait', I'll write code here later.")

# ==========================================
# CONGRATS! You can now hack any Loop! 🚀
# ==========================================
