from couchdbkit import Document, IntegerProperty

class ECADocument(Document):
	random_number = IntegerProperty(default=10)
