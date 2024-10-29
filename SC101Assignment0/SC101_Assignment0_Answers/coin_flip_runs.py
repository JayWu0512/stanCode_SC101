"""
File: coin_flip_runs.py
Name:
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


Result = []


def main():
	"""
	Step 1: throw a coin, and check the duplicated labels in the list
	Step 2: plus one run, if the label is changed.
	Step 3:	print the process
	"""
	num_run = 0
	trigger = 1
	# bool (True of False)
	print("Let's flip a coin!")
	limit = int(input('Number of runs: ') + str())
	while num_run < limit:
		throw_the_coin()

		if len(Result) < 2:
			continue
		# check the duplicated labels in the list

		previous_chart = Result[-2]
		new_chart = Result[-1]
		if trigger == 1 and previous_chart == new_chart:
			num_run += 1
			trigger = 0
		else:
			trigger = 1
		# plus one run if the label is changed

	print_the_process()
	return None


def throw_the_coin():
	t = r.randint(0, 1)
	if t == 1:
		Result.append('H')
	else:
		Result.append('T')
	return None


def print_the_process():
	string = ""
	for i in range(len(Result)):
		string += Result[i]
	print(string)
	return None


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
