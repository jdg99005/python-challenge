import os

import csv

bank_csv = os.path.join("budget_data.csv")
filepath = "budget_data.csv"

print("Financial Analysis")
print("-------------------------------------------")


def budget_data(bank_data):
    months = str(bank_data[0])
    year = int(bank_data[1])
    profit_losses = int(bank_data[2])

    total_months = (months)
    total = int(sum(profit_losses[2]))
    average_change = round(int(total) / int(profit_losses[2]))
    greatest_increase = max(profit_losses[2])
    greatest_decrease = min(profit_losses[2])


    print(f'Total Months: {str(total_months)})')
    print(f"Total: {int(total)})")
    print(f"Average Change: {str(average_change)}")
    print(f"Greatest Increase: {title.append(max(profit_losses))}")
    print(f"Greatest Decrease:  {title.append(min(profit_losses))}")


with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:

      


