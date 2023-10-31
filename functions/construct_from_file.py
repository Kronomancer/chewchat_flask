from classes.page import City, Restaurant

#parse restaurants.txt file. The first number indicsates 
def constructFromFile():
    cities = []  # List to hold the city objects
    current_city = None  # Variable to keep track of the current city while parsing

    with open('restaurants.txt', 'r') as file:
        # Read the first line with the counts and strip newline characters
        first_line = file.readline().strip()
        num_cities, num_restaurants_per_city = map(int, first_line.split())

        # Read each subsequent line
        for line in file:
            stripped_line = line.strip()

            # Check if the line is a city name
            if not stripped_line.startswith(' '):  # Cities are at the start of a new line
                current_city = City(stripped_line)  # Create a new city object
                cities.append(current_city)
            else:
                # It's a restaurant; parse name and description
                name_description = stripped_line.split(',', 1)  # Split once at the first comma
                restaurant_name = name_description[0].strip()
                restaurant_description = name_description[1].strip() if len(name_description) > 1 else ""

                # Create a new restaurant object and add it to the current city
                restaurant = Restaurant(restaurant_name, current_city, restaurant_description)
                current_city.add_restaurant(restaurant)

    return cities  # Return the list of cities with their associated restaurants
