import genshinstats as gs

# account data and browser cookies
# uid = 601273390;
cookies = gs.get_browser_cookies(browser= 'edge')
gs.set_cookie(cookies)

# coleta recompensa de Check In
print("Buscando recompensas de Check In...")
recompensa = gs.claim_daily_reward()
if recompensa is not None:
    print(f"Recompensa de Check In resgatada! {recompensa['name']}({recompensa['cnt']})\n")
else:
    print("Não existem recompensas a serem resgatadas!\n")

# mostra as recompensas resgatadas até o momento
print("Recompensas resgatadas até o momento:")
for recompensas in gs.get_claimed_rewards():
    print(f"{recompensas['name']}({recompensas['cnt']})")