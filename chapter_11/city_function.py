def get_city_country(city, country, population):
    output_string = city.title() + ", " + country.title()
    if population:
        output_string += ' population ' + str(population)
    return output_string


