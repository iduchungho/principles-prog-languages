# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraytype.
    def visitArraytype(self, ctx:MT22Parser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#number.
    def visitNumber(self, ctx:MT22Parser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#eletype.
    def visitEletype(self, ctx:MT22Parser.EletypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension.
    def visitDimension(self, ctx:MT22Parser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardeclNoEq.
    def visitVardeclNoEq(self, ctx:MT22Parser.VardeclNoEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardeclEq.
    def visitVardeclEq(self, ctx:MT22Parser.VardeclEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignment.
    def visitAssignment(self, ctx:MT22Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylist.
    def visitArraylist(self, ctx:MT22Parser.ArraylistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#compare.
    def visitCompare(self, ctx:MT22Parser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr8.
    def visitExpr8(self, ctx:MT22Parser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#factor.
    def visitFactor(self, ctx:MT22Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayCell.
    def visitArrayCell(self, ctx:MT22Parser.ArrayCellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funccall.
    def visitFunccall(self, ctx:MT22Parser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignStmt.
    def visitAssignStmt(self, ctx:MT22Parser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifStmt.
    def visitIfStmt(self, ctx:MT22Parser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forStmt.
    def visitForStmt(self, ctx:MT22Parser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initExpr.
    def visitInitExpr(self, ctx:MT22Parser.InitExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#conditionExpr.
    def visitConditionExpr(self, ctx:MT22Parser.ConditionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operator.
    def visitOperator(self, ctx:MT22Parser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#updateExpr.
    def visitUpdateExpr(self, ctx:MT22Parser.UpdateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whileStmt.
    def visitWhileStmt(self, ctx:MT22Parser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#doWhileStmt.
    def visitDoWhileStmt(self, ctx:MT22Parser.DoWhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callStmt.
    def visitCallStmt(self, ctx:MT22Parser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockStmt.
    def visitBlockStmt(self, ctx:MT22Parser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtTerm.
    def visitStmtTerm(self, ctx:MT22Parser.StmtTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmtList.
    def visitStmtList(self, ctx:MT22Parser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakStmt.
    def visitBreakStmt(self, ctx:MT22Parser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continueStmt.
    def visitContinueStmt(self, ctx:MT22Parser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnStmt.
    def visitReturnStmt(self, ctx:MT22Parser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inheritance.
    def visitInheritance(self, ctx:MT22Parser.InheritanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramterList.
    def visitParamterList(self, ctx:MT22Parser.ParamterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramterListTerm.
    def visitParamterListTerm(self, ctx:MT22Parser.ParamterListTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnType.
    def visitReturnType(self, ctx:MT22Parser.ReturnTypeContext):
        return self.visitChildren(ctx)



del MT22Parser