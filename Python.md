``` python
# Basic function
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Default arguments
def power(base: float, exp: int = 2) -> float:
    return base ** exp

# Keyword-only arguments (forces clarity when calling)
def connect(*, host: str, port: int) -> str:
    return f"Connecting to {host}:{port}"

# Variadic arguments
def summarize(*args: int, **kwargs: str) -> None:
    print("Positional:", args)
    print("Keyword:", kwargs)

# Function with type hint for list
from typing import List
def total(numbers: List[int]) -> int:
    return sum(numbers)

# Using modern built-in generics (Python 3.9+)
def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

# Lambda (anonymous function)
square = lambda x: x * x
```

# Basic class
```python
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return f"{self.name} makes a sound."

# Inheritance
class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} barks!"

# Data classes (auto __init__, __repr__, __eq__)
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

# Class with default + computed properties
class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def area(self) -> float:
        from math import pi
        return pi * self.radius**2

    @classmethod
    def unit_circle(cls) -> "Circle":
        return cls(1.0)

    @staticmethod
    def describe() -> str:
        return "A circle is defined by its radius."
```
# Python `try` / `except` Cheat Sheet

## Basic Syntax
```python
try:
    # Code that might raise an error
except SomeError:
    # Handle the error
```

## Run it
```python
if __name__ == "__main__":
```
