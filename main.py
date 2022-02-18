from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


import string, time
ALLOWED_CHARACTERS = string.printable
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)

def characterToIndex(char):
    return ALLOWED_CHARACTERS.index(char)

def indexToCharacter(index):
    if NUMBER_OF_CHARACTERS <= index:
        raise ValueError("Index out of range.")
    else:
        return ALLOWED_CHARACTERS[index]

def next(string):

    if len(string) <= 0:
        string.append(indexToCharacter(0))
    else:
        string[0] = indexToCharacter((characterToIndex(string[0]) + 1) % NUMBER_OF_CHARACTERS)
        if characterToIndex(string[0]) == 0:
            return list(string[0]) + next(string[1:])
    return string


def parseMe(array):
    buf = []
    for a in array:
        try:
            characterToIndex(chr(a))
            buf.append(chr(a))
        except:
            break
    return "".join(buf)



def codeMe(data, key):
    cipher = DES.new(key=pad(key, 8), mode=DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(data, 8))
    return ciphertext

def deCodeMe(data, key):
    cipher = DES.new(key=pad(key, 8), mode=DES.MODE_ECB)
    ciphertext = cipher.decrypt(pad(data, 8))
    return ciphertext


def main(data, key):
    sequence = list()
    chipher = codeMe(bytearray(data,"utf-8"),bytearray(key,"utf-8"))
    # testdecode = deCodeMe(chipher, bytearray(key,"utf-8"))
    # print(testdecode)
    while True:
        sequence = next(sequence)
        buf = ""
        stra = buf.join(sequence)
        key = bytearray(stra, "utf-8")
        textbyte = bytearray(parseMe(deCodeMe(chipher, key)), "utf-8")
        if codeMe(textbyte, key) == chipher:
           print("--- %s seconds ---" % (time.time() - start_time))
           print("possibility: password",textbyte.decode("utf-8"),"key", key.decode("utf-8"))

if __name__ == "__main__":
    start_time = time.time()
    key = "kod0"
    data = "taja"
    main(data, key)


