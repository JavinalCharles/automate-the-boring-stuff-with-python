import sys

def collatz(number):
	return number // 2 if (number % 2) == 0 else number * 3 + 1

if __name__ == "__main__":
	inp = ""
	while (inp == ""):
		print("Enter a number: ", end="");
		try :
			inp = int(input())
		except ValueError:
			inp = ""
		except KeyboardInterrupt:
			sys.exit()

	n = int(inp)
	print("Starting collatz sequence with number:",  n)
	while (n > 1):
		n = collatz(n)
		print(n)
	
