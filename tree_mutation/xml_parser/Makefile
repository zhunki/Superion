parser:
	java -jar ../antlr-4.7-complete.jar -o . -visitor -no-listener -Dlanguage=Cpp XMLLexer.g4 
	java -jar ../antlr-4.7-complete.jar -o . -visitor -no-listener -Dlanguage=Cpp XMLParser.g4
	./addcode.py
share:
	for f in *.cpp; do g++ -g -I ../runtime/src/ -c $$f -fPIC -std=c++11; done
	g++ -shared -std=c++11 *.o ../dist/libantlr4-runtime.a  -o libTreeMutation.so

compile:
	for f in *.cpp; do g++ -g -I ../runtime/src/ -c $$f -fPIC -std=c++11; done
	g++ -std=c++11 *.o ../dist/libantlr4-runtime.a  -o main

.PHONY: compile
