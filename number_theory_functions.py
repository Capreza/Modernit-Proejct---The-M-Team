from random import randrange

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x, y = extended_gcd(b, a % b)
    q = a // b
    return gcd, y, x - q * y


def modular_inverse(a, n):
    gcd, x, y = extended_gcd(a, n)
    if gcd != 1:
        return None
    return x % n


def modular_exponent(a, d, n):
    res = 1
    m = 1
    tmp = a % n
    while d >= 1:
        if d % 2 == 1:
            res *= tmp % n
            res = res % n
        d = d >> 1
        m *= 2
        tmp = (tmp ** 2) % n
    return res % n


def miller_rabin(n):
    a = randrange(1, n)
    k = 0
    d = n - 1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True


def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10 ** (digits - 1), 10 ** digits)
        if is_prime(n):
            return n
    return None
