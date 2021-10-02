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

# Empty list    
    voter_list = []
    county_list = []  
    candidate_list = []

# Read each row of data after the header
    for row in csv_reader:

# Fill my empty lists
        voter_list.append(row[0])
        county_list.append(row[1])    
        candidate_list.append(row[2])

# The total number of votes cast
# Count the length of month list  
counted_votes = int(len(voter_list))        

# The total number of votes each candidate won
# Count votes for each candidate       
khan_total_votes = int(candidate_list.count('Khan'))
correy_total_votes = int(candidate_list.count('Correy'))
li_total_votes = int(candidate_list.count('Li'))
tooley_total_votes = int(candidate_list.count("O'Tooley"))

# The percentage of votes each candidate won
win_percentage_khan = (khan_total_votes / counted_votes) * 100
win_percentage_correy = (correy_total_votes / counted_votes) * 100
win_percentage_li = (li_total_votes / counted_votes) * 100
win_percentage_tooley = (tooley_total_votes / counted_votes) * 100


# Print total votes
print(counted_votes)


# Print candidate votes
print(khan_total_votes)
print(correy_total_votes)
print(li_total_votes)
print(tooley_total_votes)


# Print win percentages
print(win_percentage_khan)
print(win_percentage_correy)
print(win_percentage_li)
print(win_percentage_tooley)


