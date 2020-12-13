"""
 Collects data on the latest SAMPLE_SIZE bitcoin blocks created and saves it to a csv file.
 Date: Oct 22,2020
 The data format for each block is: hash,version,previous block hash,merkel root,time,nonce,height
"""

import requests
import time

SAMPLE_SIZE = 40000

request = requests.get("https://blockchain.info/latestblock")

if (request.status_code == 200):
	latest_block = request.json()
	block_hash = latest_block["hash"]

	for i in range(SAMPLE_SIZE):
		request = requests.get("https://blockchain.info/rawblock/" + block_hash)

		if (request.status_code == 200):

			block = request.json()

			block_hash = block["prev_block"]

			f = open('bitcoin_blocks.csv', 'a')

			f.write(str(block["hash"]) + ',')
			f.write(str(block["ver"]) + ',')
			f.write(str(block["prev_block"]) + ',')
			f.write(str(block["mrkl_root"]) + ',')
			f.write(str(block["time"]) + ',')
			f.write(str(block["nonce"]) + ',')
			f.write(str(block["height"]) + '\n')

			f.close()

