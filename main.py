
import combine_single
import combine_final
import time


import os

divisions = 2

cluster = True


def joiner(core):
    combine_multi.main(core)


if __name__ == "__main__":
    time0 = time.time()
    cores = []
    completed_cores = []

    done = False
    stop = False

    try:

        f = open("Progress", "r")

        progress = f.readlines()

        progress[0] = progress[0].split(",")
        progress[0][0] = progress[0][0].strip("[")
        progress[0][-1] = progress[0][-1].replace("']", '')
        progress[0][-1] = progress[0][-1].strip("\n")

        for i in range(len(progress[0])):
            progress[0][i] = progress[0][i].strip("'")
            progress[0][i] = progress[0][i].replace(" ", '')
            progress[0][i] = progress[0][i].replace("'", '')

        cores = progress[0]

        if "core" not in progress[1]:
            completed_cores = completed_cores

        else:

            progress[1] = progress[1].split(",")
            progress[1][0] = progress[1][0].strip("[")
            progress[1][-1] = progress[1][-1].replace("']", '')
            progress[1][-1] = progress[1][-1].strip("\n")

            for i in range(len(progress[1])):
                progress[1][i] = progress[1][i].strip("'")
                progress[1][i] = progress[1][i].replace(" ", '')
                progress[1][i] = progress[1][i].replace("'", '')

            completed_cores = progress[1]

        try:
            if "done" in progress[2]:
                done = True

        except:
            done = done

        f.close()

    except:

        print("ERROR NOT DIVIDED FIRST. RUN DIVIDER.PY!")
        stop = True

    if not stop:
        print("")
        print("")

        for core in cores:

            if core not in completed_cores:
                print("")
                print("")

                print("COMBINING")

                print("================")
                print("================")
                combine_single.main(core)
                completed_cores.append(core)
                os.system("rm Progress")
                f = open("Progress", "a")
                f.write(str(cores)+"\n")
                f.write(str(completed_cores)+"\n")
                f.close()

        timei = time.time()

        delta = timei - time0

        if delta >= 20*60*60 and cluster:
            a = 0

        elif not done:

            print("")
            print("")

            print("FINAL COMBINING")

            print("================")
            print("================")
            combine_final.main(divisions)

            f = open("Progress", "a")
            f.write("done"+"\n")
