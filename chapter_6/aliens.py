aliens = []

for alien_number in range(30):
    new_aliens = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_aliens)


for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'blue'
        alien['points'] = 10
        alien['speed'] = 'fast'
for alien in aliens[:5]:
    print(alien)
print("The total number of aliens: " + str(len(aliens)))