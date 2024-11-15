# add your code here

def caesar_cipher(text, shift):
    result = " "
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result
text = input("Please enter a sentence: ")
shift = 5
encrypted_text = caesar_cipher(text, shift)
print("Encrypted:", encrypted_text)