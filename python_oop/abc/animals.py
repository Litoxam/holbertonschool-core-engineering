#!/usr/bin/env python3
"""Abstract Animal Class and its Subclasses"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract class named Animal"""
    @abstractmethod
    def sound(self):
        """Abstract method sound that does nothing"""
        pass

class Dog(Animal):
    """Class named Dog that inherits from Animal"""
    def sound(self):
        """Implement the abstract method sound to return Bark"""
        return "Bark"
    
class Cat(Animal):
    """Class named Cat that inherits from Animal"""
    def sound(self):
        """Implement the abstract method sound to return Meow"""
        return "Meow"
