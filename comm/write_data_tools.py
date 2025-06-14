import csv


def write_data_to_csv(filename, data, mode='w'):
    """
    将数据写入CSV文件。

    :param filename:要写入的CSV文件名
    :param data:要写入的数据，二维列表形式
    :param mode:写入模式，默认w模式，可选w,a
    """
    with open(filename, mode=mode, newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
