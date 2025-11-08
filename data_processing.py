import csv, os
from pathlib import Path

class DataLoader:
    """Handles loading CSV data files."""

    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files."""
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)

    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries."""
        filepath = self.base_path / filename
        data = []

        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))

        return data


class Table:
    """Represents a table of data with filtering and aggregation capabilities."""

    def __init__(self, name, rows):
        """Initialize the Table with a name and list of row dictionaries."""
        self.name = name
        self.table = rows

    def filter(self, condition):
        """Return a new Table containing rows that satisfy the condition."""
        filtered_rows = [row for row in self.table if condition(row)]
        return Table(self.name + "_filtered", filtered_rows)

    def aggregate(self, func, key):
        """Apply an aggregation function to the values of a specific key."""
        values = []
        for row in self.table:
            try:
                values.append(float(row[key]))
            except (ValueError, KeyError):
                continue
        return func(values)




loader = DataLoader()
cities = loader.load_csv('Cities.csv')
my_table1 = Table('cities', cities)

# Print the average temperature of all the cities
my_value = my_table1.aggregate(lambda x: sum(x) / len(x), 'temperature')
print(my_value)
print()

# Print all cities in Germany
my_cities = my_table1.filter(lambda x: x['country'] == 'Germany')
cities_list = [[city['city'], city['country']] for city in my_cities.table]
print("All the cities in Germany:")
for city in cities_list:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
my_cities = my_table1.filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12.0)
cities_list = [[city['city'], city['country'], city['temperature']] for city in my_cities.table]
print("All the cities in Spain with temperature above 12°C:")
for city in cities_list:
    print(city)
print()

# Count the number of unique countries
my_countries = len(set(row['country'] for row in my_table1.table))
print("The number of unique countries is:")
print(my_countries)
print()

# Print the average temperature for all the cities in Germany
my_value = my_table1.filter(lambda x: x['country'] == 'Germany').aggregate(lambda x: sum(x) / len(x), 'temperature')
print("The average temperature of all the cities in Germany:")
print(my_value)
print()

# Print the max temperature for all the cities in Italy
my_value = my_table1.filter(lambda x: x['country'] == 'Italy').aggregate(max, 'temperature')
print("The max temperature of all the cities in Italy:")
print(my_value)
print()