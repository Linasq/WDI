import pytest

@pytest.fixture(params=['apple.csv', 'iris.csv', 'sp500_data.csv'])
def csv_data(request):
    with open(request.param) as f:
        data = f.read().split('\n')
    return data

@pytest.fixture()
def csv_header(csv_data):
    return csv_data[0]

@pytest.fixture()
def column_names(csv_header):
    return csv_header.split(',')

def test_headerUppercase(csv_header):
    assert csv_header==csv_header.upper()

def test_firstDate(column_names):
    assert column_names[0].lower()=='date'