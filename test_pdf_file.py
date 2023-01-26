import json
from PDFValidator import PDFValidator


def test_compare_fields(pdf_adder):
	file = PDFValidator(pdf_adder)
	parsed_file = file.parser()
	print("parsed_file =", parsed_file[1])
