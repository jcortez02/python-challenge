# Import, open, and define the csv data file
import os
import csv
budget_data_csv = os.path.join(/Users/jacobcortez/Documents/GitHub/DS_Repos/python_challenge/py_resources/budget_data.csv)
with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

# Skip the header row for csv file
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")
