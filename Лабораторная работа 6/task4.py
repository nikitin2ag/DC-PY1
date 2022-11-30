import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file, delimiter=',', new_line='\n') -> list[dict]:
    # TODO реализовать конвертер из csv в json
    with open(file) as f:
        header = f.readline().replace(new_line, '').split(delimiter)
        for line in f:
            values = line.replace(new_line, '').split(delimiter)
        output_str = []
        for i, s in enumerate(values):
            output_str.append(dict(zip(header, values[i])))
        return output_str


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
