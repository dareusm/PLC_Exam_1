#Check if it is a valid floating point literal

import re

#Returns True if the given string is a valid floating point literal, False otherwise.
def is_float(string):
    
    regex_pat = r'^[-+]?([0-9]+\.?|[0-9]*\.[0-9]+)([eE][-+]?[0-9]+)?$'
    return re.match(regex_pat, string) is not None

print(is_float('2.46'))
print(is_float('7.52e-10'))
print(is_float('one'))
print(is_float('1'))