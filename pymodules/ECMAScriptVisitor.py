# Generated from E:\Dropbox\pyjsparser\ECMAScript.g0 by ANTLR 0.0
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
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#sourceElement.
    def visitSourceElement(self, ctx:ECMAScriptParser.SourceElementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#statement.
    def visitStatement(self, ctx:ECMAScriptParser.StatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#block.
    def visitBlock(self, ctx:ECMAScriptParser.BlockContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#statementList.
    def visitStatementList(self, ctx:ECMAScriptParser.StatementListContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#variableStatement.
    def visitVariableStatement(self, ctx:ECMAScriptParser.VariableStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx:ECMAScriptParser.VariableDeclarationListContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:ECMAScriptParser.VariableDeclarationContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#initialiser.
    def visitInitialiser(self, ctx:ECMAScriptParser.InitialiserContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#emptyStatement.
    def visitEmptyStatement(self, ctx:ECMAScriptParser.EmptyStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx:ECMAScriptParser.ExpressionStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ifStatement.
    def visitIfStatement(self, ctx:ECMAScriptParser.IfStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#DoStatement.
    def visitDoStatement(self, ctx:ECMAScriptParser.DoStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#WhileStatement.
    def visitWhileStatement(self, ctx:ECMAScriptParser.WhileStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForStatement.
    def visitForStatement(self, ctx:ECMAScriptParser.ForStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForVarStatement.
    def visitForVarStatement(self, ctx:ECMAScriptParser.ForVarStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForInStatement.
    def visitForInStatement(self, ctx:ECMAScriptParser.ForInStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ForVarInStatement.
    def visitForVarInStatement(self, ctx:ECMAScriptParser.ForVarInStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#continueStatement.
    def visitContinueStatement(self, ctx:ECMAScriptParser.ContinueStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#breakStatement.
    def visitBreakStatement(self, ctx:ECMAScriptParser.BreakStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#returnStatement.
    def visitReturnStatement(self, ctx:ECMAScriptParser.ReturnStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#withStatement.
    def visitWithStatement(self, ctx:ECMAScriptParser.WithStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#switchStatement.
    def visitSwitchStatement(self, ctx:ECMAScriptParser.SwitchStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#caseBlock.
    def visitCaseBlock(self, ctx:ECMAScriptParser.CaseBlockContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#caseClauses.
    def visitCaseClauses(self, ctx:ECMAScriptParser.CaseClausesContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#caseClause.
    def visitCaseClause(self, ctx:ECMAScriptParser.CaseClauseContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#defaultClause.
    def visitDefaultClause(self, ctx:ECMAScriptParser.DefaultClauseContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#labelledStatement.
    def visitLabelledStatement(self, ctx:ECMAScriptParser.LabelledStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#throwStatement.
    def visitThrowStatement(self, ctx:ECMAScriptParser.ThrowStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#tryStatement.
    def visitTryStatement(self, ctx:ECMAScriptParser.TryStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#catchProduction.
    def visitCatchProduction(self, ctx:ECMAScriptParser.CatchProductionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#finallyProduction.
    def visitFinallyProduction(self, ctx:ECMAScriptParser.FinallyProductionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#debuggerStatement.
    def visitDebuggerStatement(self, ctx:ECMAScriptParser.DebuggerStatementContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:ECMAScriptParser.FunctionDeclarationContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#formalParameterList.
    def visitFormalParameterList(self, ctx:ECMAScriptParser.FormalParameterListContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#functionBody.
    def visitFunctionBody(self, ctx:ECMAScriptParser.FunctionBodyContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:ECMAScriptParser.ArrayLiteralContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#elementList.
    def visitElementList(self, ctx:ECMAScriptParser.ElementListContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#elision.
    def visitElision(self, ctx:ECMAScriptParser.ElisionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#objectLiteral.
    def visitObjectLiteral(self, ctx:ECMAScriptParser.ObjectLiteralContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#propertyNameAndValueList.
    def visitPropertyNameAndValueList(self, ctx:ECMAScriptParser.PropertyNameAndValueListContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PropertyExpressionAssignment.
    def visitPropertyExpressionAssignment(self, ctx:ECMAScriptParser.PropertyExpressionAssignmentContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PropertyGetter.
    def visitPropertyGetter(self, ctx:ECMAScriptParser.PropertyGetterContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PropertySetter.
    def visitPropertySetter(self, ctx:ECMAScriptParser.PropertySetterContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#propertyName.
    def visitPropertyName(self, ctx:ECMAScriptParser.PropertyNameContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#propertySetParameterList.
    def visitPropertySetParameterList(self, ctx:ECMAScriptParser.PropertySetParameterListContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#arguments.
    def visitArguments(self, ctx:ECMAScriptParser.ArgumentsContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#argumentList.
    def visitArgumentList(self, ctx:ECMAScriptParser.ArgumentListContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#expressionSequence.
    def visitExpressionSequence(self, ctx:ECMAScriptParser.ExpressionSequenceContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#TernaryExpression.
    def visitTernaryExpression(self, ctx:ECMAScriptParser.TernaryExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#LogicalAndExpression.
    def visitLogicalAndExpression(self, ctx:ECMAScriptParser.LogicalAndExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PreIncrementExpression.
    def visitPreIncrementExpression(self, ctx:ECMAScriptParser.PreIncrementExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#ObjectLiteralExpression.
    def visitObjectLiteralExpression(self, ctx:ECMAScriptParser.ObjectLiteralExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#InExpression.
    def visitInExpression(self, ctx:ECMAScriptParser.InExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#LogicalOrExpression.
    def visitLogicalOrExpression(self, ctx:ECMAScriptParser.LogicalOrExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#NotExpression.
    def visitNotExpression(self, ctx:ECMAScriptParser.NotExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PreDecreaseExpression.
    def visitPreDecreaseExpression(self, ctx:ECMAScriptParser.PreDecreaseExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#ArgumentsExpression.
    def visitArgumentsExpression(self, ctx:ECMAScriptParser.ArgumentsExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#ThisExpression.
    def visitThisExpression(self, ctx:ECMAScriptParser.ThisExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#FunctionExpression.
    def visitFunctionExpression(self, ctx:ECMAScriptParser.FunctionExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#UnaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:ECMAScriptParser.UnaryMinusExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx:ECMAScriptParser.AssignmentExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ECMAScriptParser#PostDecreaseExpression.
    def visitPostDecreaseExpression(self, ctx:ECMAScriptParser.PostDecreaseExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#TypeofExpression.
    def visitTypeofExpression(self, ctx:ECMAScriptParser.TypeofExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#InstanceofExpression.
    def visitInstanceofExpression(self, ctx:ECMAScriptParser.InstanceofExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#UnaryPlusExpression.
    def visitUnaryPlusExpression(self, ctx:ECMAScriptParser.UnaryPlusExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#DeleteExpression.
    def visitDeleteExpression(self, ctx:ECMAScriptParser.DeleteExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#EqualityExpression.
    def visitEqualityExpression(self, ctx:ECMAScriptParser.EqualityExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitXOrExpression.
    def visitBitXOrExpression(self, ctx:ECMAScriptParser.BitXOrExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:ECMAScriptParser.MultiplicativeExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitShiftExpression.
    def visitBitShiftExpression(self, ctx:ECMAScriptParser.BitShiftExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:ECMAScriptParser.ParenthesizedExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx:ECMAScriptParser.AdditiveExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#RelationalExpression.
    def visitRelationalExpression(self, ctx:ECMAScriptParser.RelationalExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#PostIncrementExpression.
    def visitPostIncrementExpression(self, ctx:ECMAScriptParser.PostIncrementExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitNotExpression.
    def visitBitNotExpression(self, ctx:ECMAScriptParser.BitNotExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#NewExpression.
    def visitNewExpression(self, ctx:ECMAScriptParser.NewExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx:ECMAScriptParser.LiteralExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#ArrayLiteralExpression.
    def visitArrayLiteralExpression(self, ctx:ECMAScriptParser.ArrayLiteralExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx:ECMAScriptParser.MemberDotExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#MemberIndexExpression.
    def visitMemberIndexExpression(self, ctx:ECMAScriptParser.MemberIndexExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx:ECMAScriptParser.IdentifierExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitAndExpression.
    def visitBitAndExpression(self, ctx:ECMAScriptParser.BitAndExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#BitOrExpression.
    def visitBitOrExpression(self, ctx:ECMAScriptParser.BitOrExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#AssignmentOperatorExpression.
    def visitAssignmentOperatorExpression(self, ctx:ECMAScriptParser.AssignmentOperatorExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#VoidExpression.
    def visitVoidExpression(self, ctx:ECMAScriptParser.VoidExpressionContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:ECMAScriptParser.AssignmentOperatorContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#literal.
    def visitLiteral(self, ctx:ECMAScriptParser.LiteralContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#numericLiteral.
    def visitNumericLiteral(self, ctx:ECMAScriptParser.NumericLiteralContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#identifierName.
    def visitIdentifierName(self, ctx:ECMAScriptParser.IdentifierNameContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#reservedWord.
    def visitReservedWord(self, ctx:ECMAScriptParser.ReservedWordContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#keyword.
    def visitKeyword(self, ctx:ECMAScriptParser.KeywordContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#futureReservedWord.
    def visitFutureReservedWord(self, ctx:ECMAScriptParser.FutureReservedWordContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#getter.
    def visitGetter(self, ctx:ECMAScriptParser.GetterContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#setter.
    def visitSetter(self, ctx:ECMAScriptParser.SetterContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#eos.
    def visitEos(self, ctx:ECMAScriptParser.EosContext):
        gl.chunk.setdefault(0,{})[ctx.getSourceInterval()]=1
        gl.code_fragments.setdefault(0,{})[gl.currentstream.getText(ctx.getSourceInterval())]=1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ECMAScriptParser#eof.
    def visitEof(self, ctx:ECMAScriptParser.EofContext):
        return self.visitChildren(ctx)



del ECMAScriptParser
