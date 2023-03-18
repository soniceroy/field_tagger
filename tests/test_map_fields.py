import csv
import pytest
from src.field_tagger import map_row_from_format_text, map_rows_from_format_text

@pytest.fixture
def data_rows():
    with open('test_data/test.csv') as f:
        reader = csv.DictReader(f)
        d_rs = [row for row in reader]
    return d_rs

@pytest.fixture
def input_lines():
    with open('test_data/test_input.txt') as f:
        i = f.readlines()
    return i

@pytest.fixture
def row_output():
    with open('test_data/test_row_output.txt') as f:
        o = f.read()
    return o

@pytest.fixture
def rows_output():
    with open('test_data/test_rows_output.txt') as f:
        o = f.read()
    return o

def test_map_row_from_format_text(data_rows, input_lines, row_output):
    assert map_row_from_format_text(data_rows[0], input_lines) == row_output

def test_map_rows_from_format_text(data_rows, input_lines, rows_output):
    assert map_rows_from_format_text(data_rows, input_lines) == rows_output