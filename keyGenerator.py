# RSA Cryptosystem:
# how it works:
# 1. choose two prime numbers p & q
# 2. find n = pq
# 3. compute phi = (p-1)(q-1)
# 4. choose e, such that  1 < e < phi , but gcd(e,phi) = 1
# 5. d = e inv mod phi
# 6. public key = e , n ; private key = d, n
# target is to transfer one msg to another using suitable block size
# in this code, characters a-z & space is allowed
# code starts here

# imports
from random import randrange
from math import floor

# returns 0 if the number is prime , returns 1 otherwise
def checkPrime ( num ):
	if num < 2:
		return 1
	for i in range (2, num):
		if num%i == 0 :
			return 1
	return 0

# returns an appropiate block size for the code
def getBlockSize ( num ):
	size = 0
	series = 0
	while num - series > 0 :
		size = size + 1
		series = series + pow(27,size)
	return size-1

# euclid's algorithm to compute gcd of two numbers
def gcd (a, b):
	if b == 0 :
		return a
	else :
		return gcd(b,a%b)	

#extended euclid's algorithm, returns 3 values, gcd , x & y
def extendedEuclid(a , b):
	if b == 0 :
		return (a,1,0)
	else:
		d1 , x1, y1 = extendedEuclid(b, a%b)
		d,x,y = d1, y1, x1 - floor(a/b) * y1
		return d,x,y	

#this function ins used to calculate modulo using extended euclid's algorithm
def getModuloInverse ( a, b ):
	x, y, z = extendedEuclid(a,b)
	# only y is needed, discard the rest
	# if it is positive, send back else subtract from phi
	if y > 0 :
		return y
	else :
		#y is already -ve so minus minus would be plus
		return b + y	


# main code execution begins here
# get 2 prime numbers & make sure they are prime
notPrime = 1
while(notPrime):
	p = int(input("Enter the first prime number : "))
	notPrime = checkPrime(p)
notPrime = 1
while(notPrime):
	q = int(input("Enter the second prime number : "))
	notPrime = checkPrime(q)

# compute n & phi
n = p * q
phi = (p-1) * (q-1)

#get a random number e such that 1<e<phi, but gcd(e,phi) == 1
e = randrange(2,phi)
while gcd (e, phi) != 1 :
	e = randrange(1,phi)	

#compute d = e inv mod phi
d = getModuloInverse(e,phi)

# compute suitable blocksize
blockSize = getBlockSize(n)
if blockSize < 1 :
	exit()

#completed, display output
print ("public key : ",e," , ",n)
print ("private key : ",d," , ",n)
print ("preferable blockSize : ",blockSize)
