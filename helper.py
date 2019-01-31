import math

def cint(s):
	"""Convert to integer"""
	try: num = int(float(s))
	except: num = 0
	return num

def rounded(num, precision=0):
	"""round method for round halfs to nearest even algorithm aka banker's rounding - compatible with python3"""
	precision = cint(precision)
	multiplier = 10 ** precision

	# avoid rounding errors
	num = round(num * multiplier if precision else num, 8)

	floor = math.floor(num)
	decimal_part = num - floor

	if not precision and decimal_part == 0.5:
		num = floor if (floor % 2 == 0) else floor + 1
	else:
		num = round(num)

	return (num / multiplier) if precision else num