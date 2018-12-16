
# printing data summary
OUTPUT = """  Financial Analysis
  ----------------------------
  Total Months: %i
  Total: $%i
  Average  Change: $%i
  Greatest Increase in Profits: %s ($%i)
  Greatest Decrease in Profits: %s ($%i)
"""
#print(OUTPUT)
import os
import csv

def return_average_change(list): 
  length = len(list)
  total_months_sum = 0
  for i in list: 
    total_months_sum += i 
  average_change = total_months_sum/length
  average_change = round(average_change,2)
  return average_change


# The total number of months included in the dataset
total_months = 0 

# The total net amount of "Profit/Losses" over the entire period
total_profit_loss = 0 

# The average change in "Profit/Losses" between months over the entire period
# sum of months_changes/total month = avg change 
average_change = 0 

change_list = []
last = 0
#Create a loop to find the diff b/t each months 
# The greatest increase in profits (date and amount) over the entire period
greatest_increase = 0 

# The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = 0 

file_path = os.path.join('budget_data.csv')

with open(file_path, 'r') as file_object: 
  budget_data = csv.reader(file_object)

  for row in budget_data: 
    num = int(row[1])
    total_months = total_months + 1 
    total_profit_loss = total_profit_loss + num
    # find the diff b/t each months 
       
    if (last == 0): 
      last = num
    else:    
      current = num
      months_change = current - last
      change_list.append(months_change)
      last = current
 
  total_months_change = sum(change_list)
  average_change = return_average_change(change_list)
  greatest_increase = max(change_list)
  greatest_decrease = min(change_list)

  print(file_object)
  print(f"Total Months: {total_months}")
  print(f"Total: ${total_profit_loss}")
  print(f"Average Change: ${average_change}")
  print(f"Greatest Increase in Profits:  ${greatest_increase}")
  print(f"Greatest Decrease in Profits:  ${greatest_decrease}") 
  # print(f"total_months_change:${total_months_change}")
  # print(change_list)

output = (
  "Financial Analysis\n"
  "---------------------------"
  f"Total Months: {total_months}\n"
  f"Total: ${total_profit_loss}\n"
  f"Average Change: ${average_change}\n"
  f"Greatest Increase in Profits: ${greatest_increase}\n"
  f"Greatest Decrease in Profits: ${greatest_decrease}\n"
  # f"total_months_change:${total_months_change}\n"
)

output_file = "sample.txt"

with open(output_file, 'w') as txt_file:
  txt_file.write(output) 








# for x in range(0,51):
#   if x % 10 == 0: 
#     print(x)

# list = [2, 4, 6 , 8, 11, 22, 34, 56, 78]
# list2 = [x+3 for x in list]
# print(list2)

# create empty list: lsit = []

# dict = {"name": "Bob",
#         "age": 50,
#        } 

# dict = {}
# dict['name'] = "Bob"
# dict['age'] = 50

# for key, value in dict.items():
#   print(f"key: {key}, value: {value}")


    



''' total_profit_loss = 0
  greatest_increase = {'month': '', 'amount': 0}
  greatest_decrease = {'month': '', 'amount': 0}
  total_months = 0
  average_change = 0

  for line in f.readlines():
    date = line.split(',')[0]
    pl = int(line.split(',')[1])
    total_profit_loss = total_profit_loss + pl
    if pl > 0:
      if greatest_increase['amount'] < pl:
        greatest_increase = {'month': date, 'amount': pl}
    else:
      if greatest_decrease['amount'] > pl:
        greatest_decrease = {'month': date, 'amount': pl}
    total_months += 1

  print(f"{total_months}, {total_profit_loss}")


# putting data summary as a .txt file output
f = open('bank_data.txt','w')
f.write(OUTPUT)
f.close()


if __name__ == '__main__':
  main()
'''
