#!/usr/bin/env python
#vault retrieve.py: Retrieves passwords in secrets.vault
__author__ = 'jriedel'

from Crypto.Cipher import AES
from Crypto import Random
import argparse 

# CMD LINE OPTIONS
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', action="store", dest="name", required=True, help="the name of the content to retrieve")
parser.add_argument('-k', '--key', action="store", dest="key", required=True, help="the public key for the encrypted content")
args = parser.parse_args()

# CMD LINE VARS
name = args.name
vaultFile = '.' + str(name)
key = args.key


def do_decrypt(vaultCipherText, key):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    decryptedText = iv + cipher.decrypt(vaultCipherText)

    decryptedText = decryptedText[32:]

    return decryptedText

def retrieve_cipherText(vaultFile):
    vf = open(vaultFile, 'r')
    vaultCipherText = vf.readline()

    return vaultCipherText

if __name__ == '__main__':

    vaultCipherText = retrieve_cipherText(vaultFile)
    decryptedText = do_decrypt(vaultCipherText, key)

    print "%s" % (decryptedText)

