def encryption():
    text=input("Enter plain text: ")
    key=input('Enter the key: ')
    l1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cipher=''
    if len(key)==len(text):
        for i in range(len(text)):
            cipher+=l1[(l1.index(text[i])+l1.index(key[i]))%26]
        print(f'Cipher Text: {cipher}')
    else:
        print('length of key and plain text doesnt match')
        
        
def decryption():
    text=input("Enter cipher text: ")
    key=input('Enter the key: ')
    l1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cipher=''
    if len(key)==len(text):
        for i in range(len(text)):
            cipher+=l1[(l1.index(text[i])-l1.index(key[i]))%26]
        print(f'Plain Text: {cipher}')
    else:
        print('length of key and cipher text doesnt match')
        
