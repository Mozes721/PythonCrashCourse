from pygal.maps.world import World 
for country_code in sorted(World.keys()):
    print(country_code, World[country_code])