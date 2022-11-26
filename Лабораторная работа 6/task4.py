import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file, delimiter=',', new_line='\n') -> list[dict]:
    # TODO реализовать конвертер из csv в json
    with open(file) as f:
        for str_ in f:
            str_ = str_.replace(new_line, '').split(delimiter)
        header = f.readline().replace(new_line, '').split(delimiter)
        output_str = []
        for i in range(len(str_)):
            output_str.append(dict(zip(header, str_[i])))
        return output_str


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
