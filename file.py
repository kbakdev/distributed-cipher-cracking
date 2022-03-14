import datetime
import platform
import psutil

def initial(info):
    listoffindings = []
    for record in info:
        if record.len != 0:
            for findings in record.objects:
                listoffindings.append(findings)

    return listoffindings

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

def save(endtime, list):
    currentDT = datetime.datetime.now()
    timeF = currentDT.strftime("%Y-%m-%d")
    time = currentDT.strftime("%H:%M:%S")
    file = open("benchmarks/v0.0.4/"+timeF+"_"+time+".txt", "w")
    bufor = initial(list)
    file.writelines(f"Python Version: %s\n" % (platform.python_version()))

    # SYSTEM INFORMATION
    file.writelines("\nSystem Information\n")
    uname = platform.uname()
    file.writelines(f"System: {uname.system}\n")
    file.writelines(f"Release: {uname.release}\n")
    file.writelines(f"Version: {uname.version}\n")
    file.writelines(f"Processor: {uname.processor}\n")

    # CPU INFORMATION
    file.writelines("\nCPU Info\n")

    cpufreq = psutil.cpu_freq()
    file.writelines(f"Current Frequency: {cpufreq.current:.2f}Mhz\n")
    file.writelines(f"Total CPU Usage: {psutil.cpu_percent()}%\n")

    # MEMORY INFORMATION
    file.writelines("\nMemory Information\n")
    # get the memory details
    svmem = psutil.virtual_memory()
    file.writelines(f"Total: {get_size(svmem.total)}\n")
    file.writelines(f"Available: {get_size(svmem.available)}\n")
    file.writelines(f"Used: {get_size(svmem.used)}\n")
    file.writelines(f"Percentage: {svmem.percent}%\n")

    # SWAP INFORMATION
    file.writelines("\nSWAP\n")
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    file.writelines(f"Total: {get_size(swap.total)}\n")
    file.writelines(f"Free: {get_size(swap.free)}\n")
    file.writelines(f"Used: {get_size(swap.used)}\n")
    file.writelines(f"Percentage: {swap.percent}%\n")
    file.writelines("Time of this test: "+time+'\n')
    file.writelines("Run time: "+endtime + '\n')
    for record in bufor:
        file.writelines("Password: "+record.password+'\n')
        file.writelines("Key: "+record.key+'\n')
        file.writelines("LoopUnit: "+str(record.i)+'\n')
        file.writelines("Time of test: "+record.time+'\n')

    file.close()