import time
from multiprocessing import Process, Queue
import os


def multi_div(list_times, core):
    os.system("mkdir "+str(core))
    os.system("mkdir "+str(core)+"/postProcessing")
    os.system("mkdir "+str(core)+"/postProcessing/linesample")
    #os.system("cp combine_multi.py "+str(core))

    for j in list_times:
        os.system("cp -r postProcessing/linesample/"+str(j) +
                  "  "+str(core)+"/postProcessing/linesample")


def main(n_cores):

    os.system('rm -rf core*')

    os.system('ls postProcessing/linesample > times')

    tim = time.time()

    f = open("times", "r")
    times_ = f.readlines()

    times = []

    for line in times_:
        times.append(line.strip('\n'))

    times.sort(key=float)
    os.system("rm times")

    f.close()
    chunked_list = list()
    chunk_size = len(times)//n_cores

    for i in range(0, len(times), chunk_size):
        chunked_list.append(times[i:i+chunk_size])

    cores = []

    for i in range(n_cores):
        cores.append("core"+str(i))

    queue = Queue()

    processes = [Process(target=multi_div, args=(chunked_list[x], cores[x],))
                 for x in range(n_cores)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    return (cores, chunked_list)
