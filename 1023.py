#!/usr/bin/python

import re

preg = input()

string = input()

result_string = ''

preg = preg.upper() + preg.lower()

if '+' in preg:
    preg = preg+'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


if preg:
    for char in string:
        if char in preg:
            continue
        else:
            result_string = result_string + char
    
    print(result_string)

else:
    print(string)

