
class Person(object):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        if age < 0:
            raise ValueError('The value of age can be less than 0') 
        self.age = age