import genshinstats as gs
import genshin as gi

### WIP ###

client = gi.Client()
client.authkey = gi.utility.get_authkey()

for log in gs.get_primogem_log(size=1, lang="pt-pt", authkey=client.authkey):
    print(log)