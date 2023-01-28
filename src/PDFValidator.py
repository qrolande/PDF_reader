import fitz
from pdf2image import convert_from_path


class PDFValidator():
	filename = ''
	new_dict = {}
	parsed_dict = {}

	def __init__(self, filename):
		self.filename = filename
		assert '.pdf' in self.filename, "PDF file is needed"
		print()
		print("File added successfully!")

	def pdf_reader(self):
		text = {}
		with fitz.open(self.filename) as doc:
			for page in doc:
				text[page] = page.get_text()
				self.new_dict = str(text[page]).split('\n')

		return self.new_dict

	def parser(self, dictionary):
		temp = []

		for ind in range(len(dictionary)):
			temp.append(dictionary[ind].split(':'))

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

		self.parsed_dict = dict(zip(key, value))
		print("File parsed!")

		return self.parsed_dict

	def pdf_to_image(self):
		pages = convert_from_path(self.filename)
		for i, page in enumerate(pages):
			page.save('SecondPDF.jpg', 'JPEG')
