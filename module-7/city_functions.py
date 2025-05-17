def city_country(city, country, population=None, language=None):
    """Return a string like 'City, Country, population xxx, Language'."""
    country_codes = {'usa', 'uk', 'uae', 'prc', 'drc', 'ussr'}
    if country.lower() in country_codes:
        country_str = country.upper()
    else:
        country_str = country.title()
    result = f"{city.title()}, {country_str}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

print(city_country('Tokyo', 'Japan'))
print(city_country('Delhie', 'India', '28,514,000',))
print(city_country('Shanghai', 'China', '25,582,000', 'Mandarin'))
print(city_country('New York', 'USA'))
print(city_country('Los Angeles', 'USA'))
print(city_country('London', 'UK'))
print(city_country('Paris', 'France'))
print(city_country('Berlin', 'Germany'))
print(city_country('Madrid', 'Spain'))
print(city_country('Rome', 'Italy'))
print(city_country('Moscow', 'Russia'))
print(city_country('Toronto', 'Canada'))
print(city_country('Sydney', 'Australia'))
print(city_country('Rio de Janeiro', 'Brazil'))