
// Generated from E:\Dropbox\fuzzing\jsparser\ECMAScript.g4 by ANTLR 4.7

#pragma once


#include "antlr4-runtime.h"
using namespace antlr4;



class  ECMAScriptLexer : public antlr4::Lexer {
public:
  enum {
    RegularExpressionLiteral = 1, LineTerminator = 2, OpenBracket = 3, CloseBracket = 4, 
    OpenParen = 5, CloseParen = 6, OpenBrace = 7, CloseBrace = 8, SemiColon = 9, 
    Comma = 10, Assign = 11, QuestionMark = 12, Colon = 13, Dot = 14, PlusPlus = 15, 
    MinusMinus = 16, Plus = 17, Minus = 18, BitNot = 19, Not = 20, Multiply = 21, 
    Divide = 22, Modulus = 23, RightShiftArithmetic = 24, LeftShiftArithmetic = 25, 
    RightShiftLogical = 26, LessThan = 27, MoreThan = 28, LessThanEquals = 29, 
    GreaterThanEquals = 30, Equals_ = 31, NotEquals = 32, IdentityEquals = 33, 
    IdentityNotEquals = 34, BitAnd = 35, BitXOr = 36, BitOr = 37, And = 38, 
    Or = 39, MultiplyAssign = 40, DivideAssign = 41, ModulusAssign = 42, 
    PlusAssign = 43, MinusAssign = 44, LeftShiftArithmeticAssign = 45, RightShiftArithmeticAssign = 46, 
    RightShiftLogicalAssign = 47, BitAndAssign = 48, BitXorAssign = 49, 
    BitOrAssign = 50, NullLiteral = 51, BooleanLiteral = 52, DecimalLiteral = 53, 
    HexIntegerLiteral = 54, OctalIntegerLiteral = 55, Break = 56, Do = 57, 
    Instanceof = 58, Typeof = 59, Case = 60, Else = 61, New = 62, Var = 63, 
    Catch = 64, Finally = 65, Return = 66, Void = 67, Continue = 68, For = 69, 
    Switch = 70, While = 71, Debugger = 72, Function = 73, This = 74, With = 75, 
    Default = 76, If = 77, Throw = 78, Delete = 79, In = 80, Try = 81, Class = 82, 
    Enum = 83, Extends = 84, Super = 85, Const = 86, Export = 87, Import = 88, 
    Implements = 89, Let = 90, Private = 91, Public = 92, Interface = 93, 
    Package = 94, Protected = 95, Static = 96, Yield = 97, Identifier = 98, 
    StringLiteral = 99, WhiteSpaces = 100, MultiLineComment = 101, SingleLineComment = 102, 
    HtmlComment = 103, UnexpectedCharacter = 104
  };

  ECMAScriptLexer(antlr4::CharStream *input);
  ~ECMAScriptLexer();


                   
      // A flag indicating if the lexer should operate in strict mode.
      // When set to true, FutureReservedWords are tokenized, when false,
      // an octal literal can be tokenized.
      bool strictMode = true;

      // The most recently produced token.
      Token *lastToken = NULL;

      ///<summary>Returns <c>true</c> iff the lexer operates in strict mode</summary>
      /// <returns><c>true</c> iff the lexer operates in strict mode.</returns>
      bool getStrictMode() {
          return this->strictMode;
      }

  	///<summary>Sets whether the lexer operates in strict mode or not.</summary>
  	///<param name="strictMode">the flag indicating the lexer operates in strict mode or not.</param>
      void setStrictMode(bool strictMode) {
          this->strictMode = strictMode;
      }

      ///<summary>Return the next token from the character stream and records this last
      ///token in case it resides on the default channel. This recorded token
      ///is used to determine when the lexer could possibly match a regex
      ///literal.</summary>
      ///<returns>the next token from the character stream.</returns>
      /// Token* nextToken() {
      ///     
      ///     // Get the next token.
      ///     Token* next = Lexer::nextToken();
      ///     
      ///     if (next->getChannel() == Lexer::DEFAULT_TOKEN_CHANNEL) {
      ///         // Keep track of the last token on the default channel.                                              
      ///         this->lastToken = next;
      ///     }
      ///     
      ///     return next;
      /// }

