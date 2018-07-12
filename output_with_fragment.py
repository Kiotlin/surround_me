'''
Author Kiokh(ilvanime121000@gmail.com)
Module for output text surrounded by a border

Python:
  - 3.7

Usage:
  - $python3 output_with_fragment.py "..." "..."

Here is a output example:

1 sentence
?------------------------------------------?
|                                          |
|   Update available here 5.6.0 -> 6.1.0   |
|                                          |
?------------------------------------------?

several sentences
?------------------------------------------?
|                                          |
|   Update available here 5.6.0 -> 6.1.0   |
|   Run npm i npm to update                |
|   apt-get upgrade                        |
|                                          |
?------------------------------------------?

'''

import sys

def main():
	if len(sys.argv) < 1:
		print("What's wrong with you honey?")
		sys.exit("End.")
	else:
		output_words_with_fragment(sys.argv)

#output regular.
def output_words_with_fragment(sentences):

			length = len(sentences)
			for sen in sentences[1:]:
				if len(sen) > length:
					length = len(sen)
				else :
					continue

			horizontal_fragment = "?---" + "-" * length + "---?"
			vertical_border = "|   " + " " * length + "   |"

			print(horizontal_fragment)
			print(vertical_border)
			for sen in sentences[1:]:
				print("|   " + sen + " " * (length - len(sen)) + "   |")
			print(vertical_border)
			print(horizontal_fragment)

if __name__ == "__main__":
	main()
