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
	u" ": "_"
}


def replaceCharsByTranslators(chars_in):
	chars_out = ""
	for c in chars_in:
		if c in TRANSLATE.keys():
			chars_out += TRANSLATE[c]	
		else:
			chars_out += c
	return chars_out

def replaceCharsDefault(unicode_chars_in):
	ascii_chars_out = ""
	for c in unicode_chars_in:
		try:
			ascii_chars_out += c.encode("ascii")
		except UnicodeEncodeError:
			ascii_chars_out += "?"	
	return ascii_chars_out