alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def encrypt(text, shift):
    new_text = ''
    max_length = len(alphabet) - 1
    for c in text:
        shift_index = alphabet.index(c) + shift
        if shift_index > max_length:
            shift_index = shift_index - max_length
        new_text += alphabet[shift_index]
    return new_text

def decrypt(text, shift):
    new_text = ''
    for c in text:
        shift_index = alphabet.index(c) - shift
        if shift_index < 0:
            shift_index = shift_index + (len(alphabet) - 1)
        new_text += alphabet[shift_index]
    return new_text

exit = True

print(logo)

while exit:
    option = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if option != 'encode' and option != 'decode':
        exit = False
        print("Option not supported. Exiting now..")
    else:
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        if option == 'encode':
            print(encrypt(text, shift))
        else:
            print(decrypt(text, shift))
