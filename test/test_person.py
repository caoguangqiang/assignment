import pytest

from source.person.person import Person

def test_person_init_with_parameter():
    someone = Person("John", 18)
    
    assert someone.name == "John"
    assert someone.age == 18

def test_person_init_without_parameter():
    someone = Person()

    assert someone.name == None
    assert someone.age == 0

def test_person_the_value_of_age_less_than_zero():
    with pytest.raises(ValueError):
        someone = Person(age=-1)

def test_person_compare():
    p1 = Person("John", 18)
    p2 = Person("John", 18)

    assert p1 == p2 