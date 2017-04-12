#!/usr/bin/python
import math
import argparse
import fileinput as fi

# argument parser 
# program class enter the file and return reads each line  and sends to statement class for interpretation
if fi.input():
	for line in fi.input():
		print (line)
		ob=statement(line)
	
else:print "no input file"



class statement:
	def _init_(self,line):
		self.line=line
		

>>> import re
>>> # Splitting on: , <space> - ! ? :
>>> filter(None, re.split("[, \-!?:]+", "Hey, you - what are you doing here!?"))
['Hey', 'you', 'what', 'are', 'you', 'doing', 'here']

>>> re.split('\W+', 'Words, words, words.')
['Words', 'words', 'words', '']

		
