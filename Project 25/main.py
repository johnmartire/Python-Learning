alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):   
    encrypted_text = ""  
    for letter in original_text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) + shift_amount) % 26
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += letter
    print(f"Here is the encoded result: ",encrypted_text)  
def decrypt (oringinal_text,shift_amount):
    decrypted_text=""
    for letter in oringinal_text:
        if letter in alphabet:
            new_index=(alphabet.index(letter)- shift_amount)%26
            decrypted_text+= alphabet[new_index]
        else:
            encrypted_text+= letter
    print(f"Here is the Decoded result: ",decrypted_text) 

if direction=='encode':
    encrypt(text, shift)
if direction=='decode':
    decrypt(text,shift)
 