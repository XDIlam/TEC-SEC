# coding=utf-8
# Author By 1L4M G4N5

import sys, os, time

# warna
mrah="\033[1;31m"
biru="\033[1;35m"
abu2="\033[1;30m"
ntrl="\033[0m"

logo = """{}

___________                       _________
\__    ___/___   ____            /   _____/ ____   ____
  |    |_/ __ \_/ ___\   ______  \_____  \_/ __ \_/ ___\{}
  |    |\  ___/\  \___  /_____/  /        \  ___/\  \___
  |____| \___  >\___  >         /_______  /\___  >\___  >
             \/     \/                  \/     \/     \/{}
[☣]{}---------------------------------------------------{}[☣]
     {}Author : {}TS-13
     {}Github : {}https://github.com/ilam-dev
     {}contact : {}wa.me/+62895803386428{}
[☣]{}---------------------------------------------------{}[☣]

""".format(mrah,ntrl,biru,mrah,biru,abu2,ntrl,abu2,ntrl,abu2,ntrl,biru,mrah,biru)

def tik():
    titik = ['.   ', '..  ', '... ', '....', '.....']
    for o in titik:
        print '\r\x1b[1;91m[^] \x1b[1;96mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

def main():
    os.system("clear")
    time.sleep(2)
    tik()
    os.system("clear")
    print logo
    print "        {}• {}Menu {}• ".format(biru,mrah,biru)
    print ""
    print " {}1.{}TrackIP".format(abu2,ntrl)
    print " {}2.{}DDos Attack".format(abu2,ntrl)
    print " {}3.{}make sc deface \n".format(abu2,ntrl)
    pilih = raw_input(" {}pilih :{} ".format(biru,mrah))
    if pilih == "1" or pilih == "01":
        os.system("python2 Run_Track.py")
    elif pilih == "2" or pilih == "02":
        os.system("bash main.sh")
    elif pilih == "3" or pilih == "03":
        os.system("python2 dfce.py")
    else:
        print "pilih yg benar kontol!"
        main()

if __name__ == '__main__':
    main()
