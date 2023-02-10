# my_file = open('regex_test.txt')
# print(my_file.read())
# my_file.close()

import re
with open("regex_test.txt") as names:
        regex = names.readlines()

for name in regex:
    p1 = re.match(r'[A-Za-z]+[" "][A-Z][- a-zA-Z]+', name)

    if p1:
        print(p1.group())
    else:
        print(None)
