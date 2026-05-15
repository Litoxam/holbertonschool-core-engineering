#!/usr/bin/env python3
"""The Enigmatic FlyingFish - Exploring Multiple Inheritance"""

from abc import ABC, abstractmethod
import math


class Fish():
    """class named FlyingFish"""
    def swim(self):
        """Method swim that prints The fish is swimming"""
        print("The fish is swimming")

    def habitat(self):
        """Methode habitat that prints The fish lives in water"""
        print("The fish lives in water")


class Bird():
    """class named Bird"""
    def fly(self):
        """Method that prints The bird is flying"""
        print("The bird is flying")

    def habitat(self):
        """Method habitat that prints The bird lives the sky"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """class named FlyingFish that inherits from Fish and Bird"""

    def fly(self):
        """Method fly that prints The flying fish is soaring"""
        print("The flying fish is soaring!")

    def swim(self):
        """Method swim that prints The flying fish is swimming"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Method habitat"""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
    print(flying_fish.__class__.__mro__)
