#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import codecs
from antlr4 import *
from ECMAScriptLexer import ECMAScriptLexer
from ECMAScriptParser import ECMAScriptParser
from PrettyVisitor import PrettyVisitor
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
ruleNames =  [ "program", "sourceElements", "sourceElement", "statement", 
                   "block", "statementList", "variableStatement", "variableDeclarationList", 
                   "variableDeclaration", "initialiser", "emptyStatement", 
                   "expressionStatement", "ifStatement", "iterationStatement", 
                   "continueStatement", "breakStatement", "returnStatement", 
                   "withStatement", "switchStatement", "caseBlock", "caseClauses", 
                   "caseClause", "defaultClause", "labelledStatement", "throwStatement", 
                   "tryStatement", "catchProduction", "finallyProduction", 
                   "debuggerStatement", "functionDeclaration", "formalParameterList", 
                   "functionBody", "arrayLiteral", "elementList", "elision", 
                   "objectLiteral", "propertyNameAndValueList", "propertyAssignment", 
                   "propertyName", "propertySetParameterList", "arguments", 
                   "argumentList", "expressionSequence", "singleExpression", 
                   "assignmentOperator", "literal", "numericLiteral", "identifierName", 
                   "reservedWord", "keyword", "futureReservedWord", "getter", 
                   "setter", "eos", "eof" ]

def trim_comment():
    with open("/home/b/skyfire/pymodules/test.js", 'rb') as file:
        bytes = file.read()
        buf=codecs.decode(bytes, 'utf-8', 'strict')
    #print("@@@@@@@@@@@@@@@@@@@@@@@@\n"+str(buf))
    input = InputStream(buf)
    lexer = ECMAScriptLexer(input)
    stream = CommonTokenStream(lexer)
    gl.currentstream=stream
    parser = ECMAScriptParser(stream)
    tree = parser.program()
    print(tree.toStringTree(ruleNames,parser))
    #visitor = PrettyVisitor()
    #visitor.visit(tree)
if __name__=="__main__":
    trim_comment()
