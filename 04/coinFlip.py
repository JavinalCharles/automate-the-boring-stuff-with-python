import random


if __name__ == "__main__":
	numberOfStreaks = 0

	for experimentNumber in range(10000):
		flips = []
		for n in range(100):
			flips.append(random.randint(0, 1))

		maxStreak = 0
		for i in range(1, len(flips)):
			if flips[i] == flips[i-1]:
				maxStreak += 1
			else:
				maxStreak = 0
			if maxStreak >= 6:
				numberOfStreaks += 1
				break


	print("Found %s number of streaks in 10,000 experiments." % numberOfStreaks)
	print('Chance of streak: %s%%' % (numberOfStreaks / 100))