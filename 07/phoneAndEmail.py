#!/usr/bin/python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
	(\d{2,3}|\(\d{2,3}\))?
	(\s|-|\.)?
	(\d{3})
	(\s|-|\.)
	(\d{4})
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	
	)''', re.VERBOSE)

emailRegex = re.compile(r"""(
	[a-zA-Z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)""", re.VERBOSE)

def scanClipboardForContacts():
	# Find matches in clipboard text.
	text = str(pyperclip.paste())

	matches = []
	for groups in phoneRegex.findall(text):
		phoneNum = '-'.join([groups[1], groups[3], groups[5]])
		if groups[8] != '':
			phoneNum += ' x' + groups[8]
		matches.append(phoneNum)
	for groups in emailRegex.findall(text):
		matches.append(groups[0])
	
	if len(matches) > 0:
		newText = '\n'.join(matches)
		pyperclip.copy(newText)
		print('Copied to clipboard:', newText, sep="\n")
	else:
		print('No phone numbers or email addresses found.')

if __name__ == "__main__":
	scanClipboardForContacts()

