import csv, os

class DataLoader:
    def __init__(self):
        __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

        self.cities = []
        with open(os.path.join(__location__, 'Cities.csv')) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.cities.append(dict(r))

    def filter(self, condition):
        return [item for item in self.cities if condition(item)]
    
    def aggregate(self, aggregation_key, aggregation_function, data=None):
        source = data if data is not None else self.cities
        values = [item[aggregation_key] for item in source]
        return aggregation_function(values)


table = DataLoader()


# Print all cities in Germany
print(table.filter(lambda x: x['country'] == 'Germany'))

# Print all cities in Spain with a temperature above 12°C

print(table.filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12))

# Count the number of unique countries

print(len(set(item['country'] for item in table.cities)))

# Print the average temperature for all the cities in Germany

germany_list = table.filter(lambda x: x['country'] == 'Germany')

print(table.aggregate("temperature", lambda x: sum(map(float, x)) / len(x), germany_list))

# Print the max temperature for all the cities in Italy
italy_list = table.filter(lambda x: x['country'] == 'Italy')
print(table.aggregate("temperature", lambda x: max(map(float, x)), italy_list))



