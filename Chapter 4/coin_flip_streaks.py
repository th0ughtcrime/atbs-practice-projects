# ATBS Ch. 4
# Coin Flip Streaks
#
# How often does a streak of 6 appear in 100 coin-tosses (either heads or tails)?
# This program does 100 coin-tosses and checks if there's a streak of 6, for a
# total of 10000 times. In the end it prints the percentage of experiments in
# which a streak was found.

from random import randint


streak_size = 6        # Number of consecutive same results that are considered a streak
experiment_size = 100  # Number of coin tosses per experiment
iterations = 10000     # Number of iterations


number_of_streaks = 0

for experiment_number in range(iterations):
	experiment = [randint(0, 1) for i in range(experiment_size)]

	for i in range(experiment_size):
		start_index = i
		end_index = i + streak_size - 1

		streak_sum = sum(experiment[start_index:end_index])
		if streak_sum == 0 or streak_sum == 6:
			number_of_streaks += 1
			break

percentage = number_of_streaks / iterations

print(f'Chance of streak: {percentage:2.2%}')
