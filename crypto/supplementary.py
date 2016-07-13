# COMP90043 Cryptography and Security
# Geordie Wicks - 185828
# Any enquiries, please email `renlordy[at]unimelb.edu.au`. This code is maintained by Renlord.


# ============== ADD HELPER FUNCTIONS HERE =========================

# ============== END HELPER FUNCTIONS ==============================


def parityWordChecksum(key):
        assert(type(key) == type(1L))
        assert(key < (2 ** 2048))
        """
        parityWordChecksum, takes a 2048 bit key and applies a word by word XOR to yield a 64 bit result at the end. 
        INPUT:
                key, 2048bit Integer from Part A1 Diffie Hellman Key Exchange
        OUTPUT:
                result, 64bit Integer
        """

        total_bits = 2048
        word_bits = 64
        mask = (1 << total_bits) -1
        while total_bits > word_bits:
                total_bits >>= 1
                key ^= (key >> total_bits)
                mask >>= total_bits
                key &= mask
        return key



def deriveSupplementaryKey(key, p):
        assert(type(key) == type(1L))
        assert(type(p) == type(1))
        assert(key < (2 ** 2048))
        assert(p < (2 ** 64))
        """
        deriveSupplementaryKeyA, takes a 2048 bit key and applies the modulo operation to yield the modulo of `p1`. 
        INPUT:
                key, 2048bit Integer from Part A1 Diffie Hellman Key Exchange
                p1, 64bit random prime number
        OUTPUT:
                keyA, 64bit Integer for use as `a` key for Stream Cipher
        """
        # ======== IMPLEMENTATION GOES HERE =========

        subKey = key % p

        # ======== END IMPLEMENTATION ===============
        assert(type(subKey) == type(1) or type(subKey) == type(1L))
        return subKey


# ============== ADD HELPER FUNCTIONS HERE =========================

# ============== END HELPER FUNCTIONS ==============================
