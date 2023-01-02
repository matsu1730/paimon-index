import genshin as gi
import genshinstats as gs
import simple_colors as sc

# Quantity Counting
fiveStar = 0;
fourStar = 0;
threeStar = 0;
currentPity = 0;

# Getting authKey from game log files
client = gi.Client()
client.authkey = gi.utility.get_authkey()

pity = gs.get_wish_history(authkey=client.authkey, banner_type=301, size=90)
history = gs.get_wish_history(authkey=client.authkey, banner_type=301, size=200)

# Pity Counter
for index, wish in enumerate(pity):
    if (wish['rarity'] != 5):
        currentPity += 1
        continue
    else:
        break

# Wish History
for wish in history:
    if (wish['rarity'] == 5):
        fiveStar += 1
        print(sc.yellow(f"{wish['time']} - {wish['name']} ({wish['rarity']}* {wish['type']})", 'bold'))
    elif (wish['rarity'] == 4):
        fourStar += 1
        print(sc.magenta(f"{wish['time']} - {wish['name']} ({wish['rarity']}* {wish['type']})", 'bold'))
    else:
        threeStar += 1
        print(sc.blue(f"{wish['time']} - {wish['name']} ({wish['rarity']}* {wish['type']})"))


print("\nWish Results(Last 200): \n")
print(sc.yellow(f"5*: {fiveStar}", 'bold'))
print(sc.magenta(f"4*: {fourStar}", 'bold'))
print(sc.blue(f"3*: {threeStar}\n", 'bold'))
print(sc.green(f"Current Pity Counter: {currentPity} ({90 - currentPity} Wishes until you hit Pity))"))