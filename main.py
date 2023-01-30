def getPlaintext():
    plaintext = input('Enter the text you wish to encrypt: ')
    return plaintext

def getN():
    # Need error handling here - must accept an integer [1, 25]
    n = input('Enter the value you would like the characters to be rotated around by: ')
    return n

def encryption(plaintext, n):
    print('Plaintext: [' + plaintext + ']')
    
    # ROT-13 Algorithm
    i = 0
    ciphertext = ""
    # Need to handle upper and lowercase characters, as well as the space character here
    for i in range (len(plaintext)):
        ciphertext = ciphertext + chr(ord(plaintext[i]) + int(n))

    print('Ciphertext: [' + ciphertext + ']')
    return ciphertext

def main():
    plaintext = getPlaintext()
    n = getN()
    encryption(plaintext, n)
    return

main()