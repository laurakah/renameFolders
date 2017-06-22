# -*- coding: utf-8 -*-

import unittest
import os
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
		
		before = "2017 - 06 - 17 - Vút (Thai) ('Hai') (Mauricè Paul Bonk)"						#TODO: remove brackets!
		after = ["2017 - 06 - 17", "Vút (Thai) ('Hai')", "Mauricè Paul Bonk"]
		self.assertEqual(after, renameFolders.splitFolderName(before))	
		
		before = "2017 - 06 - 17 - Taj Mahal (DD) (Bork)"
		after = ["2017 - 06 - 17", "Taj Mahal (DD)", "Bork"]
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
		
	def testFormatFolderName(self):
		before = u"2017 - 06 - 17 - Vút Thai \"Hai\"使 (Mauricè Paul Bonk)"
		after = "2017-06-17__Vut_Thai_\"Hai\"?__Maurice_Paul_Bonk"
		self.assertEqual(after, renameFolders.formatFolderName(before))	
		
	def testRenameAccountFolder(self):
		before = u"2017 - 06 - 17 - Vút Thai \"Hai\"使 (Mauricè Paul Bonk)"
		after = "2017-06-17__Vut_Thai_\"Hai\"?__Maurice_Paul_Bonk"
		before_dir = os.path.join(os.getcwd(), before)
		after_dir = os.path.join(os.getcwd(), after)
 		os.mkdir(before_dir)		
 		try:
			self.assertEqual(after_dir, renameFolders.renameAccountFolder(before_dir))
			self.assertTrue(os.path.isdir(after_dir))
		except:
			os.rmdir(before_dir)
			raise
		os.rmdir(after_dir)	

	def testRenameSubfolderOrFile(self):
		before = u"Kündígung Unterlagen \"Hai\"使"
		after = "Kuendigung_Unterlagen_\"Hai\"?"
		before_name = os.path.join(os.getcwd(), before)
		after_name = os.path.join(os.getcwd(), after)
		os.mkdir(before_name)
		try:
			self.assertEqual(after_name, renameFolders.renameSubfolderOrFile(before_name))
			self.assertTrue(os.path.exists(after_name))
		except:
			os.rmdir(before_name)
			raise
		os.rmdir(after_name)		

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
		
		
		
		
#TODO:	--->	needs to be replaced!		
# 	def testRenameFolderThrowNotUnicodeException(self):
# 		with self.assertRaises(Exception) as e:
# 			renameFolder("bad_ascii_folder_name")	
# 		self.assertTrue("Argument is not unicode!" in e.exception)


		
if __name__ == "__main__":
	unittest.main()		