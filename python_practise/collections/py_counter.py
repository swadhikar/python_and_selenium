# Python script to demonstrate collections module
from collections import Counter
import re
import os

def basic_counter():
	FILE = 'numpy_other_ways_array_create.py'
	words = re.findall('\w+', open(FILE).read().lower()) # Fetch all words using regex
	print(Counter(words).most_common(10)) # print top 10 most common words with their counts

def element_method():
	"""Counter objects has a method called elements which returns an iterator over elements 
	repeating each as many times as its count. Elements are returned in **arbitrary order**."""
	c = Counter(a=4, b=3, c=2, d=1)
	print(list(c.elements()))	# or using-> for e in c.elements(): ...

def most_common_method():
	c = Counter("IndiaIsMyCountry.AndIAmProudOfIt!")
	print(c.most_common())

if __name__ == '__main__':
	os.system('cls')
	# basic_counter()
	# element_method()
	most_common_method()