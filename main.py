from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

from rich.console import Console
from rich.table import Table

import string, time

ALLOWED_CHARACTERS = string.printable
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)

KEY = "KEY"
DATA = "DATA"

def characterToIndex(char):
    return ALLOWED_CHARACTERS.index(char)

def indexToCharacter(index):
    if NUMBER_OF_CHARACTERS <= index:
        raise ValueError("Index out of range.")
    
    return ALLOWED_CHARACTERS[index]

# The function takes the next list from the interval
def n(s_list):

    if len(s_list) <= 0:
        s_list.append(indexToCharacter(0))
    else:
        s_list[0] = indexToCharacter((characterToIndex(s_list[0]) + 1) % NUMBER_OF_CHARACTERS)
        if characterToIndex(s_list[0]) == 0:
            return list(s_list[0]) + n(s_list[1:])
    return s_list


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

def decodeMe(data, key):
    cipher = DES.new(key=pad(key, 8), mode=DES.MODE_ECB)
    ciphertext = cipher.decrypt(pad(data, 8))
    return ciphertext

def main(data, key):
    sequence = []
    cipher = codeMe(bytearray(data,"utf-8"),bytearray(key,"utf-8"))
    table = Table(title="DISTRIBUTED CIPHER CRACKING")
    table.add_column("SECONDS", justify="right", style="cyan", no_wrap=True)
    table.add_column("POSSIBLE PASSWORD", style="magenta")
    table.add_column("KEY", justify="right", style="green")
    while True:
        sequence = n(sequence)
        buf = ""
        stra = buf.join(sequence)
        key = bytearray(stra, "utf-8")
        textbyte = bytearray(parseMe(decodeMe(cipher, key)), "utf-8")
        if codeMe(textbyte, key) == cipher:
            table.add_row("%s" % (time.time() - start_time), textbyte.decode("utf-8"), key.decode("utf-8"))
            if key.decode("utf-8") == KEY:
                # table.add_row("%s" % (time.time() - start_time), textbyte.decode("utf-8"), key.decode("utf-8"))
                console = Console()
                console.print(table)
                break
        
        #    print("- %s seconds -" % (time.time() - start_time))
        #    print("Possible: password",textbyte.decode("utf-8"),"key", key.decode("utf-8"))
        #    if key.decode("utf-8") == KEY:
        #         print("- %s seconds -" % (time.time() - start_time))
        #         print("KEY: ",key.decode("utf-8"))
        #         break


if __name__ == "__main__":
    start_time = time.time()
    main(DATA, KEY)