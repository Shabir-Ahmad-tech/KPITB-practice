# ==========================================
# PYTHON DAY 02: THE LEVEL GATEKEEPER 🛡️
# ==========================================
# In Python, we use 'if' statements to make decisions.
# It's like a path in a game that only opens if you have the right stats!

print("--- 1. The Basic IF ---")
level = 15
# The syntax: if CONDITION :
if level > 10:
    print("Welcome! You are high enough level to enter.")
    # IMPORTANT: Notice the indentation (4 spaces). 
    # Python only runs this line if the 'if' is True!

print("\n--- 2. IF-ELSE (The Choice) ---")
has_key = False

if has_key == True:
    print("Door Unlocked! You used the Skeleton Key.")
else:
    print("Door Locked. You need to find a key first!")

print("\n--- 3. IF-ELIF-ELSE (The Rank Rewards) ---")
# 'elif' is short for 'else if'. Use it for multiple choices.
rank = "Platinum"

if rank == "Gold":
    print("Reward: A Golden Sword!")
elif rank == "Platinum":
    print("Reward: A Platinum Shield!")
elif rank == "Diamond":
    print("Reward: A Diamond Armor!")
else:
    print("Reward: A Rusty Knife.")

print("\n--- 4. Logical Power-Ups (AND & OR) ---")
# AND - BOTH must be True
# OR - AT LEAST ONE must be True

xp = 5000
member_status = True

# Level check with AND
if xp > 4000 and member_status == True:
    print("VIP Area Access Granted!")

# Access check with OR
has_pass = False
is_admin = True

if has_pass or is_admin:
    print("Access Granted (Pass or Admin power used).")

print("\n--- 5. The Indentation Rule ---")
# Inside the IF = 4 spaces
# Outside the IF = Back to the start
if True:
    print("I am INSIDE the if.")
print("I am OUTSIDE the if (I always run).")

# ==========================================
# CONGRATS! You can now control the Game logic! 🎮
# ==========================================
