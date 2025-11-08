Lab Overview
This lab focuses on querying data from a CSV file using Python. You will create a data_processing.py file to perform the queries and practice using Git to track your progress.
- In commit 1, you write basic query code without using any functions.
- In commit 2, you refactor the code into a procedural style using functions.
- In commit 3, you convert the code into an object-oriented style using classes.
The goal is to understand how to structure data analysis code and manage changes using Git.

oop_lab_2/
├── README.md              # This file
├── Cities.csv             # Dataset file
└── data_processing.py     # Python file for querying the data

Design Overview

DataLoader Class

Purpose: Loads CSV files and returns structured data.

Attributes:
- base_path: Path to the directory containing data files.

Methods:
- load_csv(filename): Loads a CSV file and returns a list of dictionaries, one per row.

Table Class

Purpose: Encapsulates tabular data and provides filtering and aggregation operations.

Attributes:
- name: Identifier for the table (e.g., 'cities').
- table: List of dictionaries representing rows.

Methods:
- filter(condition): Returns a new Table containing rows that satisfy the given condition.
- aggregate(func, key): Applies an aggregation function (e.g., sum, max) to the values of a specified key. Values are converted to float for numeric operations.

How to Test and Run

1. Ensure Cities.csv is in the same directory as data_processing.py.
2. Run the script:
python data_processing.py
