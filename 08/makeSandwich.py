import pyinputplus as pyip

def makeSandwich():
	prices = {
		"wheat": 1.25,
		"white": 1.00,
		"sourdough": 1.75,
		"chicken": 2.25,
		"turkey": 3.50,
		"ham": 1.50,
		"tofu": 1.25,
		"cheddar": 1.50,
		"swiss": 2.0,
		"mozzarella": 2.75,
		"mayo": 0.15,
		"mustard": 0.15,
		"lettuce": 0.20,
		"tomato": 0.18
	}

	choices = []

	print("Please choose your prefered type of bread for the sandwich.")
	choices.append(pyip.inputMenu(["wheat", "white", "sourdough"]))
	print("Choose your prefered protein.")
	choices.append(pyip.inputMenu(["chicken", "turkey", "ham", "tofu"]))

	print("Do you want some cheese?")
	wantsCheese = pyip.inputYesNo(yesVal="Y") == "Y"
	if wantsCheese:
		print("What kind of cheese?")
		choices.append(pyip.inputMenu(["cheddar", "swiss", "mozzarella"]))

	print("Would you like to add mayo?")
	if pyip.inputYesNo(yesVal="Y") == "Y":
		choices.append("mayo")
	print("Would you like mustard?")
	if pyip.inputYesNo(yesVal="Y") == "Y":
		choices.append("mustard")
	print("Would you like lettuce?")
	if pyip.inputYesNo(yesVal="Y") == "Y":
		choices.append("lettuce")
	print("Would you like tomato?")
	if pyip.inputYesNo(yesVal="Y") == "Y":
		choices.append("tomato")
	print("How many sandwiches would you like?")
	quantity = pyip.inputInt(min=1)

	price = 0
	for choice in choices:
		price += prices[choice]
	
	total = price * quantity

	desc = "%s %s sandwich in %s bread" % (quantity, choices[1], choices[0])
	i = 2
	if wantsCheese:
		desc += " with %s cheese" % (choices[i])
		i += 1 
	if len(choices) > i:
		desc += " and " + ", ".join(choices[i:])
	print(desc, "Amounth: $%s x (%s)" % (price, quantity), sep="\n")
	print("Amount Total: $%s" % (total))

if __name__ == "__main__":
	makeSandwich()
