# Generated from E:\Dropbox\xml\XMLParser.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\5\2\24\n\2\3\2\7\2\27\n\2\f\2\16\2\32")
        buf.write("\13\2\3\2\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\3\3\3\7\3%\n")
        buf.write("\3\f\3\16\3(\13\3\3\3\3\3\3\4\5\4-\n\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4\64\n\4\3\4\5\4\67\n\4\7\49\n\4\f\4\16\4<\13\4")
        buf.write("\3\5\3\5\3\5\7\5A\n\5\f\5\16\5D\13\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\7\5P\n\5\f\5\16\5S\13\5\3\5\5\5")
        buf.write("V\n\5\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\2\2")
        buf.write("\n\2\4\6\b\n\f\16\20\2\5\3\2\6\7\4\2\b\b\13\13\5\2\3\3")
        buf.write("\b\b\24\24\2g\2\23\3\2\2\2\4\"\3\2\2\2\6,\3\2\2\2\bU\3")
        buf.write("\2\2\2\nW\3\2\2\2\fY\3\2\2\2\16]\3\2\2\2\20_\3\2\2\2\22")
        buf.write("\24\5\4\3\2\23\22\3\2\2\2\23\24\3\2\2\2\24\30\3\2\2\2")
        buf.write("\25\27\5\20\t\2\26\25\3\2\2\2\27\32\3\2\2\2\30\26\3\2")
        buf.write("\2\2\30\31\3\2\2\2\31\33\3\2\2\2\32\30\3\2\2\2\33\37\5")
        buf.write("\b\5\2\34\36\5\20\t\2\35\34\3\2\2\2\36!\3\2\2\2\37\35")
        buf.write("\3\2\2\2\37 \3\2\2\2 \3\3\2\2\2!\37\3\2\2\2\"&\7\n\2\2")
        buf.write("#%\5\f\7\2$#\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'")
        buf.write(")\3\2\2\2(&\3\2\2\2)*\7\r\2\2*\5\3\2\2\2+-\5\16\b\2,+")
        buf.write("\3\2\2\2,-\3\2\2\2-:\3\2\2\2.\64\5\b\5\2/\64\5\n\6\2\60")
        buf.write("\64\7\4\2\2\61\64\7\24\2\2\62\64\7\3\2\2\63.\3\2\2\2\63")
        buf.write("/\3\2\2\2\63\60\3\2\2\2\63\61\3\2\2\2\63\62\3\2\2\2\64")
        buf.write("\66\3\2\2\2\65\67\5\16\b\2\66\65\3\2\2\2\66\67\3\2\2\2")
        buf.write("\679\3\2\2\28\63\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2")
        buf.write(";\7\3\2\2\2<:\3\2\2\2=>\7\t\2\2>B\7\22\2\2?A\5\f\7\2@")
        buf.write("?\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2CE\3\2\2\2DB\3")
        buf.write("\2\2\2EF\7\f\2\2FG\5\6\4\2GH\7\t\2\2HI\7\17\2\2IJ\7\22")
        buf.write("\2\2JK\7\f\2\2KV\3\2\2\2LM\7\t\2\2MQ\7\22\2\2NP\5\f\7")
        buf.write("\2ON\3\2\2\2PS\3\2\2\2QO\3\2\2\2QR\3\2\2\2RT\3\2\2\2S")
        buf.write("Q\3\2\2\2TV\7\16\2\2U=\3\2\2\2UL\3\2\2\2V\t\3\2\2\2WX")
        buf.write("\t\2\2\2X\13\3\2\2\2YZ\7\22\2\2Z[\7\20\2\2[\\\7\21\2\2")
        buf.write("\\\r\3\2\2\2]^\t\3\2\2^\17\3\2\2\2_`\t\4\2\2`\21\3\2\2")
        buf.write("\2\r\23\30\37&,\63\66:BQU")
        return buf.getvalue()


