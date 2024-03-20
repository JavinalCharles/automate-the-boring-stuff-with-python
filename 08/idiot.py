import pyinputplus as pyip

if __name__ == "__main__":
	prompt = "Want to know how to keep an idiot busy for hours?\n"
	while True:
		response = pyip.inputYesNo(prompt)
		if response == "no":
			break
	
	print("Thank you. Have a nice day.")