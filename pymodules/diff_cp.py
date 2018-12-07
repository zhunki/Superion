#!/usr/bin/env python

import sys
import os
from shutil import copyfile
difflist = []

def main():
    for root, directories, files in os.walk("/home/b/jscout_spider/cov/diff/"):
        for f in files:
            difflist.append(f)
    print(difflist)


    for root, directories, files in os.walk("/home/b/jscout_spider/f1/queue/"):
        for f in files:
            if f in difflist:
                copyfile("/home/b/jscout_spider/f1/queue/"+f,"/home/b/jscout_spider/cov/diff/"+f)

if __name__=="__main__":
    main()