class XMLParser ( Parser ):

    grammarFileName = "XMLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'<'", "<INVALID>", 
                     "<INVALID>", "'>'", "<INVALID>", "'/>'", "'/'", "'='" ]

    symbolicNames = [ "<INVALID>", "COMMENT", "CDATA", "DTD", "EntityRef", 
                      "CharRef", "SEA_WS", "OPEN", "XMLDeclOpen", "TEXT", 
                      "CLOSE", "SPECIAL_CLOSE", "SLASH_CLOSE", "SLASH", 
                      "EQUALS", "STRING", "Name", "S", "PI" ]

    RULE_document = 0
    RULE_prolog = 1
    RULE_content = 2
    RULE_element = 3
    RULE_reference = 4
    RULE_attribute = 5
    RULE_chardata = 6
    RULE_misc = 7

    ruleNames =  [ "document", "prolog", "content", "element", "reference", 
                   "attribute", "chardata", "misc" ]

    EOF = Token.EOF
    COMMENT=1
    CDATA=2
    DTD=3
    EntityRef=4
    CharRef=5
    SEA_WS=6
    OPEN=7
    XMLDeclOpen=8
    TEXT=9
    CLOSE=10
    SPECIAL_CLOSE=11
    SLASH_CLOSE=12
    SLASH=13
    EQUALS=14
    STRING=15
    Name=16
    S=17
    PI=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class DocumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(XMLParser.ElementContext,0)


        def prolog(self):
            return self.getTypedRuleContext(XMLParser.PrologContext,0)


        def misc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.MiscContext)
            else:
                return self.getTypedRuleContext(XMLParser.MiscContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_document

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDocument" ):
                return visitor.visitDocument(self)
            else:
                return visitor.visitChildren(self)




    def document(self):

        localctx = XMLParser.DocumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_document)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==XMLParser.XMLDeclOpen:
                self.state = 16
                self.prolog()


            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << XMLParser.COMMENT) | (1 << XMLParser.SEA_WS) | (1 << XMLParser.PI))) != 0):
                self.state = 19
                self.misc()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
            self.element()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << XMLParser.COMMENT) | (1 << XMLParser.SEA_WS) | (1 << XMLParser.PI))) != 0):
                self.state = 26
                self.misc()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrologContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def XMLDeclOpen(self):
            return self.getToken(XMLParser.XMLDeclOpen, 0)

        def SPECIAL_CLOSE(self):
            return self.getToken(XMLParser.SPECIAL_CLOSE, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_prolog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProlog" ):
                return visitor.visitProlog(self)
            else:
                return visitor.visitChildren(self)




    def prolog(self):

        localctx = XMLParser.PrologContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prolog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(XMLParser.XMLDeclOpen)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==XMLParser.Name:
                self.state = 33
                self.attribute()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(XMLParser.SPECIAL_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chardata(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ChardataContext)
            else:
                return self.getTypedRuleContext(XMLParser.ChardataContext,i)


        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ElementContext)
            else:
                return self.getTypedRuleContext(XMLParser.ElementContext,i)


        def reference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.ReferenceContext)
            else:
                return self.getTypedRuleContext(XMLParser.ReferenceContext,i)


        def CDATA(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.CDATA)
            else:
                return self.getToken(XMLParser.CDATA, i)

        def PI(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.PI)
            else:
                return self.getToken(XMLParser.PI, i)

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.COMMENT)
            else:
                return self.getToken(XMLParser.COMMENT, i)

        def getRuleIndex(self):
            return XMLParser.RULE_content

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent" ):
                return visitor.visitContent(self)
            else:
                return visitor.visitChildren(self)




    def content(self):

        localctx = XMLParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==XMLParser.SEA_WS or _la==XMLParser.TEXT:
                self.state = 41
                self.chardata()


            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 49
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [XMLParser.OPEN]:
                        self.state = 44
                        self.element()
                        pass
                    elif token in [XMLParser.EntityRef, XMLParser.CharRef]:
                        self.state = 45
                        self.reference()
                        pass
                    elif token in [XMLParser.CDATA]:
                        self.state = 46
                        self.match(XMLParser.CDATA)
                        pass
                    elif token in [XMLParser.PI]:
                        self.state = 47
                        self.match(XMLParser.PI)
                        pass
                    elif token in [XMLParser.COMMENT]:
                        self.state = 48
                        self.match(XMLParser.COMMENT)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 52
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==XMLParser.SEA_WS or _la==XMLParser.TEXT:
                        self.state = 51
                        self.chardata()

             
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self, i:int=None):
            if i is None:
                return self.getTokens(XMLParser.Name)
            else:
                return self.getToken(XMLParser.Name, i)

        def content(self):
            return self.getTypedRuleContext(XMLParser.ContentContext,0)


        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(XMLParser.AttributeContext)
            else:
                return self.getTypedRuleContext(XMLParser.AttributeContext,i)


        def getRuleIndex(self):
            return XMLParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = XMLParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(XMLParser.OPEN)
                self.state = 60
                self.match(XMLParser.Name)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==XMLParser.Name:
                    self.state = 61
                    self.attribute()
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 67
                self.match(XMLParser.CLOSE)
                self.state = 68
                self.content()
                self.state = 69
                self.match(XMLParser.OPEN)
                self.state = 70
                self.match(XMLParser.SLASH)
                self.state = 71
                self.match(XMLParser.Name)
                self.state = 72
                self.match(XMLParser.CLOSE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(XMLParser.OPEN)
                self.state = 75
                self.match(XMLParser.Name)
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==XMLParser.Name:
                    self.state = 76
                    self.attribute()
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 82
                self.match(XMLParser.SLASH_CLOSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReferenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EntityRef(self):
            return self.getToken(XMLParser.EntityRef, 0)

        def CharRef(self):
            return self.getToken(XMLParser.CharRef, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_reference

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReference" ):
                return visitor.visitReference(self)
            else:
                return visitor.visitChildren(self)




    def reference(self):

        localctx = XMLParser.ReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_reference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not(_la==XMLParser.EntityRef or _la==XMLParser.CharRef):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Name(self):
            return self.getToken(XMLParser.Name, 0)

        def STRING(self):
            return self.getToken(XMLParser.STRING, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = XMLParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(XMLParser.Name)
            self.state = 88
            self.match(XMLParser.EQUALS)
            self.state = 89
            self.match(XMLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ChardataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(XMLParser.TEXT, 0)

        def SEA_WS(self):
            return self.getToken(XMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_chardata

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChardata" ):
                return visitor.visitChardata(self)
            else:
                return visitor.visitChildren(self)




    def chardata(self):

        localctx = XMLParser.ChardataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_chardata)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not(_la==XMLParser.SEA_WS or _la==XMLParser.TEXT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MiscContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(XMLParser.COMMENT, 0)

        def PI(self):
            return self.getToken(XMLParser.PI, 0)

        def SEA_WS(self):
            return self.getToken(XMLParser.SEA_WS, 0)

        def getRuleIndex(self):
            return XMLParser.RULE_misc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMisc" ):
                return visitor.visitMisc(self)
            else:
                return visitor.visitChildren(self)




    def misc(self):

        localctx = XMLParser.MiscContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_misc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << XMLParser.COMMENT) | (1 << XMLParser.SEA_WS) | (1 << XMLParser.PI))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





