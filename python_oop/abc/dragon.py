#!/usr/bin/env python3
"""The Mystical Dragon - Mastering Mixins"""

from abc import ABC, abstractmethod
import math


class FlyMixin():
    """Mixin class named FlyMixin"""
    def fly(self):
        """Method fly that prints The creature flies!"""
        print("The creature flies!")


class SwimMixin():
    """Mixin class named SwimMixin"""
    def swim(self):
        """Method swim that prints The creature swims!"""
        print("The creature swims!")


class Dragon(FlyMixin, SwimMixin):
    """Class named Dragon that inherits from FlyMixin and SwimMixin"""
    def roar(self):
        """Method roar that prints The dragon roars!"""
        print("The dragon roars!")


if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()
    dragon.fly()
    dragon.roar()
