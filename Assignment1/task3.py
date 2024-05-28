
def encrypt(filename):
    text = ''
    with open(filename, 'r') as file:
        text = file.read()
    print(f'Original Content of File: \n\n{text}\n\nEncrypted Text: \n')
    caps_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters = 'abcdefghijklmnopqrstuvwxyz'
    itr = 0
    while (itr < len(text)):
        word = text[itr]
        if word in caps_letters:
            index = caps_letters.index(word)
            index += 3
            if index == len(caps_letters):
                index -= 1
            elif index > len(caps_letters):
                index = 0
            print(caps_letters[index], end='')
        elif word in lower_letters:
            index = lower_letters.index(word)
            index += 3
            if index == len(lower_letters):
                index -= 1
            elif index > len(lower_letters):
                index = 0
            print(lower_letters[index], end='')
        else:
            print(f'{text[itr]}', end='')
        itr += 1
        # print(text)
def main():
    filename = input('Enter a filename or press 1 for default file: ')
    if filename == '1':
        filename = 'task3File.txt'
    try:
        encrypt(filename)
    except Exception as error:
        print('Invalid filename')

if __name__ == '__main__':
    main()