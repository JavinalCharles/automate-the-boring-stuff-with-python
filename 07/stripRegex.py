#!/usr/bin/python3

import re

def strip(string, pattern=r"\s*"):
	regex = re.compile(r"^" + pattern + r"(.*?)" + pattern + r"$")
	return regex.sub(r"\1", string)

if __name__ == "__main__":
	foo = " \tFoo   "
	bar = "\tbar\n\t"
	foo = strip(foo)
	bar = strip(bar)

	print(foo, bar)
	
