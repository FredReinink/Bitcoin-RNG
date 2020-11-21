"""
Converts the merkel roots, times, and nonces in a bitcoin block data file into binary data to test with entropy estimators.
"""
import binascii


data_file = open('bitcoin_blocks.csv', 'r')
lines = list(data_file.read().split('\n'))
data_file.close()


merkel_file = open('merkel_roots.dat', 'wb')
time_file = open('times.dat', 'wb')
nonce_file = open('nonces.dat', 'wb')

for i in range(len(lines)):
	if lines[i] != '':
		block = list(lines[i].split(','))

		merkel_file.write(binascii.unhexlify(block[3]))
	
		time = hex(int(block[4]) & (2**32-1))[2:]
		time = '0'*(8-len(time)) + time
		time_file.write(binascii.unhexlify(time))

		nonce = hex(int(block[5]) & (2**32-1))[2:]
		nonce = '0'*(8-len(nonce)) + nonce
		nonce_file.write(binascii.unhexlify(nonce))

merkel_file.close()
time_file.close()
nonce_file.close()
