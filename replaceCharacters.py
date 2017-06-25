# -*- coding: utf-8 -*-

TRANSLATE = {
	u"ß": "ss",
	u"ä": "ae",
	u"ö": "oe",
	u"ü": "ue",
	u"á": "a",
	u"é": "e",
	u"í": "i",
	u"ó": "o",
	u"ú": "u",
	u"à": "a",
	u"è": "e",
	u"ì": "i",
	u"ò": "o",
	u"ù": "u",
	u"â": "a",
	u"ê": "e",
	u"î": "i",
	u"ô": "o",
	u"û": "u",
	u" ": "_",
	u"(": "",
	u")": ""
}

def replaceCharsByTranslators(chars_in):
	chars_out = ""
	chars_in = unicode(chars_in, "utf-8")
	#print "\"%s\" is %s" % (chars_in, type(chars_in))
	for c in chars_in:
		if c in TRANSLATE.keys():
			t = TRANSLATE[c]
			#print "YYYYYYYYYYYYYYYYYYYY \"%s\" -> \"%s\" len(%d) (instance of: %s)" % (c, t, len(c), c.__class__)
			chars_out += t	
		else:
			chars_out += c
			#print "ZZZZZZZZZZZZZZZZZZZ \"%s\" len(%d) (instance of: %s)" % (c, len(c), c.__class__)
	return chars_out

def isUnicode(c):
	if isinstance(c, unicode):
		try:
			c.encode('ascii')
		except UnicodeEncodeError:
			return True
	else:
		try:
			c.decode('ascii')
		except UnicodeDecodeError:
			return True
	return False
		
def replaceCharsDefault(unicode_chars_in):
	ascii_chars_out = ""
	if not isinstance(unicode_chars_in, unicode):
		unicode_chars_in = unicode(unicode_chars_in, "utf-8")
	#print "\"%s\" is %s" % (unicode_chars_in, type(unicode_chars_in))	
	for c in unicode_chars_in:
		if isUnicode(c):
			ascii_chars_out += "?"	
		else:
			if isinstance(c, unicode):
				ascii_chars_out += c.encode("ascii")
			else:
				ascii_chars_out += c.decode("ascii")	
	return ascii_chars_out
	
def replaceChars(chars_in):
	chars_out = replaceCharsByTranslators(chars_in)
	chars_out = replaceCharsDefault(chars_out)
	return chars_out