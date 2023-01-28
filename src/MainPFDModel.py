from src.PDFValidator import PDFValidator
from pdf2image import convert_from_path


class MainPDFModel():
	pdf = 'pdf_file.pdf'
	file = PDFValidator(pdf)
	main_model = file.pdf_reader()

	main_dict = list(file.parser(main_model).keys())

	name = main_dict[0]
	pn = main_dict[1]
	sn = main_dict[2]
	description = main_dict[3]
	location = main_dict[4]
	condition = main_dict[5]
	receiver = main_dict[6]
	uom = main_dict[7]
	exp_data = main_dict[8]
	po = main_dict[9]
	cert_source = main_dict[10]
	rec_data = main_dict[11]
	mfg = main_dict[12]
	batch = main_dict[13]
	dom = main_dict[14]
	remark = main_dict[15]
	lot = main_dict[16]
	tagged_by = main_dict[17]
	qty = main_dict[18]
	notes = main_dict[19]

	pages = convert_from_path('pdf_file.pdf')
	for i, page in enumerate(pages):
		page.save('MainPDFModel.jpg', 'JPEG')

	def __init__(self):
		print()
		print("Main pdf model ready!")
