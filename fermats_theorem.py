# Function to compute (a^b) % p using modular exponentiation
def modular_exponentiation(a, b, p):
    result = 1  # Initialize result
    a = a % p   # Update 'a' if 'a' >= p

    while b > 0:
        # If b is odd, multiply a with the result
        if b % 2 == 1:
            result = (result * a) % p

        # b must be even now
        b = b // 2  # Divide b by 2
        a = (a * a) % p  # Change a to a^2

    return result

# Fermat's Little Theorem function: checks if the theorem holds
def fermats_little_theorem(a, p):
    if p <= 1:
        return False  # p must be prime
    
    # Compute a^(p-1) % p
    result = modular_exponentiation(a, p-1, p)

    # Fermat's theorem: a^(p-1) % p should be 1
    if result == 1:
        return True
    else:
        return False

# Example Usage:
a = int(input("Enter the value of a: "))
p = int(input("Enter the prime number p: "))

if fermats_little_theorem(a, p):
    print(f"Fermat's Little Theorem holds for a = {a} and p = {p}")
else:
    print(f"Fermat's Little Theorem does not hold for a = {a} and p = {p}")
