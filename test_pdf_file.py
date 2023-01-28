from src.PDFValidator import PDFValidator
from src.MainPFDModel import MainPDFModel
from PIL import Image, ImageChops
import os


def test_compare_fields(pdf_adder):
	main_model = MainPDFModel()
	file = PDFValidator(pdf_adder)
	new_pdf = file.pdf_reader()
	new_dict = list(file.parser(new_pdf))

	assert main_model.name == new_dict[0]
	assert main_model.pn == new_dict[1]
	assert main_model.sn == new_dict[2]
	assert main_model.description == new_dict[3]
	assert main_model.location == new_dict[4]
	assert main_model.condition == new_dict[5]
	assert main_model.receiver == new_dict[6]
	assert main_model.uom == new_dict[7]
	assert main_model.exp_data == new_dict[8]
	assert main_model.po == new_dict[9]
	assert main_model.cert_source == new_dict[10]
	assert main_model.rec_data == new_dict[11]
	assert main_model.mfg == new_dict[12]
	assert main_model.batch == new_dict[13]
	assert main_model.dom == new_dict[14]
	assert main_model.remark == new_dict[15]
	assert main_model.lot == new_dict[16]
	assert main_model.tagged_by == new_dict[17]
	assert main_model.qty == new_dict[18]
	assert main_model.notes == new_dict[19]

def test_compare_file(pdf_adder):
	try:
		MainPDFModel()
		new_pdf = PDFValidator(pdf_adder)
		new_pdf.pdf_to_image()

		assert os.path.isfile('MainPDFModel.jpg'), "There is no file MainPDFModel.jpg"
		assert os.path.isfile('SecondPDF.jpg'), "There is no file SecondPDF.jpg"

		main_pdf_model = Image.open('MainPDFModel.jpg')
		second_pdf = Image.open('SecondPDF.jpg')
		size = [800, 700]
		main_pdf_model.thumbnail(size)
		second_pdf.thumbnail(size)

		result = ImageChops.difference(main_pdf_model, second_pdf)
		if result.getbbox() == None:
			print("Files is equal")
		else:
			print(result.getbbox())
			result.save('result.jpg')
			assert result == None, "Files not equal, pleas check result.jpg"

	finally:
		main_pdf_model = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'MainPDFModel.jpg')
		second_pdf = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'SecondPDF.jpg')

		if os.path.isfile(main_pdf_model):
			os.remove(main_pdf_model)

		if os.path.isfile(second_pdf):
			os.remove(second_pdf)
