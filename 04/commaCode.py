
def stringifyList(l):
	if not isinstance(l, list):
		return ""
	if len(l) == 0:
		return "[]"
	
	resStr = "["
	for v in l:
		if (isinstance(v, list)):
			if len(resStr) > 1:
				resStr += ", "
			resStr += stringifyList(v)
		elif len(resStr) > 1:
			if isinstance(v, str):
				resStr += ", \"" + v + "\""
			else:
				resStr += ", " + str(v)
		else:
			if isinstance(v, str):
				resStr += "\"" + v + "\""
			else:
				resStr += str(v)
	resStr += "]"
	return resStr

if __name__ == "__main__":
	spam = ["apples", "bananas", "tofu", "cats"]
	eggs = ["Paris", "Germany", [], ["China", "Japan", "Korea"], "America", "Canada"]
	fizz = [5, 7, 5.5, ["c", "h", "a", "r", "l", "e", "x"], 3.1415151]


	print("spam:", stringifyList(spam))

	print("eggs:", stringifyList(eggs))

	print("fizz:", stringifyList(fizz))
	
