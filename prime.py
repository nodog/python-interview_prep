#

def is_prime(n: int):
    if (n == 0 or n == 1):
        is_prime = False
        print(f'{n} is prime? {is_prime}')
        return is_prime
    elif (n == 2):
        is_prime = True
        print(f'{n} is prime? {is_prime}')
        return is_prime
    else:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                is_prime = False
                print(f'{n} is prime? {is_prime}')
                return is_prime

    is_prime = True
    print(f'{n} is prime? {is_prime}')
    return is_prime


if __name__ == '__main__':
    is_prime(1)
    is_prime(2)
    is_prime(3)
    is_prime(4)
    is_prime(5)
    is_prime(661)
    is_prime(673)
