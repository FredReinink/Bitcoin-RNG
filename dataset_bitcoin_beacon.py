"""
This program takes a dataset of bitcoin blocks, as given by bitcoin_dataset_collector.py, as input.
It uses these blocks to produce a stream of random values, extracted from the bitcoin blocks.
"""
from Crypto.Cipher import AES
import binascii


"""
Creates a bytes object from the bitcoin block fields containing some unpredictable randomness (merkel_root, time and nonce)
"""
def extract_values(block):
	fields = block.split(',')

	# add markel root
	result = binascii.unhexlify(fields[3])

	# add time
	time = hex(int(fields[4]) & (2**32-1))[2:]
	time = '0'*(8-len(time)) + time
	result += binascii.unhexlify(time)

	# add nonce
	nonce = hex(int(fields[5]) & (2**32-1))[2:]
	nonce = '0'*(8-len(nonce)) + nonce
	result += binascii.unhexlify(nonce)

	return result


"""
Produces a 128 bit random value, based on a given bytes object.
The number of bytes should be a multiple of 16. 
To generate a random value of sufficient quality, the byte string should capture at least 256 bits of min-entropy.
"""
def postprocess(raw_bytestring):
	cipher = AES.new(b'\x7f\x97\rEY\x08Q\x07\xd4\x07\xe1\x12\x89\x01\xcfm', AES.MODE_CBC, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

	encrypted = cipher.encrypt(raw_bytestring).hex()
	return encrypted[(len(encrypted)-32):]


while(True):
	try:
		raw_string = b''
		for i in range(4):
			raw_string += extract_values(input())

		print(postprocess(raw_string))
	except EOFError:
		break
	except:
		print("There was an error processing the input.")
		break
	

