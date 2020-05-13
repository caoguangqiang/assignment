import pytest

from collections import Iterable

from source.Josephus.josephus import Ring
from source.person.person import Person

someone1: Person = Person("John", 18)
someone2: Person = Person("Bob", 19)
someone3: Person = Person("Jerry", 20)

def test_Ring_init():
    ring = Ring()

    assert ring.start == 1
    assert ring.step == 1
    assert ring.people == []

def test_Ring_append():
    ring = Ring()
    ring.append(someone1)
    
    assert ring.people == [someone1]

def test_Ring_pop():
    ring = Ring()
    ring.people = [someone1, someone2, someone3]
    ring.pop(1)

    assert ring.people == [someone1, someone3]
    
def test_Ring_query_list():
    ring = Ring()
    ring.start = 2
    ring.step = 2
    ring.people = [someone1, someone2, someone3]
    result = ring.query_list()

    assert result == [someone3, someone2, someone1]

def test_Ring_reset():
    ring = Ring()

    assert isinstance(ring, Iterable)

def test_Ring_output_iter():
    ring = Ring()
    ring.start = 2
    ring.step = 2
    ring.people = [someone1, someone2, someone3]

    assert next(ring) == someone3
    assert next(ring) == someone2
    assert next(ring) == someone1
    with pytest.raises(StopIteration):
        next(ring)
    
def test_Ring_init_with_reader():
    persons = [someone1, someone2,someone3]
    ring = Ring(reader = persons)

    assert ring.people == [someone1, someone2, someone3]