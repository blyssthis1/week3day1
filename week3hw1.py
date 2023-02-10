import re

with open("regex_test.txt") as names:
    regex = names.readlines()
        


for name in regex:
    presi = re.match(r'[A-Za-z]+[" "][A-Z][- a-zA-Z]+', name)
    if presi:
        print(presi.group())
    else:
        print(None)