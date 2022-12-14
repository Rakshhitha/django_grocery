from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import algorithms
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from base64 import b64encode, b64decode

"""
The encrypt method receives the plain_text to be encrypted. 
First we pad that plain_text in order to be able to encrypt it. 
After we assign key to iv with the size of an AES block, 128bits. 
We now create our AES cipher with AES.new with our key, in mode CBC and \
    with our just generated iv. 
We now invoke the encrypt function of our cipher, passing it our plain_text converted to bits. 
The encrypted output is then placed after our iv and \
    converted back from bits to readable characters.
"""
"""
In order to decrypt, we must backtrack all the steps done in the encrypt method. 
First we convert our encrypted_text to bits and extract the iv, 
which will be the first 128 bits of our encrypted_text. 
Much like before, we now create a new AES cipher with our key, 
in mode CBC and with the extracted iv. We now invoke the decrypt method of our cipher and 
convert it to text from bits. We remove the padding with __unpad and that’s it!
"""

class AesCrypto(object):
    def __init__(self, key):
        self.key = key.encode('utf-8')[:16]
        self.iv = self.key
        self.block_size = AES.block_size
        self.mode = AES.MODE_CBC

    @staticmethod
    def pkcs7_padding(data):
        if not isinstance(data, bytes):
            data = data.encode()
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()
        return padded_data
    
    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text
    

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        bytes_to_remove = ord(last_character)
        return plain_text[:-bytes_to_remove]

    def encrypt(self, plaintext):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plaintext = self.__pad(plaintext)
        ciphertext = cryptor.encrypt(plaintext.encode())
        return b64encode(ciphertext).decode('utf-8')

    def decrypt(self, ciphertext):
        ciphertext = b64decode(ciphertext)
        cryptor = AES.new(self.key, self.mode, self.iv)
        plaintext = cryptor.decrypt(ciphertext).decode("utf-8")
        return self.__unpad(plaintext)

    def web_encrypt(self, plaintext):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plaintext = self.__pad(plaintext)
        ciphertext = cryptor.encrypt(plaintext.encode())
        # return b64encode(ciphertext).decode('utf-8')
        return (ciphertext).decode('utf-8')


# aes = AesCrypto('ddfbccae-b4c4-11')
# aes = AesCrypto('(1#p1r1xt_^%2-)yc=$6f+olxszb1xzmm_phx_#bnt&nn)j!c7')
# encrypted = aes.encrypt('Congratulations, 123, gooood! ')
# print(encrypted)
# decrypted = aes.decrypt(encrypted)
# print(decrypted)