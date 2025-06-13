import csv
import json


def get_csv_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        file = csv.reader(f)
        date_list = [row for row in file]
    return date_list


def get_json_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        # 将文件转化为字典或者列表
        file = json.load(f)
    return file
