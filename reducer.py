#!/usr/bin/env python

import sys
import csv

count_word = 0
current_word = None
word = None

for line in sys.stdin:
	line = line.strip()
	word, count = line.split('\t', 1)

        count = int(count)
	if current_word == word:
		count_word += count
    	else:
        	if current_word:
            		print(current_word+"\t"+str(count_word))
        	count_word = count
        	current_word = word

if current_word == word:
    print(current_word+"\t"+str(count_word))	
