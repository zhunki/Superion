#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import codecs
import time
from antlr4 import *
from XMLLexer import XMLLexer
from XMLParser import XMLParser
from XMLParserVisitor import XMLParserVisitor
'''
Simple Chunk Cross-Over Replacement Module for AFLFuzz

@author:     Christian Holler (:decoder)

@license:

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

@contact:    choller@mozilla.com
'''

def trim_comment():
    buf=""
    fout = open("/home/b/xml_parse_time.txt", 'w')
    fmu = open("/home/b/xml_mutation_time.txt", 'w')
    for root, directories, files in os.walk("/home/b/libplist_xml/"):
        for f in files:
            print(f)
            types=[]
            gl.error = 0
            gl.chunk = {}
            gl.code_fragments = {}
            try:
                start =time.time()
                with open(root+"/"+f, 'rb') as file:
                    bytes = file.read()
                    buf=codecs.decode(bytes, 'utf-8', 'strict')
                #print("@@@@@@@@@@@@@@@@@@@@@@@@\n"+str(buf))
                input = InputStream(buf)
                lexer = XMLLexer(input)
                stream = CommonTokenStream(lexer)
                parser = XMLParser(stream)
                tree = parser.document()
                gl.currentstream = stream
                visitor = XMLParserVisitor()
                visitor.visit(tree)
                end=time.time()
                #print(end-start)
                #print("$$$$$$$$$$$$$$$\n"+str(ret))
                fout.write(str(end-start)+","+str(len(bytes))+"\n")

                for type in gl.chunk.keys():
                    for interval in gl.chunk[type]:
                        if interval[0] < interval[1] and interval[0]>0:
                            start =time.time()
                            rewriter = TokenStreamRewriter(stream)
                            rewriter.replaceRange(interval[0],interval[1],"a")
                            ret=rewriter.getText("default")
                            end=time.time()
                            fmu.write(str(end-start)+"\n")
            except UnicodeDecodeError:
                continue
            except ValueError:
                continue
    fout.close()
    fmu.close()
if __name__=="__main__":
    trim_comment()
