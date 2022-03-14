import string, multiprocessing, time, sys, file
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
#initials
ALLOWED_CHARACTERS = string.printable
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)



#Classes
class findings:
    def __init__(self):
        self.password = 0
        self.key = 0
        self.i = 0
        self.time = 0

class frame:
    def __init__(self):
        self.name = ""
        self.i = 0
        self.len = 0
        self.objects = []

    def lenMe(self):
        self.len = len(self.objects)

    def boutMe(self):
        print("My name is range: ("+self.name+")")
        print("Number of my findigs is:"+str(self.len))
        print("My ID is: "+str(self.i))



#Helper functions
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

    return buffor

def sortMe(list):
    bufor = []
    min = 1000000000000000000000000000
    max = 0
    for record in list:
        if record.i < min:
            min = record.i
        if record.i > max:
            max = record.i

    if min == max:
        min = 0

    for i in range(min, max+1):
        for record in list:
            if record.i == i:
                bufor.append(record)
    return bufor

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
    i = pp["StandardMin"]
    while True:
        buf = ""
        stra = buf.join(sequence)
        key = bytearray(stra, "utf-8")
        textbyte = bytearray(parseMe(deCodeMe(pp["Chipher"], key)), "utf-8")
        if codeMe(textbyte, key) == pp["Chipher"]:
            record = findings()
            record.i = i
            record.password = textbyte.decode("utf-8")
            record.key = key.decode("utf-8")
            record.time = str(time.time() - pp["TimeStamp"])
            omega.append(record)
        i = i +1
        sequence = next(sequence)
        if i == pp["StandardMax"]:
            break

    fr = frame()
    fr.name = (str(pp["StandardMin"]) +" : " + str(pp["StandardMax"]))
    fr.objects = omega[:]
    fr.lenMe()
    fr.i = round(pp["StandardMax"]/100000)
    return fr

def prepere(ran, number, chipher):
    buf = []
    ts = time.time()

    for i in range(ran, number):
        bar = {
            "ID" : str(i),
            "StandardMin": i*100000,
            "StandardMax": ((i+1)*100000)-1,
            "Chipher": chipher,
            "Sentence": findMe(i*100000)[:],
            "TimeStamp" : ts,
        }

        buf.append(bar)
    return buf




if __name__ == '__main__':
    startTimeProgram = time.time()
    #Base info
    data = "0"
    key = "0"
    numberOfCycles = 1
    ran = 0
    #Options by terminal
    if len(sys.argv) > 1:
        data = sys.argv[1]
        key = sys.argv[2]
        numberOfCycles = int(sys.argv[3])
        if sys.argv[4] != "" and sys.argv[3] != "":
            if int(sys.argv[4]) < int(sys.argv[3]):
                ran = int(sys.argv[4])
            else:
                ran = int(sys.argv[3])

    coreNumber = multiprocessing.cpu_count()


    chipher = codeMe(bytearray(data, "utf-8"), bytearray(key, "utf-8"))
    tab = prepere(ran, numberOfCycles, chipher)
    p = multiprocessing.Pool(coreNumber)

    outputList = p.map(begin, tab)
    '''
    output Structure:
    
    outputList list -> frame class obj
    frame struct:
        name string #The interval in which the process operated.
        len #Number of results
        objects list -> findings class obj #Stores the results of an interval
     
    findings class obj:
        password #Likely password
        key #Likely key
        i #loop number
        time #Current time to find the record
    '''

    sortlist = sortMe(outputList)
    print("Done, check benchmarks -> v0.0.4")
    file.save(str(time.time() - startTimeProgram),sortlist)


