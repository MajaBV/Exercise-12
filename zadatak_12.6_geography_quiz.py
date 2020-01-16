import random

countries_cities = {"Afghanistan": "Kabul", "Albania": "Tirana", "Algeria": "Algiers", "Andorra": "Andorra la Vella", "Angola": "Luanda", "Antigua and Barbuda": "Saint John's", "Argentina": "Buenos Aires",
                    "Armenia": "Yerevan", "Australia": "Canberra", "Austria": "Vienna", "Azerbaijan": "Baku", "Bahamas": "Nassau", "Bahrain": "Manama", "Bangladesh": "Dhaka", "Barbados": "Bridgetown",
                    "Belarus": "Minsk", "Belgium": "Brussels", "Belize": "Belmopan", "Benin": "Porto-Novo", "Bhutan": "Thimphu", "Bolivia": "Sucre", "Bosnia and Herzegovina": "Sarajevo", "Botswana": "Gaborone",
                    "Brazil": "Brasilia", "Brunei": "Bandar Seri Begawan", "Bulgaria": "Sofia", "Burkina Faso": "Ouagadougou", "Burundi": "Gitega", "Cabo Verde": "Praia", "Cambodia": "Phnom Penh",
                    "Cameroon": "Yaounde", "Canada": "Ottawa","Central African Republic": "Bangui", "Chad": "N'Djamena", "Chile": "Santiago", "China": "Beijing", "Colombia": "Bogotá", "Comoros": "Moroni",
                    "Congo, Democratic Republic of the": "Kinshasa", "Congo, Republic of the": "Brazzaville","Costa Rica": "San Jose", "Cote d'Ivoire": "Yamoussoukro", "Croatia": "Zagreb", "Cuba": "Havana",
                    "Cyprus": "Nicosia", "Czechia": "Prague", "Denmark": "Copenhagen", "Djibouti": "Djibouti", "Dominica": "Roseau", "Dominican Republic": "Santo Domingo"}
def play_game():
    for country in countries_cities.items():
        country = random.choice(list(countries_cities.keys()))
        game = input("Game: What is the capital city of {0}? ".format(country))
        if game == countries_cities.get(country):
            print("Game: This is correct!")
            break
        else:
            print("Game: This is wrong!")

while True:
    selection = input("Would you like to A) play a new game or B) quit? ")

    if selection.upper() == "A":
        play_game()
    else:
        print("Game: Goodbye!")
        break
