import requests
from config import base_uri
from config import invalid_base_uri
from constants import test_invalid_url_failed_message
from constants import response_code_not_found
from utils.readtestdata import read_file
from pytest import mark

@mark.parametrize("input",read_file("testdata.json"))
def test_conversionFromDateStringToTimestamp(input):
    response = requests.get(f'{base_uri}',params=input['param'])
    assert response.status_code == input['expected_status']
    assert response.text == input['expected_data'], input['test_failed_message']

def test_invalidUrlPath():
    response = requests.get(invalid_base_uri)
    assert response.status_code == response_code_not_found, test_invalid_url_failed_message



