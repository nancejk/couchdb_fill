from couchdbkit import * 
from random import randint

class ECADocument(Document):
	random_number = IntegerProperty(default=10)

class DemoDocument(Document):
	random_string = StringProperty(default="".join([chr(randint(97,113)) for placeholder in range(10)]))
	random_integer = IntegerProperty(randint(0,100) for placeholder in range(0,1000))
