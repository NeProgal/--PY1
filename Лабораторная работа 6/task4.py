import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename) as src_file:
        lines = [line.replace(new_line, "").split(delimiter) for line in src_file]
        header = lines[0]

    return [dict(zip(header, lines[i])) for i in range(1, len(lines))]


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
