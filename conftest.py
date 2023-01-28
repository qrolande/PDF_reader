import pytest


def pytest_addoption(parser):
    parser.addoption('--filename', action='store', default=None, help="Choose PDF file")


@pytest.fixture()
def pdf_adder(request):
    filename = request.config.getoption("filename")
    return filename
