import random

from exponent import power, fast_pow


def find_integers_for_prime_testing(n):
    # n >= 3
    q = (n-1)
    k = 0
    while True:
        q = q // 2
        k += 1
        if q % 2 == 1:
            return (k, q)

    return (-1, -1)


def is_prime(n):
    if n == 2:
        return True
    (k, q) = find_integers_for_prime_testing(n)
    a = random.randint(2, n-2)
    print("n: %d" % n)
    print("k: %d" % k)
    print("q: %d" % q)
    print("a: %d" % a)
    if power(a, q, n) == 1:
        return True
    for j in range(0, k-1):
        if power(a, fast_pow(2, j)*q, n) == n-1:
            return True

    return False
