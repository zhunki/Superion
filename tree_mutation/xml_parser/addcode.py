#!/usr/bin/env python3
import os

with open('XMLParserBaseVisitor.h', 'r') as input_f:
    code = input_f.read()
    code = code.replace('#include "antlr4-runtime.h"\n#include "XMLParserVisitor.h"', '#include <iostream>\n#include <vector>\n#include "antlr4-runtime.h"\n#include "XMLParserVisitor.h"\nusing namespace std;\nusing namespace antlr4;\n')
    code = code.replace('public:\n', 'public:\n\tvector<misc::Interval> intervals;\n\tvector<string> texts;\n\n')
with open('XMLParserBaseVisitor.h', 'w') as output_f:
    code1 = code.replace('override {\n', 'override {\n    intervals.push_back(ctx->getSourceInterval());\n    \n    misc::Interval intvl= new misc::Interval(ctx->getStart()->getStartIndex(), ctx->getStop()->getStopIndex());\n    texts.push_back(ctx->start->getInputStream()->getText(intvl));\n')
    output_f.write(code1)
with open('XMLParserSecondVisitor.h', 'w') as output_f:
    code2 = code.replace('override {\n', 'override {\n    //intervals.push_back(ctx->getSourceInterval());\n    \n    misc::Interval intvl= new misc::Interval(ctx->getStart()->getStartIndex(), ctx->getStop()->getStopIndex());\n    texts.push_back(ctx->start->getInputStream()->getText(intvl));\n')
    code2 = code2.replace('BaseVisitor', 'SecondVisitor')
    output_f.write(code2)

with open('XMLParserBaseVisitor.cpp', 'r') as input_f:
    code = input_f.read()
    code = code.replace('BaseVisitor', 'SecondVisitor')
with open('XMLParserSecondVisitor.cpp', 'w') as output_f:
    output_f.write(code)
