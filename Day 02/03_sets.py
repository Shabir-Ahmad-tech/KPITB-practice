# ==========================================
# PYTHON DAY 02: THE UNIQUE ITEM REPOSITORY 💎
# ==========================================
# A Set is a special collection where every item MUST be unique.
# It's perfect for things that shouldn't repeat, like usernames or items in a bag.

print("--- 1. Making Your Set Collection ---")
# Use curly brackets { } to make a set
inventory = {"Axe", "Shield", "Mana", "Shield"} # "Shield" is added twice!
print("Inventory (No duplicates!):", inventory)

print("\n--- 2. Adding & Removing Items ---")
inventory.add("Sword") # Add one item
print("After adding Sword:", inventory)

inventory.remove("Mana") # Remove an item
print("After removing Mana:", inventory)

print("\n--- 3. Set Magic: Power-Up Operations ---")
# Let's compare sets of friends or teams!
player_1_gear = {"Sword", "Shield", "Axe"}
player_2_gear = {"Bow", "Shield", "Arrows"}

# A. UNION - Combining all items (No duplicates)
all_gear = player_1_gear.union(player_2_gear)
print("Union (All gear combined):", all_gear)

# B. INTERSECTION - Finding what's in BOTH sets
shared_gear = player_1_gear.intersection(player_2_gear)
print("Intersection (What both have):", shared_gear)

# C. DIFFERENCE - What is in Player 1 but NOT Player 2?
unique_to_p1 = player_1_gear.difference(player_2_gear)
print("Difference (Only Player 1 has this):", unique_to_p1)

print("\n--- 4. Unordered Nature ---")
# Remember: Sets have NO indexes like inventory[0].
# The order changes every time you look at them!
print("Current inventory order:", inventory)

print("\n--- 5. Checking for Items ---")
if "Sword" in inventory:
    print("Yes! The Sword is in your unique collection.")

# ==========================================
# CONGRATS! You mastered Sets for Day 02! 🔥
# ==========================================