      std::unique_ptr<Token> nextToken() override {
	      std::unique_ptr<Token> next = Lexer::nextToken();
	      if (next.get()->getChannel()== Lexer::DEFAULT_TOKEN_CHANNEL) {
		      this->lastToken = next.get();
	      }
	      return next;
      }

      ///<summary>Returns <c>true</c> iff the lexer can match a regex literal.</summary>
      ///<returns><c>true</c> iff the lexer can match a regex literal.</returns>
      bool isRegexPossible() {
                                         
          if (this->lastToken == NULL) {
              // No token has been produced yet: at the start of the input,
              // no division is possible, so a regex literal _is_ possible.
              return true;
          }
          
          switch (this->lastToken->getType()) {
              case Identifier:
              case NullLiteral:
              case BooleanLiteral:
              case This:
              case CloseBracket:
              case CloseParen:
              case OctalIntegerLiteral:
              case DecimalLiteral:
              case HexIntegerLiteral:
              case StringLiteral:
              case PlusPlus:
              case MinusMinus:
                  // After any of the tokens above, no regex literal can follow.
                  return false;
              default:
                  // In all other cases, a regex literal _is_ possible.
                  return true;
          }
      }

  virtual std::string getGrammarFileName() const override;
  virtual const std::vector<std::string>& getRuleNames() const override;

  virtual const std::vector<std::string>& getChannelNames() const override;
  virtual const std::vector<std::string>& getModeNames() const override;
  virtual const std::vector<std::string>& getTokenNames() const override; // deprecated, use vocabulary instead
  virtual antlr4::dfa::Vocabulary& getVocabulary() const override;

  virtual const std::vector<uint16_t> getSerializedATN() const override;
  virtual const antlr4::atn::ATN& getATN() const override;

  virtual bool sempred(antlr4::RuleContext *_localctx, size_t ruleIndex, size_t predicateIndex) override;

private:
  static std::vector<antlr4::dfa::DFA> _decisionToDFA;
  static antlr4::atn::PredictionContextCache _sharedContextCache;
  static std::vector<std::string> _ruleNames;
  static std::vector<std::string> _tokenNames;
  static std::vector<std::string> _channelNames;
  static std::vector<std::string> _modeNames;

  static std::vector<std::string> _literalNames;
  static std::vector<std::string> _symbolicNames;
  static antlr4::dfa::Vocabulary _vocabulary;
  static antlr4::atn::ATN _atn;
  static std::vector<uint16_t> _serializedATN;


  // Individual action functions triggered by action() above.

  // Individual semantic predicate functions triggered by sempred() above.
  bool RegularExpressionLiteralSempred(antlr4::RuleContext *_localctx, size_t predicateIndex);
  bool OctalIntegerLiteralSempred(antlr4::RuleContext *_localctx, size_t predicateIndex);
  bool ImplementsSempred(antlr4::RuleContext *_localctx, size_t predicateIndex);
  bool LetSempred(antlr4::RuleContext *_localctx, size_t predicateIndex);
  bool PrivateSempred(antlr4::RuleContext *_localctx, size_t predicateIndex);
  bool PublicSempred(antlr4::RuleContext *_localctx, size_t predicateIndex);
  bool InterfaceSempred(antlr4::RuleContext *_localctx, size_t predicateIndex);
  bool PackageSempred(antlr4::RuleContext *_localctx, size_t predicateIndex);
  bool ProtectedSempred(antlr4::RuleContext *_localctx, size_t predicateIndex);
  bool StaticSempred(antlr4::RuleContext *_localctx, size_t predicateIndex);
  bool YieldSempred(antlr4::RuleContext *_localctx, size_t predicateIndex);

  struct Initializer {
    Initializer();
  };
  static Initializer _init;
};

