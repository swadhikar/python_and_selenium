import re
line = "Cats are smarter than dogs"
mo = re.match(r'(.*) are (.*) than (.*)', line)

if mo:
    print mo.group()
    print mo.group(1)    #Cats
    print mo.group(2)    #smarter
    print mo.group(3)    #dogs
else:
    print "No match!"
