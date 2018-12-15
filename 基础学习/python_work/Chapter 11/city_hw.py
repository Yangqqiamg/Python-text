def city_country_test(city, country, population=''):
    if population:
        full_message = city + ', ' + country +' - population ' + str(population)
    else:
        full_message = city + ', ' + country
    return full_message.title()
    pass

message = city_country_test('shanghai', 'china',649)
print(message)