from typing import List, Optional

from source.file_reader.reader import Reader
from source.person.person import Person

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
    def append(self, obj) -> None:
        if(len(self.people) > Ring.max_size):
            raise Exception("exceed the max cap of people.")
        self.people.append(obj)
   
    # 删功能
    def pop(self, index: int) -> None:
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
    def iter(self) :
        if len(self.temp) == 0:
            return None

        for i in range(len(self.temp)):
            self.current_id = (self.current_id + self.step - 1) % len(self.temp)
            index = self.temp.pop(self.current_id)
            yield index