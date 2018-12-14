# Superion

Superion is a fuzzer which extends the famous AFL (http://lcamtuf.coredump.cx/afl/) to support structured inputs such as JavaScript and XML. The paper "Superion: Grammar-Aware Greybox Fuzzing" is accepted by ICSE 2019 (https://2019.icse-conferences.org/track/icse-2019-Technical-Papers#event-overview). 

Superion mainly adds a mutation strategy to AFL. The mutation strategy first parses a input into Abstract Syntax Tree(AST)  and then randomly choose another input from AFL’s queue and also parse it into AST. A sub tree of the target input can be replaced by another sub tree ether from target input itself or randomly chosen supplementary sample. Therefore, hundreds of new samples are generated and executed to find new path in tested programs.

The parsing ability of Superion is provided by ANTLR (https://www.antlr.org/), which can automatically generates a parser given the grammar file. 

## Building Superion

### Build ANTLR runtime

To build Superion, we first need to build the ANTLR runtime. The ANTLR runtime is located in tree_mutation folder.

```
cd tree_mutation/
cmake ./
make
```

If a missing uuid error is raised, you need to install uuid first and add -fPIC to MY_CXX_WARNING_FLAGS in tree_mutation/CMakeLists.txt.

```
sudo apt-get install uuid-dev
//add -fPIC to MY_CXX_WARNING_FLAGS in tree_mutation/CMakeLists.txt
```

### Build Tree Mutator

The JS parser is located in tree_mutation/js_parser folder. Besides, we also have a xml_parser, vbs_parser there.

```
cd tree_mutation/js_parser
for f in *.cpp; do g++ -I ../runtime/src/ -c $f -std=c++11; done
g++ -shared -std=c++11 *.o ../dist/libantlr4-runtime.a  -o libTreeMutation.so
cc -O3 -funroll-loops -Wall -D_FORTIFY_SOURCE=2 -g -Wno-pointer-sign -DAFL_PATH=\"/usr/local/lib/afl\" -DDOC_PATH=\"/usr/local/share/doc/afl\" -DBIN_PATH=\"/usr/local/bin\" afl-fuzz.c -o afl-fuzz -ldl ./tree_mutation/js_parser/libTreeMutation.so
```

### Build AFL

```
//add ./js_parser/tree_mutation/libTreeMutation.so to makefile
cd llvm_mode/
LLVM_CONFIG=llvm-config-3.8 CXXFLAGS="-DLLVM38" make
make
```

## Fuzzing WebKit

Webkit is one of our fuzzing target. Its source code can be find in https://github.com/WebKit/webkit.

To fuzz it using AFL or Superion, we first need to instrument the executable. 

```
export CC=~/superion/afl-clang-fast
export CXX=~/superion/afl-clang-fast++
export AFL_HARDEN=1
./Tools/Scripts/build-jsc --jsc-only --j14
```

In the experiments, we fuzzed it using four processes.

```
./afl-fuzz -M f1 -m 4G -t 500+ -i ~/js_seeds_cmin_coverage_only/ -o ~/jscout_test/ ~/webkit/WebKitBuild/Release/bin/jsc @@
./afl-fuzz -S f2 -m 4G -t 500+ -i ~/js_seeds_cmin_coverage_only/ -o ~/jscout_test/ ~/webkit/WebKitBuild/Release/bin/jsc @@
./afl-fuzz -S f3 -m 4G -t 500+ -i ~/js_seeds_cmin_coverage_only/ -o ~/jscout_test/ ~/webkit/WebKitBuild/Release/bin/jsc @@
./afl-fuzz -S f4 -m 4G -t 500+ -i ~/js_seeds_cmin_coverage_only/ -o ~/jscout_test/ ~/webkit/WebKitBuild/Release/bin/jsc @@
```

## Fuzzing JerryScript:

```
export CC=~/superion/afl-gcc
export CXX=~/superion/afl-g++

python ./tools/build.py --clean --debug --compile-flag=-fsanitize=address --compile-flag=-m32 --compile-flag=-fno-omit-frame-pointer --compile-flag=-fno-common --jerry-libc=off --static-link=off --lto=off --error-message=on --system-allocator=on

./afl-fuzz -M f1 -x ~/superion/dictionaries/js.dict -t 40+ -m 2000 -i ~/jerry_seeds/ -o ~/jerry_out/ ~/jerryscript/build/bin/jerry @@
./afl-fuzz -S f2 -t 40+ -m 2000 -i ~/jerry_seeds/ -o ~/jerry_out/ ~/jerryscript/build/bin/jerry @@
./afl-fuzz -S f3 -t 40+ -m 2000 -i ~/jerry_seeds/ -o ~/jerry_out/ ~/jerryscript/build/bin/jerry @@
```
