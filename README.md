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

In this repository,
 1. keyGenerator.py file asks for 2 prime numbers ( user inputs) & generates 3 output for privateKey, publicKey, & recommended blockSize
    this output is displayed to the user so that s/he may use it for the nextfiles
2. encryptor.py file asks for message, private key ( 2 inputs) & blocksize , allowed characters are a-z & spacebar only, padding will be auto-adjusted incase the blocksize is large. The output will be displayed  to the user so that it can be retireved later.
3. decryptor.py file asks for ciphertext, public key (2 inputs) & blocksize, the numbers that were generated will be converted back into readable text. This output will also been shown to the user.
