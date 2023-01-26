import fitz


class PDFValidator():
	filename = ''
	parsed_text = {}

	def __init__(self, filename):
		self.filename = filename
		assert '.pdf' in self.filename, "PDF file is needed"
		print("File added successfully!")

	def parser(self):
		text = {}
		with fitz.open(self.filename) as doc:
			for page in doc:
				text[page] = page.get_text()
				self.parsed_text = str(text[page])

		return self.parsed_text.split('\n')

