class Group:
    def __init__(self, elements, operation, identity):
        self.elements = elements
        self.operation = operation  # A binary operation, e.g., addition, multiplication
        self.identity = identity
    
    # Check closure: all combinations of elements remain within the set
    def check_closure(self):
        for a in self.elements:
            for b in self.elements:
                if self.operation(a, b) not in self.elements:
                    return False
        return True

    # Check associativity: (a * b) * c == a * (b * c)
    def check_associativity(self):
        for a in self.elements:
            for b in self.elements:
                for c in self.elements:
                    if self.operation(self.operation(a, b), c) != self.operation(a, self.operation(b, c)):
                        return False
        return True

    # Check identity: a * e == e * a == a
    def check_identity(self):
        for a in self.elements:
            if self.operation(a, self.identity) != a or self.operation(self.identity, a) != a:
                return False
        return True

    # Check inverse: a * a_inv == a_inv * a == identity
    def check_inverses(self):
        for a in self.elements:
            inverse_exists = False
            for b in self.elements:
                if self.operation(a, b) == self.identity and self.operation(b, a) == self.identity:
                    inverse_exists = True
                    break
            if not inverse_exists:
                return False
        return True

    def is_group(self):
        return self.check_closure() and self.check_associativity() and self.check_identity() and self.check_inverses()


# Example of a group: integers mod n under addition
def add_mod(a, b, n=5):
    return (a + b) % n

# Define a group of integers mod 5
elements = [0, 1, 2, 3, 4]
identity_element = 0  # For addition, the identity is 0
g = Group(elements, lambda a, b: add_mod(a, b, 5), identity_element)

print("Is this a group?", g.is_group())
