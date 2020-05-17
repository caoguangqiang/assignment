import zipfile

from source.Josephus.josephus import Ring
from source.file_reader.reader import CSVReader
from source.file_reader.reader import TxtReader
from source.file_reader.reader import TxtZipReader
from source.file_reader.reader import CSVZipReader

def write_josephus_ring(reader=None):
    ring = Ring(reader)
    total = len(ring.people)

    while True:
        try:
            start = int(input("请输入开始位置:"))
            if start > total or start < 1:
                print(f"请输入1至{total}的正整数!")
                continue
            break
        except ValueError:
            print(f"请输入1至{total}的正整数!")

    while True:        
        try:
            step = int(input("请输入步长:"))
            if step < 1:
                print("请输入正整数!")
                continue
            break
        except ValueError:
            print(f"请输入从1到 {total}的数!")
    ring.reset(start, step)
    return ring

def creat_reader():
    print("游戏即将开始\n根据提示选择一种文件的类型")
    while True:
        n = int(input("1: txt 2: csv 3:zip 4: 其他\n"))
        if n == 1:
            reader = data_from_txt()
        elif n == 2:
            reader = data_from_csv()
        elif n == 3:
            reader = data_from_zip()
        elif n == 4:
            print("暂不支持其他类型，请在1至3中选择！")
            break
        else:
            reader = None

        return reader

def data_from_txt():
    while True:
        try:
            file_path = input("输入txt文件名:")
            txt_reader = TxtReader(file_path)
            break
        except FileNotFoundError:
            print("文件名无效\n请输入有效文件名!")
    return txt_reader

def data_from_csv():
    while True:
        try:
            file_path = input("输入csv文件名:")
            csv_reader = CSVReader(file_path)
            break
        except FileNotFoundError:
            print("文件名无效\n请输入有效文件名!")
    return csv_reader 

def data_from_zip():
    while True:
        file_path = input("请输入zip文件名:")
        if zipfile.is_zipfile(file_path):
            break
        print("文件名无效\n请输入有效文件名!")

    while True:
        target_file = input("填写你想选择的文件:")
        try:
            if '.txt' in target_file:
                zip_reader = TxtZipReader(file_path, target_file)
            elif '.csv' in target_file:
                zip_reader = CSVZipReader(file_path, target_file)
            else:
                print("输入有效文件名!")
                continue
            break
        except KeyError:
            print("该文件不存在，请再次输入:")
    
    return zip_reader

def print_result(ring):
    print("结果如下：")
    size = len(ring.people)
    index = 1

    ring = ring.iter()
    for each in ring:
        if index == size:
            print(f"本局获胜者是: {each.name}\t{each.age}")
        else:
            print(f"淘汰者: {each.name}\t{each.age}")
        index += 1



if __name__ == '__main__':
    reader = creat_reader()
    ring = write_josephus_ring(reader)
    print_result(ring)