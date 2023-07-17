#!/usr/bin/env python3


class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def display_info(self):
        print(f"name is {self.name}, breed is {self.breed}")


fido = Dog("Fido", "lebrador")
fido.display_info()
