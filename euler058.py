def is_prime(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

def get_corners_for_size(s):
    c_1 = (s - 2) ** 2 + 1 + (s - 2)
    c_2 = c_1 + (s - 1)
    c_3 = c_2 + (s - 1)
    c_4 = c_3 + (s - 1)
    return c_1, c_2, c_3, c_4


num_corners = 1
num_primes = 0
ratio = 1
i = 3
while ratio >=  0.1:

    corners  = get_corners_for_size(i)

    for corner in corners:
        num_corners += 1
        if is_prime(corner):
            num_primes += 1

    ratio = num_primes / num_corners
    print(f"Size {i}, ratio {num_primes}/{num_corners} | {ratio}")
    i += 2

