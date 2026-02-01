# ==========================================
# PYTHON LISTS: THE ULTIMATE SQUAD GUIDE 🎮
# ==========================================
# Imagine a List is like your Gaming Squad or a Team.
# It's a place to keep your stuff in order!

print("--- 1. Making Your Squad (Creation) ---")
# You create a list using square brackets [ ]
squad = ["Ali", "Hamza", "Zain"]
print("My Squad:", squad)

print("\n--- 2. Adding New Members (Adding) ---")
# .append() - Adds someone to the end of the line
squad.append("Umer") 
print("After append:", squad)

# .insert() - Put someone exactly where you want (index starts at 0)
squad.insert(1, "Bilal") # Bilal is now at index 1
print("After inserting Bilal at position 1:", squad)

# .extend() - Add another whole group at once
new_players = ["Saad", "Hassan"]
squad.extend(new_players)
print("After adding a whole new group:", squad)

print("\n--- 3. Removing People (Removing) ---")
# .remove() - Kick someone out by their name
squad.remove("Hamza")
print("Hamza left the squad:", squad)

# .pop() - Remove someone by their position (index)
# If you don't give a number, it removes the last person.
kicked_player = squad.pop(0) # Kicks whoever is first (Ali)
print("We kicked the captain:", kicked_player)
print("Squad now:", squad)

print("\n--- 4. Finding Your Friends (Searching) ---")
# Check if someone is in the squad
if "Zain" in squad:
    print("Yes! Zain is online.")

# Find WHAT POSITION they are at
position = squad.index("Zain")
print("Zain is at position number:", position)

print("\n--- 5. Picking a Sub-Team (Slicing) ---")
# Syntax is [start : end]
# Grab the first 3 players
top_three = squad[0:3] 
print("Our Top 3 players are:", top_three)

print("\n--- 6. Arranging the Squad (Sorting) ---")
# .sort() - Put them in Alphabetical order (A to Z)
squad.sort()
print("Squad in A-Z order:", squad)

# .reverse() - Flip the whole list upside down
squad.reverse()
print("Squad flipped upside down:", squad)

print("\n--- 7. Other Useful Power-ups ---")
# len() - How many players total?
print("Total players in squad:", len(squad))

# Change a name directly
squad[0] = "ULTRA_GAMER"
print("Renamed the first player:", squad)

# .clear() - Kick EVERYONE out at once
squad.clear()
print("Squad after clearing everyone:", squad)

# ==========================================
# CONGRATS! You now control the Squad! 🚀
# ==========================================
