import os


def main(n_cores):

    os.system("rm -rf combined")
    os.system("mkdir combined")

    cores = []

    for i in range(n_cores):
        cores.append("core"+str(i))

    os.system('ls core0/combined > samplelines')

    f = open("samplelines", "r")
    samplines_ = f.readlines()

    samplines = []

    for line in samplines_:
        samplines.append(line.strip('\n'))
    os.system("rm samplelines")
    f.close()
    n = 0
    for core in cores:

        print((n+1)/len(cores))

        for line in samplines:

            f = open(core+'/combined/' + line, "r")
            data = f.readlines()

            f2 = open('combined/'+line, "a")

            f2.writelines(data)

            f2.close()

            f.close()

        n += 1
