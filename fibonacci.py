#!/usr/bin/env python3

"""
Generates Fibonacci
"""


__author__ = 'abdulkareem'


a, b = 0, 1
print(a)
print(b)
while b < 50:
    a, b = b, a + b
    print(b)