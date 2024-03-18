#!/usr/bin/python3

import re

pwRegexes = [
	re.compile(r"[A-Z]"),
	re.compile(r"[a-z]"),
	re.compile(r"\d"),
	re.compile(r"[^A-Za-z0-9]")
]

def detectPasswordStrength(password):
	strength = 0
	if len(password) >= 8:
		strength = len(password) / 8
	
	for regex in pwRegexes:
		if regex.search(password):
			strength = strength + 1

	return strength
	
if __name__ == "__main__":
	passwords = ["Password", "PASSWORD", "pass123", "12pass34word", "The quick brown fox jumps over the lazy dog", "GetYourOwnWifi", "H@ck3rman", "!Tid@CR05?13"]
	
	for password in passwords:
		print(password, detectPasswordStrength(password), sep=": ")