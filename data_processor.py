"""
 Processes all csv's in data/ to be .txt files containing ASCII 1s and 0s.
 Date: Nov 20, 2020

 Refs: 
 https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
 https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
"""

import binascii
import os
from os import listdir
from os.path import isfile, join

cwd = os.getcwd()
dataPath = cwd + "/data/"

compatibleDataPath = cwd + "/nist_compatible_data/"
try:
	os.mkdir(compatibleDataPath)
except:
	pass

data = [f for f in listdir(dataPath) if isfile(join(dataPath, f))]

for f in data:
	fname = f.split(".")[0]
	if fname == "bitcoin_blocks": continue
	dataIn = open(dataPath + f, 'r')
	dataOut = open(compatibleDataPath + fname + ".bin", 'wb')

	chars = dataIn.read()
	chars = chars.replace(",", "")
	chars = chars.replace("\n", "")
	bytes_object = bytes.fromhex(chars)
	dataOut.write(bytes_object)