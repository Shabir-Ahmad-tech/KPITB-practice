# ==========================================
# PYTHON DAY 02: THE ULTIMATE PLAYER PROFILER 📋
# ==========================================
# A Dictionary is like a database for your game.
# It uses KEY: VALUE pairs to keep track of EVERYTHING.

print("--- 1. Making the Profile ---")
player = {
    "name": "Ace_Ventura",
    "level": 25,
    "class": "Sniper",
    "points": 1500
}
print("Initial Player Info:", player)

print("\n--- 2. Safe Peeking with .get() ---")
# If you try player["rank"] and it doesn't exist, Python crashes.
# .get() is the HERO! It looks for the key, and if it's missing, it gives back 'None' instead of crashing.
rank = player.get("rank") 
print(f"Rank check: {rank}") 

# You can even set a default value if it's missing!
rank = player.get("rank", "Unranked") 
print(f"Rank with default: {rank}")

print("\n--- 3. Bulk Updates with .update() ---")
# Instead of one-by-one, you can update multiple things at once!
new_stats = {"level": 26, "points": 1800, "is_online": True}
player.update(new_stats)
print("Profile after Bulk Upgrade:", player)

print("\n--- 4. Deleting & Resetting ---")
# del - Permanently deletes a key
del player["is_online"]
print("After 'del' player['is_online']:", player)

# .pop() - Removes the key and GIVES it to you (useful if you need the data one last time)
old_level = player.pop("level")
print(f"Removed level {old_level}. Current Profile:", player)

print("\n--- 5. Looping (Printing the whole Profile) ---")
# You can loop through just keys, just values, or both!
print("Reading full profile entries:")
for category, data in player.items():
    print(f"  {category.upper()}: {data}")

print("\n--- 6. Nesting (Dictionary inside Dictionary) ---")
# This is how real games work!
player["inventory"] = {
    "primary": "Long Range Rifle",
    "secondary": "Knife",
    "ammo": 50
}
print("Advanced profile with Inventory:")
print(f"  Ammo count: {player['inventory']['ammo']}")

print("\n--- 7. The Final Reset ---")
# .clear() - Wipes the whole dictionary clean!
player.clear()
print("Profile after .clear():", player)

# ==========================================
# CONGRATS! You are now a Dictionary Master! �
# ==========================================
