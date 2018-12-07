#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import codecs
from antlr4 import *
from ECMAScriptLexer import ECMAScriptLexer
from ECMAScriptParser import ECMAScriptParser
from ECMAScriptVisitor import ECMAScriptVisitor
from ECMAScriptVisito import ECMAScriptVisito
'''
Simple Chunk Cross-Over Replacement Module for AFLFuzz

@author:     Christian Holler (:decoder)

@license:

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

@contact:    choller@mozilla.com
'''
intervals = []
stream = None
stream1 = None
pos = [0]*96
lastReplaced=""
lastIndex=-1
ret=""

def parse(buf):

    global stream

    gl.error = 0
    gl.chunk = {}
    gl.code_fragments = {}

    input = InputStream(buf)
    lexer = ECMAScriptLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream)
    #print stream.getText((0,100))
    tree = parser.program()
    if gl.error > 0:
        return 0

    gl.currentstream = stream
    visitor = ECMAScriptVisitor()
    visitor.visit(tree)
    return len(gl.chunk.values())

def parse1(buf):

    global intervals
    global fragments
    global types

    input = InputStream(buf)
    lexer = ECMAScriptLexer(input)
    stream1 = CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream1)
    #print stream.getText((0,100))
    tree = parser.program()

    gl.currentstream = stream1
    visitor = ECMAScriptVisito()
    visitor.visit(tree)

    intervals=[]
    fragments=[]
    types=[]
    for type in gl.chunk.keys():
        for interval in gl.chunk[type]:
            if interval not in intervals and interval[0] < interval[1] and interval[0]>0:
                for fragment in gl.code_fragments[type]:
                #print(fragment)
                    #types.append(type)
                    if len(fragment) > 0 and len(fragment) < 100:
                        intervals.append(interval)
                        fragments.append(fragment)
    #print(len(types)) 
    #print(len(fragments))          
    #print(len(intervals))
    #fout=open("/home/b/typecount.txt","w")
    #for i in range(0,96):
    #    fout.write(str(pos[i])+"\n")
    #fout.close()
    return len(intervals)

def fuzz(index):
    #print interval_l
    #print interval_r
    #print intervals[interval_l]
    #print intervals[interval_r]
    #input = InputStream(buf)
    #lexer = ECMAScriptLexer(input)
    #stream = CommonTokenStream(lexer)
    #stream.fill()
    #print(stream.getText((0,100)))
    rewriter = TokenStreamRewriter(stream)
    rewriter.replaceRange(intervals[index][0],intervals[index][1],fragments[index])
    #pos[types[index]]=pos[types[index]]+1
    ret=rewriter.getText("default")
    #print(ret)
    #print(intervals[interval_l][1])
    return (ret,0)

def init_trim(buf):
    global intervals
    global stream
    #@type buf: bytearray
    #@param buf: the buffer that should be trimmed.

    #@type: int
    #@return: the maximum number of trimming steps.
    gl.chunk = {}
    gl.error = 0
    #print("\n\n\n\n\n\n\n\n\n\n\n@@@@@@@@@@@@@@@@@@@@@@@@"+str(buf))
    input = InputStream(buf)
    lexer = ECMAScriptLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ECMAScriptParser(stream)
    #print("\n\n\n\n\n\n\n\n\n\n\n@@@@@@@@@@@@@@@@@@@@@@@@"+stream.getText((0,100)))
    tree = parser.program()
    if gl.error > 0:
        return 0

    gl.currentstream = stream
    visitor = ECMAScriptVisitor()
    visitor.visit(tree)

    intervals=[]
    for type in gl.chunk.keys():
        #print("type:"+str(type))
        for interval in gl.chunk[type]:
            if interval not in intervals and interval[0] < interval[1] and interval[0]>0:
                intervals.append(interval)
    #print(intervals)
    return len(intervals)

def trim(index):
    global lastReplaced
    global lastIndex
    global ret
    #print(stream.getText((0,100)))
    #print(intervals[index])
    #print("index:"+str(index))
    rewriter = TokenStreamRewriter(stream)
    lastIndex = index
    lastReplaced = stream.getText(intervals[index])
    #print("lastReplaced:---------------------------\n"+lastReplaced)
    rewriter.replaceRange(intervals[index][0],intervals[index][1],None)
    ret=rewriter.getText("default")
    #print(ret)
    #print("-----------------------------")
    #print(len(ret))
    #print(intervals[interval_l][1])
    return (ret,len(ret))

def post_trim(success):
    global lastReplaced
    global ret
    if success:
        print("lastReplaced:"+lastReplaced)
        leng=init_trim(ret)
        if leng > 0:
            return 0
        else:
            return -1
    else:
        rewriter = TokenStreamRewriter(stream)
        rewriter.replaceRange(intervals[lastIndex][0],intervals[lastIndex][1],lastReplaced)
        ret=rewriter.getText("default")
        #print(ret)
        #print(intervals[interval_l][1])
        if lastIndex+1 < len(intervals):
            return lastIndex+1
        else:
            return -1

def pre_process():
    buf=""
    for root, directories, files in os.walk("/home/b/smintest/"):
        for f in files:
            print(f)
            with open(root+"/"+f, 'rb') as file:
                bytes = file.read()
                buf=codecs.decode(bytes, 'utf-8', 'strict')
            #print("@@@@@@@@@@@@@@@@@@@@@@@@\n"+str(buf))
            input = InputStream(buf)
            lexer = ECMAScriptLexer(input)
            stream = CommonTokenStream(lexer)
            parser = ECMAScriptParser(stream)
            tree = parser.program()
            rewriter = TokenStreamRewriter(stream)
            ret=rewriter.getTextWithoutWhitespace("default")
            #print("$$$$$$$$$$$$$$$\n"+str(ret))
            with open("/home/b/smintest2/"+f, 'w') as file:
                file.write(ret)


if __name__=="__main__":
    pre_process()

'''
if __name__=="__main__":
    buf=""
    for root, directories, files in os.walk("/home/b/seeds/"):
        for f in files:
            #print(f)
            with open(root+"/"+f, 'rb') as file:
                bytes = file.read()
                buf=codecs.decode(bytes, 'utf-8', 'strict')
            size=init_trim(buf)
            index=0
            #print(size)
            while index < size and index!=-1:
                #print(index)
                buf=trim(index)
                #print("result:===============================\n"+buf)
                if index%2 == 0:
                    index=post_trim(False)
                else:
                    index=post_trim(True)
            break
'''
