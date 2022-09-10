import string 
from collections import OrderedDict
class cipher:
	def __init__(self, text, keyword):
		self.open_alphabet = string.ascii_lowercase + chr(32)
		self.keyword = keyword.lower()
		self.text = text.lower()
		self.cipher_alphabet = str()
		self.result_text = str()
	def process(self, tujuan):
		self.cipher_alphabet = self.keyword + self.open_alphabet + chr(32)
		self.cipher_alphabet = str().join(OrderedDict.fromkeys(self.cipher_alphabet))
		count = 0
		while count < len(self.text):
			if tujuan == "encrypt":
				index = self.open_alphabet.index(self.text[count])
				self.result_text += self.cipher_alphabet[index]
			elif tujuan == "decrypt":
				index = self.cipher_alphabet.index(self.text[count])
				self.result_text += self.open_alphabet[index]
			count += 1
		return self.result_text
# coded by ./meicookies
