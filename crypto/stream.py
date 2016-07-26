
# COMP90043 Cryptography and Security
# Geordie Wicks - 185828

from supplementary import *
from dhex import *
from base64 import b64encode, b64decode 

# ============== ADD HELPER FUNCTIONS HERE =========================

# Helper function to take number and return a 8 bit binary string
# Padded to ensure leading zero's are retained.

def binary(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i >>= 1
    c = int(s)
    l = format(c, '008')
    return l

# ============== END HELPER FUNCTIONS ==============================

class StreamCipher:
    # TODO
    def __init__(self, dh_key, dh_p, p1, p2):
        """
        __init__, constructor for StreamCipher class.
        INPUT:
            dh_key, 2048bit DH Key from Part A1
            p, DH Key Parameter, Prime Modulus
        OUTPUT:
            returns an instantiated StreamCipher object
        """
      
        self.dh_key = dh_key #dh_key # 2048bit DH Key from Part A1
        
        self.dh_p = dh_p # DH Key Parameter, Prime Modulus
        
        self.a =  deriveSupplementaryKey(dh_key, p1) # Supplementary Key A for Stream Cipher
        self.b = deriveSupplementaryKey(dh_key, p2) # Supplementary Key B for Stream Cipher
        self.r_i = parityWordChecksum(dh_key) # Shift Register
        
   
    # =============== ADD CLASS ADDITIONAL METHODS ==================


    # =============================================================
    
    # Most significant Byte function.
    # Input integer, return 8 leading bytes, padding to ensure leading
    # zeros are retained.
    
    def msb(self,i):
        a = binary(i)
        b = a[0:8]
        c = int(b)
        l = format(c, '008')

        return l
    
    # =============== END CLASS ADDTIONAL METHODS ===================

    # TODO
    def updateShiftRegister(self):
        """
        updateShiftRegister, updates the shift register for XOR-ing the next 
        byte.
        INPUT:
            nothing
        OUTPUT:
            nothing
        """
    
        
        r_new = (self.a*self.r_i +self.b) % self.dh_p
        self.r_i = r_new

    
        return None

    # TODO
    def _crypt(self, msg):
        assert(type(msg) == type("hello"))
        """
        _crypt, takes a cipher text/plain text and decrypts/encrypts it.
        INPUT:
        
            msg, either Plain Text or Cipher Text.
        OUTPUT:
            new_msg, if PT, then output is CT and vice-versa.
        """
    

        # Takes a binary input xor's it with shift register and then outputs a binary
        
        msb_num = self.msb(self.r_i)                               # Get most significant byte of Shift
        new_msg = int(msg,2) ^ int(msb_num,2)           # Perform XOR
        self.updateShiftRegister()                           # update the Shift Register

      
        return new_msg

    # TODO
    def reset(self):
        """
        reset, resets the shift register back to its initial state.
        INPUT:
            nothing
        OUTPUT:
            nothing
        """
       
        # reset shift Register to original
        self.r_i = parityWordChecksum(self.dh_key)
       
        return None

    # =============== ADD CLASS ADDITIONAL METHODS ==================
    def encrypt(self,msg):
        
        ciphertext = ""                             # cipher text string
        cipherb64 = ''                              # Cipher b64 string
        
        for x in range(len(msg)):                   # Loop over message
            integer = ord(msg[x])                   # Convert char to ACHII int
            binary_rep = binary(integer)            # Convert to binary 
            cipher_binary = self._crypt(binary_rep)      # Perform XOR encryption
            cipher_char = chr(cipher_binary)        # Convert Binary to char
            ciphertext = ciphertext + cipher_char   # Add to ciphertext String
            now =  b64encode(cipher_char)           # Encode to B64
            cipherb64 = cipherb64 + now
  
        ciphertext1 = b64encode(ciphertext)
        another = b64encode(ciphertext1)
        #reset()                                     # Reset Shift Register
        return another                              # Return ciphertext b64 string

    def decrypt(self,msg):

        plaintext = ''
        decode = b64decode(msg)                     # Decode b64
        decode2 = b64decode(decode)
        for x in range(len(decode2)):               # Loop of message
            integer = ord(decode2[x])               # Convert char to int
            binary_rep = binary(integer)            # Get Binary representation
            cipher_binary = self._crypt(binary_rep)      # Perform XOR
            cipher_char = chr(cipher_binary)        # Convert to Char
            plaintext = plaintext + cipher_char
            now = b64encode(cipher_char)
    
        return plaintext                            # Return Plaintext

    # =============================================================
    
    # Most significant Byte function.
    # Input integer, return 8 leading bytes, padding to ensure leading
    # zeros are retained.
    ''' 
    def msb(i):
        a = binary(i)
        b = a[0:8]
        c = int(b)
        l = format(c, '008')

        return l
        '''
    # =============== END CLASS ADDTIONAL METHODS ===================

# ============== ADD HELPER FUNCTIONS HERE =========================

# ============== END HELPER FUNCTIONS ==============================

