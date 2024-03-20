import random, time

def startMultiplicationQuiz(numberOfQestions=10, timeout=10, trylimit=3):
	correctAnswers = 0

	for questionNumber in range(numberOfQestions):
		num1 = random.randint(0, 9)
		num2 = random.randint(0, 9)

		prompt = "#%s.) %s x %s = " %(questionNumber+1, num1, num2)

		tries = 0
		startTime = time.time()
		while True:
			try:
				answer = int(input(prompt))
			except ValueError:
				tries += 1
				endTime = time.time()
				if (endTime-startTime >= timeout):
					print("Out of time!")
					break
				if tries >= trylimit:
					print("Out of tries")
					break
			else:
				endTime = time.time()
				if (endTime-startTime >= timeout):
					print("Out of time!")
					break
				tries += 1
				if answer == (num1*num2):
					correctAnswers += 1
					print("Correct!")
					break
				else:
					print("Incorrect!")
				if tries >= trylimit:
					print("Out of tries!")
		time.sleep(1)
	print("Score: %s / %s (%s percent)" %(correctAnswers, numberOfQestions, (correctAnswers / numberOfQestions) * 100))

if __name__ == "__main__":
	startMultiplicationQuiz()