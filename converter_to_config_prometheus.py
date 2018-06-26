#!/usr/bin/python
import re
from ruamel_yaml import YAML



#SOURCE_FILE = "/etc/ansible/hosts"
SOURCE_FILE = "source"
OUT_FILE = "targets.yml"
PORT = 9100


def create_data_yaml(yaml, node, port):
    yaml_str = """\
    targets:
    labels:
        job:

    """
    data = yaml.load(yaml_str)
    data['targets'] = "[%s:%d]" % (node, port)
    data['labels']['job'] = node
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
                    yaml = YAML()
                    data = create_data_yaml(yaml, line.rstrip(), PORT)
                    yaml.dump(data, out_file)


def main():
    try:
        copy_text()
        print('OK! List for config was created')
    except:
        print('WARNING! List for config was not created')


if __name__ == '__main__':
    main()
