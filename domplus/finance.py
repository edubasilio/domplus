# -*- coding: utf-8 -*-


def is_creditcard(card_number):
	"""
	Accept an string parameter card_number and
	check if is a Credcard Number valid.
	Return True or False
	"""
	# From http://en.wikipedia.org/wiki/Luhn_algorithm (2015/04/12)

	# if card_number is string
	if not isinstance(card_number, str):
		raise TypeError("card_number must be string")

	# if does not contain numerical characters
	for i in card_number:
		if not i.isdigit():
			return False

	def digits_of(n):
		return [int(d) for d in str(n)]

	digits = digits_of(card_number)
	odd_digits = digits[-1::-2]
	even_digits = digits[-2::-2]
	checksum = 0
	checksum += sum(odd_digits)
	for d in even_digits:
		checksum += sum(digits_of(d*2))

	return True if checksum % 10 == 0 else False
