
# COMP90043 Cryptography and Security
# Diffie Hellman Key Exchange Skeleton
#
# Instructions to candidates:
# 	Copy and paste your implementations from Part A1 of the project into this 
# 	component. 

import random

def diffie_hellman_private(numbits):
    """
        diffie_hellman_private

        Returns a private secret integer with `numbits`. 
    """
    private = random.getrandbits(numbits)
    
    return private

# TODO
def diffie_hellman_pair(generator, modulus, private):
    """
        diffie_hellman_pair

        Given a generator, prime modulus and a private integer, produce the public integer.
        Return a tuple of (Private Integer, Public Integer)
    """
    public = modexp(generator, private, modulus)
    public2 = pow(generator, private,modulus)

    
    return (private, public2)

# TODO 
def diffie_hellman_shared(private, public, modulus):
    """
        diffie_hellman_shared

        Given a private integer, public integer and prime modulus.
        Compute the shared key for the communication channel, then return it.
    """
    shared_key = modexp(public, private, modulus)
    shared_key2 = pow(public, private, modulus)
    return shared_key2

def sha(private, public, modulus):

    shared_key = (public ** private) % modulus
    print shared_key

# TODO
def modexp(base, exponent, modulo):

    result = 1
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulo
        exponent = exponent >> 1
        base = (base * base) % modulo
    return result




