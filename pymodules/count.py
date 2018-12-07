#!/usr/bin/env python
# encoding: utf-8

import os

def main():
    pos = [0]*96
    for root, directories, files in os.walk("/home/b/out/f1/queue/"):
        for i in range(0,96):
            for f in files:
                if f.endswith(",pos:"+str(i)) or ",pos:"+str(i)+"," in f:
                    pos[i]=pos[i]+1
                    #print("+++++++++"+str(pos[i]))

    for i in range(0,96):
        print(pos[i])

if __name__=="__main__":
    main()
