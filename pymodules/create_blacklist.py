#!/usr/bin/env python

import sys
import os

blacklist = []

def main():
    fin=open("/home/b/oldjscblacklist.txt","r")
    for line in fin:
        blacklist.append(line)
    fin.close()
    fin=open("/home/b/jscout/f1/cov/diff/id:000108,orig:15.4.4.18-7-c-ii-1.js","r")
    for line in fin:
        if line.startswith("/home/b/webkit_gcov/") and line not in blacklist:
            blacklist.append(line)
    fin.close()
    fout=open("/home/b/jscblacklist.txt","w")
    for line in blacklist:
        fout.write(line)
    fout.close()

if __name__=="__main__":
    main()
