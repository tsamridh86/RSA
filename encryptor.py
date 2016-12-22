# this code changes msg into number and then encrypts into msg

# convert into numbers
def convertToNumber ( string ):
	numberText = []
	for letter in string:
		numberText.append(ord(letter)-32)
	return numberText

#square and multiply method returns
# x = a^b mod n
def squareAndMultiply( base , exponent , divisor ):
	exponent = bin(exponent)[2:]
	d = 1
	for i in exponent:
		d = (d * d) % divisor
		if i == '1':
			d = (d * base) % divisor
	return d

#this function takes plainText in numerical format & encrpyts it using RSA protocol
def encrypt(plainText,privateKey,divisorKey,blockSize):
	i = 0
	lenPlainText = len(plainText)
	numBuff = 0
	cipherText = []
	while i < lenPlainText:
		copyBlockSize = blockSize
		numBuff = 0
		while copyBlockSize > 0:
			if copyBlockSize == blockSize:
				numBuff = plainText[i]
			else:	
				numBuff = numBuff + plainText[i] * 96 ** (blockSize - copyBlockSize)
			copyBlockSize = copyBlockSize - 1
			i = i + 1
		numBuff = squareAndMultiply(numBuff,privateKey,divisorKey)
		cipherText.append(numBuff)
	return cipherText		



plainText = input("Input your plain text message (a-z & space): ")
privateKey = int(input("Enter your private key : "))
divisorKey = int(input("Enter your divisor key : "))
blockSize = int(input("Enter your preferred blockSize : "))
plainText = convertToNumber(plainText)
padding = len(plainText) % blockSize
for i in range(padding):
	plainText.append(32)
#plainText is ready to be encrypted
cipherText = encrypt(plainText,privateKey,divisorKey,blockSize)
print ("Your CipherText : ")
print (cipherText)
