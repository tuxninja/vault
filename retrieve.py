#!/usr/bin/env python
#vault retrieve.py: Retrieves passwords in secrets.vault
__author__ = 'jriedel'

from Crypto.Cipher import AES
from Crypto import Random
import base64
import argparse
import getpass

# CMD LINE OPTIONS
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', action="store", dest="name", required=True, help="the name of the content to retrieve")
parser.add_argument('-k', '--key', action="store", dest="key", required=False, help="the public key for the encrypted content")
args = parser.parse_args()

# CMD LINE VARS
name = args.name
vaultFile = '.' + str(name)
key = args.key


def do_decrypt(vaultCipherText, key, BS, unpad):
    vaultCipherText = base64.b64decode(vaultCipherText)
    iv = Random.new().read(BS)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    decryptedText = iv + cipher.decrypt(vaultCipherText)

    decryptedText = unpad(decryptedText[32:])

    return decryptedText

def retrieve_cipherText(vaultFile):
    vf = open(vaultFile, 'r')
    vaultCipherText = vf.readline()

    return vaultCipherText

if __name__ == '__main__':
    if not key:
        key = getpass.getpass('Key:')

    BS = 16
    unpad = lambda s : s[:-ord(s[len(s)-1:])]

    vaultCipherText = retrieve_cipherText(vaultFile)
    decryptedText = do_decrypt(vaultCipherText, key, BS, unpad)

    print "%s" % (decryptedText)

