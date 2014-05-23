class RomanNumeralConverter(object):
	@classmethod
	def to_roman(cls, number):
		result = ""
		if not isinstance( number, int):
			raise NotIntegerError
		elif number < 1:
			raise OutOfRangeError
		elif number > 3999:
			raise OutOfRangeError
    # result = "" # <-- this line MUST NEVER be included
		while number >= 1000:
			number -= 1000
			result += "M"
		if number >= 900:
			number -= 900
			result += "CM"
		while number >= 500:
			number -= 500
			result += "D"
		if number >= 400:
			number -= 400
			result += "CD"
		while number >= 100:
			number -= 100
			result += "C"
		if number >= 90:
			number -= 90
			result += "XC"
		while number >= 50:
			number -= 50
			result += "L"
		if number >= 40:
			number -= 40
			result += "XL"
		while number >= 10:
			number -= 10
			result += "X"
		if number >= 9:
			number -= 9
			result += "IX"
		while number >= 5:
			number -= 5
			result += "V"
		if number >= 4:
			result += "IV"
		else:
			result += "I" * number

		return result

	@classmethod
	def from_roman(cls, string):
		i = len(string) - 1
		number = 0
		while i >= 0:
			character = string[i]
			if character == 'I':
				number += 1
			elif string[(i-1):2] == 'IV':
				number += 4
				i -= 1
			elif character == 'V':
				number += 5
			i -= 1
		return number

class OutOfRangeError(Exception):
	pass

class NotIntegerError(Exception):
	pass