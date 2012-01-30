from example_c import hello as hello_c
from example_cc import hello as hello_cc
from example_java import hello as hello_java

def example_hello( lang ) :
	if lang == 'c' :
		return hello_c()
	if lang == 'cc' :
		return hello_cc()
	if lang == 'java' :
		return hello_java()
	return '' 

def html_str_replace( html ):
	return replace_all( html, { "\n": "\\n" } )

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text
