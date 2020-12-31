enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
}
all_enemies=[]


for x in range(0, 10):
    all_enemies.append(enemy.copy())
print(all_enemies)
print("**************************")
for ene in all_enemies:
    print(ene)
print("+++++++++++++++++++++++++++++")
all_enemies[5]['health']=3
for ene in all_enemies:
    print(ene)

