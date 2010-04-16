from couchdbkit import * 
from utility import *

class PDSTDocument(Document):
	valid_begin = ListProperty(default=[0.0, 0.0])
	valid_end = ListProperty(default=[0.0,0.0])
	pdst_status = ListProperty(default=get_random_int_list(0,2**32,10000)) 
	pdst_qhs = ListProperty(default=get_random_float_list(100,1000,10000)) 
	pdst_qhl = ListProperty(default=get_random_float_list(100,1000,10000))
	pdst_qlx = ListProperty(default=get_random_float_list(100,1000,10000)) 
	pdst_tac = ListProperty(default=get_random_float_list(1500,2500,10000))
	pdst_qhswidth = ListProperty(default=get_random_float_list(0,5,10000)) 
	pdst_qhlwidth = ListProperty(default=get_random_float_list(0,5,10000)) 
	pdst_qlxwidth = ListProperty(default=get_random_float_list(0,5,10000)) 
	pdst_tacwidth = ListProperty(default=get_random_float_list(0,5,10000)) 
	pdst_dqid = ListProperty(get_random_int_list(0,16**6,10000))

class TSLPDocument(Document):
	tslp_status = ListProperty()
	tslp_bad = ListProperty()
	tslp_points = ListProperty()
	tslp_fitpars = ListProperty()
	tslp_dqid = ListProperty()
	tslp_ntimes = ListProperty()
	tslp_times = ListProperty()

class DemoDocument(Document):
	random_string = StringProperty(default=get_random_string(10))
	random_integer = IntegerProperty(randint(0,100)) 
