from couchdbkit import Server
from doc_wrappers import *

class CouchClient(object):
	def __init__(self,config):
		try:
			# First figure out which document template we are using here.
			if config.get_param('template') not in ['eca','random']:
				raise Exception('Template parameter not recognized.  Try: eca random')
			
			self.server = Server(uri='http://' + \
						config.get_param('server') + \
						':' + config.get_param('port'))
			self.db = self.server.get_or_create_db(config.get_param('db'))

			self. docu_class = None
			if config.get_param('template') == 'eca':
				self.docu_class = ECADocument	
			elif config.get_param('template') == 'random':
				self.docu_class = DemoDocument
			self.docu_class.set_db(self.db)
		
			# OK, if that all worked, consider the object initialized wrt couch,
			# and store the other params we need to iterate.
			self.maxcounts = int(config.get_param('total'))
			self.increment = int(config.get_param('increment'))

		except Exception, msg:
			raise Exception(msg)
	def go(self):
		for run_set in range(self.increment, self.maxcounts + self.increment, self.increment):
			docs = [self.docu_class()._doc for placeholder in range(0,self.increment)]
			self.db.bulk_save(docs)
