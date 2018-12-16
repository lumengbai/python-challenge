import csv

file_path = "election_data.csv"

#The total number of votes cast 
total_votes = 0

#List of candidates 
list_candidates = []
#The percentage of votes each candidate won 

#The total number of votes each candidate won
dict_candidates = {}
#The winner of the election based on popular vote 


with open(file_path) as file_object: 
	poll_data = csv.reader(file_object)

	next(poll_data)

	for row in poll_data: 
		total_votes += 1

		candidate = row[2]

		if candidate in dict_candidates.keys():
		  dict_candidates[candidate] += 1
		else: 
		  dict_candidates[candidate] = 1 
		#check which candidate is in the row
		  #add 1 to their vote

print(dict_candidates)


		#check what name the row contains













# def total_votes_list(list): 
#   length = len(list)
#   total_votes_sum = 0

#   for i in list: 
#     total_votes_sum += i 
 
#   return total_votes_sum







