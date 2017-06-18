# -*- coding: utf-8 -*-

import unittest
import renameFolders
import replaceCharacters

class renamerTestCase(unittest.TestCase):	

	def testSplitFolderName(self):
		before = "2017.06.17 - Restaurant Name (Account Inhaber)"
		after = ["2017.06.17", "Restaurant Name", "Account Inhaber"]
		self.assertEqual(after, renameFolders.splitFolderName(before))
		
		before = "2017-06-17 - Ponyhof (Zwisele)"
		after = ["2017-06-17", "Ponyhof", "Zwisele"]
		self.assertEqual(after, renameFolders.splitFolderName(before))
		
		before = "2017 - 06 - 17 - Vút Thai 'Hai' (Mauricè Paul Bonk)"
		after = ["2017 - 06 - 17", "Vút Thai 'Hai'", "Mauricè Paul Bonk"]
		self.assertEqual(after, renameFolders.splitFolderName(before))
		
		before = "2017 - 06 - 17 - Vút Thai \"Hai\" (Mauricè Paul Bonk)"
		after = ["2017 - 06 - 17", "Vút Thai \"Hai\"", "Mauricè Paul Bonk"]
		self.assertEqual(after, renameFolders.splitFolderName(before))
		
		before = "2017 - 06 - 17 - Vút (Thai) ('Hai') (Mauricè Paul Bonk)"
		after = ["2017 - 06 - 17", "Vút (Thai) ('Hai')", "Mauricè Paul Bonk"]
		self.assertEqual(after, renameFolders.splitFolderName(before))	
			
	def testFormatDate(self):
		before = "2017 - 06 - 17"
		after = "2017-06-17"
		self.assertEqual(after, renameFolders.formatDate(before))
		
		before = "2017.06.17"
		after = "2017-06-17"	
		self.assertEqual(after, renameFolders.formatDate(before))
		
	def testAddSeperators(self):
		before = ["2017-06-17", "Ponyhof", "Zwisele"]
		after = "2017-06-17__Ponyhof__Zwisele"
		self.assertEqual(after, renameFolders.addSeperators(before))
		
# 	def testRenameFolder(self):
# 		before = "2017 - 06 - 17 - Vút Thai \"Hai\"使 (Mauricè Paul Bonk)"
# 		after = "2017-06-17__Vut_Thai_\"Hai\"?__Maurice_Paul_Bonk"
# 		self.assertEqual(after, renameFolders.renameFolder(before))
		
	def testReplaceCharsByTranslators(self):
		before = u"ä ö ü á é ú ó í à è ù ò ì â ê û ô î ß"
		after = "ae_oe_ue_a_e_u_o_i_a_e_u_o_i_a_e_u_o_i_ss"
		self.assertEqual(after, replaceCharacters.replaceCharsByTranslators(before))	
		
	def testReplaceCharsDefault(self):
		before = u"տպوى的使пр刷及ობסתνόhallo"
		after = "????????????????hallo"
		self.assertEqual(after, replaceCharacters.replaceCharsDefault(before))
		
	def testReplaceChars(self):
		before = u"aäáàâ刷及"
		after = "aaeaaa??"
		self.assertEqual(after, replaceCharacters.replaceChars(before))		


		
if __name__ == "__main__":
	unittest.main()		