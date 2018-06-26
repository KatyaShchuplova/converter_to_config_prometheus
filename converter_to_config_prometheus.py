#!/usr/bin/python
import re
import yaml


SOURCE_FILE = "/etc/ansible/hosts"
OUT_FILE = "targets.yml"
PORT = 9100


def create_data_yaml(node):
    format_line = "%s:%d" % (node, PORT)
    data = [{'targets': format_line, 'labels': {'job': node}}]
    return data


def copy_text():
    patterns = [r'\#', r'\[*\]']
    with open(SOURCE_FILE) as source_file:
        with open(OUT_FILE, "w") as out_file:
            for line in source_file:
                is_line_valid = True
                for pattern in patterns:
                    if re.search(pattern, line):
                        is_line_valid = False
                        break
                if is_line_valid and not line.isspace():
                    data = create_data_yaml(line.rstrip())
                    yaml.dump(data, out_file, default_flow_style=False)


def main():
    try:
        copy_text()
        print('OK! List for config was created')
    except:
        print('WARNING! List for config was not created')


if __name__ == '__main__':
    main()
