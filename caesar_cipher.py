def encrypt(text, shift):
    result = ""

    # Traverse through the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # For non-alphabetic characters, add them as they are
        else:
            result += char

    return result

# Driver code
if __name__ == "__main__":
    text = input("Enter the text to be encrypted: ")
    shift = int(input("Enter the shift number: "))
    print("Encrypted Text: " + encrypt(text, shift))
