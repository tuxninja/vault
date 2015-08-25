#!/usr/bin/env python
#vault store.py: Stores passwords in secrets.vault
__author__ = 'jriedel'

from Crypto.Cipher import AES
from Crypto import Random
import argparse
import os.path
import logging
import base64
logging.basicConfig(level=logging.INFO)

# CMD LINE OPTIONS
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', action="store", dest="name", required=True, help="name to store the plainText under")
parser.add_argument('-t', '--text', action="store", dest="plainText", required=True,
                    help="clear plainText plainText to store, make sure you use quotes for things with spaces.")
parser.add_argument('-k', '--key', action="store", dest="key", required=True,
                    help="Specify a key 16, 24 or 32 bytes")
parser.add_argument('-f', '--force', action="store_true", dest="force", required=False,
                    help="Overwrite an existing name stored")
args = parser.parse_args()

# CMD LINE VARS
name = args.name
vaultFile = '.' + str(name)
plainText = args.plainText
key = args.key
force = args.force

def do_encrypt(plainText, key, BS, pad):
    plainText = pad(plainText)
    iv = Random.new().read(BS)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    cipherText = iv + cipher.encrypt(plainText)

    return base64.b64encode(cipherText)

def name_check(name):
    if ' ' in name:
        msg = "Sorry names cannot have spaces."
        logging.error(msg)
        success = False
    elif "'" in name:
        msg = "Sorry names cannot have quotes."
        logging.error(msg)
        success=False
    else:
        success=True

    return success

def store_data(cipherText):
    vf = open(vaultFile, 'w')
    line = "%s" % (cipherText)
    vf.write(line)
    vf.close()

    print "%s was stored as %s" % (cipherText, name)

if __name__ == '__main__':

    BS = 16
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    cipherText = do_encrypt(plainText, key, BS, pad)

    success = name_check(name)
    if success:
        if not force and os.path.isfile(vaultFile):
            msg = "Sorry an entry was already stored for %s, please try another name or re-run with -f to force an overwrite." % (name)
            logging.error(msg)
        else:
            store_data(cipherText)