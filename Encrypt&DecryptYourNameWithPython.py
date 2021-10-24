# Encrypt and Decrypt a Name using a combination of the Joints of the Alphabet


def encrypt(name):
    """
    Encrypt a name using the Joints of the Alphabet
    :param name: a string
    :return: a string
    """
    # Initialize the Joints of the Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Initialize the Joints of the Cipher
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    # Initialize the encrypted name
    encrypted_name = ""
    # Loop through the name
    for letter in name:
        # Find the index of the letter in the alphabet
        index = alphabet.find(letter)
        # Add the cipher letter to the encrypted name
        encrypted_name += cipher[index]
    # Return the encrypted name
    return encrypted_name


def decrypt(name):
    """
    Decrypt an encrypted name using the Joints of the Alphabet
    :param name: a string
    :return: a string
    """
    # Initialize the Joints of the Alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Initialize the Joints of the Cipher
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    # Initialize the decrypted name
    decrypted_name = ""
    # Loop through the name
    for letter in name:
        # Find the index of the letter in the cipher
        index = cipher.find(letter)
        # Add the alphabet letter to the decrypted name
        decrypted_name += alphabet[index]
    # Return the decrypted name
    return decrypted_name


def main():
    """
    Test the encrypt and decrypt functions
    """
    # Get the name to encrypt
    name = input("Enter a name to encrypt: ")
    # Encrypt the name
    encrypted_name = encrypt(name)
    # Print the encrypted name
    print("Encrypted name:", encrypted_name)
    # Decrypt the name
    decrypted_name = decrypt(encrypted_name)
    # Print the decrypted name
    print("Decrypted name:", decrypted_name)


# Call the main function
main()


