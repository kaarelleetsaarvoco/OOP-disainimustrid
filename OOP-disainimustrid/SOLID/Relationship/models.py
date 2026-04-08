from enum import Enum


class Person:
    """Represents a person with a name"""
    
    def __init__(self, name):
        self.name = name


class Relationship(Enum):
    """Enum for different types of relationships"""
    PARENT = 0
    CHILD = 1
    SIBLING = 2
