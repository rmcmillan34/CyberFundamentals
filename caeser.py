# Simple script to encipher/decipher text with a caesar cipher.
# given input key will produce a decryption key
# TODO implement error checking for inputs
# TODO create an encode/decode option

import string

characters = list(string.ascii_uppercase)

def print_title():
    print("\nRyan's Caesar Cipher")
    print("--------------------")


def get_key() -> int:
    print("Enter the key as an iteger",end=": ")
    key = int(input())
    return key


def get_message() -> str:
    print("Enter the message",end=": ")
    message = input()
    message = "".join(message.split())
    return message.upper()


def encode(key: int, message: str):
    encoded_message = []
    for char in message:
        idx = characters.index(char)
        encoded_message.append(characters[(idx+key)%26])

    return "".join(encoded_message)


def get_decode_key(key: int) -> int:
    return (26-key)%26


def main():
    print_title()
    key = get_key()
    message = get_message()
    print(encode(key, message))
    decode_key = get_decode_key(key)
    print(f"Decode key is :{decode_key}\n")


if __name__ == '__main__':
    main()