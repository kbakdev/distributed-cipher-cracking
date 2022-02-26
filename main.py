import string, multiprocessing, pytest
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

ALLOWED_CHARACTERS = string.printable
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)

def characterToIndex(char):
    return ALLOWED_CHARACTERS.index(char)


def indexToCharacter(index):
    if NUMBER_OF_CHARACTERS <= index:
        raise ValueError("Index out of range.")

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

def findMe(jakisint):
    test = round((len(str(jakisint))/2)-0.5)
    stars = test
    map = {}
    map[0] = 0
    for i in range(test):
        map[i+1] =  (100**(i+1))
    print(map)
    cycles = {}
    buffor = {}
    for i in range(len(cycles)+1):
        buffor[i] = 0
    for i in map:
        cycles[i] = map[i]
    for i in cycles:
        if i != 0:
            cycles[i] = cycles[i] + cycles[i - 1]
    beta = len(cycles)
    for _ in range(len(cycles)):
        beta = beta-1
        buffor[(beta+1)] = cycles[beta]
    cycles = {}
    for i in range(len(buffor)):
        cycles[i] = buffor[i]

    # len(cycles)
    i = len(cycles)

    used = 0
    if jakisint - cycles[i - 1] < 0:
        test = jakisint - cycles[i - 2]
        used = i-2

    if jakisint - cycles[i - 1] > 0:
        test = jakisint - cycles[i - 1]
        used = i - 1

    print(test)
    workString = str(test)
    if len(workString) % 2 == 1:
        workString = "0"+workString

    # if stars
    if used != round(len(workString)/2):
        i =   used - round(len(workString)/2)
        workString = ("00"*(i))+workString


    buffor = []
    if len(workString) > 2:
        i = len(workString)
        for _ in range(round(i/2)):
            i = i-2
            buffor.append(indexToCharacter(int(workString[i] + workString[i+1])))

    if  len(workString) <= 2:
        buffor.append(indexToCharacter(int(workString)))

    if jakisint == cycles[len(cycles)-1]:
        buffor = []
        for _ in range(stars+1):
            buffor.append("0")

    print(buffor)
    return buffor


def codeMe(data, key):
    cipher = DES.new(key=pad(key, 8), mode=DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(data, 8))
    return ciphertext

def deCodeMe(data, key):
    cipher = DES.new(key=pad(key, 8), mode=DES.MODE_ECB)
    ciphertext = cipher.decrypt(pad(data, 8))
    return ciphertext

def begin(pp):

    sequence = next(pp["Sentence"])
    omega = []
    i = 0
    while True:
        buf = ""
        stra = buf.join(sequence)
        key = bytearray(stra, "utf-8")
        textbyte = bytearray(parseMe(deCodeMe(pp["Chipher"], key)), "utf-8")
        if codeMe(textbyte, key) == pp["Chipher"]:

            omega.append("possibility: password = "+textbyte.decode("utf-8")+ "; key = "+ key.decode("utf-8"))
        i = i +1
        sequence = next(sequence)
        if i == pp["StandardMax"]:
            break
    return omega

def prepere(number, chipher):
    buf = []
    for i in range(number):
        bar = {
            "StandardMin": i*100000,
            "StandardMax": ((i+1)*100000)-1,
            "Chipher": chipher,
            "Sentence": [],
        }

        bar["Sentence"] = findMe(bar["StandardMin"])[:]
        buf.append(bar)
    return buf

def prepereOne(number, chipher):
    bar = {
            "StandardMin": number*100000,
            "StandardMax": ((number+1)*100000)-1,
            "Chipher": chipher,
            "Sentence": [],
    }

    bar["Sentence"] = findMe(bar["StandardMin"])[:]

    return bar


if __name__ == '__main__':

    data = "Taj"
    key = "Bet"
    chipher = codeMe(bytearray(data, "utf-8"), bytearray(key, "utf-8"))
    proc = []
    output = {}
    tab = prepere(13, chipher) # (number of structs to check, same)



    p = multiprocessing.Pool(14) # number of proceses


    def test_func_fast():
        pass


    
    print(p.map(begin, tab)) #output

