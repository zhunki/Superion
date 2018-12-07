#!/usr/bin/env python
# encoding: utf-8
import sys
import os
from antlr4 import *
from ECMAScriptLexer import ECMAScriptLexer
from ECMAScriptParser import ECMAScriptParser
from ECMAScriptVisitor import ECMAScriptVisitor
from ECMAScriptVisito import ECMAScriptVisito

intervals=[]
fragments=[]
types=[]
stream = None
stream1 = None
fileindex=0

def parse(f):
    global stream
    global intervals
    global fragments
    global types

    gl.chunk = {}
    gl.code_fragments = {}
#parse the first input
    input = FileStream(f)
    lexer = ECMAScriptLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream)
    tree = parser.program()
    gl.currentstream = stream
    visitor = ECMAScriptVisitor()
    visitor.visit(tree)

    intervals=[]
    fragments=[]
    types=[]
    for type in gl.chunk.keys():
        for interval in gl.chunk[type]:
           #the same
            if interval[0] <= interval[1]:
                #for fragment in gl.code_fragments[type]:
                    #types.append(type)
                intervals.append(interval)
                    #fragments.append(fragment)
            else:
                print("intervals:"+str(interval[0])+","+str(interval[1]))
#            for fragment in gl.code_fragments.values():
#            for type1 in gl.code_fragments.keys():
#                if type1 != type:
#                    for fragment in gl.code_fragments[type1]:
#                        types.append(type1)
#                        intervals.append(interval)
#                        fragments.append(fragment)
    return len(intervals)

def fuzz(index):
    global fileindex

    rewriter = TokenStreamRewriter(stream)
    #print("intervals:"+str(intervals[index][0])+","+str(intervals[index][1]))
    rewriter.insertBefore("default",intervals[index][0],"for(var i=0;i<1000;i++)")
    ret=rewriter.getText("default")
    fout=open("/home/b/js/"+str(fileindex),"w")
    fileindex+=1
    fout.write(ret)
    fout.close()

if __name__=="__main__":
    for root, directories, files in os.walk("/home/b/seeds/"):
        for f in files:
            print(f)
            size=parse(root+"/"+f)
            for i in range(0,size-1):
                fuzz(i)
