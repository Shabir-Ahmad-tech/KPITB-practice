# ==========================================
# PYTHON DAY 02: THE SKILL CRAFTER (FUNCTIONS)
# ==========================================
# A Function is a block of code that you can reuse anytime.
# Think of it like a "Custom Macro" or a "Saved Skill".

print("--- 1. Defining Your First Skill ---")
# Use 'def' to define a function.
def say_hello():
    print("  [SYSTEM] Hello, Player! Ready to fight?")

# IMPORTANT: Defining it doesn't run it. You have to CALL it!
say_hello() 
say_hello() # We can use it as many times as we want!

print("\n--- 2. Skills with Stats (Parameters) ---")
# Parameters are like inputs. You put them inside the brackets ().

def attack(enemy_name, damage):
    print(f"  [ATTACK] You hit {enemy_name} for {damage} damage!")

# Now we call it and pass in the actual stats
attack("Goblino", 50)
attack("Draco", 120)

print("\n--- 3. Getting Results Back (Return) ---")
# Sometimes a skill needs to calculate something and GIVE it back to you.

def heal_check(current_hp, potion_value):
    new_hp = current_hp + potion_value
    return new_hp # This sends the result back to where it was called.

# We save the result in a variable
my_hp = 30
print(f"  Current HP: {my_hp}")

my_hp = heal_check(my_hp, 25)
print(f"  HP After Healing: {my_hp}")

print("\n--- 4. Organizing Your Toolbox ---")
# Why use functions?
# 1. Cleaner code (less messy).
# 2. Easy to fix (change it once, it fixes everywhere).
# 3. Sharing! You can use skills across your whole program.

# ==========================================
# CONGRATS! You are now a Skill Crafter!
# ==========================================
