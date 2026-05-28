#!/usr/bin/env python3
"""Module for serializing and deserializing custom objects with pickle."""
import pickle


class CustomObject:
    """A custom class that can be serialized and deserialized using pickle."""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object to a file using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file using pickle."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
