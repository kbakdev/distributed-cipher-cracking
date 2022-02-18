from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

from rich.console import Console
from rich.table import Table

import platform
import sys
import psutil

import string, time

ALLOWED_CHARACTERS = string.printable
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)

KEY = "KEY"
DATA = "DATA"

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

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
                print(f"Python Version: %s" % (platform.python_version()))

                # SYSTEM INFORMATION
                print("\nSystem Information")
                uname = platform.uname()
                print(f"System: {uname.system}")
                print(f"Release: {uname.release}")
                print(f"Version: {uname.version}")
                print(f"Processor: {uname.processor}")

                # CPU INFORMATION
                print("\nCPU Info")
                print("Physical cores:", psutil.cpu_count(logical=False))
                print("Total cores:", psutil.cpu_count(logical=True))
                cpufreq = psutil.cpu_freq()
                print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
                print(f"Total CPU Usage: {psutil.cpu_percent()}%")

                # MEMORY INFORMATION
                print("\nMemory Information")
                # get the memory details
                svmem = psutil.virtual_memory()
                print(f"Total: {get_size(svmem.total)}")
                print(f"Available: {get_size(svmem.available)}")
                print(f"Used: {get_size(svmem.used)}")
                print(f"Percentage: {svmem.percent}%")

                # SWAP INFORMATION
                print("\nSWAP")
                # get the swap memory details (if exists)
                swap = psutil.swap_memory()
                print(f"Total: {get_size(swap.total)}")
                print(f"Free: {get_size(swap.free)}")
                print(f"Used: {get_size(swap.used)}")
                print(f"Percentage: {swap.percent}%")
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