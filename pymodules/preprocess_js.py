#!/usr/bin/env python
# encoding: utf-8

import os

def main():
    for root, directories, files in os.walk("/home/b/queue/"):
        for f in files:
            fin=open(os.path.join(root,f),"r")
            fout=open("/home/b/afterprocess/"+f,"w")
            for line in fin:
                if "startTest();" in line:
                    print(line)
                    fout.write(line.replace("startTest();",""))
                elif "stopTest();" in line:
                    fout.write(line.replace("stopTest();",""))
                elif "assert.sameValue" in line:
                    fout.write(line.replace("assert.sameValue",""))
                elif "assert.notSameValue" in line:
                    fout.write(line.replace("assert.notSameValue",""))
                elif "assert.throws" in line:
                    fout.write(line.replace("assert.throws",""))
                elif "WScript.Echo" in line:
                    fout.write(line.replace("WScript.Echo","print"))
                elif "document.writeln(" in line:
                    fout.write(line.replace("document.writeln(","print("))
                elif "postMessage(" in line:
                    fout.write(line.replace("postMessage(","print("))
                elif "verifyWritable(" in line:
                    fout.write(line.replace("verifyWritable(","("))
                elif "verifyNotWritable(" in line:
                    fout.write(line.replace("verifyNotWritable(","("))
                elif "verifyConfigurable(" in line:
                    fout.write(line.replace("verifyConfigurable(","("))
                elif "verifyNotConfigurable(" in line:
                    fout.write(line.replace("verifyNotConfigurable(","("))
                elif "verifyEnumerable(" in line:
                    fout.write(line.replace("verifyEnumerable(","("))
                elif "verifyNotEnumerable(" in line:
                    fout.write(line.replace("verifyNotEnumerable(","("))
                elif "verifyEqualTo(" in line:
                    fout.write(line.replace("verifyEqualTo(","("))
                elif "testWithTypedArrayConstructors(" in line:
                    fout.write(line.replace("testWithTypedArrayConstructors(","("))
                elif "testWithIntlConstructors(" in line:
                    fout.write(line.replace("testWithIntlConstructors(","("))
                elif "$DONE" in line:
                    fout.write(line.replace("$DONE",""))
                elif "WScript.LoadScriptFile" in line:
                    print(line)
                elif "describe(" in line:
                    fout.write(line.replace("describe(","("))
                elif "description(" in line:
                    fout.write(line.replace("description(","("))
                elif "shouldBe(" in line:
                    fout.write(line.replace("shouldBe(","("))
                elif "writeHeaderToLog" in line:
                    fout.write(line.replace("writeHeaderToLog","print"))
                elif "assert(" in line:
                    fout.write(line.replace("assert(","("))
                else:
                    fout.write(line)
            fin.close()
            fout.close()

if __name__=="__main__":
    main()


