﻿"""Przykładowe funkcje w module utils.py"""

def add(a: int, b: int) -> int:
    """Zwraca sumę a i b."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Zwraca różnicę a i b (a minus b)."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Zwraca iloczyn a i b."""
    return a * b

def divide(a: int, b: int) -> float:
    """Zwraca iloraz a i b. Jeśli b == 0, rzuca ZeroDivisionError."""
    return a / b
