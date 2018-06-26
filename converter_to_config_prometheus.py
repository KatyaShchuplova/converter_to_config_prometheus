#!/usr/bin/python
import re

SOURCE_FILE = "source"
OUT_FILE = "out"
PORT = 9100


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
                    out_file.write(format_line(line.rstrip(), PORT))


def format_line(node, port):
    line = "-targets:['{0}:{1}']\n labels:\n   job: {2}\n\n".format(node, port, node)
    return line


def main():
    try:
        copy_text()
        print('OK! List for config was created')
    except:
        print('WARNING! List for config was not created')


if __name__ == '__main__':
    main()
