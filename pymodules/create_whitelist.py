#!/usr/bin/env python

import sys
import os

whitelist = []
blacklist = []

def is_source_file(filename):
    source_exts = ['.cpp', '.cc', '.cxx', '.c', '.h', '.hxx']
    for source_ext in source_exts:
        if filename.endswith(source_ext):
            return True
    return False

def main():
    fin=open("/home/b/jscblacklist.txt","r")
    for line in fin:
        blacklist.append(line)
        #print(line)
    fin.close()
    #print(blacklist)
    fout=open("/home/b/jscwhitelist.txt","w")
    for root, directories, files in os.walk("/home/b/webkit/Source/"):
        for f in files:
#            if is_source_file(f) and "build_OPT.OBJ" not in os.path.join(root,f):
            if is_source_file(f) and os.path.join(root,f)+"\n" not in blacklist and "/home/b/webkit/Source/ThirdParty/" not in os.path.join(root,f) and "/home/b/webkit/Source/WebDriver/" not in os.path.join(root,f) and "/home/b/webkit/Source/WebCore/" not in os.path.join(root,f) and "/home/b/webkit/Source/WebKitLegacy/" not in os.path.join(root,f):
                #print(os.path.join(root,f))
                fout.write(os.path.join(root,f)+"\n")
    fout.close()

if __name__=="__main__":
    main()
