#Vault

Vault is a simple command line utility for storing & retrieving AES encrypted data. 

### Clone
	git clone https://github.com/tuxninja/vault.git

### Usage 

	➜  vault  python store.py --name root --text 'boobs are better than newbs' -k '01234567890987654321abcdefghijkl'
	?;_mjd?{?j?&:x?fr????*"!?!??I??J?o?Y?? was stored as root
	➜  vault  python retrieve.py --name root -k '01234567890987654321abcdefghijkl'
	boobs are better than newbs
	➜  vault  
