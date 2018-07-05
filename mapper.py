#!/usr/bin/env python

import sys
import csv

with sys.stdin as data:
	reader = csv.reader(data, delimiter=',')
	reader.next()
	for row in reader:
		row = filter(None,row[-5:])
		for items in row:
   			print(items+"\t"+str(1))
