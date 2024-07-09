Plain_text = input ('Enter a Text:')
key = int (input ('Enter a key: '))
for letter in Plain_text:
    if(ord(letter)>96 and ord(letter)<123):
        cipher = (ord(letter) + key)
        cipher = cipher - 97
        cipher = cipher % 26
        cipher = cipher + 97
        print(chr(cipher), end = '')
    elif(ord(letter)>64 and ord(letter)<91):
        cipher = (ord(letter) + key)
        cipher = cipher - 65
        cipher = cipher % 26
        cipher = cipher + 65
        print(chr(cipher), end = '')

Plain_text = input ('  write:')
key = -int (input ('Enter a key: '))
for letter in Plain_text:
    if(ord(letter)>96 and ord(letter)<123):
        cipher = (ord(letter) + key)
        cipher = cipher - 97
        cipher = cipher % 26
        cipher = cipher + 97
        print(chr(cipher), end = '')
    elif(ord(letter)>64 and ord(letter)<91):
        cipher = (ord(letter) + key)
        cipher = cipher - 65
        cipher = cipher % 26
        cipher = cipher + 65
        print(chr(cipher), end = '')

