# Extended Euclidean Algorithm to find the modular inverse of N_i modulo n_i
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Modular inverse of N_i modulo n_i using the extended Euclidean algorithm
def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist for a = {a}, m = {m}")
    else:
        return x % m

# Chinese Remainder Theorem function to solve the system of congruences
def chinese_remainder_theorem(a, n):
    # Step 1: Calculate the product of all n_i (moduli)
    N = 1
    for ni in n:
        N *= ni

    # Step 2: Calculate the solution x
    x = 0
    for i in range(len(a)):
        # N_i = N / n_i
        Ni = N // n[i]

        # Find the modular inverse of N_i modulo n_i
        inv_Ni = mod_inverse(Ni, n[i])

        # Add the contribution to x
        x += a[i] * Ni * inv_Ni

    # Return the solution modulo N
    return x % N

# Example usage
a = [2, 3, 1]  # Remainders
n = [3, 5, 7]  # Moduli

solution = chinese_remainder_theorem(a, n)
print(f"The solution to the system of congruences is: x = {solution}")
