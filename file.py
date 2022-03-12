import datetime

def initial(info):
    listoffindings = []
    for record in info:
        if record.len != 0:
            for findings in record.objects:
                listoffindings.append(findings)

    return listoffindings


def save(endtime, list):
    currentDT = datetime.datetime.now()
    timeF = currentDT.strftime("%Y-%m-%d")
    time = currentDT.strftime("%H:%M:%S")
    file = open("benchmarks/v0.0.3/"+timeF+"_"+time+".txt", "w")
    bufor = initial(list)
    file.writelines("Time of this test: "+time+'\n')
    file.writelines("Run time: "+endtime + '\n')
    for record in bufor:
        file.writelines("Password: "+record.password+'\n')
        file.writelines("Key: "+record.key+'\n')
        file.writelines("LoopUnit: "+str(record.i)+'\n')
        file.writelines("Time of test: "+record.time+'\n')

    file.close()