# Generated from dafny.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .dafnyParser import dafnyParser
else:
    from dafnyParser import dafnyParser

# This class defines a complete listener for a parse tree produced by dafnyParser.
class dafnyListener(ParseTreeListener):

    # Enter a parse tree produced by dafnyParser#boolLiteral.
    def enterBoolLiteral(self, ctx:dafnyParser.BoolLiteralContext):
        pass

    # Exit a parse tree produced by dafnyParser#boolLiteral.
    def exitBoolLiteral(self, ctx:dafnyParser.BoolLiteralContext):
        pass


    # Enter a parse tree produced by dafnyParser#intLiteral.
    def enterIntLiteral(self, ctx:dafnyParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by dafnyParser#intLiteral.
    def exitIntLiteral(self, ctx:dafnyParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by dafnyParser#realLiteral.
    def enterRealLiteral(self, ctx:dafnyParser.RealLiteralContext):
        pass

    # Exit a parse tree produced by dafnyParser#realLiteral.
    def exitRealLiteral(self, ctx:dafnyParser.RealLiteralContext):
        pass


    # Enter a parse tree produced by dafnyParser#charLiteral.
    def enterCharLiteral(self, ctx:dafnyParser.CharLiteralContext):
        pass

    # Exit a parse tree produced by dafnyParser#charLiteral.
    def exitCharLiteral(self, ctx:dafnyParser.CharLiteralContext):
        pass


    # Enter a parse tree produced by dafnyParser#stringToken.
    def enterStringToken(self, ctx:dafnyParser.StringTokenContext):
        pass

    # Exit a parse tree produced by dafnyParser#stringToken.
    def exitStringToken(self, ctx:dafnyParser.StringTokenContext):
        pass


    # Enter a parse tree produced by dafnyParser#unaryOperator.
    def enterUnaryOperator(self, ctx:dafnyParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by dafnyParser#unaryOperator.
    def exitUnaryOperator(self, ctx:dafnyParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by dafnyParser#upperIdentifier.
    def enterUpperIdentifier(self, ctx:dafnyParser.UpperIdentifierContext):
        pass

    # Exit a parse tree produced by dafnyParser#upperIdentifier.
    def exitUpperIdentifier(self, ctx:dafnyParser.UpperIdentifierContext):
        pass


    # Enter a parse tree produced by dafnyParser#identifier.
    def enterIdentifier(self, ctx:dafnyParser.IdentifierContext):
        pass

    # Exit a parse tree produced by dafnyParser#identifier.
    def exitIdentifier(self, ctx:dafnyParser.IdentifierContext):
        pass


    # Enter a parse tree produced by dafnyParser#topDecl.
    def enterTopDecl(self, ctx:dafnyParser.TopDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#topDecl.
    def exitTopDecl(self, ctx:dafnyParser.TopDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#sequence.
    def enterSequence(self, ctx:dafnyParser.SequenceContext):
        pass

    # Exit a parse tree produced by dafnyParser#sequence.
    def exitSequence(self, ctx:dafnyParser.SequenceContext):
        pass


    # Enter a parse tree produced by dafnyParser#genericInstantiation.
    def enterGenericInstantiation(self, ctx:dafnyParser.GenericInstantiationContext):
        pass

    # Exit a parse tree produced by dafnyParser#genericInstantiation.
    def exitGenericInstantiation(self, ctx:dafnyParser.GenericInstantiationContext):
        pass


    # Enter a parse tree produced by dafnyParser#type.
    def enterType(self, ctx:dafnyParser.TypeContext):
        pass

    # Exit a parse tree produced by dafnyParser#type.
    def exitType(self, ctx:dafnyParser.TypeContext):
        pass


    # Enter a parse tree produced by dafnyParser#arrayType.
    def enterArrayType(self, ctx:dafnyParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by dafnyParser#arrayType.
    def exitArrayType(self, ctx:dafnyParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by dafnyParser#mapType.
    def enterMapType(self, ctx:dafnyParser.MapTypeContext):
        pass

    # Exit a parse tree produced by dafnyParser#mapType.
    def exitMapType(self, ctx:dafnyParser.MapTypeContext):
        pass


    # Enter a parse tree produced by dafnyParser#setType.
    def enterSetType(self, ctx:dafnyParser.SetTypeContext):
        pass

    # Exit a parse tree produced by dafnyParser#setType.
    def exitSetType(self, ctx:dafnyParser.SetTypeContext):
        pass


    # Enter a parse tree produced by dafnyParser#multisetType.
    def enterMultisetType(self, ctx:dafnyParser.MultisetTypeContext):
        pass

    # Exit a parse tree produced by dafnyParser#multisetType.
    def exitMultisetType(self, ctx:dafnyParser.MultisetTypeContext):
        pass


    # Enter a parse tree produced by dafnyParser#sequenceType.
    def enterSequenceType(self, ctx:dafnyParser.SequenceTypeContext):
        pass

    # Exit a parse tree produced by dafnyParser#sequenceType.
    def exitSequenceType(self, ctx:dafnyParser.SequenceTypeContext):
        pass


    # Enter a parse tree produced by dafnyParser#datatypeDecl.
    def enterDatatypeDecl(self, ctx:dafnyParser.DatatypeDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#datatypeDecl.
    def exitDatatypeDecl(self, ctx:dafnyParser.DatatypeDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#datatypeConstructor.
    def enterDatatypeConstructor(self, ctx:dafnyParser.DatatypeConstructorContext):
        pass

    # Exit a parse tree produced by dafnyParser#datatypeConstructor.
    def exitDatatypeConstructor(self, ctx:dafnyParser.DatatypeConstructorContext):
        pass


    # Enter a parse tree produced by dafnyParser#classDecl.
    def enterClassDecl(self, ctx:dafnyParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#classDecl.
    def exitClassDecl(self, ctx:dafnyParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#classMemberDecl.
    def enterClassMemberDecl(self, ctx:dafnyParser.ClassMemberDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#classMemberDecl.
    def exitClassMemberDecl(self, ctx:dafnyParser.ClassMemberDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#traitDecl.
    def enterTraitDecl(self, ctx:dafnyParser.TraitDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#traitDecl.
    def exitTraitDecl(self, ctx:dafnyParser.TraitDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#traitMemberDecl.
    def enterTraitMemberDecl(self, ctx:dafnyParser.TraitMemberDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#traitMemberDecl.
    def exitTraitMemberDecl(self, ctx:dafnyParser.TraitMemberDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#functionSignatureDecl.
    def enterFunctionSignatureDecl(self, ctx:dafnyParser.FunctionSignatureDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#functionSignatureDecl.
    def exitFunctionSignatureDecl(self, ctx:dafnyParser.FunctionSignatureDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#methodSignatureDecl.
    def enterMethodSignatureDecl(self, ctx:dafnyParser.MethodSignatureDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#methodSignatureDecl.
    def exitMethodSignatureDecl(self, ctx:dafnyParser.MethodSignatureDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#predicateSignatureDecl.
    def enterPredicateSignatureDecl(self, ctx:dafnyParser.PredicateSignatureDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#predicateSignatureDecl.
    def exitPredicateSignatureDecl(self, ctx:dafnyParser.PredicateSignatureDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#fieldDecl.
    def enterFieldDecl(self, ctx:dafnyParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#fieldDecl.
    def exitFieldDecl(self, ctx:dafnyParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#identifierType.
    def enterIdentifierType(self, ctx:dafnyParser.IdentifierTypeContext):
        pass

    # Exit a parse tree produced by dafnyParser#identifierType.
    def exitIdentifierType(self, ctx:dafnyParser.IdentifierTypeContext):
        pass


    # Enter a parse tree produced by dafnyParser#parameters.
    def enterParameters(self, ctx:dafnyParser.ParametersContext):
        pass

    # Exit a parse tree produced by dafnyParser#parameters.
    def exitParameters(self, ctx:dafnyParser.ParametersContext):
        pass


    # Enter a parse tree produced by dafnyParser#functionDecl.
    def enterFunctionDecl(self, ctx:dafnyParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#functionDecl.
    def exitFunctionDecl(self, ctx:dafnyParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#methodDecl.
    def enterMethodDecl(self, ctx:dafnyParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#methodDecl.
    def exitMethodDecl(self, ctx:dafnyParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#predicateDecl.
    def enterPredicateDecl(self, ctx:dafnyParser.PredicateDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#predicateDecl.
    def exitPredicateDecl(self, ctx:dafnyParser.PredicateDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#constructorDecl.
    def enterConstructorDecl(self, ctx:dafnyParser.ConstructorDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#constructorDecl.
    def exitConstructorDecl(self, ctx:dafnyParser.ConstructorDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#disj.
    def enterDisj(self, ctx:dafnyParser.DisjContext):
        pass

    # Exit a parse tree produced by dafnyParser#disj.
    def exitDisj(self, ctx:dafnyParser.DisjContext):
        pass


    # Enter a parse tree produced by dafnyParser#expression.
    def enterExpression(self, ctx:dafnyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#expression.
    def exitExpression(self, ctx:dafnyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#datatypeFieldUpdate.
    def enterDatatypeFieldUpdate(self, ctx:dafnyParser.DatatypeFieldUpdateContext):
        pass

    # Exit a parse tree produced by dafnyParser#datatypeFieldUpdate.
    def exitDatatypeFieldUpdate(self, ctx:dafnyParser.DatatypeFieldUpdateContext):
        pass


    # Enter a parse tree produced by dafnyParser#modulus.
    def enterModulus(self, ctx:dafnyParser.ModulusContext):
        pass

    # Exit a parse tree produced by dafnyParser#modulus.
    def exitModulus(self, ctx:dafnyParser.ModulusContext):
        pass


    # Enter a parse tree produced by dafnyParser#multisetConversion.
    def enterMultisetConversion(self, ctx:dafnyParser.MultisetConversionContext):
        pass

    # Exit a parse tree produced by dafnyParser#multisetConversion.
    def exitMultisetConversion(self, ctx:dafnyParser.MultisetConversionContext):
        pass


    # Enter a parse tree produced by dafnyParser#literal.
    def enterLiteral(self, ctx:dafnyParser.LiteralContext):
        pass

    # Exit a parse tree produced by dafnyParser#literal.
    def exitLiteral(self, ctx:dafnyParser.LiteralContext):
        pass


    # Enter a parse tree produced by dafnyParser#callParameters.
    def enterCallParameters(self, ctx:dafnyParser.CallParametersContext):
        pass

    # Exit a parse tree produced by dafnyParser#callParameters.
    def exitCallParameters(self, ctx:dafnyParser.CallParametersContext):
        pass


    # Enter a parse tree produced by dafnyParser#functionCall.
    def enterFunctionCall(self, ctx:dafnyParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by dafnyParser#functionCall.
    def exitFunctionCall(self, ctx:dafnyParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by dafnyParser#classInstantiation.
    def enterClassInstantiation(self, ctx:dafnyParser.ClassInstantiationContext):
        pass

    # Exit a parse tree produced by dafnyParser#classInstantiation.
    def exitClassInstantiation(self, ctx:dafnyParser.ClassInstantiationContext):
        pass


    # Enter a parse tree produced by dafnyParser#datatypeInstantiation.
    def enterDatatypeInstantiation(self, ctx:dafnyParser.DatatypeInstantiationContext):
        pass

    # Exit a parse tree produced by dafnyParser#datatypeInstantiation.
    def exitDatatypeInstantiation(self, ctx:dafnyParser.DatatypeInstantiationContext):
        pass


    # Enter a parse tree produced by dafnyParser#ternaryExpression.
    def enterTernaryExpression(self, ctx:dafnyParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#ternaryExpression.
    def exitTernaryExpression(self, ctx:dafnyParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#matchExpression.
    def enterMatchExpression(self, ctx:dafnyParser.MatchExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#matchExpression.
    def exitMatchExpression(self, ctx:dafnyParser.MatchExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#caseExpression.
    def enterCaseExpression(self, ctx:dafnyParser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#caseExpression.
    def exitCaseExpression(self, ctx:dafnyParser.CaseExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#arrayLength.
    def enterArrayLength(self, ctx:dafnyParser.ArrayLengthContext):
        pass

    # Exit a parse tree produced by dafnyParser#arrayLength.
    def exitArrayLength(self, ctx:dafnyParser.ArrayLengthContext):
        pass


    # Enter a parse tree produced by dafnyParser#index.
    def enterIndex(self, ctx:dafnyParser.IndexContext):
        pass

    # Exit a parse tree produced by dafnyParser#index.
    def exitIndex(self, ctx:dafnyParser.IndexContext):
        pass


    # Enter a parse tree produced by dafnyParser#setDisplay.
    def enterSetDisplay(self, ctx:dafnyParser.SetDisplayContext):
        pass

    # Exit a parse tree produced by dafnyParser#setDisplay.
    def exitSetDisplay(self, ctx:dafnyParser.SetDisplayContext):
        pass


    # Enter a parse tree produced by dafnyParser#setComprehension.
    def enterSetComprehension(self, ctx:dafnyParser.SetComprehensionContext):
        pass

    # Exit a parse tree produced by dafnyParser#setComprehension.
    def exitSetComprehension(self, ctx:dafnyParser.SetComprehensionContext):
        pass


    # Enter a parse tree produced by dafnyParser#sequenceDisplay.
    def enterSequenceDisplay(self, ctx:dafnyParser.SequenceDisplayContext):
        pass

    # Exit a parse tree produced by dafnyParser#sequenceDisplay.
    def exitSequenceDisplay(self, ctx:dafnyParser.SequenceDisplayContext):
        pass


    # Enter a parse tree produced by dafnyParser#sequenceComprehension.
    def enterSequenceComprehension(self, ctx:dafnyParser.SequenceComprehensionContext):
        pass

    # Exit a parse tree produced by dafnyParser#sequenceComprehension.
    def exitSequenceComprehension(self, ctx:dafnyParser.SequenceComprehensionContext):
        pass


    # Enter a parse tree produced by dafnyParser#mapConstructor.
    def enterMapConstructor(self, ctx:dafnyParser.MapConstructorContext):
        pass

    # Exit a parse tree produced by dafnyParser#mapConstructor.
    def exitMapConstructor(self, ctx:dafnyParser.MapConstructorContext):
        pass


    # Enter a parse tree produced by dafnyParser#mapComprehension.
    def enterMapComprehension(self, ctx:dafnyParser.MapComprehensionContext):
        pass

    # Exit a parse tree produced by dafnyParser#mapComprehension.
    def exitMapComprehension(self, ctx:dafnyParser.MapComprehensionContext):
        pass


    # Enter a parse tree produced by dafnyParser#indexElem.
    def enterIndexElem(self, ctx:dafnyParser.IndexElemContext):
        pass

    # Exit a parse tree produced by dafnyParser#indexElem.
    def exitIndexElem(self, ctx:dafnyParser.IndexElemContext):
        pass


    # Enter a parse tree produced by dafnyParser#statement.
    def enterStatement(self, ctx:dafnyParser.StatementContext):
        pass

    # Exit a parse tree produced by dafnyParser#statement.
    def exitStatement(self, ctx:dafnyParser.StatementContext):
        pass


    # Enter a parse tree produced by dafnyParser#assertStatement.
    def enterAssertStatement(self, ctx:dafnyParser.AssertStatementContext):
        pass

    # Exit a parse tree produced by dafnyParser#assertStatement.
    def exitAssertStatement(self, ctx:dafnyParser.AssertStatementContext):
        pass


    # Enter a parse tree produced by dafnyParser#breakStatement.
    def enterBreakStatement(self, ctx:dafnyParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by dafnyParser#breakStatement.
    def exitBreakStatement(self, ctx:dafnyParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by dafnyParser#continueStatement.
    def enterContinueStatement(self, ctx:dafnyParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by dafnyParser#continueStatement.
    def exitContinueStatement(self, ctx:dafnyParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by dafnyParser#declIdentifier.
    def enterDeclIdentifier(self, ctx:dafnyParser.DeclIdentifierContext):
        pass

    # Exit a parse tree produced by dafnyParser#declIdentifier.
    def exitDeclIdentifier(self, ctx:dafnyParser.DeclIdentifierContext):
        pass


    # Enter a parse tree produced by dafnyParser#declAssignLhs.
    def enterDeclAssignLhs(self, ctx:dafnyParser.DeclAssignLhsContext):
        pass

    # Exit a parse tree produced by dafnyParser#declAssignLhs.
    def exitDeclAssignLhs(self, ctx:dafnyParser.DeclAssignLhsContext):
        pass


    # Enter a parse tree produced by dafnyParser#declAssignRhs.
    def enterDeclAssignRhs(self, ctx:dafnyParser.DeclAssignRhsContext):
        pass

    # Exit a parse tree produced by dafnyParser#declAssignRhs.
    def exitDeclAssignRhs(self, ctx:dafnyParser.DeclAssignRhsContext):
        pass


    # Enter a parse tree produced by dafnyParser#declarationLhs.
    def enterDeclarationLhs(self, ctx:dafnyParser.DeclarationLhsContext):
        pass

    # Exit a parse tree produced by dafnyParser#declarationLhs.
    def exitDeclarationLhs(self, ctx:dafnyParser.DeclarationLhsContext):
        pass


    # Enter a parse tree produced by dafnyParser#declaration.
    def enterDeclaration(self, ctx:dafnyParser.DeclarationContext):
        pass

    # Exit a parse tree produced by dafnyParser#declaration.
    def exitDeclaration(self, ctx:dafnyParser.DeclarationContext):
        pass


    # Enter a parse tree produced by dafnyParser#assignmentLhs.
    def enterAssignmentLhs(self, ctx:dafnyParser.AssignmentLhsContext):
        pass

    # Exit a parse tree produced by dafnyParser#assignmentLhs.
    def exitAssignmentLhs(self, ctx:dafnyParser.AssignmentLhsContext):
        pass


    # Enter a parse tree produced by dafnyParser#assignment.
    def enterAssignment(self, ctx:dafnyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by dafnyParser#assignment.
    def exitAssignment(self, ctx:dafnyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by dafnyParser#print.
    def enterPrint(self, ctx:dafnyParser.PrintContext):
        pass

    # Exit a parse tree produced by dafnyParser#print.
    def exitPrint(self, ctx:dafnyParser.PrintContext):
        pass


    # Enter a parse tree produced by dafnyParser#voidMethodCall.
    def enterVoidMethodCall(self, ctx:dafnyParser.VoidMethodCallContext):
        pass

    # Exit a parse tree produced by dafnyParser#voidMethodCall.
    def exitVoidMethodCall(self, ctx:dafnyParser.VoidMethodCallContext):
        pass


    # Enter a parse tree produced by dafnyParser#matchStatement.
    def enterMatchStatement(self, ctx:dafnyParser.MatchStatementContext):
        pass

    # Exit a parse tree produced by dafnyParser#matchStatement.
    def exitMatchStatement(self, ctx:dafnyParser.MatchStatementContext):
        pass


    # Enter a parse tree produced by dafnyParser#caseStatement.
    def enterCaseStatement(self, ctx:dafnyParser.CaseStatementContext):
        pass

    # Exit a parse tree produced by dafnyParser#caseStatement.
    def exitCaseStatement(self, ctx:dafnyParser.CaseStatementContext):
        pass


    # Enter a parse tree produced by dafnyParser#ifStatement.
    def enterIfStatement(self, ctx:dafnyParser.IfStatementContext):
        pass

    # Exit a parse tree produced by dafnyParser#ifStatement.
    def exitIfStatement(self, ctx:dafnyParser.IfStatementContext):
        pass


    # Enter a parse tree produced by dafnyParser#forallStatement.
    def enterForallStatement(self, ctx:dafnyParser.ForallStatementContext):
        pass

    # Exit a parse tree produced by dafnyParser#forallStatement.
    def exitForallStatement(self, ctx:dafnyParser.ForallStatementContext):
        pass


    # Enter a parse tree produced by dafnyParser#forLoop.
    def enterForLoop(self, ctx:dafnyParser.ForLoopContext):
        pass

    # Exit a parse tree produced by dafnyParser#forLoop.
    def exitForLoop(self, ctx:dafnyParser.ForLoopContext):
        pass


    # Enter a parse tree produced by dafnyParser#whileStatement.
    def enterWhileStatement(self, ctx:dafnyParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by dafnyParser#whileStatement.
    def exitWhileStatement(self, ctx:dafnyParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by dafnyParser#ghostVarDecl.
    def enterGhostVarDecl(self, ctx:dafnyParser.GhostVarDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#ghostVarDecl.
    def exitGhostVarDecl(self, ctx:dafnyParser.GhostVarDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#verifierAnnotation.
    def enterVerifierAnnotation(self, ctx:dafnyParser.VerifierAnnotationContext):
        pass

    # Exit a parse tree produced by dafnyParser#verifierAnnotation.
    def exitVerifierAnnotation(self, ctx:dafnyParser.VerifierAnnotationContext):
        pass


    # Enter a parse tree produced by dafnyParser#decreases.
    def enterDecreases(self, ctx:dafnyParser.DecreasesContext):
        pass

    # Exit a parse tree produced by dafnyParser#decreases.
    def exitDecreases(self, ctx:dafnyParser.DecreasesContext):
        pass


    # Enter a parse tree produced by dafnyParser#ensures.
    def enterEnsures(self, ctx:dafnyParser.EnsuresContext):
        pass

    # Exit a parse tree produced by dafnyParser#ensures.
    def exitEnsures(self, ctx:dafnyParser.EnsuresContext):
        pass


    # Enter a parse tree produced by dafnyParser#invariant.
    def enterInvariant(self, ctx:dafnyParser.InvariantContext):
        pass

    # Exit a parse tree produced by dafnyParser#invariant.
    def exitInvariant(self, ctx:dafnyParser.InvariantContext):
        pass


    # Enter a parse tree produced by dafnyParser#modifies.
    def enterModifies(self, ctx:dafnyParser.ModifiesContext):
        pass

    # Exit a parse tree produced by dafnyParser#modifies.
    def exitModifies(self, ctx:dafnyParser.ModifiesContext):
        pass


    # Enter a parse tree produced by dafnyParser#reads.
    def enterReads(self, ctx:dafnyParser.ReadsContext):
        pass

    # Exit a parse tree produced by dafnyParser#reads.
    def exitReads(self, ctx:dafnyParser.ReadsContext):
        pass


    # Enter a parse tree produced by dafnyParser#requires.
    def enterRequires(self, ctx:dafnyParser.RequiresContext):
        pass

    # Exit a parse tree produced by dafnyParser#requires.
    def exitRequires(self, ctx:dafnyParser.RequiresContext):
        pass


    # Enter a parse tree produced by dafnyParser#arrayConstructor.
    def enterArrayConstructor(self, ctx:dafnyParser.ArrayConstructorContext):
        pass

    # Exit a parse tree produced by dafnyParser#arrayConstructor.
    def exitArrayConstructor(self, ctx:dafnyParser.ArrayConstructorContext):
        pass


    # Enter a parse tree produced by dafnyParser#arrayComprehension.
    def enterArrayComprehension(self, ctx:dafnyParser.ArrayComprehensionContext):
        pass

    # Exit a parse tree produced by dafnyParser#arrayComprehension.
    def exitArrayComprehension(self, ctx:dafnyParser.ArrayComprehensionContext):
        pass


    # Enter a parse tree produced by dafnyParser#arrayValues.
    def enterArrayValues(self, ctx:dafnyParser.ArrayValuesContext):
        pass

    # Exit a parse tree produced by dafnyParser#arrayValues.
    def exitArrayValues(self, ctx:dafnyParser.ArrayValuesContext):
        pass


    # Enter a parse tree produced by dafnyParser#topDeclMember.
    def enterTopDeclMember(self, ctx:dafnyParser.TopDeclMemberContext):
        pass

    # Exit a parse tree produced by dafnyParser#topDeclMember.
    def exitTopDeclMember(self, ctx:dafnyParser.TopDeclMemberContext):
        pass


    # Enter a parse tree produced by dafnyParser#program.
    def enterProgram(self, ctx:dafnyParser.ProgramContext):
        pass

    # Exit a parse tree produced by dafnyParser#program.
    def exitProgram(self, ctx:dafnyParser.ProgramContext):
        pass



del dafnyParser