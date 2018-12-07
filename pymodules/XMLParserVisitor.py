# Generated from E:\Dropbox\xml\XMLParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .XMLParser import XMLParser
else:
    from XMLParser import XMLParser

# This class defines a complete generic visitor for a parse tree produced by XMLParser.

class XMLParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by XMLParser#document.
    def visitDocument(self, ctx:XMLParser.DocumentContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#prolog.
    def visitProlog(self, ctx:XMLParser.PrologContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#content.
    def visitContent(self, ctx:XMLParser.ContentContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#element.
    def visitElement(self, ctx:XMLParser.ElementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#reference.
    def visitReference(self, ctx:XMLParser.ReferenceContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#attribute.
    def visitAttribute(self, ctx:XMLParser.AttributeContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#chardata.
    def visitChardata(self, ctx:XMLParser.ChardataContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by XMLParser#misc.
    def visitMisc(self, ctx:XMLParser.MiscContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)



del XMLParser
