import os
import csv
import zipfile
import copy

from typing import Iterator, List

from joseph.person.person import Person

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

    def __iter__(self):
        return self
    
    def __next__(self):
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

    def __iter__(self):
        return self

    def __next__(self):
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