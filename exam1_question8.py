#Check if it is a valid email address

import re

#Returns True if the given string is a valid email address, False otherwise.
def is_email(string):
    
    
    regex_pat = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex_pat, string) is not None

print (is_email('dareusm@outlook.com'))
print(is_email('dmorris32@student.gsu.edu'))
print(is_email('dareusm.outlook.com'))
print(is_email('dareusm@outlook'))
print(is_email('Im an email'))