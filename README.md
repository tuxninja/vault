#Vault

Vault is a simple command line utility for storing & retrieving AES encrypted data. 

### Clone
	git clone https://github.com/tuxninja/vault.git

### Usage 

	➜  vault git:(master) python store.py --name tuxlabs --text 'boobs are better than newbs' --key 01234567890987654321abcdefghijkl 
	OYBD5YmuaBEorgFeuUjDdcR/A1fDOQxu3oFEiCTwNJPV0b0gg1StVqtn/87orx/P was stored as tuxlabs

	➜  vault git:(master) ✗ python retrieve.py --name tuxlabs --key 01234567890987654321abcdefghijkl
	boobs are better than newbs
	➜  vault git:(master) ✗ 
