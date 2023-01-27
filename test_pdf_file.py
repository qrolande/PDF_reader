from PDFValidator import PDFValidator


def test_compare_fields(pdf_adder):
	file = PDFValidator(pdf_adder)
	parsed_file = file.parser()
	keys_value_1 = list(parsed_file.keys())
	print("parsed_file =", keys_value_1)
