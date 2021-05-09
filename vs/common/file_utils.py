import io
import json
import csv


def read_lines(file_name):
    """Read a utf-8 file line by line to a list"""
    words = []
    with io.open(file_name, mode="r", encoding="utf-8") as f:
        for line in f.readlines():
            words.append(line.strip())
    return words


def write_lines(file_name, lines):
    """Read a utf-8 file line by line to a list"""
    with io.open(file_name, mode="w", encoding="utf-8") as f:
        for line in lines:
            f.write(line.strip() + '\n')


def read_json_file(file_path):
    with open(file_path, mode='r', encoding='utf8') as f:
        json_data = json.load(f)
        return json_data


def write_json_file(path, content):
    with io.open(path, 'w', encoding='utf8') as fw:
        json.dump(content, fw, ensure_ascii=False, indent=2)


def read_tsv_file(file_path):
    data_list = []
    with open(file_path, 'r', encoding='utf8') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            data_list.append(row)
    data_list.remove(data_list[0])
    return data_list


def write_tsv_file(file_path, header, content):
    with io.open(file_path, 'w', encoding='utf8') as fw:
        tsv_writer = csv.writer(fw, delimiter='\t')
        tsv_writer.writerow(header)
        for item in content:
            tsv_writer.writerow(item.values())
