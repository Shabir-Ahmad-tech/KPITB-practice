# ==========================================
# PYTHON TUPLES: THE LOCKED TREASURE CHEST 🔒
# ==========================================
# A Tuple is like a List, but with one HUGE difference:
# Once you lock it, you CANNOT change it! It's Immutable.

print("--- 1. Making Your Locked Chest (Creation) ---")
# Tuples use round brackets ( )
# Think of this as a permanent record, like your Game ID or Birth Date.
my_id = ("Pro_Gamer_99", "Level 50", "Diamond Rank")
print("My Fixed ID Info:", my_id)

# Even a single item needs a comma to be a tuple!
solo_item = ("Legendary Sword",) # Without the comma, it's just a string.
print("Solo Item Tuple:", solo_item)

print("\n--- 2. The Golden Rule: NO CHANGES! (Immutability) ---")
print("# If I try to do: my_id[0] = 'Noob_Player', Python will CRASH!")
print("# It's a 'Locked Chest' - you can't swap the items inside.")

print("\n--- 3. Opening the Chest (Accessing) ---")
# Just like lists, indexing starts at 0
print("My Username is:", my_id[0])
print("My Rank is:", my_id[2])

print("\n--- 4. Taking Items Out (Unpacking) ---")
# This is a super cool Tuple power. You can give each item a variable name!
username, level, rank = my_id
print(f"Username extracted: {username}")
print(f"Level extracted: {level}")

print("\n--- 5. Finding Stuff (Methods) ---")
scores = (10, 20, 10, 30, 10, 40)

# .count() - How many times does a number appear?
print("How many times did I score 10?", scores.count(10))

# .index() - Where is the FIRST occurrence of a number?
print("When did I first score 30? At position:", scores.index(30))

print("\n--- 6. Why Use Tuples? ---")
# 1. They are FASTER than lists.
# 2. They are SAFE - nobody can accidentally change your important data.
# 3. Use them for things that SHOULDN'T change (like X, Y coordinates).

coordinates = (45.123, -93.456)
print("Locked Map Coordinates:", coordinates)

# ==========================================
# CONGRATS! You've mastered the Locked Chest! 🔓
# ==========================================
