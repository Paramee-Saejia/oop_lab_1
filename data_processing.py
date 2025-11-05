import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany

temp = []
for city in cities:
    if city['country'] == 'Germany':
        temp.append(city['city'])
print(temp)
print()

# Print all cities in Spain with a temperature above 12°C

temp = []
for city in cities:
    if city['country'] == 'spain':
        if city['temperature'] > 12:
            temp.append(city['city'])

print(temp)
print()

# Count the number of unique countries

temp = []
count = 0

for city in cities:
    if city['country'] not in temp:
        count += 1
        temp.append(city['country'])
        

print(count)
print()

# Print the average temperature for all the cities in Germany

temp = []
temperature = 0

for city in cities:
    if city['country'] == 'Germany':
        temp.append(float(city['temperature']))

avg = sum(temp) / len(temp)
print(avg)
print()

# Print the max temperature for all the cities in Italy
temp = []

for city in cities:
    if city['country'] == 'Italy':
        temp.append(float(city['temperature']))

print(max(temp))