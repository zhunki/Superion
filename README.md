========================================================

1. build antlr-runtime

cd js_parser/
cmake ./
// missing uuid error: sudo apt-get install uuid-dev
//add -fPIC to MY_CXX_WARNING_FLAGS in js_parser/CMakeLists.txt
make

========================================================

2. build treemutatior

cd js_parser/tree_mutation
for f in *.cpp; do g++ -I ../runtime/src/ -c $f -std=c++11; done
g++ -shared -std=c++11 *.o ../dist/libantlr4-runtime.a  -o libTreeMutation.so
cc -O3 -funroll-loops -Wall -D_FORTIFY_SOURCE=2 -g -Wno-pointer-sign -DAFL_PATH=\"/usr/local/lib/afl\" -DDOC_PATH=\"/usr/local/share/doc/afl\" -DBIN_PATH=\"/usr/local/bin\" afl-fuzz.c -o afl-fuzz -ldl ./js_parser/tree_mutation/libTreeMutation.so

//build TreeMutation alone
g++ -std=c++11 *.o ../dist/libantlr4-runtime.a  -o TreeMutation

//build TreeMutation with asan
for f in *.cpp; do g++ -fsanitize=address -I ../runtime/src/ -c $f -std=c++11; done
g++ -fsanitize=address -shared -std=c++11 *.o ../dist/libantlr4-runtime.a  -o libTreeMutation.so

========================================================

AFL:

//add ./js_parser/tree_mutation/libTreeMutation.so to makefile

LLVM_CONFIG=llvm-config-3.8 CXXFLAGS="-DLLVM38" make

========================================================

Webkit:

export CC=~/afl-2.52b/afl-clang-fast
export CXX=~/afl-2.52b/afl-clang-fast++
export AFL_HARDEN=1
./Tools/Scripts/build-jsc --jsc-only --j14

./afl-fuzz -M f1 -m 4G -t 500+ -i ~/js_seeds_cmin_coverage_only/ -o ~/jscout_test/ ~/webkit/WebKitBuild/Release/bin/jsc @@
./afl-fuzz -S f2 -m 4G -t 500+ -i ~/js_seeds_cmin_coverage_only/ -o ~/jscout_test/ ~/webkit/WebKitBuild/Release/bin/jsc @@
./afl-fuzz -S f3 -m 4G -t 500+ -i ~/js_seeds_cmin_coverage_only/ -o ~/jscout_test/ ~/webkit/WebKitBuild/Release/bin/jsc @@
./afl-fuzz -S f4 -m 4G -t 500+ -i ~/js_seeds_cmin_coverage_only/ -o ~/jscout_test/ ~/webkit/WebKitBuild/Release/bin/jsc @@

========================================================

SpiderMonkey:

export CC=~/afl-2.52b/afl-clang-fast
export CXX=~/afl-2.52b/afl-clang-fast++
export CFLAGS+="-fsanitize=address"
export CXXFLAGS+="-fsanitize=address"
export LDFLAGS+="-fsanitize=address"
export AFL_INST_RATIO=30
../configure --enable-optimize --enable-address-sanitizer --disable-jemalloc
make -j8

./afl-fuzz -M f1 -m 4G -t 500+ -i ~/js_seeds_cmin_coverage_only/ -o ~/jscout_test/ ~/webkit/WebKitBuild/Release/bin/jsc @@

========================================================

jerryScript:

export CC=~/afl-2.52b/afl-gcc
export CXX=~/afl-2.52b/afl-g++

python ./tools/build.py --clean --debug --compile-flag=-fsanitize=address --compile-flag=-m32 --compile-flag=-fno-omit-frame-pointer --compile-flag=-fno-common --jerry-libc=off --static-link=off --lto=off --error-message=on --system-allocator=on

./afl-fuzz -M f1 -x ~/afl-2.52b/dictionaries/js.dict -t 40+ -m 2000 -i ~/jerry_seeds/ -o ~/jerry_out/ ~/jerryscript/build/bin/jerry @@
./afl-fuzz -S f2 -t 40+ -m 2000 -i ~/jerry_seeds/ -o ~/jerry_out/ ~/jerryscript/build/bin/jerry @@
./afl-fuzz -S f3 -t 40+ -m 2000 -i ~/jerry_seeds/ -o ~/jerry_out/ ~/jerryscript/build/bin/jerry @@

~/afl-cov --live -d ~/jerry_out/f1/ --coverage-cmd "/home/b/jerryscript_gcov/build/bin/jerry AFL_FILE" --code-dir /home/b/jerryscript_gcov/
========================================================
