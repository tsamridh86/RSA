# RSA
This is a public key Crytpography method:

#how it works:
 1. choose two prime numbers p & q
 2. find n = pq
 3. compute phi = (p-1)(q-1)
 4. choose e, such that  1 < e < phi , but gcd(e,phi) = 1
 5. d = e inv mod phi
 6. public key = e , n ; private key = d, n
 Then we can choose a preferable block size & use it to encrypt the messages.
 
 #encryption
  ciphertext = plaintext ^ privateKey modulo n
  
  #decryption 
    plaintext = ciphertext ^ publicKey modulo n

#choosing of blocksize
 consider the number of possible characters that are being encrypted,
 currently, since, we are using all printable ascii characters, there are 95 of them
 hence the divisor should be atleast 96.
 for blocksize 2, divisor should be greater that, 96 + 96^2
 similarly, a larger blocksize can be estimated:
  blocksize <= n,
  where,
  96 + 96^2 + 96^3 + ... + 96^n < divisorKey

In this repository,
 1. keyGenerator.py file asks for 2 prime numbers ( user inputs) & generates 3 output for privateKey, publicKey, & recommended blockSize
    this output is displayed to the user so that s/he may use it for the nextfiles
2. encryptor.py uses the message present in plainText.txt , private key ( 2 inputs) & blocksize , only printable ascii charaters maybe used, padding will be auto-adjusted incase the blocksize is large. The output will be displayed to the user so that it can be retireved later, also it will be automaticaly written in cipherText.txt file for easier use on larger file.
3. decryptor.py file uses the message present in cipherText.txt, public key (2 inputs) & blocksize, the numbers that were generated will be converted back into readable text. This output will also been shown to the user & will be written into plainText.txt for eaiser use on later purposes.
