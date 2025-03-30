# /utils/rsa_utils.py
import random
import hashlib


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime(n, k=5):
    if n <= 1 or n % 2 == 0:
        return False
    if n == 2 or n == 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True


def generate_prime(start, end):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p


def generate_keys(file_path):
    p = generate_prime(10**100, 10**150)  # Large primes for security
    q = generate_prime(10**100, 10**150)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = pow(e, -1, phi)

    with open(f"{file_path}/public_key.txt", "w") as pub_file:
        pub_file.write(f"{e}\n{n}")

    with open(f"{file_path}/private_key.txt", "w") as priv_file:
        priv_file.write(f"{d}\n{n}")


def hash_message(message):
    return int.from_bytes(hashlib.sha256(message.encode()).digest(), 'big')
