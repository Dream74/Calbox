# -*- coding: utf-8 -*-
import json
import re
def json_message( message, mess_type ):
  #return json.dumps({"message": re.compile( r'.+[\\\/]').sub( '', unicode(message,'utf-8') ), "type": mess_type}, sort_keys=True, indent=4)
  return json.dumps({"message": re.compile( r'.+[\\\/]').sub( '', message ), "type": mess_type}, ensure_ascii = False)
  return json.dumps({"message": re.compile( r'.+[\\\/]').sub( '', message ), "type": mess_type}, sort_keys=True, indent=4, ensure_ascii = False)
  #return json.dumps({"message": message, "type": mess_type}, sort_keys=True, indent=4, ensure_ascii = False)

