# Superion

See https://github.com/zhunki/Superion for the basic instructions. This repo supplements with the instructions on 1) how to build TreeMutation and 2) minor improvement.

### Build ANTLR runtime
To build Superion, we first need to build the ANTLR runtime. The ANTLR runtime is located in the tree_mutation folder.

```shell
cd /path/to/Superion/tree_mutation/
cmake ./
make
```
If a missing uuid error is raised, you need to install uuid first.
```shell
sudo apt-get install uuid-dev
```
### Generate lexer, parser, and visitor, given an ANTLR grammar (Using XML parser as an example here!)
0. In summary, you just run 
```shell
cd xml_parser
Make parser
```
If you are interested in the details, read ahead!

1. Automatically generate basic lexers, parsers, and visitors from ANTLR. (Ensure `antlr-4.7-complete.jar` is under parent directory.)
```
java -jar ../antlr-4.7-complete.jar -o . -visitor -no-listener -Dlanguage=Cpp GRAMMAR.g4 
```
You can replace the `GRAMMAR.g4` with your own grammar. Note that sometimes a language grammar is divided into two parts---lexer and parser, you just run the above command for two `*.g4`, respectively.

2. The authors have modified their `BaseVisitor` in their examples. In detail, they added two vectors:
    ```cpp
    vector<misc::Interval> intervals;
    vector<string> texts;
    ```
and the corresponding operations in each visitor:
    ```cpp
    intervals.push_back(ctx->getSourceInterval());
    texts.push_back(ctx->start->getInputStream()->getText(ctx->getSourceInterval()));
    ```

3. The authors also used `SecondVisitor` in their examples. The `SecondVisitor` is almost identical with `BaseVisitor` with only one vector:
    ```cpp
    vector<string> texts;
    ```
and the corresponding operations in each visitor:
    ```cpp
    texts.push_back(ctx->start->getInputStream()->getText(ctx->getSourceInterval()));
    ```
**I wrote a simple script `addcode.py` to achieve this**, e.g., add code to `BaseVisitor` and automatically generate `SecondVisitor`.
    
    Note that, the script automatically adds code to all visitors, which might not be always necessary. You can manually comment newly added code in some visitors for better performance.

### Compile the TreeMutation
0. Simply run:
    ```shell
    make compile
    ```
to test with `main.cpp`;
Or you run:
    ```shell
    make share
    ```
to construct the shared object `libTreeMutation.so`.

Above instructions and scripts temporarily hardcode for XML, if you'd like try other languages, you need:
1. Update the `TreeMutation.cpp` to a newer version by modifying the `XML` related headers, visitors to your target language, e.g., line 5-8, 33, 35, 44, 74, 76, 83. You can also write scripts to do that.

2. Update `Markfile`

3. Update `addcode.py`

#### Notice
From code line 6166, actually Superion will never go to the `havoc` mode! If the tree mutation fails, the entries are just abandoned, which is not suggested. In my testing, the performance of Superion is not as good as expected because of this. You can comment 6165-6166.


#### Contact
I am happy to discuss about this tool, please contact me via <lipenghui315@gmail.com>.
