from source.reader.txt_reader import TxtReader
from source.reader.csv_reader import CSVReader
from source.person.person import Person

def test_txt_reader():
    txt_reader = TxtReader("person.txt")
    result = []
    for each in txt_reader:
        result.append(each)

    assert result == [
        Person("John", 18),
        Person("Bob", 19),
        Person("Jerry", 20),
        Person("Mark", 21),
        Person("Jack", 22),
        Person("Neil", 23),
        Person("Oscar", 24)
    ]

def test_txt_reader_from_zip_file():
    txt_reader = TxtReader.from_zip('person.zip', 'person.txt')
    result = []
    for each in txt_reader:
        result.append(each)

    assert result == [
        Person("John", 18),
        Person("Bob", 19),
        Person("Jerry", 20),
        Person("Mark", 21),
        Person("Jack", 22),
        Person("Neil", 23),
        Person("Oscar", 24)
    ]

def test_csv_reader():
    csv_reader = CSVReader('person.csv')
    result = []
    for each in csv_reader:
        result.append(each)

    assert result == [
        Person("John", 18),
        Person("Bob", 19),
        Person("Jerry", 20),
        Person("Mark", 21),
        Person("Jack", 22),
        Person("Neil", 23),
        Person("Oscar", 24)
    ]

def test_csv_reader_from_zip_file():
    csv_reader = CSVReader.from_zip('person.zip', 'person.csv')
    result = []
    for each in csv_reader:
        result.append(each)

    assert result == [
        Person("John", 18),
        Person("Bob", 19),
        Person("Jerry", 20),
        Person("Mark", 21),
        Person("Jack", 22),
        Person("Neil", 23),
        Person("Oscar", 24)
    ]