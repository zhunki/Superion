# Superion

Superion is a fuzzer which extends the famous AFL (http://lcamtuf.coredump.cx/afl/) to support structured inputs such as JavaScript and XML. The paper "Superion: Grammar-Aware Greybox Fuzzing" is accepted by ICSE 2019 (https://2019.icse-conferences.org/track/icse-2019-Technical-Papers#event-overview). 

Superion mainly adds a mutation strategy to AFL. The mutation strategy first parses an input into Abstract Syntax Tree(AST)  and then randomly choose another input from AFL’s queue and also parse it into AST. A sub tree of the target input can be replaced by another sub tree either from target input itself or randomly chosen supplementary sample. Therefore, hundreds of new samples are generated and executed to find a new path in tested programs.

The parsing ability of Superion is provided by ANTLR (https://www.antlr.org/), which can automatically generate a parser given the grammar file. 

## Some harmless POCs

Here we listed some harmless bugs we found using Superion, which is either fixed for a long time span or hard to be exploited. The following two POCs can crash older version of Safari browser and now fixed by the developer.

```
function f(eval){
    eval(0x12345678);
    f(function(){});
}
f(function(){});

==27305==ERROR: AddressSanitizer: SEGV on unknown address 0x12345688 (pc 0xabc04b1f bp 0xbfb2b9d8 sp 0xbfb2b9a0 T0)
    #0 0xabc04b1e  (<unknown module>)
```

```
class A { };

class B extends A {
    constructor(a, b) {
        var f = () => b ? this : {};
        if (a) {
            var val = f() == super();
        } else {
            super();
            var val = f();
        }
    }
};

for (var i=0; i < 10000; i++) {
    try {
        new B(true, true);
    } catch (e) {
    }
    var a = new B(false, true);
    var c = new B(true, false);
}
```

## Building Superion

The following build instructions are tested on Ubuntu 16.04 with gcc-5.4.0 and clang-3.8.

### Build ANTLR runtime

To build Superion, we first need to build the ANTLR runtime. The ANTLR runtime is located in tree_mutation folder.

```
cd /path_to_Superion/tree_mutation/
cmake ./
make
```

If a missing uuid error is raised, you need to install uuid first.

```
sudo apt-get install uuid-dev
```

### Generate Lexer, Parser, Visitor automatically

add antlr-4.7-complete.jar to classpath

xml:
```
java org.antlr.v4.Tool -o path -visitor -no-listener -Dlanguage=Cpp XMLLexer.g4 
java org.antlr.v4.Tool -o path -visitor -no-listener -Dlanguage=Cpp XMLParser.g4
```

javascript:
```
java org.antlr.v4.Tool -o path -visitor -no-listener -Dlanguage=Cpp JavaScriptLexer.g4 
java org.antlr.v4.Tool -o path -visitor -no-listener -Dlanguage=Cpp JavaScriptParser.g4
```


### Build tree mutator

The JS parser is located in tree_mutation/js_parser folder. Besides, we also have an xml_parser, vbs_parser there.

```
cd /path_to_Superion/tree_mutation/js_parser

for f in *.cpp; do g++ -I ../runtime/src/ -c $f -fPIC -std=c++11; done

g++ -shared -std=c++11 *.o ../dist/libantlr4-runtime.a  -o libTreeMutation.so
```

### Build AFL

To compile afl-clang-fast and afl-clang-fast++, which are used to instrument fuzzing targets.
```
cd /path_to_Superion/llvm_mode/
LLVM_CONFIG=llvm-config-3.8 CXXFLAGS="-DLLVM38" make

cd /path_to_Superion/
make
```

## Fuzzing WebKit

Webkit is one of our fuzzing targets. Its source code can be found in https://github.com/WebKit/webkit. The initial seeds we used is obtained from https://github.com/WebKit/webkit/tree/master/JSTests/stress.

To download WebKit source code:

```
svn checkout https://svn.webkit.org/repository/webkit/trunk WebKit
```

To fuzz it using AFL or Superion, we first need to instrument the executable. 

```
export CC=~/path_to_Superion/afl-clang-fast
export CXX=~/path_to_Superion/afl-clang-fast++
export AFL_HARDEN=1
./Tools/Scripts/build-jsc --jsc-only --j14
```

In the experiments, we fuzzed it using four processes.

```
./afl-fuzz -M f1 -m 1G -t 100+ -i ~/stress/ -o ~/jscout/ ~/webkit/WebKitBuild/Release/bin/jsc @@
./afl-fuzz -S f2 -m 1G -t 100+ -i ~/stress/ -o ~/jscout/ ~/webkit/WebKitBuild/Release/bin/jsc @@
./afl-fuzz -S f3 -m 1G -t 100+ -i ~/stress/ -o ~/jscout/ ~/webkit/WebKitBuild/Release/bin/jsc @@
./afl-fuzz -S f4 -m 1G -t 100+ -i ~/stress/ -o ~/jscout/ ~/webkit/WebKitBuild/Release/bin/jsc @@
```

## Fuzzing JerryScript:

```
export CC=~/path_to_Superion/afl-gcc
export CXX=~/path_to_Superion/afl-g++

python ./tools/build.py --clean --debug --compile-flag=-fsanitize=address --compile-flag=-m32 --compile-flag=-fno-omit-frame-pointer --compile-flag=-fno-common --jerry-libc=off --static-link=off --lto=off --error-message=on --system-allocator=on

./afl-fuzz -M f1 -x ~/path_to_Superion/dictionaries/js.dict -t 40+ -m 2000 -i ~/jerry_seeds/ -o ~/jerry_out/ ~/jerryscript/build/bin/jerry @@
./afl-fuzz -S f2 -t 40+ -m 2000 -i ~/jerry_seeds/ -o ~/jerry_out/ ~/jerryscript/build/bin/jerry @@
./afl-fuzz -S f3 -t 40+ -m 2000 -i ~/jerry_seeds/ -o ~/jerry_out/ ~/jerryscript/build/bin/jerry @@
```
