#!/usr/bin/python3

import re

dateRegex = re.compile(r"(0\d|[1-2]\d|3[0-1])/(0\d|1[0-2])/([12]\d{3})")

def isLeapYear(year):
	year = float(year)
	if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
		return True
	return False

def isDateValid(dateText):
	matchedDate = dateRegex.search(dateText)
	if matchedDate == None:
		return False
	
	day, month, year = matchedDate.groups()
	day = float(day)
	month = float(month)

	maxDay = None
	if month == 2:
		if isLeapYear(year):
			maxDay = 29
		else:
			maxDay = 28
	elif month in (4, 6, 9, 11):
		maxDay = 30
	elif month in (1, 3, 5, 7, 8, 10, 12):
		maxDay = 31
	else:
		return False
	
	if day <= maxDay:
		return True
	return False


if __name__ == "__main__":
	print("29/02/2012", isDateValid("29/02/2012"))
	print("13/05/1995", isDateValid("13/05/1995"))
	print("31/06/2000", isDateValid("31/06/2000"))
		