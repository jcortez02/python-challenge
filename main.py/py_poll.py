# Import, open, and define the csv data file
import os
import csv
from statistics import mean
from typing import Counter
poll_data = os.path.join('/Users/jacobcortez/Documents/GitHub/DS_Repos/python_challenge/py_resources/election_data.csv')    
with open (poll_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

# Skip the header row for csv file
    csv_header = next(csv_reader)
    print(f"{csv_header}")

# Empty list    
    voter_list = []
    county_list = []  
    candidate_list = []

# Read each row of data after the header
    for row in csv_reader:
        print(row)

# Fill my empty lists
        voter_list.append(int(row[0]))
        county_list.append(row[1])    
        candidate_list.append(row[2])

# Count the length of month list
    counted_votes = print(len(voter_list))        
