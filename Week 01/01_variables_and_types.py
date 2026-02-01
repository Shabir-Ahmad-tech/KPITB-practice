# ==========================================
# PYTHON DAY 01: CHARACTER CREATOR 🛠️
# ==========================================
# In Python, we use Variables to store information.
# Think of a Variable as a box with a label on it!

print("--- 1. Variables & Naming ---")
# To make a variable, write the name, then '=' then the value.
# Note: No spaces in names! Use underscores _
player_name = "Shadow_Stalker"
print("Player Name:", player_name)

print("\n--- 2. Core Data Types ---")

# A. STRINGS (Text)
character_class = "Warrior"
print(f"Class: {character_class} (Data Type: {type(character_class)})")

# B. INTEGERS (Whole Numbers)
health_points = 100
level = 15
print(f"HP: {health_points}, Level: {level} (Data Type: {type(health_points)})")

# C. FLOATS (Decimal Numbers)
movement_speed = 5.5
print(f"Speed: {movement_speed} (Data Type: {type(movement_speed)})")

# D. BOOLEANS (True or False)
is_online = True
print(f"Online Status: {is_online} (Data Type: {type(is_online)})")

print("\n--- 3. Math Operators (+, -, *, /, //, %, **) ---")
a = 10
b = 3

print(f"Addition (10 + 3): {a + b}")
print(f"Subtraction (10 - 3): {a - b}")
print(f"Multiplication (10 * 3): {a * b}")
print(f"Division (10 / 3): {a / b}")
print(f"Floor Division (10 // 3): {a // b}") # Removes decimal
print(f"Modulus (10 % 3): {a % b}") # Gives the remainder
print(f"Power (10 ** 3): {a ** b}") # 10 to the power of 3

print("\n--- 4. Assignment Operators (=, +=, -=, *=, /=) ---")
# These are "Shortcuts" for math!
coins = 100
coins += 50  # Same as coins = coins + 50
print("Coins after += 50:", coins)

coins -= 20  # Same as coins = coins - 20
print("Coins after -= 20:", coins)

coins *= 2   # Double the coins
print("Coins after *= 2:", coins)

print("\n--- 5. Comparison Operators (==, !=, >, <, >=, <=) ---")
# These always give back a Boolean (True or False)
my_hp = 50
enemy_hp = 50

print("Is my_hp equal to enemy_hp? (==)", my_hp == enemy_hp)
print("Is my_hp NOT equal to 100? (!=)", my_hp != 100)
print("Is my_hp greater than 20? (>)", my_hp > 20)

print("\n--- 6. Logical Operators (and, or, not) ---")
# Use 'and' if BOTH conditions must be True
# Use 'or' if ANY one condition can be True
# Use 'not' to flip the result

has_key = True
has_energy = False

print("Can open door (Key AND Energy):", has_key and has_energy)
print("Can open door (Key OR Energy):", has_key or has_energy)
print("Flip key status (NOT Key):", not has_key)

print("\n--- 7. Type Conversion (Casting) ---")
score = 500
print("Score as string: " + str(score))

xp_input = "250"
total_xp = int(xp_input) + 50
print("Total XP:", total_xp)

# ==========================================
# BOOM! Your Character is created! 🚀
# ==========================================
