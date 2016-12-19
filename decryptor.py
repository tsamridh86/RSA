# this code converts cipher text into msg & displays it to the user

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

# this functions converts the cipherText into number format plainText
def decrypt( cipherText, publicKey, divisorKey , blockSize):
	i = 0
	lenCipherText = len(cipherText)
	plainText = []
	while i < lenCipherText:
		copyBlockSize = blockSize
		numArr = []
		numBuff = squareAndMultiply(cipherText[i],publicKey,divisorKey)
		while copyBlockSize > 0:
			numArr.append(numBuff%27)
			copyBlockSize = copyBlockSize - 1
			numBuff = numBuff // 27
		for j in range(blockSize):
			plainText.append(numArr[j])
		i = i + 1
	return plainText

# this is the reverse of the text to number converter that is used in the encryptor
def convertIntoText( numericText ):
	string = []
	for number in numericText:
		if number == 26 :
			string.append(chr(32))
		else:
			string.append(chr(number+97))
	string = ''.join(string)
	return string

#take input from the use, stop when a -ve number is inserted
cipherText = []
getInput = 1
while getInput > 0 :
	getInput = int(input("Enter cipherText (-ve number to stop input) : "))
	cipherText.append(getInput)
cipherText.pop()
publicKey = int(input("Enter public key : "))
divisorKey = int(input("Enter divisor key : "))
blockSize = int(input("Enter preffered blockSize : "))
plainText = decrypt(cipherText,publicKey,divisorKey,blockSize)
plainText = convertIntoText(plainText)
print ("Your PlainText : ")
print (plainText)