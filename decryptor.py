# this code converts cipher text into msg & displays it to the user

# this functions converts the cipherText into number format plainText
def decrypt( cipherText, publicKey, divisorKey , blockSize):
	i = 0
	lenCipherText = len(cipherText)
	plainText = []
	while i < lenCipherText:
		copyBlockSize = blockSize
		numArr = []
		numBuff = pow(cipherText[i],publicKey,divisorKey)
		while copyBlockSize > 0:
			numArr.append(numBuff%96)
			copyBlockSize = copyBlockSize - 1
			numBuff = numBuff // 96
		for j in range(blockSize):
			plainText.append(numArr[j])
		i = i + 1
	return plainText

# this is the reverse of the text to number converter that is used in the encryptor
def convertIntoText( numericText ):
	string = []
	for number in numericText:
		string.append(chr(number+32))
	string = ''.join(string)
	return string

#take input from the cipherText.txt 
cipherTextFile = open("cipherText.txt","r")
cipherText = [int(x.strip("\n")) for x in cipherTextFile.readlines()]
cipherTextFile.close()
publicKey = int(input("Enter public key : "))
divisorKey = int(input("Enter divisor key : "))
blockSize = int(input("Enter preffered blockSize : "))
plainText = decrypt(cipherText,publicKey,divisorKey,blockSize)
plainText = convertIntoText(plainText)
print ("Your PlainText : ")
print (plainText)
plainTextFile = open("plainText.txt","w")
plainTextFile.write(plainText)
plainTextFile.close()