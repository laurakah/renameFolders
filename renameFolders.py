# -*- coding: utf-8 -*-

import re
import string
import os
import replaceCharacters
	
def splitFolderName(str_in):
	res = re.match(r"(?P<date>.*) - (?P<accountName>.*) \((?P<accountOwner>.*)\)", str_in)
	if not res:
		array_out = []
	else:
		array_out = [res.group("date"), res.group("accountName"), res.group("accountOwner")]
	return array_out

def formatDate(date_in):
	dateSep = "-"
	res = re.match(r"(?P<year>\d+)[\. \-_]+(?P<month>\d+)[\. \-_]+(?P<day>\d+)", date_in)
	if not res:
		date_out = ""
	else:
		date_out = "%s%s%s%s%s" % (res.group("year"), dateSep, res.group("month"), dateSep, res.group("day"))	
	return date_out		
	
def addSeperators(array_out):
	nameSep = "__"
	newName = "%s%s%s%s%s" % (array_out[0], nameSep, array_out[1], nameSep, array_out[2])
	return newName
	
def formatFolderName(oldFolderName):
# 	if not replaceCharacters.isUnicode(oldFolderName):			---> TODO:	needs to be replaced!
# 		raise Exception("Argument is not unicode!")
	folderNameParts = splitFolderName(oldFolderName)
	folderNameParts[0] = formatDate(folderNameParts[0])
	newFolderName = addSeperators(folderNameParts)
# 	newFolderName = replaceCharacters.replaceChars(newFolderName)
	return newFolderName
	
def renameAccountFolder(before_dir):
	after_dir = ""
	oldFolderName = os.path.basename(before_dir)
 	newFolderName = formatFolderName(oldFolderName)
#  	newFolderName = replaceCharacters.replaceChars(newFolderName)
	after_dir = os.path.join(os.path.split(before_dir)[0], newFolderName)
	os.rename(before_dir, after_dir)
	return after_dir	
	
def renameSubfolderOrFile(before_name):
	after_name = ""
	oldName = os.path.basename(before_name)
 	newName = replaceCharacters.replaceChars(oldName)
 	after_name = os.path.join(os.path.split(before_name)[0], newName)
 	os.rename(before_name, after_name)
	return after_name
	
def renameAll(parentDir):
	for d in os.listdir(parentDir):
		absolutePath = os.path.join(parentDir, d)
 		newPathFormat = renameAccountFolder(absolutePath)
 		formatedFolderName = os.path.basename(newPathFormat)
 		formatedFolderName = unicode(formatedFolderName, "utf-8")
 		print "1. XXXXXXXXX %s XXXXXXX" % formatedFolderName
		newFolderName = replaceCharacters.replaceCharsByTranslators(formatedFolderName)
		print "2. XXXXXXXXX %s XXXXXXX" % newFolderName
		print "Type of formatedFolderName: %s" % type(formatedFolderName)
		print "Type of newFolderName: %s" % type(newFolderName)
		if formatedFolderName == newFolderName:
			print "NO CHANGE!"
		newFolderName = replaceCharacters.replaceCharsDefault(newFolderName)
		print "3. XXXXXXXXX %s XXXXXXX" % newFolderName
		after_dir = os.path.join(os.path.split(absolutePath)[0], newFolderName)
		os.rename(newPathFormat, after_dir)
	return	