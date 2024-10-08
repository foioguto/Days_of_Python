country = input("Country name: ") 
visits = int(input("Number of visits: ")) 
list_of_cities = eval(input("Cities: ")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

def add_new_country(name, times, cities):
    new_log = {}
    new_log["country"] = name
    new_log["visits"] = times
    new_log["cities"] = cities
    travel_log.append(new_log)

add_new_country(country, visits, list_of_cities)

print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")