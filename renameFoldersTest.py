# -*- coding: utf-8 -*-

import unittest
import renameFolders
import replaceCharacters

class renamerTestCase(unittest.TestCase):	

	def testStrToArray(self):
		before = "2017.06.17 - Restaurant Name (Account Inhaber)"
		after = ["2017.06.17", "Restaurant Name", "Account Inhaber"]
		self.assertEqual(after, renameFolders.split(before))
		
		before = "2017-06-17 - Ponyhof (Zwisele)"
		after = ["2017-06-17", "Ponyhof", "Zwisele"]
		self.assertEqual(after, renameFolders.split(before))
		
		before = "2017 - 06 - 17 - Vút Thai 'Hai' (Mauricè Paul Bonk)"
		after = ["2017 - 06 - 17", "Vút Thai 'Hai'", "Mauricè Paul Bonk"]
		self.assertEqual(after, renameFolders.split(before))
		
		before = "2017 - 06 - 17 - Vút Thai \"Hai\" (Mauricè Paul Bonk)"
		after = ["2017 - 06 - 17", "Vút Thai \"Hai\"", "Mauricè Paul Bonk"]
		self.assertEqual(after, renameFolders.split(before))
		
		before = "2017 - 06 - 17 - Vút (Thai) ('Hai') (Mauricè Paul Bonk)"
		after = ["2017 - 06 - 17", "Vút (Thai) ('Hai')", "Mauricè Paul Bonk"]
		self.assertEqual(after, renameFolders.split(before))
			
		
	def testFormatDate(self):
		before = "2017.06.17"
		after = "2017-06-17"	
		self.assertEqual(after, renameFolders.formatDate(before))
		
		
	def testSpecialCharacterReplacement(self):
		before = u"ä ö ü á é ú ó í à è ù ò ì â ê û ô î ß"
		after = "ae oe ue a e u o i a e u o i a e u o i ss"
		self.assertEqual(after, replaceCharacters.replaceChars(before))	


# 		before = "ä ö ü á é ú ó í à è ù ò ì â ê û ô î ß"
# 		after = "ae oe ue a e u o i a e u o i a e u o i ss"
		
if __name__ == "__main__":
	unittest.main()		