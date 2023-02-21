#Check if it is a valid integer literal

import re

#Returns True if the given string is a valid integer literal, False otherwise.
def is_integer(string):
   
    regex_pat = r'^[-+]?\d+$'
    return re.match(regex_pat, string) is not None

print(is_integer('2'))
print(is_integer('7.52e-10'))
print(is_integer('One'))