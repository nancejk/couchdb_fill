from random import randint, uniform

def get_random_string(size):
	return "".join([chr(randint(97,113)) for placeholder in range(size)])

def get_random_int_list(min,max,length):
	return [randint(min,max) for placeholder in range(length)]

def get_random_float_list(min,max,length):
	return [uniform(min,max) for placeholder in range(length)]
	
def date_generator(begin,end,increment):
	pass
