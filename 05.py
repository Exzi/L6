def caesar_cipher(text, shift):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphabet_upper = alphabet.upper()
    result = ''
    for char in text:
        if char in alphabet: 
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[new_index]
        elif char in alphabet_upper: 
            new_index = (alphabet_upper.index(char) + shift) % len(alphabet_upper)
            result += alphabet_upper[new_index]
        else:
            result += char  

    return result

message = input("Введите сообщение: ")
k = int(input("Введите сдвиг: "))

encrypted_message = caesar_cipher(message, k)

print("Зашифрованное сообщение:", encrypted_message)