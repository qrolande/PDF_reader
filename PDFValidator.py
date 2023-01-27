import fitz


class PDFValidator():
	filename = ''
	new_dict = {}

	def __init__(self, filename):
		self.filename = filename
		assert '.pdf' in self.filename, "PDF file is needed"
		print("File added successfully!")

	def parser(self):
		text = {}
		mydict = {}
		with fitz.open(self.filename) as doc:
			for page in doc:
				text[page] = page.get_text()
				mydict = str(text[page]).split('\n')

		temp = []
		for ind in range(len(mydict)):
			temp.append(mydict[ind].split(':'))

		key = []
		value = []
		for i in range(len(temp)):
			if i == 0:
				value.append('')
			for y in range(len(temp[i])):
				if y == 0 and temp[i][y] == ' ':
					break
				elif y == 0:
					key.append(temp[i][y])
				else:
					value.append(temp[i][y])

		self.new_dict = dict(zip(key, value))
		print("File parsed!")

		return self.new_dict

