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

# Empty list    
    month_list = []
    pnl_list = []  
    pnl_changes = []  

# Read each row of data after the header
    for row in csv_reader:


# Fill my empty lists
        month_list.append(row[0])
        pnl_list.append(int(row[1]))
        
# Count the length of month list
    count_month = len(month_list)
    count_month_str = str(count_month)

# What is the sum of PNL list
    total_list = (sum(pnl_list))
    total_list_str = str(total_list)

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
 # Create dictionary    
    for i in range(1,len(pnl_list)):
        pnl_changes.append(pnl_list[i] - pnl_list[i-1])  
 
# Calcluate average of profit/loss changes
    average_change = format(mean(pnl_changes),'.2f')
    average_change_str = str(average_change)   

# What is the greatest increase in profits?
    greatest_increase = max(pnl_changes)
    greatest_increase_str = str(greatest_increase)

# What is the greatest decrease in profits?
    greatest_decrease = min(pnl_changes)
    greatest_decrease_str = str(greatest_decrease)

# What is the dates of greatest increase/decrease in profits?
    greatest_increase_date = month_list[pnl_changes.index(greatest_increase)+1]  
    greatest_decrease_date = month_list[pnl_changes.index(greatest_decrease)+1]

# Print answers in summary text

    print("Financial Analysis")

    print("----------------------------------------")

    print("Total Months: "+ count_month_str)  
    print('Total:  $'+ total_list_str)
    print('Average Change: $'+ average_change_str)
    print('Greatest Increase In Profits: '+ greatest_increase_date + ' ' + '($' + greatest_increase_str + ')')
    print('Greatest Decrease In Profits: '+ greatest_decrease_date + ' ' + '($' + greatest_decrease_str + ')')


with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + count_month_str + "\n")
    text.write("    Total Profits: " + "$" + total_list_str + "\n")
    text.write("    Average Change: " + '$' + average_change_str + "\n")
    text.write("    Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + greatest_increase_str + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + greatest_decrease_str + ")\n")
    text.write("----------------------------------------------------------\n")