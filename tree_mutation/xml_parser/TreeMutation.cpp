#include <iostream>
#include <cstring>
#include <fstream>
#include "antlr4-runtime.h"
#include "XMLLexer.h"
#include "XMLParser.h"
#include "XMLParserBaseVisitor.h"
#include "XMLParserSecondVisitor.h"
#include <dirent.h>

using namespace antlr4;
using namespace std;

/*
extern "C" int parse(char* target,size_t len,char* second,size_t lenS);
extern "C" void fuzz(int index, char** ret, size_t* retlen);
*/

#define MAXSAMPLES 10000
#define MAXTEXT 200
string ret[MAXSAMPLES];

int parse(const char* target,size_t len,const char* second,size_t lenS) {
	vector<misc::Interval> intervals;
	vector<string> texts;
	int num_of_samples=0;
	//parse the target
	string targetString;
	try{
		targetString=string(target,len);
		ANTLRInputStream input(targetString);
		//ANTLRInputStream input(target);
		XMLLexer lexer(&input);
		CommonTokenStream tokens(&lexer);
		XMLParser parser(&tokens);
		TokenStreamRewriter rewriter(&tokens);
		tree::ParseTree* tree = parser.document();
		cout<<targetString<<endl;
		if(parser.getNumberOfSyntaxErrors()>0){
			std::cerr<<"NumberOfSyntaxErrors:"<<parser.getNumberOfSyntaxErrors()<<endl;
			return 0;
		}else{
 
			XMLParserBaseVisitor *visitor=new XMLParserBaseVisitor();
			visitor->visit(tree);

			int interval_size = visitor->intervals.size();
            cout << interval_size <<endl;

			for(int i=0;i<interval_size;i++){
				if(find(intervals.begin(),intervals.end(),visitor->intervals[i])!=intervals.end()){
				}else if(visitor->intervals[i].a<=visitor->intervals[i].b){
					intervals.push_back(visitor->intervals[i]);
				}
			}
			int texts_size = visitor->texts.size();
            cout << texts_size << endl;
			for(int i=0;i<texts_size;i++){
				if(find(texts.begin(),texts.end(),visitor->texts[i])!=texts.end()){
				}else if(visitor->texts[i].length()>MAXTEXT){
				}else{
					texts.push_back(visitor->texts[i]);
        			}
			}
            		delete visitor;


			//parse sencond
            cout << "111second" <<endl;
			string secondString;
			try{
				secondString=string(second,lenS);
				ANTLRInputStream inputS(secondString);
				XMLLexer lexerS(&inputS);
				CommonTokenStream tokensS(&lexerS);
				XMLParser parserS(&tokensS);
				tree::ParseTree* treeS = parserS.document();
                cout << "second" <<endl;

				if(parserS.getNumberOfSyntaxErrors()>0){
		 			std::cerr<<"second NumberOfSyntaxErrors S:"<<parserS.getNumberOfSyntaxErrors()<<endl;
				}else{
					XMLParserSecondVisitor *visitorS=new XMLParserSecondVisitor();
					visitorS->visit(treeS);
					texts_size = visitorS->texts.size();
					for(int i=0;i<texts_size;i++){
						if(find(texts.begin(),texts.end(),visitorS->texts[i])!=texts.end()){
                        			}else if(visitorS->texts[i].length()>MAXTEXT){
						}else{
							texts.push_back(visitorS->texts[i]);
						}
					}
          			delete visitorS;
				}

				interval_size = intervals.size();
				texts_size = texts.size();
                cout << interval_size << endl;
                cout << texts_size << endl;

				for(int i=0;i<interval_size;i++){
					for(int j=0;j<texts_size;j++){
						rewriter.replace(intervals[i].a,intervals[i].b,texts[j]);
                        cout << 1111 <<endl;
						ret[num_of_samples++]=rewriter.getText();
						if(num_of_samples>MAXSAMPLES){
							break;
						}
					}
					if(num_of_samples>MAXSAMPLES){
						break;
					}
				}
			}catch(range_error e){
				std::cerr<<"range_error"<<second<<endl;
			}
		}
	}catch(range_error e){
		//std::cerr<<"range_error:"<<target<<endl;
	}

	return num_of_samples;
}

void fuzz(int index, char** result, size_t* retlen){
  *retlen=ret[index].length();
  *result=strdup(ret[index].c_str());
  //result=(char*)malloc(retlen+1);
  //strcpy(result,ret[index].c_str());
}

int main(){
  	//ifstream in;
	//string target;
  	//in.open("./test.md");
	//while(in>>target){
	//}
    ifstream ifs("test.md");
    string target( (std::istreambuf_iterator<char>(ifs) ),
                       (std::istreambuf_iterator<char>()));
    ifstream ifs1("source.md");
    string second( (std::istreambuf_iterator<char>(ifs1) ),
                       (std::istreambuf_iterator<char>()));

  	int len = target.length();
  	int lenS= second.length();
    cout <<target << endl;
  	int num_of_samples=parse(target.c_str(),len,second.c_str(),lenS);
  	for(int i=0;i<num_of_samples;i++){
     	char* retbuf=nullptr;
     	size_t retlen=0;
     	fuzz(i,&retbuf,&retlen);
     	cout<<retlen<<retbuf<<endl;
  	}
  	cout<<num_of_samples<<endl;
}
/*
void getFiles(string path, vector<string>& files){
	DIR *dir;
	struct dirent *dp;
	if((dir=opendir(path.c_str()))==NULL){
		cout<<"Error"<<errno<<path<<endl;
	}
	while((dp=readdir(dir))!=NULL){
		files.push_back(string(dp->d_name));
	}
	closedir(dir);
}

int main(){
	string filePath="/home/b/XML/";
	vector<string> files;

	getFiles(filePath,files);

	char str[30];
	int size=files.size();
	for(int i=0;i<size;i++){
		cout<<files[i].c_str()<<endl;
	}
}
*/

