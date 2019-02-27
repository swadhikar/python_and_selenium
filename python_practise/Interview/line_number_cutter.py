import re

line = r'ip_address.py\nline_number_cutter.py\npattern.py\npatterns_2.py\nregex_match.py \nregex_search.py\n'
new_ln = re.sub(r'\n', ' ', line)

print "Old: " + line
print "New: " + new_ln
