"""
 Collects data on new bitcoin blocks being created and saves it to a csv file.
 Date: Oct 18,2020
 The data format is: hash,version,previous block hash,merkel root,time,nonce,height
"""

import requests
import time
import os

cwd = os.getcwd()
dataPath = cwd + "/data/"
try:
	os.mkdir(dataPath)
except:
	pass

previous_block_hash = ""

while(True):
	request = requests.get("https://blockchain.info/latestblock")

	if(request.status_code == 200):

		latest_block = request.json()
		block_hash = latest_block["hash"]
	
		if(block_hash != previous_block_hash):
			request = requests.get("https://blockchain.info/rawblock/" + block_hash)

			if(request.status_code == 200):
	
				block = request.json()

				previous_block_hash = block["hash"]

				f = open(dataPath + 'bitcoin_blocks.csv', 'a')

				f.write(str(block["hash"]) + ',')
				f.write(str(block["ver"]) + ',')
				f.write(str(block["prev_block"]) + ',')
				f.write(str(block["mrkl_root"]) + ',')
				f.write(str(block["time"]) + ',')
				f.write(str(block["nonce"]) + ',')
				f.write(str(block["height"]) + '\n')
	
				f.close()
	time.sleep(120)

