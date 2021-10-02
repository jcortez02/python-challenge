# Import, open, and define the csv data file
import os
import csv
from statistics import mean
from typing import Counter
budget_data_csv = os.path.join("/Users/jacobcortez/Documents/GitHub/DS_Repos/python_challenge/py_resources/budget_data.csv")
with open(budget_data_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

# Skip the header row for csv file
    csv_header = next(csv_reader)
    print(f"{csv_header}")

# Empty list    
    month_list = []
    pnl_list = []  
    pnl_changes = []  
    

# Read each row of data after the header
    for row in csv_reader:
        print(row)

# Fill my empty lists
        month_list.append(row[0])
        pnl_list.append(int(row[1]))

# Count the length of month list
        count_month = print(len(month_list))

# What is the sum of PNL list
        print(sum(pnl_list))

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    for i in range(1,len(pnl_list)):
        pnl_changes.append(pnl_list[i] - pnl_list[i-1])
    
# Calcluate average of profit/loss changes
        print(mean(pnl_changes))
       
# What is the greatest increase in profits?
        print(max(pnl_list))

# What is the greatest decrease in profits?
    print(min(pnl_list))

# Print answers in summary text

    print("Financial Analysis")

    print("----------------------------------------")

    print("Total Months: " + count_month + "") 