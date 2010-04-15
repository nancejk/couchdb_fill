import sys,getopt
from couch_writer import CouchClient

# A useful class for option parsing
class Usage(Exception):
	def __init__(self,msg):
		self.msg = msg

class Config(object):
	def __init__(self):
		self.state = {}
	def set_params(self,**kwargs):
		for key in kwargs:
			self.state[key] = kwargs[key]
	def validate(self):
		# No server specified is not recoverable.
		if 'server' not in self.state:
			raise Usage("You must specify a server with -s.")
		# We also need to know which type of document we are using.
		if 'template' not in self.state:
			raise Usage("You must specify a template (ECA) with -t.")
		# The default increment is 1000
		if 'increment' not in self.state:
			self.state['increment'] = '1000'
		# The default total is 100000 documents
		if 'total' not in self.state:
			self.state['total'] = '100000'
		# The default database name is couchfill_test
		if 'db' not in self.state:
			self.state['db'] = 'couchfill_test'
		if 'port' not in self.state:
			self.state['port'] = '5984'
	def get_param(self,par):
		return self.state[par]
	def __str__(self):
		return str(self.state)

def main(argv=None):
	# If argv is unmodified just use sys.argv
	if argv is None:
		argv = sys.argv
	try:
		# Instantiate a new config object and try to fill it with getopt.
		local_config = Config()
		try:
			opts,args = getopt.getopt(sys.argv[1:], "s:n:N:d:t:")
		except getopt.error, msg:
			raise Usage(msg)
		for opt, arg in opts:
			if opt == "-s":
				local_config.set_params(server=arg)
			if opt == "-t":
				local_config.set_params(template=arg)
			if opt == "-n":
				local_config.set_params(increment=arg)
			if opt == "-N":
				local_config.set_params(total=arg)
			if opt == "-d":
				local_config.set_params(db=arg)
			if opt == "-p":
				local_config.set_params(port=arg)

		# Validate the config and move on.
		local_config.validate()
		
		# Instantiate the client and run it.
		client = CouchClient(local_config)
		client.go()
	
	except Usage, err:
		print(err.msg)
		return 2
		
	except Exception, msg:
		print(msg)
		return 2
		
if __name__ == "__main__":
	sys.exit(main())
