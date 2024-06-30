# Generated from dafny.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .dafnyParser import dafnyParser
else:
    from dafnyParser import dafnyParser

# This class defines a complete listener for a parse tree produced by dafnyParser.
class dafnyListener(ParseTreeListener):

    # Enter a parse tree produced by dafnyParser#program.
    def enterProgram(self, ctx:dafnyParser.ProgramContext):
        pass

    # Exit a parse tree produced by dafnyParser#program.
    def exitProgram(self, ctx:dafnyParser.ProgramContext):
        pass


    # Enter a parse tree produced by dafnyParser#includeDirective_.
    def enterIncludeDirective_(self, ctx:dafnyParser.IncludeDirective_Context):
        pass

    # Exit a parse tree produced by dafnyParser#includeDirective_.
    def exitIncludeDirective_(self, ctx:dafnyParser.IncludeDirective_Context):
        pass


    # Enter a parse tree produced by dafnyParser#topDecl.
    def enterTopDecl(self, ctx:dafnyParser.TopDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#topDecl.
    def exitTopDecl(self, ctx:dafnyParser.TopDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#declModifier.
    def enterDeclModifier(self, ctx:dafnyParser.DeclModifierContext):
        pass

    # Exit a parse tree produced by dafnyParser#declModifier.
    def exitDeclModifier(self, ctx:dafnyParser.DeclModifierContext):
        pass


    # Enter a parse tree produced by dafnyParser#subModuleDecl.
    def enterSubModuleDecl(self, ctx:dafnyParser.SubModuleDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#subModuleDecl.
    def exitSubModuleDecl(self, ctx:dafnyParser.SubModuleDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#moduleDefinition.
    def enterModuleDefinition(self, ctx:dafnyParser.ModuleDefinitionContext):
        pass

    # Exit a parse tree produced by dafnyParser#moduleDefinition.
    def exitModuleDefinition(self, ctx:dafnyParser.ModuleDefinitionContext):
        pass


    # Enter a parse tree produced by dafnyParser#moduleImport.
    def enterModuleImport(self, ctx:dafnyParser.ModuleImportContext):
        pass

    # Exit a parse tree produced by dafnyParser#moduleImport.
    def exitModuleImport(self, ctx:dafnyParser.ModuleImportContext):
        pass


    # Enter a parse tree produced by dafnyParser#qualifiedModuleExport.
    def enterQualifiedModuleExport(self, ctx:dafnyParser.QualifiedModuleExportContext):
        pass

    # Exit a parse tree produced by dafnyParser#qualifiedModuleExport.
    def exitQualifiedModuleExport(self, ctx:dafnyParser.QualifiedModuleExportContext):
        pass


    # Enter a parse tree produced by dafnyParser#moduleExportSuffix.
    def enterModuleExportSuffix(self, ctx:dafnyParser.ModuleExportSuffixContext):
        pass

    # Exit a parse tree produced by dafnyParser#moduleExportSuffix.
    def exitModuleExportSuffix(self, ctx:dafnyParser.ModuleExportSuffixContext):
        pass


    # Enter a parse tree produced by dafnyParser#moduleExport.
    def enterModuleExport(self, ctx:dafnyParser.ModuleExportContext):
        pass

    # Exit a parse tree produced by dafnyParser#moduleExport.
    def exitModuleExport(self, ctx:dafnyParser.ModuleExportContext):
        pass


    # Enter a parse tree produced by dafnyParser#exportSignature.
    def enterExportSignature(self, ctx:dafnyParser.ExportSignatureContext):
        pass

    # Exit a parse tree produced by dafnyParser#exportSignature.
    def exitExportSignature(self, ctx:dafnyParser.ExportSignatureContext):
        pass


    # Enter a parse tree produced by dafnyParser#type.
    def enterType(self, ctx:dafnyParser.TypeContext):
        pass

    # Exit a parse tree produced by dafnyParser#type.
    def exitType(self, ctx:dafnyParser.TypeContext):
        pass


    # Enter a parse tree produced by dafnyParser#domainType_.
    def enterDomainType_(self, ctx:dafnyParser.DomainType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#domainType_.
    def exitDomainType_(self, ctx:dafnyParser.DomainType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#namedType.
    def enterNamedType(self, ctx:dafnyParser.NamedTypeContext):
        pass

    # Exit a parse tree produced by dafnyParser#namedType.
    def exitNamedType(self, ctx:dafnyParser.NamedTypeContext):
        pass


    # Enter a parse tree produced by dafnyParser#nameSegmentForTypeName.
    def enterNameSegmentForTypeName(self, ctx:dafnyParser.NameSegmentForTypeNameContext):
        pass

    # Exit a parse tree produced by dafnyParser#nameSegmentForTypeName.
    def exitNameSegmentForTypeName(self, ctx:dafnyParser.NameSegmentForTypeNameContext):
        pass


    # Enter a parse tree produced by dafnyParser#boolType_.
    def enterBoolType_(self, ctx:dafnyParser.BoolType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#boolType_.
    def exitBoolType_(self, ctx:dafnyParser.BoolType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#intType_.
    def enterIntType_(self, ctx:dafnyParser.IntType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#intType_.
    def exitIntType_(self, ctx:dafnyParser.IntType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#realType_.
    def enterRealType_(self, ctx:dafnyParser.RealType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#realType_.
    def exitRealType_(self, ctx:dafnyParser.RealType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#bitVectorType_.
    def enterBitVectorType_(self, ctx:dafnyParser.BitVectorType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#bitVectorType_.
    def exitBitVectorType_(self, ctx:dafnyParser.BitVectorType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#ordinalType_.
    def enterOrdinalType_(self, ctx:dafnyParser.OrdinalType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#ordinalType_.
    def exitOrdinalType_(self, ctx:dafnyParser.OrdinalType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#charType_.
    def enterCharType_(self, ctx:dafnyParser.CharType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#charType_.
    def exitCharType_(self, ctx:dafnyParser.CharType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#genericInstantiation.
    def enterGenericInstantiation(self, ctx:dafnyParser.GenericInstantiationContext):
        pass

    # Exit a parse tree produced by dafnyParser#genericInstantiation.
    def exitGenericInstantiation(self, ctx:dafnyParser.GenericInstantiationContext):
        pass


    # Enter a parse tree produced by dafnyParser#genericParameters.
    def enterGenericParameters(self, ctx:dafnyParser.GenericParametersContext):
        pass

    # Exit a parse tree produced by dafnyParser#genericParameters.
    def exitGenericParameters(self, ctx:dafnyParser.GenericParametersContext):
        pass


    # Enter a parse tree produced by dafnyParser#typeParameterCharacteristics.
    def enterTypeParameterCharacteristics(self, ctx:dafnyParser.TypeParameterCharacteristicsContext):
        pass

    # Exit a parse tree produced by dafnyParser#typeParameterCharacteristics.
    def exitTypeParameterCharacteristics(self, ctx:dafnyParser.TypeParameterCharacteristicsContext):
        pass


    # Enter a parse tree produced by dafnyParser#tPCharOption.
    def enterTPCharOption(self, ctx:dafnyParser.TPCharOptionContext):
        pass

    # Exit a parse tree produced by dafnyParser#tPCharOption.
    def exitTPCharOption(self, ctx:dafnyParser.TPCharOptionContext):
        pass


    # Enter a parse tree produced by dafnyParser#finiteSetType_.
    def enterFiniteSetType_(self, ctx:dafnyParser.FiniteSetType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#finiteSetType_.
    def exitFiniteSetType_(self, ctx:dafnyParser.FiniteSetType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#infiniteSetType_.
    def enterInfiniteSetType_(self, ctx:dafnyParser.InfiniteSetType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#infiniteSetType_.
    def exitInfiniteSetType_(self, ctx:dafnyParser.InfiniteSetType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#multisetType_.
    def enterMultisetType_(self, ctx:dafnyParser.MultisetType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#multisetType_.
    def exitMultisetType_(self, ctx:dafnyParser.MultisetType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#sequenceType_.
    def enterSequenceType_(self, ctx:dafnyParser.SequenceType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#sequenceType_.
    def exitSequenceType_(self, ctx:dafnyParser.SequenceType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#stringType_.
    def enterStringType_(self, ctx:dafnyParser.StringType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#stringType_.
    def exitStringType_(self, ctx:dafnyParser.StringType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#finiteMapType_.
    def enterFiniteMapType_(self, ctx:dafnyParser.FiniteMapType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#finiteMapType_.
    def exitFiniteMapType_(self, ctx:dafnyParser.FiniteMapType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#infiniteMapType_.
    def enterInfiniteMapType_(self, ctx:dafnyParser.InfiniteMapType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#infiniteMapType_.
    def exitInfiniteMapType_(self, ctx:dafnyParser.InfiniteMapType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#synonymTypeDecl.
    def enterSynonymTypeDecl(self, ctx:dafnyParser.SynonymTypeDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#synonymTypeDecl.
    def exitSynonymTypeDecl(self, ctx:dafnyParser.SynonymTypeDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#synonymTypeName.
    def enterSynonymTypeName(self, ctx:dafnyParser.SynonymTypeNameContext):
        pass

    # Exit a parse tree produced by dafnyParser#synonymTypeName.
    def exitSynonymTypeName(self, ctx:dafnyParser.SynonymTypeNameContext):
        pass


    # Enter a parse tree produced by dafnyParser#synonymTypeDecl_.
    def enterSynonymTypeDecl_(self, ctx:dafnyParser.SynonymTypeDecl_Context):
        pass

    # Exit a parse tree produced by dafnyParser#synonymTypeDecl_.
    def exitSynonymTypeDecl_(self, ctx:dafnyParser.SynonymTypeDecl_Context):
        pass


    # Enter a parse tree produced by dafnyParser#opaqueTypeDecl_.
    def enterOpaqueTypeDecl_(self, ctx:dafnyParser.OpaqueTypeDecl_Context):
        pass

    # Exit a parse tree produced by dafnyParser#opaqueTypeDecl_.
    def exitOpaqueTypeDecl_(self, ctx:dafnyParser.OpaqueTypeDecl_Context):
        pass


    # Enter a parse tree produced by dafnyParser#typeMembers.
    def enterTypeMembers(self, ctx:dafnyParser.TypeMembersContext):
        pass

    # Exit a parse tree produced by dafnyParser#typeMembers.
    def exitTypeMembers(self, ctx:dafnyParser.TypeMembersContext):
        pass


    # Enter a parse tree produced by dafnyParser#subsetTypeDecl_.
    def enterSubsetTypeDecl_(self, ctx:dafnyParser.SubsetTypeDecl_Context):
        pass

    # Exit a parse tree produced by dafnyParser#subsetTypeDecl_.
    def exitSubsetTypeDecl_(self, ctx:dafnyParser.SubsetTypeDecl_Context):
        pass


    # Enter a parse tree produced by dafnyParser#natType_.
    def enterNatType_(self, ctx:dafnyParser.NatType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#natType_.
    def exitNatType_(self, ctx:dafnyParser.NatType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#newtypeDecl.
    def enterNewtypeDecl(self, ctx:dafnyParser.NewtypeDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#newtypeDecl.
    def exitNewtypeDecl(self, ctx:dafnyParser.NewtypeDeclContext):
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


    # Enter a parse tree produced by dafnyParser#objectType_.
    def enterObjectType_(self, ctx:dafnyParser.ObjectType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#objectType_.
    def exitObjectType_(self, ctx:dafnyParser.ObjectType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#arrayType_.
    def enterArrayType_(self, ctx:dafnyParser.ArrayType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#arrayType_.
    def exitArrayType_(self, ctx:dafnyParser.ArrayType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#iteratorDecl.
    def enterIteratorDecl(self, ctx:dafnyParser.IteratorDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#iteratorDecl.
    def exitIteratorDecl(self, ctx:dafnyParser.IteratorDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#arrowType_.
    def enterArrowType_(self, ctx:dafnyParser.ArrowType_Context):
        pass

    # Exit a parse tree produced by dafnyParser#arrowType_.
    def exitArrowType_(self, ctx:dafnyParser.ArrowType_Context):
        pass


    # Enter a parse tree produced by dafnyParser#datatypeDecl.
    def enterDatatypeDecl(self, ctx:dafnyParser.DatatypeDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#datatypeDecl.
    def exitDatatypeDecl(self, ctx:dafnyParser.DatatypeDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#datatypeMemberDecl.
    def enterDatatypeMemberDecl(self, ctx:dafnyParser.DatatypeMemberDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#datatypeMemberDecl.
    def exitDatatypeMemberDecl(self, ctx:dafnyParser.DatatypeMemberDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#fieldDecl.
    def enterFieldDecl(self, ctx:dafnyParser.FieldDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#fieldDecl.
    def exitFieldDecl(self, ctx:dafnyParser.FieldDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#constantFieldDecl.
    def enterConstantFieldDecl(self, ctx:dafnyParser.ConstantFieldDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#constantFieldDecl.
    def exitConstantFieldDecl(self, ctx:dafnyParser.ConstantFieldDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#methodDecl.
    def enterMethodDecl(self, ctx:dafnyParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#methodDecl.
    def exitMethodDecl(self, ctx:dafnyParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#methodKeyword_.
    def enterMethodKeyword_(self, ctx:dafnyParser.MethodKeyword_Context):
        pass

    # Exit a parse tree produced by dafnyParser#methodKeyword_.
    def exitMethodKeyword_(self, ctx:dafnyParser.MethodKeyword_Context):
        pass


    # Enter a parse tree produced by dafnyParser#methodSignature_.
    def enterMethodSignature_(self, ctx:dafnyParser.MethodSignature_Context):
        pass

    # Exit a parse tree produced by dafnyParser#methodSignature_.
    def exitMethodSignature_(self, ctx:dafnyParser.MethodSignature_Context):
        pass


    # Enter a parse tree produced by dafnyParser#formals.
    def enterFormals(self, ctx:dafnyParser.FormalsContext):
        pass

    # Exit a parse tree produced by dafnyParser#formals.
    def exitFormals(self, ctx:dafnyParser.FormalsContext):
        pass


    # Enter a parse tree produced by dafnyParser#functionDecl.
    def enterFunctionDecl(self, ctx:dafnyParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#functionDecl.
    def exitFunctionDecl(self, ctx:dafnyParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#opaqueAttribute.
    def enterOpaqueAttribute(self, ctx:dafnyParser.OpaqueAttributeContext):
        pass

    # Exit a parse tree produced by dafnyParser#opaqueAttribute.
    def exitOpaqueAttribute(self, ctx:dafnyParser.OpaqueAttributeContext):
        pass


    # Enter a parse tree produced by dafnyParser#functionSignatureOrEllipsis_.
    def enterFunctionSignatureOrEllipsis_(self, ctx:dafnyParser.FunctionSignatureOrEllipsis_Context):
        pass

    # Exit a parse tree produced by dafnyParser#functionSignatureOrEllipsis_.
    def exitFunctionSignatureOrEllipsis_(self, ctx:dafnyParser.FunctionSignatureOrEllipsis_Context):
        pass


    # Enter a parse tree produced by dafnyParser#functionSignature_.
    def enterFunctionSignature_(self, ctx:dafnyParser.FunctionSignature_Context):
        pass

    # Exit a parse tree produced by dafnyParser#functionSignature_.
    def exitFunctionSignature_(self, ctx:dafnyParser.FunctionSignature_Context):
        pass


    # Enter a parse tree produced by dafnyParser#predicateSignatureOrEllipsis_.
    def enterPredicateSignatureOrEllipsis_(self, ctx:dafnyParser.PredicateSignatureOrEllipsis_Context):
        pass

    # Exit a parse tree produced by dafnyParser#predicateSignatureOrEllipsis_.
    def exitPredicateSignatureOrEllipsis_(self, ctx:dafnyParser.PredicateSignatureOrEllipsis_Context):
        pass


    # Enter a parse tree produced by dafnyParser#predicateSignature_.
    def enterPredicateSignature_(self, ctx:dafnyParser.PredicateSignature_Context):
        pass

    # Exit a parse tree produced by dafnyParser#predicateSignature_.
    def exitPredicateSignature_(self, ctx:dafnyParser.PredicateSignature_Context):
        pass


    # Enter a parse tree produced by dafnyParser#functionBody.
    def enterFunctionBody(self, ctx:dafnyParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by dafnyParser#functionBody.
    def exitFunctionBody(self, ctx:dafnyParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by dafnyParser#methodSpec.
    def enterMethodSpec(self, ctx:dafnyParser.MethodSpecContext):
        pass

    # Exit a parse tree produced by dafnyParser#methodSpec.
    def exitMethodSpec(self, ctx:dafnyParser.MethodSpecContext):
        pass


    # Enter a parse tree produced by dafnyParser#functionSpec.
    def enterFunctionSpec(self, ctx:dafnyParser.FunctionSpecContext):
        pass

    # Exit a parse tree produced by dafnyParser#functionSpec.
    def exitFunctionSpec(self, ctx:dafnyParser.FunctionSpecContext):
        pass


    # Enter a parse tree produced by dafnyParser#lambdaSpec.
    def enterLambdaSpec(self, ctx:dafnyParser.LambdaSpecContext):
        pass

    # Exit a parse tree produced by dafnyParser#lambdaSpec.
    def exitLambdaSpec(self, ctx:dafnyParser.LambdaSpecContext):
        pass


    # Enter a parse tree produced by dafnyParser#iteratorSpec.
    def enterIteratorSpec(self, ctx:dafnyParser.IteratorSpecContext):
        pass

    # Exit a parse tree produced by dafnyParser#iteratorSpec.
    def exitIteratorSpec(self, ctx:dafnyParser.IteratorSpecContext):
        pass


    # Enter a parse tree produced by dafnyParser#loopSpec.
    def enterLoopSpec(self, ctx:dafnyParser.LoopSpecContext):
        pass

    # Exit a parse tree produced by dafnyParser#loopSpec.
    def exitLoopSpec(self, ctx:dafnyParser.LoopSpecContext):
        pass


    # Enter a parse tree produced by dafnyParser#requiresClause.
    def enterRequiresClause(self, ctx:dafnyParser.RequiresClauseContext):
        pass

    # Exit a parse tree produced by dafnyParser#requiresClause.
    def exitRequiresClause(self, ctx:dafnyParser.RequiresClauseContext):
        pass


    # Enter a parse tree produced by dafnyParser#ensuresClause.
    def enterEnsuresClause(self, ctx:dafnyParser.EnsuresClauseContext):
        pass

    # Exit a parse tree produced by dafnyParser#ensuresClause.
    def exitEnsuresClause(self, ctx:dafnyParser.EnsuresClauseContext):
        pass


    # Enter a parse tree produced by dafnyParser#decreasesClause.
    def enterDecreasesClause(self, ctx:dafnyParser.DecreasesClauseContext):
        pass

    # Exit a parse tree produced by dafnyParser#decreasesClause.
    def exitDecreasesClause(self, ctx:dafnyParser.DecreasesClauseContext):
        pass


    # Enter a parse tree produced by dafnyParser#decreasesList.
    def enterDecreasesList(self, ctx:dafnyParser.DecreasesListContext):
        pass

    # Exit a parse tree produced by dafnyParser#decreasesList.
    def exitDecreasesList(self, ctx:dafnyParser.DecreasesListContext):
        pass


    # Enter a parse tree produced by dafnyParser#possiblyWildExpression.
    def enterPossiblyWildExpression(self, ctx:dafnyParser.PossiblyWildExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#possiblyWildExpression.
    def exitPossiblyWildExpression(self, ctx:dafnyParser.PossiblyWildExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#modifiesClause.
    def enterModifiesClause(self, ctx:dafnyParser.ModifiesClauseContext):
        pass

    # Exit a parse tree produced by dafnyParser#modifiesClause.
    def exitModifiesClause(self, ctx:dafnyParser.ModifiesClauseContext):
        pass


    # Enter a parse tree produced by dafnyParser#invariantClause_.
    def enterInvariantClause_(self, ctx:dafnyParser.InvariantClause_Context):
        pass

    # Exit a parse tree produced by dafnyParser#invariantClause_.
    def exitInvariantClause_(self, ctx:dafnyParser.InvariantClause_Context):
        pass


    # Enter a parse tree produced by dafnyParser#readsClause.
    def enterReadsClause(self, ctx:dafnyParser.ReadsClauseContext):
        pass

    # Exit a parse tree produced by dafnyParser#readsClause.
    def exitReadsClause(self, ctx:dafnyParser.ReadsClauseContext):
        pass


    # Enter a parse tree produced by dafnyParser#possiblyWildFrameExpression.
    def enterPossiblyWildFrameExpression(self, ctx:dafnyParser.PossiblyWildFrameExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#possiblyWildFrameExpression.
    def exitPossiblyWildFrameExpression(self, ctx:dafnyParser.PossiblyWildFrameExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#frameExpression.
    def enterFrameExpression(self, ctx:dafnyParser.FrameExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#frameExpression.
    def exitFrameExpression(self, ctx:dafnyParser.FrameExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#frameField.
    def enterFrameField(self, ctx:dafnyParser.FrameFieldContext):
        pass

    # Exit a parse tree produced by dafnyParser#frameField.
    def exitFrameField(self, ctx:dafnyParser.FrameFieldContext):
        pass


    # Enter a parse tree produced by dafnyParser#stmt.
    def enterStmt(self, ctx:dafnyParser.StmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#stmt.
    def exitStmt(self, ctx:dafnyParser.StmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#nonLabeledStmt.
    def enterNonLabeledStmt(self, ctx:dafnyParser.NonLabeledStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#nonLabeledStmt.
    def exitNonLabeledStmt(self, ctx:dafnyParser.NonLabeledStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#breakStmt.
    def enterBreakStmt(self, ctx:dafnyParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#breakStmt.
    def exitBreakStmt(self, ctx:dafnyParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#blockStmt.
    def enterBlockStmt(self, ctx:dafnyParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#blockStmt.
    def exitBlockStmt(self, ctx:dafnyParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#returnStmt.
    def enterReturnStmt(self, ctx:dafnyParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#returnStmt.
    def exitReturnStmt(self, ctx:dafnyParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#yieldStmt.
    def enterYieldStmt(self, ctx:dafnyParser.YieldStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#yieldStmt.
    def exitYieldStmt(self, ctx:dafnyParser.YieldStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#updateStmt.
    def enterUpdateStmt(self, ctx:dafnyParser.UpdateStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#updateStmt.
    def exitUpdateStmt(self, ctx:dafnyParser.UpdateStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#updateFailureStmt.
    def enterUpdateFailureStmt(self, ctx:dafnyParser.UpdateFailureStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#updateFailureStmt.
    def exitUpdateFailureStmt(self, ctx:dafnyParser.UpdateFailureStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#varDeclStatement.
    def enterVarDeclStatement(self, ctx:dafnyParser.VarDeclStatementContext):
        pass

    # Exit a parse tree produced by dafnyParser#varDeclStatement.
    def exitVarDeclStatement(self, ctx:dafnyParser.VarDeclStatementContext):
        pass


    # Enter a parse tree produced by dafnyParser#casePatternLocal.
    def enterCasePatternLocal(self, ctx:dafnyParser.CasePatternLocalContext):
        pass

    # Exit a parse tree produced by dafnyParser#casePatternLocal.
    def exitCasePatternLocal(self, ctx:dafnyParser.CasePatternLocalContext):
        pass


    # Enter a parse tree produced by dafnyParser#guard.
    def enterGuard(self, ctx:dafnyParser.GuardContext):
        pass

    # Exit a parse tree produced by dafnyParser#guard.
    def exitGuard(self, ctx:dafnyParser.GuardContext):
        pass


    # Enter a parse tree produced by dafnyParser#bindingGuard.
    def enterBindingGuard(self, ctx:dafnyParser.BindingGuardContext):
        pass

    # Exit a parse tree produced by dafnyParser#bindingGuard.
    def exitBindingGuard(self, ctx:dafnyParser.BindingGuardContext):
        pass


    # Enter a parse tree produced by dafnyParser#ifStmt.
    def enterIfStmt(self, ctx:dafnyParser.IfStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#ifStmt.
    def exitIfStmt(self, ctx:dafnyParser.IfStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#alternativeBlock.
    def enterAlternativeBlock(self, ctx:dafnyParser.AlternativeBlockContext):
        pass

    # Exit a parse tree produced by dafnyParser#alternativeBlock.
    def exitAlternativeBlock(self, ctx:dafnyParser.AlternativeBlockContext):
        pass


    # Enter a parse tree produced by dafnyParser#alternativeBlockCase.
    def enterAlternativeBlockCase(self, ctx:dafnyParser.AlternativeBlockCaseContext):
        pass

    # Exit a parse tree produced by dafnyParser#alternativeBlockCase.
    def exitAlternativeBlockCase(self, ctx:dafnyParser.AlternativeBlockCaseContext):
        pass


    # Enter a parse tree produced by dafnyParser#whileStmt.
    def enterWhileStmt(self, ctx:dafnyParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#whileStmt.
    def exitWhileStmt(self, ctx:dafnyParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#forLoopStmt.
    def enterForLoopStmt(self, ctx:dafnyParser.ForLoopStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#forLoopStmt.
    def exitForLoopStmt(self, ctx:dafnyParser.ForLoopStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#matchStmt.
    def enterMatchStmt(self, ctx:dafnyParser.MatchStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#matchStmt.
    def exitMatchStmt(self, ctx:dafnyParser.MatchStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#caseStmt.
    def enterCaseStmt(self, ctx:dafnyParser.CaseStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#caseStmt.
    def exitCaseStmt(self, ctx:dafnyParser.CaseStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#assertStmt.
    def enterAssertStmt(self, ctx:dafnyParser.AssertStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#assertStmt.
    def exitAssertStmt(self, ctx:dafnyParser.AssertStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#assumeStmt.
    def enterAssumeStmt(self, ctx:dafnyParser.AssumeStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#assumeStmt.
    def exitAssumeStmt(self, ctx:dafnyParser.AssumeStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#expectStmt.
    def enterExpectStmt(self, ctx:dafnyParser.ExpectStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#expectStmt.
    def exitExpectStmt(self, ctx:dafnyParser.ExpectStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#printStmt.
    def enterPrintStmt(self, ctx:dafnyParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#printStmt.
    def exitPrintStmt(self, ctx:dafnyParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#revealStmt.
    def enterRevealStmt(self, ctx:dafnyParser.RevealStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#revealStmt.
    def exitRevealStmt(self, ctx:dafnyParser.RevealStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#forallStmt.
    def enterForallStmt(self, ctx:dafnyParser.ForallStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#forallStmt.
    def exitForallStmt(self, ctx:dafnyParser.ForallStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#modifyStmt.
    def enterModifyStmt(self, ctx:dafnyParser.ModifyStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#modifyStmt.
    def exitModifyStmt(self, ctx:dafnyParser.ModifyStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#calcStmt.
    def enterCalcStmt(self, ctx:dafnyParser.CalcStmtContext):
        pass

    # Exit a parse tree produced by dafnyParser#calcStmt.
    def exitCalcStmt(self, ctx:dafnyParser.CalcStmtContext):
        pass


    # Enter a parse tree produced by dafnyParser#calcBody_.
    def enterCalcBody_(self, ctx:dafnyParser.CalcBody_Context):
        pass

    # Exit a parse tree produced by dafnyParser#calcBody_.
    def exitCalcBody_(self, ctx:dafnyParser.CalcBody_Context):
        pass


    # Enter a parse tree produced by dafnyParser#calcLine_.
    def enterCalcLine_(self, ctx:dafnyParser.CalcLine_Context):
        pass

    # Exit a parse tree produced by dafnyParser#calcLine_.
    def exitCalcLine_(self, ctx:dafnyParser.CalcLine_Context):
        pass


    # Enter a parse tree produced by dafnyParser#hints_.
    def enterHints_(self, ctx:dafnyParser.Hints_Context):
        pass

    # Exit a parse tree produced by dafnyParser#hints_.
    def exitHints_(self, ctx:dafnyParser.Hints_Context):
        pass


    # Enter a parse tree produced by dafnyParser#calcOp.
    def enterCalcOp(self, ctx:dafnyParser.CalcOpContext):
        pass

    # Exit a parse tree produced by dafnyParser#calcOp.
    def exitCalcOp(self, ctx:dafnyParser.CalcOpContext):
        pass


    # Enter a parse tree produced by dafnyParser#expression.
    def enterExpression(self, ctx:dafnyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#expression.
    def exitExpression(self, ctx:dafnyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#equivExpression.
    def enterEquivExpression(self, ctx:dafnyParser.EquivExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#equivExpression.
    def exitEquivExpression(self, ctx:dafnyParser.EquivExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#impliesExpliesExpression.
    def enterImpliesExpliesExpression(self, ctx:dafnyParser.ImpliesExpliesExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#impliesExpliesExpression.
    def exitImpliesExpliesExpression(self, ctx:dafnyParser.ImpliesExpliesExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#impliesExpression.
    def enterImpliesExpression(self, ctx:dafnyParser.ImpliesExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#impliesExpression.
    def exitImpliesExpression(self, ctx:dafnyParser.ImpliesExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#logicalExpression.
    def enterLogicalExpression(self, ctx:dafnyParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#logicalExpression.
    def exitLogicalExpression(self, ctx:dafnyParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#relationalExpression.
    def enterRelationalExpression(self, ctx:dafnyParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#relationalExpression.
    def exitRelationalExpression(self, ctx:dafnyParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#relOp.
    def enterRelOp(self, ctx:dafnyParser.RelOpContext):
        pass

    # Exit a parse tree produced by dafnyParser#relOp.
    def exitRelOp(self, ctx:dafnyParser.RelOpContext):
        pass


    # Enter a parse tree produced by dafnyParser#shiftTerm.
    def enterShiftTerm(self, ctx:dafnyParser.ShiftTermContext):
        pass

    # Exit a parse tree produced by dafnyParser#shiftTerm.
    def exitShiftTerm(self, ctx:dafnyParser.ShiftTermContext):
        pass


    # Enter a parse tree produced by dafnyParser#term.
    def enterTerm(self, ctx:dafnyParser.TermContext):
        pass

    # Exit a parse tree produced by dafnyParser#term.
    def exitTerm(self, ctx:dafnyParser.TermContext):
        pass


    # Enter a parse tree produced by dafnyParser#factor.
    def enterFactor(self, ctx:dafnyParser.FactorContext):
        pass

    # Exit a parse tree produced by dafnyParser#factor.
    def exitFactor(self, ctx:dafnyParser.FactorContext):
        pass


    # Enter a parse tree produced by dafnyParser#bitvectorFactor.
    def enterBitvectorFactor(self, ctx:dafnyParser.BitvectorFactorContext):
        pass

    # Exit a parse tree produced by dafnyParser#bitvectorFactor.
    def exitBitvectorFactor(self, ctx:dafnyParser.BitvectorFactorContext):
        pass


    # Enter a parse tree produced by dafnyParser#asExpression.
    def enterAsExpression(self, ctx:dafnyParser.AsExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#asExpression.
    def exitAsExpression(self, ctx:dafnyParser.AsExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#unaryExpression.
    def enterUnaryExpression(self, ctx:dafnyParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#unaryExpression.
    def exitUnaryExpression(self, ctx:dafnyParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:dafnyParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:dafnyParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#lambdaExpression.
    def enterLambdaExpression(self, ctx:dafnyParser.LambdaExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#lambdaExpression.
    def exitLambdaExpression(self, ctx:dafnyParser.LambdaExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#lhs.
    def enterLhs(self, ctx:dafnyParser.LhsContext):
        pass

    # Exit a parse tree produced by dafnyParser#lhs.
    def exitLhs(self, ctx:dafnyParser.LhsContext):
        pass


    # Enter a parse tree produced by dafnyParser#rhs.
    def enterRhs(self, ctx:dafnyParser.RhsContext):
        pass

    # Exit a parse tree produced by dafnyParser#rhs.
    def exitRhs(self, ctx:dafnyParser.RhsContext):
        pass


    # Enter a parse tree produced by dafnyParser#arrayAllocation_.
    def enterArrayAllocation_(self, ctx:dafnyParser.ArrayAllocation_Context):
        pass

    # Exit a parse tree produced by dafnyParser#arrayAllocation_.
    def exitArrayAllocation_(self, ctx:dafnyParser.ArrayAllocation_Context):
        pass


    # Enter a parse tree produced by dafnyParser#actualBindings.
    def enterActualBindings(self, ctx:dafnyParser.ActualBindingsContext):
        pass

    # Exit a parse tree produced by dafnyParser#actualBindings.
    def exitActualBindings(self, ctx:dafnyParser.ActualBindingsContext):
        pass


    # Enter a parse tree produced by dafnyParser#actualBinding.
    def enterActualBinding(self, ctx:dafnyParser.ActualBindingContext):
        pass

    # Exit a parse tree produced by dafnyParser#actualBinding.
    def exitActualBinding(self, ctx:dafnyParser.ActualBindingContext):
        pass


    # Enter a parse tree produced by dafnyParser#objectAllocation_.
    def enterObjectAllocation_(self, ctx:dafnyParser.ObjectAllocation_Context):
        pass

    # Exit a parse tree produced by dafnyParser#objectAllocation_.
    def exitObjectAllocation_(self, ctx:dafnyParser.ObjectAllocation_Context):
        pass


    # Enter a parse tree produced by dafnyParser#constAtomExpression.
    def enterConstAtomExpression(self, ctx:dafnyParser.ConstAtomExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#constAtomExpression.
    def exitConstAtomExpression(self, ctx:dafnyParser.ConstAtomExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#literalExpression.
    def enterLiteralExpression(self, ctx:dafnyParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#literalExpression.
    def exitLiteralExpression(self, ctx:dafnyParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#nat.
    def enterNat(self, ctx:dafnyParser.NatContext):
        pass

    # Exit a parse tree produced by dafnyParser#nat.
    def exitNat(self, ctx:dafnyParser.NatContext):
        pass


    # Enter a parse tree produced by dafnyParser#dec.
    def enterDec(self, ctx:dafnyParser.DecContext):
        pass

    # Exit a parse tree produced by dafnyParser#dec.
    def exitDec(self, ctx:dafnyParser.DecContext):
        pass


    # Enter a parse tree produced by dafnyParser#thisExpression_.
    def enterThisExpression_(self, ctx:dafnyParser.ThisExpression_Context):
        pass

    # Exit a parse tree produced by dafnyParser#thisExpression_.
    def exitThisExpression_(self, ctx:dafnyParser.ThisExpression_Context):
        pass


    # Enter a parse tree produced by dafnyParser#oldExpression_.
    def enterOldExpression_(self, ctx:dafnyParser.OldExpression_Context):
        pass

    # Exit a parse tree produced by dafnyParser#oldExpression_.
    def exitOldExpression_(self, ctx:dafnyParser.OldExpression_Context):
        pass


    # Enter a parse tree produced by dafnyParser#freshExpression_.
    def enterFreshExpression_(self, ctx:dafnyParser.FreshExpression_Context):
        pass

    # Exit a parse tree produced by dafnyParser#freshExpression_.
    def exitFreshExpression_(self, ctx:dafnyParser.FreshExpression_Context):
        pass


    # Enter a parse tree produced by dafnyParser#allocatedExpression_.
    def enterAllocatedExpression_(self, ctx:dafnyParser.AllocatedExpression_Context):
        pass

    # Exit a parse tree produced by dafnyParser#allocatedExpression_.
    def exitAllocatedExpression_(self, ctx:dafnyParser.AllocatedExpression_Context):
        pass


    # Enter a parse tree produced by dafnyParser#unchangedExpression_.
    def enterUnchangedExpression_(self, ctx:dafnyParser.UnchangedExpression_Context):
        pass

    # Exit a parse tree produced by dafnyParser#unchangedExpression_.
    def exitUnchangedExpression_(self, ctx:dafnyParser.UnchangedExpression_Context):
        pass


    # Enter a parse tree produced by dafnyParser#cardinalityExpression_.
    def enterCardinalityExpression_(self, ctx:dafnyParser.CardinalityExpression_Context):
        pass

    # Exit a parse tree produced by dafnyParser#cardinalityExpression_.
    def exitCardinalityExpression_(self, ctx:dafnyParser.CardinalityExpression_Context):
        pass


    # Enter a parse tree produced by dafnyParser#parensExpression.
    def enterParensExpression(self, ctx:dafnyParser.ParensExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#parensExpression.
    def exitParensExpression(self, ctx:dafnyParser.ParensExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#tupleArgs.
    def enterTupleArgs(self, ctx:dafnyParser.TupleArgsContext):
        pass

    # Exit a parse tree produced by dafnyParser#tupleArgs.
    def exitTupleArgs(self, ctx:dafnyParser.TupleArgsContext):
        pass


    # Enter a parse tree produced by dafnyParser#seqDisplayExpr.
    def enterSeqDisplayExpr(self, ctx:dafnyParser.SeqDisplayExprContext):
        pass

    # Exit a parse tree produced by dafnyParser#seqDisplayExpr.
    def exitSeqDisplayExpr(self, ctx:dafnyParser.SeqDisplayExprContext):
        pass


    # Enter a parse tree produced by dafnyParser#setDisplayExpr.
    def enterSetDisplayExpr(self, ctx:dafnyParser.SetDisplayExprContext):
        pass

    # Exit a parse tree produced by dafnyParser#setDisplayExpr.
    def exitSetDisplayExpr(self, ctx:dafnyParser.SetDisplayExprContext):
        pass


    # Enter a parse tree produced by dafnyParser#mapDisplayExpr.
    def enterMapDisplayExpr(self, ctx:dafnyParser.MapDisplayExprContext):
        pass

    # Exit a parse tree produced by dafnyParser#mapDisplayExpr.
    def exitMapDisplayExpr(self, ctx:dafnyParser.MapDisplayExprContext):
        pass


    # Enter a parse tree produced by dafnyParser#mapLiteralExpressions.
    def enterMapLiteralExpressions(self, ctx:dafnyParser.MapLiteralExpressionsContext):
        pass

    # Exit a parse tree produced by dafnyParser#mapLiteralExpressions.
    def exitMapLiteralExpressions(self, ctx:dafnyParser.MapLiteralExpressionsContext):
        pass


    # Enter a parse tree produced by dafnyParser#endlessExpression.
    def enterEndlessExpression(self, ctx:dafnyParser.EndlessExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#endlessExpression.
    def exitEndlessExpression(self, ctx:dafnyParser.EndlessExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#ifExpression.
    def enterIfExpression(self, ctx:dafnyParser.IfExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#ifExpression.
    def exitIfExpression(self, ctx:dafnyParser.IfExpressionContext):
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


    # Enter a parse tree produced by dafnyParser#casePattern.
    def enterCasePattern(self, ctx:dafnyParser.CasePatternContext):
        pass

    # Exit a parse tree produced by dafnyParser#casePattern.
    def exitCasePattern(self, ctx:dafnyParser.CasePatternContext):
        pass


    # Enter a parse tree produced by dafnyParser#singleExtendedPattern.
    def enterSingleExtendedPattern(self, ctx:dafnyParser.SingleExtendedPatternContext):
        pass

    # Exit a parse tree produced by dafnyParser#singleExtendedPattern.
    def exitSingleExtendedPattern(self, ctx:dafnyParser.SingleExtendedPatternContext):
        pass


    # Enter a parse tree produced by dafnyParser#extendedPattern.
    def enterExtendedPattern(self, ctx:dafnyParser.ExtendedPatternContext):
        pass

    # Exit a parse tree produced by dafnyParser#extendedPattern.
    def exitExtendedPattern(self, ctx:dafnyParser.ExtendedPatternContext):
        pass


    # Enter a parse tree produced by dafnyParser#possiblyNegatedLiteralExpression.
    def enterPossiblyNegatedLiteralExpression(self, ctx:dafnyParser.PossiblyNegatedLiteralExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#possiblyNegatedLiteralExpression.
    def exitPossiblyNegatedLiteralExpression(self, ctx:dafnyParser.PossiblyNegatedLiteralExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#quantifierExpression.
    def enterQuantifierExpression(self, ctx:dafnyParser.QuantifierExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#quantifierExpression.
    def exitQuantifierExpression(self, ctx:dafnyParser.QuantifierExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#setComprehensionExpr.
    def enterSetComprehensionExpr(self, ctx:dafnyParser.SetComprehensionExprContext):
        pass

    # Exit a parse tree produced by dafnyParser#setComprehensionExpr.
    def exitSetComprehensionExpr(self, ctx:dafnyParser.SetComprehensionExprContext):
        pass


    # Enter a parse tree produced by dafnyParser#mapComprehensionExpr.
    def enterMapComprehensionExpr(self, ctx:dafnyParser.MapComprehensionExprContext):
        pass

    # Exit a parse tree produced by dafnyParser#mapComprehensionExpr.
    def exitMapComprehensionExpr(self, ctx:dafnyParser.MapComprehensionExprContext):
        pass


    # Enter a parse tree produced by dafnyParser#stmtInExpr.
    def enterStmtInExpr(self, ctx:dafnyParser.StmtInExprContext):
        pass

    # Exit a parse tree produced by dafnyParser#stmtInExpr.
    def exitStmtInExpr(self, ctx:dafnyParser.StmtInExprContext):
        pass


    # Enter a parse tree produced by dafnyParser#letExpression.
    def enterLetExpression(self, ctx:dafnyParser.LetExpressionContext):
        pass

    # Exit a parse tree produced by dafnyParser#letExpression.
    def exitLetExpression(self, ctx:dafnyParser.LetExpressionContext):
        pass


    # Enter a parse tree produced by dafnyParser#nameSegment.
    def enterNameSegment(self, ctx:dafnyParser.NameSegmentContext):
        pass

    # Exit a parse tree produced by dafnyParser#nameSegment.
    def exitNameSegment(self, ctx:dafnyParser.NameSegmentContext):
        pass


    # Enter a parse tree produced by dafnyParser#hashCall.
    def enterHashCall(self, ctx:dafnyParser.HashCallContext):
        pass

    # Exit a parse tree produced by dafnyParser#hashCall.
    def exitHashCall(self, ctx:dafnyParser.HashCallContext):
        pass


    # Enter a parse tree produced by dafnyParser#suffix.
    def enterSuffix(self, ctx:dafnyParser.SuffixContext):
        pass

    # Exit a parse tree produced by dafnyParser#suffix.
    def exitSuffix(self, ctx:dafnyParser.SuffixContext):
        pass


    # Enter a parse tree produced by dafnyParser#augmentedDotSuffix_.
    def enterAugmentedDotSuffix_(self, ctx:dafnyParser.AugmentedDotSuffix_Context):
        pass

    # Exit a parse tree produced by dafnyParser#augmentedDotSuffix_.
    def exitAugmentedDotSuffix_(self, ctx:dafnyParser.AugmentedDotSuffix_Context):
        pass


    # Enter a parse tree produced by dafnyParser#datatypeUpdateSuffix_.
    def enterDatatypeUpdateSuffix_(self, ctx:dafnyParser.DatatypeUpdateSuffix_Context):
        pass

    # Exit a parse tree produced by dafnyParser#datatypeUpdateSuffix_.
    def exitDatatypeUpdateSuffix_(self, ctx:dafnyParser.DatatypeUpdateSuffix_Context):
        pass


    # Enter a parse tree produced by dafnyParser#memberBindingUpdate.
    def enterMemberBindingUpdate(self, ctx:dafnyParser.MemberBindingUpdateContext):
        pass

    # Exit a parse tree produced by dafnyParser#memberBindingUpdate.
    def exitMemberBindingUpdate(self, ctx:dafnyParser.MemberBindingUpdateContext):
        pass


    # Enter a parse tree produced by dafnyParser#subsequenceSuffix_.
    def enterSubsequenceSuffix_(self, ctx:dafnyParser.SubsequenceSuffix_Context):
        pass

    # Exit a parse tree produced by dafnyParser#subsequenceSuffix_.
    def exitSubsequenceSuffix_(self, ctx:dafnyParser.SubsequenceSuffix_Context):
        pass


    # Enter a parse tree produced by dafnyParser#slicesByLengthSuffix_.
    def enterSlicesByLengthSuffix_(self, ctx:dafnyParser.SlicesByLengthSuffix_Context):
        pass

    # Exit a parse tree produced by dafnyParser#slicesByLengthSuffix_.
    def exitSlicesByLengthSuffix_(self, ctx:dafnyParser.SlicesByLengthSuffix_Context):
        pass


    # Enter a parse tree produced by dafnyParser#sequenceUpdateSuffix_.
    def enterSequenceUpdateSuffix_(self, ctx:dafnyParser.SequenceUpdateSuffix_Context):
        pass

    # Exit a parse tree produced by dafnyParser#sequenceUpdateSuffix_.
    def exitSequenceUpdateSuffix_(self, ctx:dafnyParser.SequenceUpdateSuffix_Context):
        pass


    # Enter a parse tree produced by dafnyParser#selectionSuffix_.
    def enterSelectionSuffix_(self, ctx:dafnyParser.SelectionSuffix_Context):
        pass

    # Exit a parse tree produced by dafnyParser#selectionSuffix_.
    def exitSelectionSuffix_(self, ctx:dafnyParser.SelectionSuffix_Context):
        pass


    # Enter a parse tree produced by dafnyParser#argumentListSuffix_.
    def enterArgumentListSuffix_(self, ctx:dafnyParser.ArgumentListSuffix_Context):
        pass

    # Exit a parse tree produced by dafnyParser#argumentListSuffix_.
    def exitArgumentListSuffix_(self, ctx:dafnyParser.ArgumentListSuffix_Context):
        pass


    # Enter a parse tree produced by dafnyParser#expressions.
    def enterExpressions(self, ctx:dafnyParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by dafnyParser#expressions.
    def exitExpressions(self, ctx:dafnyParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by dafnyParser#quantifierDomain.
    def enterQuantifierDomain(self, ctx:dafnyParser.QuantifierDomainContext):
        pass

    # Exit a parse tree produced by dafnyParser#quantifierDomain.
    def exitQuantifierDomain(self, ctx:dafnyParser.QuantifierDomainContext):
        pass


    # Enter a parse tree produced by dafnyParser#quantifierVarDecl.
    def enterQuantifierVarDecl(self, ctx:dafnyParser.QuantifierVarDeclContext):
        pass

    # Exit a parse tree produced by dafnyParser#quantifierVarDecl.
    def exitQuantifierVarDecl(self, ctx:dafnyParser.QuantifierVarDeclContext):
        pass


    # Enter a parse tree produced by dafnyParser#ident.
    def enterIdent(self, ctx:dafnyParser.IdentContext):
        pass

    # Exit a parse tree produced by dafnyParser#ident.
    def exitIdent(self, ctx:dafnyParser.IdentContext):
        pass


    # Enter a parse tree produced by dafnyParser#dotSuffix.
    def enterDotSuffix(self, ctx:dafnyParser.DotSuffixContext):
        pass

    # Exit a parse tree produced by dafnyParser#dotSuffix.
    def exitDotSuffix(self, ctx:dafnyParser.DotSuffixContext):
        pass


    # Enter a parse tree produced by dafnyParser#noUSIdent.
    def enterNoUSIdent(self, ctx:dafnyParser.NoUSIdentContext):
        pass

    # Exit a parse tree produced by dafnyParser#noUSIdent.
    def exitNoUSIdent(self, ctx:dafnyParser.NoUSIdentContext):
        pass


    # Enter a parse tree produced by dafnyParser#wildIdent.
    def enterWildIdent(self, ctx:dafnyParser.WildIdentContext):
        pass

    # Exit a parse tree produced by dafnyParser#wildIdent.
    def exitWildIdent(self, ctx:dafnyParser.WildIdentContext):
        pass


    # Enter a parse tree produced by dafnyParser#identOrDigits.
    def enterIdentOrDigits(self, ctx:dafnyParser.IdentOrDigitsContext):
        pass

    # Exit a parse tree produced by dafnyParser#identOrDigits.
    def exitIdentOrDigits(self, ctx:dafnyParser.IdentOrDigitsContext):
        pass


    # Enter a parse tree produced by dafnyParser#noUSIdentOrDigits.
    def enterNoUSIdentOrDigits(self, ctx:dafnyParser.NoUSIdentOrDigitsContext):
        pass

    # Exit a parse tree produced by dafnyParser#noUSIdentOrDigits.
    def exitNoUSIdentOrDigits(self, ctx:dafnyParser.NoUSIdentOrDigitsContext):
        pass


    # Enter a parse tree produced by dafnyParser#moduleName.
    def enterModuleName(self, ctx:dafnyParser.ModuleNameContext):
        pass

    # Exit a parse tree produced by dafnyParser#moduleName.
    def exitModuleName(self, ctx:dafnyParser.ModuleNameContext):
        pass


    # Enter a parse tree produced by dafnyParser#className.
    def enterClassName(self, ctx:dafnyParser.ClassNameContext):
        pass

    # Exit a parse tree produced by dafnyParser#className.
    def exitClassName(self, ctx:dafnyParser.ClassNameContext):
        pass


    # Enter a parse tree produced by dafnyParser#datatypeName.
    def enterDatatypeName(self, ctx:dafnyParser.DatatypeNameContext):
        pass

    # Exit a parse tree produced by dafnyParser#datatypeName.
    def exitDatatypeName(self, ctx:dafnyParser.DatatypeNameContext):
        pass


    # Enter a parse tree produced by dafnyParser#datatypeMemberName.
    def enterDatatypeMemberName(self, ctx:dafnyParser.DatatypeMemberNameContext):
        pass

    # Exit a parse tree produced by dafnyParser#datatypeMemberName.
    def exitDatatypeMemberName(self, ctx:dafnyParser.DatatypeMemberNameContext):
        pass


    # Enter a parse tree produced by dafnyParser#newtypeName.
    def enterNewtypeName(self, ctx:dafnyParser.NewtypeNameContext):
        pass

    # Exit a parse tree produced by dafnyParser#newtypeName.
    def exitNewtypeName(self, ctx:dafnyParser.NewtypeNameContext):
        pass


    # Enter a parse tree produced by dafnyParser#iteratorName.
    def enterIteratorName(self, ctx:dafnyParser.IteratorNameContext):
        pass

    # Exit a parse tree produced by dafnyParser#iteratorName.
    def exitIteratorName(self, ctx:dafnyParser.IteratorNameContext):
        pass


    # Enter a parse tree produced by dafnyParser#typeVariableName.
    def enterTypeVariableName(self, ctx:dafnyParser.TypeVariableNameContext):
        pass

    # Exit a parse tree produced by dafnyParser#typeVariableName.
    def exitTypeVariableName(self, ctx:dafnyParser.TypeVariableNameContext):
        pass


    # Enter a parse tree produced by dafnyParser#methodFunctionName.
    def enterMethodFunctionName(self, ctx:dafnyParser.MethodFunctionNameContext):
        pass

    # Exit a parse tree produced by dafnyParser#methodFunctionName.
    def exitMethodFunctionName(self, ctx:dafnyParser.MethodFunctionNameContext):
        pass


    # Enter a parse tree produced by dafnyParser#labelName.
    def enterLabelName(self, ctx:dafnyParser.LabelNameContext):
        pass

    # Exit a parse tree produced by dafnyParser#labelName.
    def exitLabelName(self, ctx:dafnyParser.LabelNameContext):
        pass


    # Enter a parse tree produced by dafnyParser#attributeName.
    def enterAttributeName(self, ctx:dafnyParser.AttributeNameContext):
        pass

    # Exit a parse tree produced by dafnyParser#attributeName.
    def exitAttributeName(self, ctx:dafnyParser.AttributeNameContext):
        pass


    # Enter a parse tree produced by dafnyParser#exportId.
    def enterExportId(self, ctx:dafnyParser.ExportIdContext):
        pass

    # Exit a parse tree produced by dafnyParser#exportId.
    def exitExportId(self, ctx:dafnyParser.ExportIdContext):
        pass


    # Enter a parse tree produced by dafnyParser#typeNameOrCtorSuffix.
    def enterTypeNameOrCtorSuffix(self, ctx:dafnyParser.TypeNameOrCtorSuffixContext):
        pass

    # Exit a parse tree produced by dafnyParser#typeNameOrCtorSuffix.
    def exitTypeNameOrCtorSuffix(self, ctx:dafnyParser.TypeNameOrCtorSuffixContext):
        pass


    # Enter a parse tree produced by dafnyParser#moduleQualifiedName.
    def enterModuleQualifiedName(self, ctx:dafnyParser.ModuleQualifiedNameContext):
        pass

    # Exit a parse tree produced by dafnyParser#moduleQualifiedName.
    def exitModuleQualifiedName(self, ctx:dafnyParser.ModuleQualifiedNameContext):
        pass


    # Enter a parse tree produced by dafnyParser#identType.
    def enterIdentType(self, ctx:dafnyParser.IdentTypeContext):
        pass

    # Exit a parse tree produced by dafnyParser#identType.
    def exitIdentType(self, ctx:dafnyParser.IdentTypeContext):
        pass


    # Enter a parse tree produced by dafnyParser#fIdentType.
    def enterFIdentType(self, ctx:dafnyParser.FIdentTypeContext):
        pass

    # Exit a parse tree produced by dafnyParser#fIdentType.
    def exitFIdentType(self, ctx:dafnyParser.FIdentTypeContext):
        pass


    # Enter a parse tree produced by dafnyParser#cIdentType.
    def enterCIdentType(self, ctx:dafnyParser.CIdentTypeContext):
        pass

    # Exit a parse tree produced by dafnyParser#cIdentType.
    def exitCIdentType(self, ctx:dafnyParser.CIdentTypeContext):
        pass


    # Enter a parse tree produced by dafnyParser#gIdentType.
    def enterGIdentType(self, ctx:dafnyParser.GIdentTypeContext):
        pass

    # Exit a parse tree produced by dafnyParser#gIdentType.
    def exitGIdentType(self, ctx:dafnyParser.GIdentTypeContext):
        pass


    # Enter a parse tree produced by dafnyParser#localIdentTypeOptional.
    def enterLocalIdentTypeOptional(self, ctx:dafnyParser.LocalIdentTypeOptionalContext):
        pass

    # Exit a parse tree produced by dafnyParser#localIdentTypeOptional.
    def exitLocalIdentTypeOptional(self, ctx:dafnyParser.LocalIdentTypeOptionalContext):
        pass


    # Enter a parse tree produced by dafnyParser#identTypeOptional.
    def enterIdentTypeOptional(self, ctx:dafnyParser.IdentTypeOptionalContext):
        pass

    # Exit a parse tree produced by dafnyParser#identTypeOptional.
    def exitIdentTypeOptional(self, ctx:dafnyParser.IdentTypeOptionalContext):
        pass


    # Enter a parse tree produced by dafnyParser#typeIdentOptional.
    def enterTypeIdentOptional(self, ctx:dafnyParser.TypeIdentOptionalContext):
        pass

    # Exit a parse tree produced by dafnyParser#typeIdentOptional.
    def exitTypeIdentOptional(self, ctx:dafnyParser.TypeIdentOptionalContext):
        pass


    # Enter a parse tree produced by dafnyParser#formalsOptionalIds.
    def enterFormalsOptionalIds(self, ctx:dafnyParser.FormalsOptionalIdsContext):
        pass

    # Exit a parse tree produced by dafnyParser#formalsOptionalIds.
    def exitFormalsOptionalIds(self, ctx:dafnyParser.FormalsOptionalIdsContext):
        pass


    # Enter a parse tree produced by dafnyParser#attribute.
    def enterAttribute(self, ctx:dafnyParser.AttributeContext):
        pass

    # Exit a parse tree produced by dafnyParser#attribute.
    def exitAttribute(self, ctx:dafnyParser.AttributeContext):
        pass



del dafnyParser