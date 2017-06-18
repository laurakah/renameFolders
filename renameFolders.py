# -*- coding: utf-8 -*-

import re
import string
	
def split(str_in):
	res = re.match(r"(?P<date>.*) - (?P<accountName>.*) \((?P<accountOwner>.*)\)", str_in)
	if not res:
		array_out = []
	else:
		array_out = [res.group("date"), res.group("accountName"), res.group("accountOwner")]
	return array_out

def formatDate(date_in):
	dateSep = "-"
	res = re.match(r"(?P<year>\d+)[\. -_](?P<month>\d+)[\. -_](?P<day>\d+)", date_in)
	if not res:
		date_out = ""
	else:
		date_out = "%s%s%s%s%s" % (res.group("year"), dateSep, res.group("month"), dateSep,  res.group("day"))	
	return date_out		
	
