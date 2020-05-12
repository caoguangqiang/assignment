import os
import csv
import zipfile
import copy

from typing import Iterator, List, Optional

class Person(object):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        if age < 0:
            raise ValueError('The value of age can be less than 0') 
        self.age = age

class Reader:
    def __iter__(self) -> Iterator[Person]:
        raise NotImplementedError

    def __next__(self) -> List[Person]:
        raise NotImplementedError

class TxtReader(Reader):
    def __init__(self, path: str) -> None:
        self.file = open(path)

    def __del__(self):
        if self.file:
            self.file.close()

    def __iter__(self) -> Iterator[Person]:
        return self
    
    def __next__(self) -> List[Person]:
        row = next(self.file)
        if not row:
            self.file.close()
            raise StopIteration
        line = row.strip().split(',')
        name = line[0]
        try:
            age = int(line[1])
        except ValueError:
            age = 0
        return Person(name, age)

class CSVReader(Reader):
    def __init__(self, path: str) -> None:
        self.csv_file = open(path)
        self.csv_reader = csv.reader(self.csv_file)
        # self.it = csv_reader.__iter__()

    def __del__(self):
        if self.csv_file:
            self.csv_file.close()

    def __iter__(self) -> Iterator[Person]:
        return self

    def __next__(self) -> List[Person]:
        line = next(self.csv_reader)
        name = line[0]
        try:
            age = int(line[1])
        except ValueError:
            age = 0
        return Person(name, age)

class TxtZipReader(TxtReader):
    def __init__(self, path: str, target_file) -> None:
        with zipfile.ZipFile(path) as zip_file:
            target_path = zip_file.extract(target_file)
        super().__init__(target_path)

class CSVZipReader(CSVReader):
    def __init__(self, path: str, target_file) -> None:
        with zipfile.ZipFile(path) as zip_file:
            target_path = zip_file.extract(target_file)
        super().__init__(target_path)

class Ring:
    max_size = 100

    def __init__(self, reader: Optional[Reader] = None) -> None:
        self.start = 0
        self.step = 1
        self.people: List[Person] = []
        if reader:
            for each in reader:
                self.people.append(each)
    
     # 增功能
    def append(self, obj):
        if(len(self.people) > Ring.max_size):
            raise Exception("exceed the max cap of people.")
        self.people.append(obj)
   
    # 删功能
    def pop(self, index: int):
        if index >= len(self.people):
            raise IndexError
        self.people.pop(index)
    
    # 查找
    def query_list(self) -> List[Person]:
        return self.people
    
    def reset(self) -> None:  
        self.current_id = self.start - 1
        self.temp = copy.copy(self.people)
        self.length = len(self.people)

    # 生成器迭代输出
    def iter(self) -> Iterator:
        if len(self.temp) == 0:
            return None

        for i in range(len(self.temp)):
            self.current_id = (self.current_id + self.step - 1) % len(self.temp)
            index = self.temp.pop(self.current_id)
            yield index

txt_reader = TxtReader('people.txt')
ring = Ring(txt_reader)
for each in ring.people:
    print("name:{}, age:{}" .format(each.name, each.age))

print('-'*30)

ring.start = 2
ring.step = 3
ring.reset()
generator = ring.iter()
for i in range(ring.length):
    index = next(generator)
    if index:
        print("第{}个出列的人：{}；年龄：{}". format(i+1, index.name, index.age))

csv_reader = CSVReader('people.csv')
ring = Ring(csv_reader)

ring.start = 2
ring.step = 3
ring.reset()
generator = ring.iter()
for i in range(ring.length):
    index = next(generator)
    if index:
        print("第{}个出列的人：{}；年龄：{}". format(i+1, index.name, index.age))        