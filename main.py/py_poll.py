# Import, open, and define the csv data file
import os
import csv
from statistics import mean
from typing import Counter
poll_data = os.path.join('python_challenge/py_resources/election_data.csv')    
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

# Print win percentages
khan_summary_percent = format(win_percentage_khan,'.3f')
correy_summary_percent = format(win_percentage_correy,'.3f')
li_summary_percent = format(win_percentage_li,'.3f')
tooley_summary_percent = format(win_percentage_tooley,'.3f')

# Print candidate votes
khan_summary_votes = format(khan_total_votes,',d')
correy_summary_votes = format(correy_total_votes,',d')
li_summary_votes = format(li_total_votes,',d')
tooley_summary_votes = format(tooley_total_votes,',d')

# Print title
print( 'Election Results')

print('----------------------------')

# Print total votes
print('Total Votes:  '+ format(counted_votes,',d'))

print('----------------------------')

# Print Candidate Summary
print('Khan: ' + khan_summary_percent +'%  (' + khan_summary_votes + ')')
print('Correy: ' + correy_summary_percent +'%  (' + correy_summary_votes + ')')
print('Li: ' + li_summary_percent +'%  (' + li_summary_votes + ')')
print("O'Tooley: " + tooley_summary_percent +'%  (' + tooley_summary_votes + ')')

print('----------------------------')

# Print winner of Election Results
winner = str(50.000)
if correy_summary_percent > winner:
    print('Winner: Correy')
elif li_summary_percent > winner:
    print('Winner: Li')
elif tooley_summary_percent > winner:
    print("Winner: O'Tooley")
else: khan_summary_percent > winner
print('Winner: Khan')


with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(counted_votes) + "\n")
    text.write("---------------------------------------\n")
    text.write('Khan: ' + khan_summary_percent +'%  (' + khan_summary_votes + "\n")
    text.write('Correy: ' + correy_summary_percent +'%  (' + correy_summary_votes + "\n")
    text.write('Li: ' + li_summary_percent +'%  (' + li_summary_votes + "\n")
    text.write("O'Tooley: " + tooley_summary_percent +'%  (' + tooley_summary_votes + "\n")
    text.write("---------------------------------------\n")
    text.write('Winner: Khan')