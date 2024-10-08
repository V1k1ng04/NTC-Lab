# Extended Euclidean Algorithm to find gcd and coefficients (x, y)
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Function to solve the Diophantine equation a*x + b*y = c
def solve_diophantine(a, b, c):
    # Step 1: Compute gcd(a, b) and find one particular solution
    gcd, x, y = extended_gcd(a, b)

    # Step 2: Check if the equation has a solution
    if c % gcd != 0:
        print("No solution exists for the given equation.")
        return None

    # Step 3: Scale the solution (x, y) by c / gcd
    x = x * (c // gcd)
    y = y * (c // gcd)

    # Display the particular solution
    print(f"A particular solution to {a}*x + {b}*y = {c} is: x = {x}, y = {y}")
    return x, y

# Example Usage
if __name__ == "__main__":
    # Input values for a, b, and c
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))

    # Solve the Diophantine equation
    solve_diophantine(a, b, c)
