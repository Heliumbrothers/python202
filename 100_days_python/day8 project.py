import os, time, random
os.system('cts' if os.name == 'nt' else 'clear')
for i in range(0, 5):
    print('initializing.')
    time.sleep(0.25)
    os.system('cts' if os.name == 'nt' else 'clear')
    print('initializing..')
    time.sleep(0.25)
    os.system('cts' if os.name == 'nt' else 'clear')
    print('initializing...')
    time.sleep(0.25)
    os.system('cts' if os.name == 'nt' else 'clear')
print('initializing.')
time.sleep(0.25)
os.system('cts' if os.name == 'nt' else 'clear')
print('initializing..')
time.sleep(0.25)
os.system('cts' if os.name == 'nt' else 'clear')
print('initializing...')
time.sleep(0.25)
    
time_wait = int(random.uniform(0.5, 1.5))
time.sleep(time_wait)
os.system('cts' if os.name == 'nt' else 'clear')

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '=', '+', '{', '}', '[', ']', '|', ':', ';', '"', "'", ',', '<', '>', '.', '?', '/', '~', '`', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "encode":
        def encrypt(plain_text, shift_amount):
            cipher_text = ""
            for letter in plain_text:
                position = characters.index(letter)
                new_position = position + shift_amount
                cipher_text += characters[new_position]
            print(f"The encoded text is: {cipher_text}")
    else:
        def decrypt(cipher_text, shift_amount):
            plain_text = ""
            for letter in cipher_text:
                position = characters.index(letter)
                new_position = position - shift_amount
                plain_text += characters[new_position]
            print(f"The decoded text is: {plain_text}")
    if cipher_direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)
    print(f"Here's the {cipher_direction}d result: {end_text}")
repeat = input("Thank you. Would you like to go again? 'yes' or 'no': ")
repeat_bool = repeat.lower() == 'yes'
while repeat_bool:
    cipher_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift, cipher_direction)
    repeat = input("Would you like to go again? 'yes' or 'no': ")
    repeat_bool = repeat.lower() == 'yes'
print("Goodbye! We hope you had a pleasant experience.")