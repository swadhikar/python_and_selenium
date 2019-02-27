import re

line = "Cats are more smarter than dogs."
pattern = r'(.*) are (.*) .*' # The final .* is considered to hold one word

so = re.search(pattern, line)

print so.group()
print so.group(1)
print so.group(2)
