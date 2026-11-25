#create a function that takes in a city and country and returns a string in the format 'City, Country'
def city_country(city, country, population=None, language=None):
    """Return a string in the format 'City, Country'."""
    result = f"{city.title()}, {country.title()}"

    if population is not None:
        result += f" - population {population}"

    if language is not None:
        result += f", {language}"

    return result

if __name__ == "__main__":
    print(city_country("Omaha", "United States"))

    print(city_country("Paris", "France", 2100000))

    print(city_country("Santiago", "Chile", 5000000, "Spanish"))


