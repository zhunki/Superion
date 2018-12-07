# Generated from E:\Dropbox\pyjsparser\ECMAScript.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ECMAScriptParser import ECMAScriptParser
else:
    from ECMAScriptParser import ECMAScriptParser

# This class defines a complete generic visitor for a parse tree produced by ECMAScriptParser.

class ECMAScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ECMAScriptParser#program.
    def visitProgram(self, ctx:ECMAScriptParser.ProgramContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#sourceElements.
    def visitSourceElements(self, ctx:ECMAScriptParser.SourceElementsContext):
        gl.chunk.setdefault(1,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(1,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#sourceElement.
    def visitSourceElement(self, ctx:ECMAScriptParser.SourceElementContext):
        gl.chunk.setdefault(2,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(2,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#statement.
    def visitStatement(self, ctx:ECMAScriptParser.StatementContext):
        gl.chunk.setdefault(3,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(3,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#block.
    def visitBlock(self, ctx:ECMAScriptParser.BlockContext):
        gl.chunk.setdefault(4,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(4,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#statementList.
    def visitStatementList(self, ctx:ECMAScriptParser.StatementListContext):
        gl.chunk.setdefault(5,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(5,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#variableStatement.
    def visitVariableStatement(self, ctx:ECMAScriptParser.VariableStatementContext):
        gl.chunk.setdefault(6,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(6,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx:ECMAScriptParser.VariableDeclarationListContext):
        gl.chunk.setdefault(7,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(7,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:ECMAScriptParser.VariableDeclarationContext):
        gl.chunk.setdefault(8,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(8,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#initialiser.
    def visitInitialiser(self, ctx:ECMAScriptParser.InitialiserContext):
        gl.chunk.setdefault(9,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(9,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#emptyStatement.
    def visitEmptyStatement(self, ctx:ECMAScriptParser.EmptyStatementContext):
        gl.chunk.setdefault(10,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(10,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx:ECMAScriptParser.ExpressionStatementContext):
        gl.chunk.setdefault(11,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(11,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ifStatement.
    def visitIfStatement(self, ctx:ECMAScriptParser.IfStatementContext):
        gl.chunk.setdefault(12,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(12,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#DoStatement.
    def visitDoStatement(self, ctx:ECMAScriptParser.DoStatementContext):
        gl.chunk.setdefault(13,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(13,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#WhileStatement.
    def visitWhileStatement(self, ctx:ECMAScriptParser.WhileStatementContext):
        gl.chunk.setdefault(14,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(14,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForStatement.
    def visitForStatement(self, ctx:ECMAScriptParser.ForStatementContext):
        gl.chunk.setdefault(15,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(15,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForVarStatement.
    def visitForVarStatement(self, ctx:ECMAScriptParser.ForVarStatementContext):
        gl.chunk.setdefault(16,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(16,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForInStatement.
    def visitForInStatement(self, ctx:ECMAScriptParser.ForInStatementContext):
        gl.chunk.setdefault(17,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(17,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForVarInStatement.
    def visitForVarInStatement(self, ctx:ECMAScriptParser.ForVarInStatementContext):
        gl.chunk.setdefault(18,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(18,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#continueStatement.
    def visitContinueStatement(self, ctx:ECMAScriptParser.ContinueStatementContext):
        gl.chunk.setdefault(19,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(19,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#breakStatement.
    def visitBreakStatement(self, ctx:ECMAScriptParser.BreakStatementContext):
        gl.chunk.setdefault(20,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(20,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#returnStatement.
    def visitReturnStatement(self, ctx:ECMAScriptParser.ReturnStatementContext):
        gl.chunk.setdefault(21,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(21,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#withStatement.
    def visitWithStatement(self, ctx:ECMAScriptParser.WithStatementContext):
        gl.chunk.setdefault(22,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(22,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#switchStatement.
    def visitSwitchStatement(self, ctx:ECMAScriptParser.SwitchStatementContext):
        gl.chunk.setdefault(23,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(23,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#caseBlock.
    def visitCaseBlock(self, ctx:ECMAScriptParser.CaseBlockContext):
        gl.chunk.setdefault(24,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(24,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#caseClauses.
    def visitCaseClauses(self, ctx:ECMAScriptParser.CaseClausesContext):
        gl.chunk.setdefault(25,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(25,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#caseClause.
    def visitCaseClause(self, ctx:ECMAScriptParser.CaseClauseContext):
        gl.chunk.setdefault(26,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(26,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#defaultClause.
    def visitDefaultClause(self, ctx:ECMAScriptParser.DefaultClauseContext):
        gl.chunk.setdefault(27,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(27,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#labelledStatement.
    def visitLabelledStatement(self, ctx:ECMAScriptParser.LabelledStatementContext):
        gl.chunk.setdefault(28,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(28,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#throwStatement.
    def visitThrowStatement(self, ctx:ECMAScriptParser.ThrowStatementContext):
        gl.chunk.setdefault(29,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(29,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#tryStatement.
    def visitTryStatement(self, ctx:ECMAScriptParser.TryStatementContext):
        gl.chunk.setdefault(30,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(30,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#catchProduction.
    def visitCatchProduction(self, ctx:ECMAScriptParser.CatchProductionContext):
        gl.chunk.setdefault(31,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(31,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#finallyProduction.
    def visitFinallyProduction(self, ctx:ECMAScriptParser.FinallyProductionContext):
        gl.chunk.setdefault(32,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(32,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#debuggerStatement.
    def visitDebuggerStatement(self, ctx:ECMAScriptParser.DebuggerStatementContext):
        gl.chunk.setdefault(33,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(33,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:ECMAScriptParser.FunctionDeclarationContext):
        gl.chunk.setdefault(34,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(34,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#formalParameterList.
    def visitFormalParameterList(self, ctx:ECMAScriptParser.FormalParameterListContext):
        gl.chunk.setdefault(35,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(35,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#functionBody.
    def visitFunctionBody(self, ctx:ECMAScriptParser.FunctionBodyContext):
        gl.chunk.setdefault(36,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(36,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:ECMAScriptParser.ArrayLiteralContext):
        gl.chunk.setdefault(37,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(37,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#elementList.
    def visitElementList(self, ctx:ECMAScriptParser.ElementListContext):
        gl.chunk.setdefault(38,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(38,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#elision.
    def visitElision(self, ctx:ECMAScriptParser.ElisionContext):
        gl.chunk.setdefault(39,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(39,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#objectLiteral.
    def visitObjectLiteral(self, ctx:ECMAScriptParser.ObjectLiteralContext):
        gl.chunk.setdefault(40,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(40,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#propertyNameAndValueList.
    def visitPropertyNameAndValueList(self, ctx:ECMAScriptParser.PropertyNameAndValueListContext):
        gl.chunk.setdefault(41,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(41,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PropertyExpressionAssignment.
    def visitPropertyExpressionAssignment(self, ctx:ECMAScriptParser.PropertyExpressionAssignmentContext):
        gl.chunk.setdefault(42,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(42,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PropertyGetter.
    def visitPropertyGetter(self, ctx:ECMAScriptParser.PropertyGetterContext):
        gl.chunk.setdefault(43,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(43,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PropertySetter.
    def visitPropertySetter(self, ctx:ECMAScriptParser.PropertySetterContext):
        gl.chunk.setdefault(44,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(44,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#propertyName.
    def visitPropertyName(self, ctx:ECMAScriptParser.PropertyNameContext):
        gl.chunk.setdefault(45,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(45,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#propertySetParameterList.
    def visitPropertySetParameterList(self, ctx:ECMAScriptParser.PropertySetParameterListContext):
        gl.chunk.setdefault(46,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(46,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#arguments.
    def visitArguments(self, ctx:ECMAScriptParser.ArgumentsContext):
        gl.chunk.setdefault(47,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(47,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#argumentList.
    def visitArgumentList(self, ctx:ECMAScriptParser.ArgumentListContext):
        gl.chunk.setdefault(48,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(48,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#expressionSequence.
    def visitExpressionSequence(self, ctx:ECMAScriptParser.ExpressionSequenceContext):
        gl.chunk.setdefault(49,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(49,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#TernaryExpression.
    def visitTernaryExpression(self, ctx:ECMAScriptParser.TernaryExpressionContext):
        gl.chunk.setdefault(50,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(50,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#LogicalAndExpression.
    def visitLogicalAndExpression(self, ctx:ECMAScriptParser.LogicalAndExpressionContext):
        gl.chunk.setdefault(51,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(51,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PreIncrementExpression.
    def visitPreIncrementExpression(self, ctx:ECMAScriptParser.PreIncrementExpressionContext):
        gl.chunk.setdefault(52,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(52,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#ObjectLiteralExpression.
    def visitObjectLiteralExpression(self, ctx:ECMAScriptParser.ObjectLiteralExpressionContext):
        gl.chunk.setdefault(53,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(53,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#InExpression.
    def visitInExpression(self, ctx:ECMAScriptParser.InExpressionContext):
        gl.chunk.setdefault(54,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(54,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#LogicalOrExpression.
    def visitLogicalOrExpression(self, ctx:ECMAScriptParser.LogicalOrExpressionContext):
        gl.chunk.setdefault(55,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(55,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#NotExpression.
    def visitNotExpression(self, ctx:ECMAScriptParser.NotExpressionContext):
        gl.chunk.setdefault(56,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(56,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PreDecreaseExpression.
    def visitPreDecreaseExpression(self, ctx:ECMAScriptParser.PreDecreaseExpressionContext):
        gl.chunk.setdefault(57,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(57,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#ArgumentsExpression.
    def visitArgumentsExpression(self, ctx:ECMAScriptParser.ArgumentsExpressionContext):
        gl.chunk.setdefault(58,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(58,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#ThisExpression.
    def visitThisExpression(self, ctx:ECMAScriptParser.ThisExpressionContext):
        gl.chunk.setdefault(59,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(59,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#FunctionExpression.
    def visitFunctionExpression(self, ctx:ECMAScriptParser.FunctionExpressionContext):
        gl.chunk.setdefault(60,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(60,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#UnaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:ECMAScriptParser.UnaryMinusExpressionContext):
        gl.chunk.setdefault(61,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(61,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx:ECMAScriptParser.AssignmentExpressionContext):
        gl.chunk.setdefault(62,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(62,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PostDecreaseExpression.
    def visitPostDecreaseExpression(self, ctx:ECMAScriptParser.PostDecreaseExpressionContext):
        gl.chunk.setdefault(63,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(63,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#TypeofExpression.
    def visitTypeofExpression(self, ctx:ECMAScriptParser.TypeofExpressionContext):
        gl.chunk.setdefault(64,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(64,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#InstanceofExpression.
    def visitInstanceofExpression(self, ctx:ECMAScriptParser.InstanceofExpressionContext):
        gl.chunk.setdefault(65,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(65,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#UnaryPlusExpression.
    def visitUnaryPlusExpression(self, ctx:ECMAScriptParser.UnaryPlusExpressionContext):
        gl.chunk.setdefault(66,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(66,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#DeleteExpression.
    def visitDeleteExpression(self, ctx:ECMAScriptParser.DeleteExpressionContext):
        gl.chunk.setdefault(67,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(67,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#EqualityExpression.
    def visitEqualityExpression(self, ctx:ECMAScriptParser.EqualityExpressionContext):
        gl.chunk.setdefault(68,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(68,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitXOrExpression.
    def visitBitXOrExpression(self, ctx:ECMAScriptParser.BitXOrExpressionContext):
        gl.chunk.setdefault(69,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(69,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:ECMAScriptParser.MultiplicativeExpressionContext):
        gl.chunk.setdefault(70,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(70,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitShiftExpression.
    def visitBitShiftExpression(self, ctx:ECMAScriptParser.BitShiftExpressionContext):
        gl.chunk.setdefault(71,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(71,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:ECMAScriptParser.ParenthesizedExpressionContext):
        gl.chunk.setdefault(72,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(72,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx:ECMAScriptParser.AdditiveExpressionContext):
        gl.chunk.setdefault(73,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(73,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#RelationalExpression.
    def visitRelationalExpression(self, ctx:ECMAScriptParser.RelationalExpressionContext):
        gl.chunk.setdefault(74,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(74,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#PostIncrementExpression.
    def visitPostIncrementExpression(self, ctx:ECMAScriptParser.PostIncrementExpressionContext):
        gl.chunk.setdefault(75,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(75,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitNotExpression.
    def visitBitNotExpression(self, ctx:ECMAScriptParser.BitNotExpressionContext):
        gl.chunk.setdefault(76,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(76,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#NewExpression.
    def visitNewExpression(self, ctx:ECMAScriptParser.NewExpressionContext):
        gl.chunk.setdefault(77,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(77,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx:ECMAScriptParser.LiteralExpressionContext):
        gl.chunk.setdefault(78,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(78,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ArrayLiteralExpression.
    def visitArrayLiteralExpression(self, ctx:ECMAScriptParser.ArrayLiteralExpressionContext):
        gl.chunk.setdefault(79,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(79,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx:ECMAScriptParser.MemberDotExpressionContext):
        gl.chunk.setdefault(80,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(80,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#MemberIndexExpression.
    def visitMemberIndexExpression(self, ctx:ECMAScriptParser.MemberIndexExpressionContext):
        gl.chunk.setdefault(81,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(81,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx:ECMAScriptParser.IdentifierExpressionContext):
        gl.chunk.setdefault(82,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(82,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitAndExpression.
    def visitBitAndExpression(self, ctx:ECMAScriptParser.BitAndExpressionContext):
        gl.chunk.setdefault(83,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(83,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitOrExpression.
    def visitBitOrExpression(self, ctx:ECMAScriptParser.BitOrExpressionContext):
        gl.chunk.setdefault(84,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(84,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#AssignmentOperatorExpression.
    def visitAssignmentOperatorExpression(self, ctx:ECMAScriptParser.AssignmentOperatorExpressionContext):
        gl.chunk.setdefault(85,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(85,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#VoidExpression.
    def visitVoidExpression(self, ctx:ECMAScriptParser.VoidExpressionContext):
        gl.chunk.setdefault(86,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(86,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:ECMAScriptParser.AssignmentOperatorContext):
        gl.chunk.setdefault(87,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(87,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#literal.
    def visitLiteral(self, ctx:ECMAScriptParser.LiteralContext):
        gl.chunk.setdefault(88,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(88,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#numericLiteral.
    def visitNumericLiteral(self, ctx:ECMAScriptParser.NumericLiteralContext):
        gl.chunk.setdefault(89,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(89,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#identifierName.
    def visitIdentifierName(self, ctx:ECMAScriptParser.IdentifierNameContext):
        gl.chunk.setdefault(90,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(90,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#reservedWord.
    def visitReservedWord(self, ctx:ECMAScriptParser.ReservedWordContext):
        gl.chunk.setdefault(91,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(91,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#keyword.
    def visitKeyword(self, ctx:ECMAScriptParser.KeywordContext):
        gl.chunk.setdefault(92,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(92,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#futureReservedWord.
    def visitFutureReservedWord(self, ctx:ECMAScriptParser.FutureReservedWordContext):
        gl.chunk.setdefault(93,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(93,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#getter.
    def visitGetter(self, ctx:ECMAScriptParser.GetterContext):
        gl.chunk.setdefault(94,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(94,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#setter.
    def visitSetter(self, ctx:ECMAScriptParser.SetterContext):
        gl.chunk.setdefault(95,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(95,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#eos.
    def visitEos(self, ctx:ECMAScriptParser.EosContext):
        gl.chunk.setdefault(96,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(96,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#eof.
    def visitEof(self, ctx:ECMAScriptParser.EofContext):
        return self.visitChildren(ctx)



del ECMAScriptParser
