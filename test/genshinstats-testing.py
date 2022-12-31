import genshinstats as gs
import genshin as gi

giClient = gi.Client()

cookiesGS = gs.get_browser_cookies(browser= 'edge')

print(cookiesGS)
print(cookiesGI)


#stats = gs.get_user_stats(uid)['stats']
#for field, value in stats.items():
#    print(f"{field} : {value}")