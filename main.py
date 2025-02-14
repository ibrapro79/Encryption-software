import json

def decodeChar(char:str, jsonData:dict):
    text = ''
    for i in range(0,int(len(char) / 5)):
        for j in jsonData:
            if jsonData[j] == char[i*5:(i+1)*5]:
                text = text + j
    return text
def encodeChar(text:str, jsonData:dict):
    char = ''
    for i in text:
        char = char + jsonData[i]
    return char
jsonData = json.loads(open('data.json').read())

print('''Commands:
    encode: Encode the text in <text.txt>
    decode: Decode the text
    exit: Exit the program''')
while True:
    command = input('>>')
    if command == 'encode':

        print('Entre the text in <text.txt> to encode')
        print("Complete? [y]",end=' ')
        if input() == 'y':
            text = open('text.txt')
            print("\n----------------------------------------------\n" + encodeChar(text.read(),jsonData) + "\n----------------------------------------------\n")

    elif command == 'decode':
        textDecoded = input('Entre the text to decode: ')
        print("\n----------------------------------------------\n" + decodeChar(textDecoded,jsonData) + "\n----------------------------------------------\n")
    elif command == 'exit':
        break

