#!/usr/bin/env python3
import os, sys
if __name__ == '__main__':
    if not(len(sys.argv) > 1 and os.path.exists(sys.argv[1])):
        print("please specify the folder of parser1")
        exit(0)
    for f in os.listdir(sys.argv[1]):
        if f.endswith('BaseVisitor.h'):
            name = f.strip('.h')

    os.chdir(sys.argv[1])

    with open("%s.h" % name, 'r+') as fp:
        code = fp.read()
        code = code.replace('#include "antlr4-runtime.h"\n#include "%s.h"' % name, '#include <iostream>\n#include <vector>\n#include "antlr4-runtime.h"\n#include "%s.h"\nusing namespace std;\nusing namespace antlr4;\n' % name)
        code = code.replace('public:\n', 'public:\n\tvector<misc::Interval> intervals;\n\tvector<string> texts;\n\n')
        fp.seek(0)

        code1 = code.replace('override {\n', 'override {\n    texts.push_back(ctx->start->getInputStream()->getText(misc::Interval(ctx->getStart()->getStartIndex(), ctx->getStop()->getStopIndex()));\n')
        fp.write(code1)

    secondName = name.replace('Base', 'Second')

    with open('%s.h' % secondName, 'w') as output_f:
        code2 = code.replace('override {\n', 'override {\n    //intervals.push_back(ctx->getSourceInterval());\n    texts.push_back(ctx->start->getInputStream()->getText(misc::Interval(ctx->getStart()->getStartIndex(), ctx->getStop()->getStopIndex()));\n')
        code2 = code2.replace('BaseVisitor', 'SecondVisitor')
        output_f.write(code2)

    with open('%s.cpp' % name, 'r') as input_f:
        code = input_f.read()
        code = code.replace('BaseVisitor', 'SecondVisitor')
        with open('XMLParserSecondVisitor.cpp', 'w') as output_f:
            output_f.write(code)
