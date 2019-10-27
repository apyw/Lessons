""" 
Lesson 1:
    Eliminating redundancy
"""

def is_less_than_ten_v1(x):
    if x < 10 == True:
        return True
    if x >= 10 == True:
        return False

def is_less_than_ten_v2(x):
    # We simplify this condition
    if x < 10:
        return True
    # We use else here instead
    else:
        return False

def is_less_than_ten_v3(x):
    if x < 10:
        return True
    # We can actually eliminate else since it's redundant
    return False

# We can see that doing "x < 10" in-line is shorter than using our function, making it completely useless
def is_less_than_ten_v4(x):
    # We can directly return the boolean value
    return x < 10:


""" 
Lesson 2:
    Typing Library
    List Comprehension
    Generators
    Tuples
"""
from typing import List, Generator, Tuple


def get_unique_numbers_v1(end: int = 1000) -> List[int]:
    unique_numbers = []
    for n in range(end):
        if "42" in str(n):
            unique_numbers.append(n)
    return unique_numbers

def get_unique_numbers_v2(end: int = 1000) -> List[int]:
    return [n for n in range(end) if "42" in str(n)]

def get_unique_numbers_v3(end: int = 1000) -> Generator[int, None, None]:
    for n in range(end):
        if "42" in str(n):
            yield n

def create_custom_deck_v1(suits: List[str], values: List[str]) -> List[Tuple[str, str]]:
    deck = []
    for suit in suits:
        for value in values:
            if value != "JOKER":
                deck.append((suit, value))

def create_custom_deck_v2(suits: List[str], values: List[str]) -> List[Tuple[str, str]]:
    return [(suit, value) for suit in suits for value in values if value is not "JOKER"]


"""
Lesson 3:
    Exceptions
    Custom Exceptions
    Try/Except/Else/Finally
"""
from datetime import datetime

class InvalidTimeException(Exception):
    pass

class TemperatureException(Exception):
    pass

class TooColdException(TemperatureException):
    pass

class TooHotException(TemperatureException):
    pass

def _change_temperature(temperature: int) -> None:
    if temperature > 25:
        raise TooHotException()
    elif temperature < 15:
        raise TooColdException()
    
def set_thermostat(temperature: int, time: datetime = datetime.now()):
    try:
        _change_temperature(temperature)
        # _change_time(time)
    except TemperatureException:
        _change_temperature(20)
    except InvalidTimeException:
        # _change_time(datetime.now())        

"""
Lesson 4:
    Sets
    Dictionaries
    Array
"""

"""
Lesson 5:
    'is' versus '=='
    Special Methods
"""
