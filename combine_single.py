import os
import time
import threading
import time


def combine(timei, line, folder):

    f = open(folder+'/postProcessing/linesample/' + timei+'/'+line, "r")
    data = f.readlines()

    f2 = open(folder+'/combined/'+line, "a")

    for i in range(len(data)):

        data[i] = timei + "      " + data[i]

    f2.writelines(data)

    f2.close()

    f.close()


def main(folder):
    tim = time.time()

    os.system('ls '+folder+'/postProcessing/linesample > times'+folder)
    #os.system('rm -rf combined')
    os.system('mkdir '+folder+'/combined')

    f = open("times"+folder, "r")
    times_ = f.readlines()

    times = []

    for line in times_:
        times.append(line.strip('\n'))

    times.sort(key=float)
    os.system("rm times"+folder)

    os.system('ls '+folder+'/postProcessing/linesample/' +
              times[0]+' > samplines')

    f.close()

    f = open("samplines", "r")
    samplines_ = f.readlines()

    samplines = []

    for line in samplines_:
        samplines.append(line.strip('\n'))

    threads = list()

    os.system("rm samplines")

    f.close()

    n = 0
    for timei in times:
        n += 1
        print(folder+": "+str(100*n/len(times)))
        for index in samplines:

            x = threading.Thread(target=combine,
                                 args=(timei, index, folder))
            threads.append(x)
            x.start()

        for index, thread in enumerate(threads):

            thread.join()

    print(folder+" time: "+str(time.time()-tim))
