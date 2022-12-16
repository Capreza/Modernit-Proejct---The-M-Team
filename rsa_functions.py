# import random
#
# from number_theory_functions import generate_prime, extended_gcd, modular_inverse, modular_exponent
#
#
# class RSA:
#     def __init__(self, public_key, private_key=None):
#         self.public_key = public_key
#         self.private_key = private_key
#
#     @staticmethod
#     def generate(digits=10):
#         q = generate_prime(digits)
#         p = generate_prime(digits)
#         n = q * p
#         k = (q - 1) * (p - 1)
#         while True:
#             e = random.randint(1, k)
#             (gcd, x, y) = extended_gcd(e, k)
#             if gcd == 1:
#                 break
#         d = modular_inverse(e, k)
#         return RSA((n, e), d)
#
#     def encrypt(self, m):
#         c = modular_exponent(m, self.public_key[1], self.public_key[0])
#         return c
#
#     def decrypt(self, c):
#         m = modular_exponent(c, self.private_key, self.public_key[0])
#         return m

import number_theory_functions
import random


class RSA():
    def __init__(self, public_key, private_key=None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits=10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        q = number_theory_functions.generate_prime(digits)
        p = number_theory_functions.generate_prime(digits)
        n = q * p
        k = (q - 1) * (p - 1)

        while True:
            e = random.randint(1, k)
            (gcd, x, y) = number_theory_functions.extended_gcd(k, e)
            if gcd == 1:
                break

        d = number_theory_functions.modular_inverse(e, k)
        return RSA((n, e), d)

    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        c = number_theory_functions.modular_exponent(m, self.public_key[1], self.public_key[0])
        return c

    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        m = number_theory_functions.modular_exponent(c, self.private_key, self.public_key[0])
        return m