FIRST_CHAR = ord("A")
LAST_CHAR = ord("Z")
RANGE = LAST_CHAR - FIRST_CHAR + 1


def caesar_cipher(message, shift):
 
    result = ""

    for char in message.upper():
        if char.isalpha():
           
            char_code = ord(char)
            new_char_code = char_code + shift

            if new_char_code > LAST_CHAR:
                new_char_code -= RANGE

            if new_char_code < FIRST_CHAR:
                new_char_code += RANGE

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char

    return result


user_message = input("Message to Encrypt: ")
shift = 5
cipher_text = caesar_cipher(user_message, shift)
print(f"Cipher Text: {cipher_text}")# add your code here
