import csv
from pathlib import Path
import argparse

def map_row_from_format_text(data_row, format_text):
    output_lines = []
    for line in format_text:
        for (key, value) in data_row.items():
            line = line.replace(key, value)
        output_lines.append(line)
    output = ''.join(output_lines)
    return output



def map_rows_from_format_text(data_rows, format_text):
    rows_output = [map_row_from_format_text(r, format_text) for r in data_rows]
    return '\n'.join(rows_output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='field_tagger',
        description="""\
Takes a simple text file with fieldnames in it and a csv file, and uses them to generate
mapped output for each row.. prints the output to stdout unless an output filepath is given"""   
    )
    parser.add_argument('-c', '--csv', dest='csv', type=Path, required=True)
    parser.add_argument('-f','--field_text', dest='field_text', type=Path, required=True)
    parser.add_argument('-o', '--output-file', dest='output_file', type=Path)
    args = parser.parse_args()

    if not args.csv.exists() or not args.csv.is_file():
        print('-c/--csv must be a valid csv file')
        exit(1)
    if not args.field_text.exists() or not args.field_text.is_file():
        print('-f/--field_text must be a valid text file')
        exit(1)

    with args.csv.open() as f:
        try:
            reader = csv.DictReader(f)
            data_rows = [row for row in reader]
        except:
            print(f'invalid csv file provided')
    
    with args.field_text.open() as f:
        field_text = f.read()
    
    output = map_rows_from_format_text(data_rows, field_text)

    if args.output_file is None:
        print(output)
        exit(0)
    
    with args.output_file.open('w') as f:
        f.write(output)

    print(f'done see output in {args.output_file}')