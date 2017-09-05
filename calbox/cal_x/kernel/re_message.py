# -*- coding: utf-8 -*-
from conf import *
import json
import re
def json_message( message, mess_type ):
	#return json.dumps({"message": re.compile( r'.+[\\\/]').sub( '', unicode(message,'utf-8') ), "type": mess_type}, sort_keys=True, indent=4)
	return json.dumps({"message": re.compile( r'.+[\\\/]').sub( '', message ), "type": mess_type}, sort_keys=True, indent=4, ensure_ascii = False)

