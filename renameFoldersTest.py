# -*- coding: utf-8 -*-

import unittest
import os
import shutil
import renameFolders
import replaceCharacters

class renamerTestCase(unittest.TestCase):
		
	def testIsUnicode(self):
		self.assertEqual(True, replaceCharacters.isUnicode("使"))
		self.assertEqual(False, replaceCharacters.isUnicode("a"))
		self.assertEqual(False, replaceCharacters.isUnicode("a"))	
	
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
		before = "2017 - 06 - 17 - Vút Thai \"Hai\"使 (Mauricè Paul Bonk)"
		after = "2017-06-17__Vút Thai \"Hai\"使__Mauricè Paul Bonk"
		self.assertEqual(after, renameFolders.formatFolderName(before))
		
	def testFormatFolderNameFix(self):
		before = "2016.08.23 - Restauränt ობסת Bistro (T. Schlößer)"
		after = "2016-08-23__Restauränt ობסת Bistro__T. Schlößer"
		self.assertEqual(after, renameFolders.formatFolderName(before))		
		
	def testRenameAccountFolder(self):
		before = "2017 - 06 - 17 - Vút Thai \"Hai\"使 (Mauricè Paul Bonk)"
		after = "2017-06-17__Vút Thai \"Hai\"使__Mauricè Paul Bonk"
		before_dir = os.path.join(os.getcwd(), before)
		after_dir = os.path.join(os.getcwd(), after)
 		os.mkdir(before_dir)		
 		try:
			self.assertEqual(after_dir, renameFolders.renameAccountFolder(before_dir))
			self.assertTrue(os.path.isdir(after_dir))
		except:
			#os.rmdir(before_dir)
			raise
		#os.rmdir(after_dir)	

	def testRenameSubfolderOrFile(self):
		before = "Kündígung Unterlagen \"Hai\"使"
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
		
	def testRenameAll(self):
		
		testDirName = "renameAllTest"
		testDir = os.path.join(os.getcwd(), testDirName)
		
		#test folders need to end with '/' in order to create them!
		
# 		before = [
# 			u"2016.08.23 - Restauränt ობסת Bistro (T. Schlößer)/",
# 			u"2016.08.23 - Restauränt ობסת Bistro (T. Schlößer)/Kündigung (2017)/",
# 			u"2016.08.23 - Restauränt ობסת Bistro (T. Schlößer)/Kündigung (2017)/Kündigung 2017 ობסת.txt"
# 		]
# 		after = [
# 			u"2016-08-23__Restauraent_????_Bistro__T._Schloesser/",
# 			u"2016-08-23__Restauraent_????_Bistro__T._Schloesser/Kuendigung_2017/",
# 			u"2016-08-23__Restauraent_????_Bistro__T._Schloesser/Kuendigung_2017/Kuendigung_2017_????.txt"
# 		]
		
		before = [
			"2017 - 06 - 17 - Vút Thäi Hai使 (Mauricè Paul Bonk)/",
			"2017 - 06 - 17 - Vút Thäi Hai使 (Mauricè Paul Bonk)/Kündigung (2017)/",
			"2017 - 06 - 17 - Vút Thäi Hai使 (Mauricè Paul Bonk)/Kündigung (2017)/Kündigung.txt"
		]
		
		after = [
			"2017-06-17__Vut_Thaei_Hai?__Maurice_Paul_Bonk)/",
			"2017-06-17__Vut_Thaei_Hai?__Maurice_Paul_Bonk)/Kuendigung_2017/",
			"2017-06-17__Vut_Thaei_Hai?__Maurice_Paul_Bonk)/Kuendigung_2017/Kuendigung.txt"
		]
		
		#prepare absolute path:
		
		before_path = []
		after_path = []
		for e in before:
			before_path.append(os.path.join(testDir, e))
		for e in after:
			after_path.append(os.path.join(testDir, e))
			
		#create test directories and files:
		
		os.mkdir(testDir)
		for p in before_path:
			if p.endswith("/"):
				os.mkdir(p)
			else:
				open(p, "w").close()			
		try:
			renameFolders.renameAll(testDir)
			for p in after_path:
				self.assertTrue(os.path.exists(p))
		except:
# 			shutil.rmtree(testDir)
			raise
# 		shutil.rmtree(testDir)
			

	def testReplaceCharsByTranslators(self):
		before = "äöü á é ú ó í à è ù ò ì â ê û ô î ß ( )"
		after = "aeoeue_a_e_u_o_i_a_e_u_o_i_a_e_u_o_i_ss__"
		self.assertEqual(after, replaceCharacters.replaceCharsByTranslators(before))	
		
	def testReplaceCharsDefault(self):
		before = "տպوى的使пр刷及ობסתνόhallo"
		after = "????????????????hallo"
		self.assertEqual(after, replaceCharacters.replaceCharsDefault(before))
		
	def testReplaceChars(self):
		before = "aäáàâ刷及"
		after = "aaeaaa??"
		self.assertEqual(after, replaceCharacters.replaceChars(before))

		
if __name__ == "__main__":
	unittest.main()		