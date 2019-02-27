# Match list of characters
import re

pattern = r'^\d'
txt = str(raw_input('Enter a name: >> '))

s = re.search(pattern, txt)

if s:
    print "Incorrect name. (Should not begin with a digit!)"
else:
    print "Valid name!"
