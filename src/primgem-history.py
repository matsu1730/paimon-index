import genshinstats as gs
import genshin as gi
import simple_colors as sc

### WIP ###

count = 0

client = gi.Client()
client.authkey = gi.utility.get_authkey()

for log in gs.get_primogem_log(size=1000, lang="en-us", authkey=client.authkey):
    count += 1
    if (log['amount'] < 0 ):
        print(sc.red(f"{log['time']} - {log['reason']}: {log['amount']} Primogems"))
    else:
        print(sc.blue(f"{log['time']} - {log['reason']}: {log['amount']} Primogems"))

print(count)