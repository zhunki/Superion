#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import codecs
from antlr4 import *
from ECMAScriptLexer import ECMAScriptLexer
from ECMAScriptParser import ECMAScriptParser
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

def trim_comment():
    buf=""
    for root, directories, files in os.walk("/home/b/grammar-correct/"):
        for f in files:
            print(f)
            try:
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
                with open("/home/b/trimmed/"+f, 'w') as file:
                    file.write(ret)
                os.remove(root+"/"+f)
            except UnicodeDecodeError:
                continue

if __name__=="__main__":
    trim_comment()
