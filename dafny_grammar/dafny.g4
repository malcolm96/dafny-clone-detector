grammar dafny;

fragment EOL: '\r\n' | '\n';
WHITESPACE: [ \t\n\r]+ -> skip;
COMMENT: '//' .*? EOL -> skip;

fragment LETTER : [A-Za-z];

fragment DIGIT : [0-9];
fragment POS_DIGIT : [1-9];
fragment POS_DIGIT_FROM_2 : [2-9];

fragment HEXDIGIT : [0-9A-Fa-f];

fragment SPECIAL : [_'?];

fragment CR : '\r';

fragment LF : '\n';

fragment TAB : '\t';

fragment SPACE : ' ';

fragment NONDIGIT_ID_CHAR : LETTER | SPECIAL;

fragment IDCHAR : NONDIGIT_ID_CHAR | DIGIT;

fragment NONIDCHAR : ~[A-Za-z0-9_'?];

fragment CHARCHAR : ~('\'' | '\\' | '\r' | '\n');

fragment STRINGCHAR : ~('"' | '\\' | '\r' | '\n');

fragment VERBATIMSTRINGCHAR : ~'"';

SEMICOLON: ';';

RESERVED_WORDS
    : 'abstract' | 'allocated' | 'as' | 'assert' | 'assume'
    | 'bool' | 'break' | 'by'
    | 'calc' | 'case' | 'char' | 'class' | 'codatatype'
    | 'const' | 'constructor' | 'continue'
    | 'datatype' | 'decreases'
    | 'else' | 'ensures' | 'exists' | 'expect' | 'export' | 'extends'
    | 'false' | 'for' | 'forall' | 'fresh' | 'function' | 'ghost'
    | 'if' | 'imap' | 'import' | 'in' | 'include'
    | 'int' | 'invariant' | 'is' | 'iset' | 'iterator'
    | 'label' | 'lemma' | 'map' | 'match' | 'method'
    | 'modifies' | 'modify' | 'module' | 'multiset'
    | 'nameonly' | 'nat' | 'new' | 'newtype' | 'null'
    | 'object' | 'object?' | 'old' | 'opaque' | 'opened' | 'ORDINAL'
    | 'predicate' | 'print' | 'provides'
    | 'reads' | 'real' | 'refines' | 'requires' | 'return'
    | 'returns' | 'reveal' | 'reveals'
    | 'seq' | 'set' | 'static' | 'string'
    | 'then' | 'this' | 'trait' | 'true' | 'twostate' | 'type'
    | 'unchanged' | 'var' | 'while' | 'witness'
    | 'yield' | 'yields'
    | ARRAY_TOKEN | BV_TOKEN
    ;

IDENT: NONDIGIT_ID_CHAR (IDCHAR)*;

ARRAY_TOKEN
    : 'array' (POS_DIGIT_FROM_2 | POS_DIGIT DIGIT* ) '?'
    ;

BV_TOKEN
    : 'bv' ( '0' | POS_DIGIT DIGIT* )
    ;


DIGITS
    : DIGIT ('_'? DIGIT)*
    ;

HEXDIGITS
    : '0x' HEXDIGIT ('_'? HEXDIGIT)*
    ;

DECIMALDIGITS
    : DIGIT ('_'? DIGIT)* '.' DIGIT ('_'? DIGIT)*
    ;

ESCAPEDCHAR
    : '\'' | '"' | '\\' | '0' | '\n' | '\r' | '\t'
    | 'u' HEXDIGIT HEXDIGIT HEXDIGIT HEXDIGIT
    | 'U{' HEXDIGIT+ '}'
    ;

CHARTOKEN
    : '\'' ( CHARCHAR | ESCAPEDCHAR ) '\''
    ;

STRINGTOKEN
    : '"' ( STRINGCHAR | ESCAPEDCHAR )* '"'
    | '@' '"' ( VERBATIMSTRINGCHAR | '""' )* '"'
    ;

ELLIPSIS
    : '...'
    ;

program
    : includeDirective_*
      topDecl*
      EOF
    ;

includeDirective_
    : 'include' STRINGTOKEN
    ;


topDecl
    :  declModifier
      | subModuleDecl
      | classDecl
      | datatypeDecl
      | newtypeDecl
      | synonymTypeDecl  // includes abstract types
      | iteratorDecl
      | traitDecl
      | classMemberDecl
    ;


declModifier
    : 'abstract' | 'ghost' | 'static' | 'opaque'
    ;

subModuleDecl
    : moduleDefinition
    | moduleImport
    | moduleExport
    ;

moduleDefinition
    : 'module' attribute* moduleQualifiedName
      ('refines' moduleQualifiedName )?
      '{' topDecl* '}'
    ;

moduleImport
    : 'import'
      ( 'opened' )?
      ( qualifiedModuleExport
      | moduleName '=' qualifiedModuleExport
      | moduleName ':' qualifiedModuleExport
      )
    ;

qualifiedModuleExport
    : moduleQualifiedName ( '`' moduleExportSuffix )?
    ;

moduleExportSuffix
    : exportId
    | '{' exportId ( ',' exportId )* '}'
    ;

moduleExport
    : 'export'
      ( exportId )?
      ( '...' )?
      (
        'extends'  exportId ( ',' exportId )*
      | 'provides' ( exportSignature ( ',' exportSignature )* | '*' )
      | 'reveals'  ( exportSignature ( ',' exportSignature )* | '*' )
      )
    ;

exportSignature
    : typeNameOrCtorSuffix ( '.' typeNameOrCtorSuffix )?
    ;

type
    : domainType_
    | arrowType_
    ;

domainType_
    : boolType_
    | charType_
    | intType_
    | realType_
    | ordinalType_
    | bitVectorType_
    | objectType_
    | finiteSetType_
    | infiniteSetType_
    | multisetType_
    | finiteMapType_
    | infiniteMapType_
    | sequenceType_
    | natType_
    | stringType_
    | arrayType_
    | namedType
    ;

namedType
    : nameSegmentForTypeName ( '.' nameSegmentForTypeName )*
    ;

nameSegmentForTypeName
    : IDENT ( genericInstantiation )?
    ;

boolType_
    : 'bool'
    ;

intType_
    : 'int'
    ;

realType_
    : 'real'
    ;

bitVectorType_
    : BV_TOKEN
    ;

ordinalType_
    : 'ORDINAL'
    ;

charType_
    : 'char'
    ;

genericInstantiation
    : '<' type ( ',' type )* '>'
    ;

genericParameters
    : '<' ( Variance )? typeVariableName typeParameterCharacteristics*
      ( ',' ( Variance )? typeVariableName typeParameterCharacteristics* )*
      '>'
    ;

Variance
    : '*' | '+' | '!' | '-'
    ;

typeParameterCharacteristics
    : '(' tPCharOption ( ',' tPCharOption )* ')'
    ;

tPCharOption
    : '==' | '0' | '00' | '!' 'new'
    ;

finiteSetType_
    : 'set' ( genericInstantiation )?
    ;

infiniteSetType_
    : 'iset' ( genericInstantiation )?
    ;

multisetType_
    : 'multiset' (genericInstantiation)?
    ;

sequenceType_
    : 'seq' ( genericInstantiation )?
    ;

stringType_
    : 'string'
    ;

finiteMapType_
    : 'map' ( genericInstantiation )
    ;

infiniteMapType_
    : 'imap' ( genericInstantiation )
    ;

synonymTypeDecl
    : synonymTypeDecl_
    | opaqueTypeDecl_
    | subsetTypeDecl_
    ;

synonymTypeName
    : noUSIdent
    ;

synonymTypeDecl_
    : 'type' attribute* synonymTypeName
      typeParameterCharacteristics*
      ( genericParameters )?
      '=' type
    ;

opaqueTypeDecl_
    : 'type' attribute* synonymTypeName
      typeParameterCharacteristics*
      ( genericParameters )?
      (typeMembers)?
    ;

typeMembers
    : '{'
      (
        declModifier*
        classMemberDecl
      )*
      '}'
    ;

subsetTypeDecl_
    : 'type'
      attribute*
      synonymTypeName ( genericParameters )?
      '='
      localIdentTypeOptional
      '|'
      expression
      (
        'ghost' 'witness' expression
      | 'witness' expression
      | 'witness' '*'
      )?
    ;

natType_
    : 'nat'
    ;

newtypeDecl
    : 'newtype' attribute* newtypeName '='
      (ELLIPSIS)?
      (
        localIdentTypeOptional
        '|'
        expression
        (
          'ghost' 'witness' expression
        | 'witness' expression
        | 'witness' '*'
        )?
      | type
      )
      (typeMembers)?
    ;

classDecl
    : 'class' attribute* className ( genericParameters )?
      ( 'extends' type ( ',' type )* | ELLIPSIS )?
      '{'
      (
        declModifier*
        classMemberDecl+
      )*
      '}'
    ;

classMemberDecl
    : fieldDecl // allowed iff moduleLevelDecl is false
    | constantFieldDecl
    | functionDecl
    | methodDecl
    ;

traitDecl
    : 'trait' attribute* className ( genericParameters )?
      ( 'extends' type ( ',' type )* | ELLIPSIS )
      '{'
      (
        declModifier*
        classMemberDecl+
      )*
      '}'
    ;

objectType_
    : 'object' | 'object?'
    ;

arrayType_
    : ARRAY_TOKEN ( genericInstantiation )?
    ;

iteratorDecl
    : 'iterator' attribute* iteratorName
      (
        ( genericParameters )?
        formals
        ( 'yields' formals )?
      | ELLIPSIS
      )
      iteratorSpec
      ( blockStmt )?
    ;

arrowType_
    : domainType_ '~>' type
    | domainType_ '-->' type
    | domainType_ '->' type
    ;

datatypeDecl
    : ('datatype' | 'codatatype')
      attribute*
      datatypeName (genericParameters)?
      '='
      (ELLIPSIS)?
      ( '|' )? datatypeMemberDecl
      ( '|' datatypeMemberDecl )*
      ( typeMembers )?
    ;

datatypeMemberDecl
    : attribute* datatypeMemberName ( formalsOptionalIds )?
    ;

fieldDecl
    : 'var' attribute* fIdentType ( ',' fIdentType )*
    ;

constantFieldDecl
    : 'const' attribute* cIdentType (ELLIPSIS)?
      ( ':=' expression )?
    ;

methodDecl
    : methodKeyword_ attribute* ( methodFunctionName )?
      ( methodSignature_ // isExtreme is true if this is a least or greatest lemma declaration
      | ELLIPSIS
      )
      methodSpec // isConstructor is true if this is a constructor declaration
      ( blockStmt)?
    ;

methodKeyword_
    : 'method'
    | 'constructor'
    | 'lemma'
    | 'twostate' 'lemma'
    | 'least' 'lemma'
    | 'greatest' 'lemma'
    ;

methodSignature_
    : ( genericParameters )?
      ( KType )? // permitted only if isExtreme == true
      formals
      ( 'returns' formals )?
    ;

KType
    : '[' ( 'nat' | 'ORDINAL' ) ']'
    ;

formals
    : '(' ( attribute* gIdentType
            ( ',' attribute* gIdentType )*
          )?
      ')'
    ;

functionDecl
    : (
        ( 'twostate' )? 'function' ( 'method' )? attribute* opaqueAttribute?
        methodFunctionName
        functionSignatureOrEllipsis_
      | 'predicate' ( 'method' )? attribute*
        methodFunctionName
        predicateSignatureOrEllipsis_
      | ( 'least' | 'greatest' ) 'predicate' attribute*
        methodFunctionName
        predicateSignatureOrEllipsis_
      )
      functionSpec
      (functionBody)?
    ;

opaqueAttribute
    : '{:opaque}'
    ;

functionSignatureOrEllipsis_
    : functionSignature_ | ELLIPSIS
    ;

functionSignature_
    : ( genericParameters )?
      formals
      ':'
      (
        type
      | '(' gIdentType')'
      )
    ;

predicateSignatureOrEllipsis_
    : predicateSignature_ | ELLIPSIS
    ;

predicateSignature_
    : ( genericParameters )?
      ( KType )?
      formals
      (
        ':'
        (
          type
        | '(' IDENT ':' 'bool' ')'
        )
      )?
    ;

functionBody
    : '{' expression '}' ( 'by' 'method' blockStmt )?
    ;

methodSpec
    : (
        modifiesClause
      | requiresClause
      | ensuresClause
      | decreasesClause
      )*
    ;

functionSpec
    : (
        requiresClause
      | readsClause
      | ensuresClause
      | decreasesClause
      )*
    ;

lambdaSpec
    : (
        readsClause
      | 'requires' expression
      )*
    ;

iteratorSpec
    : (
        readsClause
      | modifiesClause
      | ( 'yield' )? requiresClause
      | ( 'yield' )? ensuresClause
      | decreasesClause
      )*
    ;

loopSpec
    : (
        invariantClause_
      | decreasesClause
      | modifiesClause
      )*
    ;

requiresClause
    : 'requires' attribute*
      ( labelName ':' )? // Label allowed only if allowLabel is true
      expression SEMICOLON?
    ;

ensuresClause
    : 'ensures' attribute* expression
    ;

decreasesClause
    : 'decreases' attribute* decreasesList
    ;

decreasesList
    : possiblyWildExpression
      ( ',' possiblyWildExpression )*
    ;

possiblyWildExpression
    : ( '*'  // if allowWild is false, using '*' provokes an error
      | expression
      )
    ;

modifiesClause
    : 'modifies' attribute*
      frameExpression
      ( ',' frameExpression )*
    ;

invariantClause_
    : 'invariant' attribute*
      expression
    ;

readsClause
    : 'reads' attribute*
      possiblyWildFrameExpression
      ( ',' possiblyWildFrameExpression )*
    ;

possiblyWildFrameExpression
    : ( '*'  // if allowWild is false, using '*' provokes an error
      | frameExpression
      )
    ;

frameExpression
    : ( expression ( frameField )?
      | frameField
      )
    ;

frameField
    : '`' identOrDigits
    ;


stmt
    : ( 'label' labelName ':' )* nonLabeledStmt
    ;

nonLabeledStmt
    : assertStmt
    | assumeStmt
    | blockStmt
    | breakStmt
    | calcStmt
    | expectStmt
    | forallStmt
    | ifStmt
    | matchStmt
    | modifyStmt
    | printStmt
    | returnStmt
    | revealStmt
    | updateStmt
    | updateFailureStmt
    | varDeclStatement
    | whileStmt
    | forLoopStmt
    | yieldStmt
    ;

breakStmt
    : 'break' labelName ';'
    | 'continue' labelName ';'
    | ( 'break' )* 'break' ';'
    | ( 'break' )* 'continue' ';'
    ;

blockStmt
    : '{' stmt* '}'
    ;

returnStmt
    : 'return' ( rhs ( ',' rhs )* )? ';'
    ;

yieldStmt
    : 'yield' ( rhs ( ',' rhs )* )? ';'
    ;

updateStmt
    : lhs
      (
        attribute* ';'
      |
        ( ',' lhs )*
        (
          ':=' rhs ( ',' rhs )*
        | ':|' ( 'assume' )? expression
        )
        ';'
      )
    ;

updateFailureStmt
    : ( lhs ( ',' lhs )* )?
      ':-'
      ( 'expect' | 'assert' | 'assume' )?
      expression
      ( ',' rhs )*
      ';'
    ;

varDeclStatement
    : ( 'ghost' )? 'var' attribute*
      (
        localIdentTypeOptional
        ( ',' attribute* localIdentTypeOptional )*
        (
          ':=' rhs ( ',' rhs )*
        | ':-' ( 'expect' | 'assert' | 'assume' )?
               expression
               ( ',' rhs )*
        | attribute* ':|' ( 'assume' )? expression
        )?
      | casePatternLocal
        ( ':=' | attribute* ':|' )
        expression
      )
      ';'
    ;

casePatternLocal
    : ( IDENT)? '(' casePatternLocal ( ',' casePatternLocal )* ')'
    | localIdentTypeOptional
    ;

guard
    : '*'
    | '(' '*' ')'
    | expression
    ;

bindingGuard
    : identTypeOptional ( ',' identTypeOptional )*
      attribute*
      ':|'
      expression
    ;

ifStmt
    : 'if'
      (
        alternativeBlock
      | ( bindingGuard
        | guard
        )
        blockStmt ( 'else' ( ifStmt | blockStmt ) )?
      )
    ;

alternativeBlock
    : ( alternativeBlockCase )*
    | '{' ( alternativeBlockCase )* '}'
    ;

alternativeBlockCase
    : 'case'
      (
        bindingGuard // permitted iff allowBindingGuards == true
      | expression
      )
      '=>' stmt*
    ;

whileStmt
    : 'while'
      (
        loopSpec
        alternativeBlock
      | guard
        loopSpec
        ( blockStmt
        |           // no body
        )
      )
    ;

forLoopStmt
    : 'for' identTypeOptional ':='
      expression
      ( 'to' | 'downto' )
      ( '*' | expression )
      loopSpec
      ( blockStmt
      |           // no body
      )
    ;

matchStmt
    : 'match'
      expression
      (
        '{' caseStmt* '}'
      | caseStmt*
      )
    ;

caseStmt
    : 'case' extendedPattern '=>' stmt*
    ;

assertStmt
    : 'assert'
      attribute*
      ( labelName ':' )?
      expression
      (
        ';'
      | 'by' blockStmt
      )
    ;

assumeStmt
    : 'assume'
      attribute*
      expression
      ';'
    ;

expectStmt
    : 'expect'
      attribute*
      expression
      ( ',' expression )?
      ';'
    ;

printStmt
    : 'print'
      expression
      ( ',' expression )*
      ';'
    ;

revealStmt
    : 'reveal'
      expression
      ( ',' expression )*
      ';'
    ;

forallStmt
    : 'forall'
      ( '(' ( quantifierDomain )? ')'
      | ( quantifierDomain )
      )
      ensuresClause*
      ( blockStmt )?
    ;

modifyStmt
    : 'modify'
      attribute*
      frameExpression
      ( ',' frameExpression )*
      ';'
    ;

calcStmt
    : 'calc' attribute* ( calcOp )? '{' calcBody_ '}'
    ;

calcBody_
    : ( calcLine_ ( calcOp )? hints_ )*
    ;

calcLine_
    : expression ';'
    ;

hints_
    : ( blockStmt | calcStmt )*
    ;

calcOp
    : '=='
      ( '#' '[' expression ']' )?
    | '<' | '>' | '!=' | '<=' | '>='
    | '<==>' | '==>' | '<=='
    ;

expression
    : equivExpression
      ( ';' expression )?
    ;

equivExpression
    : impliesExpliesExpression
      ( '<==>' impliesExpliesExpression )*
    ;

impliesExpliesExpression
    : logicalExpression
      (
        '==>' impliesExpression
      | '<==' logicalExpression
            ( '<==' logicalExpression )*
      )?
    ;

impliesExpression
    : logicalExpression
      ( '==>' impliesExpression )?
    ;

logicalExpression
    : ( '&&' | '||' )?
      relationalExpression
      ( ( '&&' | '||' )
        relationalExpression
      )*
    ;

relationalExpression
    : shiftTerm
      ( relOp shiftTerm )*
    ;

relOp
    : '=='
      ( '#' '[' expression']' )?
    | '!='
      ( '#' '[' expression']' )?
    | '<' | '>' | '<=' | '>='
    | 'in'
    | '!in'
    | '!!'
    ;

shiftTerm
    : term
      ( ShiftOp term )*
    ;

ShiftOp
    : '<<' | '>>'
    ;

term
    : factor
      ( AddOp factor )*
    ;

AddOp
    : '+' | '-'
    ;

factor
    : bitvectorFactor
      ( MulOp bitvectorFactor )*
    ;

MulOp
    : '*' | '/' | '%'
    ;

bitvectorFactor
    : asExpression
      ( BVOp asExpression )*
    ;

BVOp
    : '|' | '&' | '^'
    ;

asExpression
    : unaryExpression
      ( ( 'as' | 'is' ) type )*
    ;

unaryExpression
    : '-' unaryExpression
    | '!' unaryExpression
    | primaryExpression
    ;

primaryExpression
    : nameSegment ( suffix )*
    | lambdaExpression
    | mapDisplayExpr ( suffix )*
    | seqDisplayExpr ( suffix )*
    | setDisplayExpr ( suffix )*
    | endlessExpression
    | constAtomExpression ( suffix )*
    ;

 lambdaExpression
    : ( wildIdent
      | '(' ( identTypeOptional ( ',' identTypeOptional )* )? ')'
      )
      lambdaSpec
      '=>'
      expression
    ;

lhs
    : nameSegment ( suffix )*
    | constAtomExpression suffix ( suffix )*
    ;

rhs
    : arrayAllocation_
    | objectAllocation_
    | expression
    | HavocRhs_
    attribute*
    ;

arrayAllocation_
    : 'new' ( type )? '[' ( expressions )? ']'
      ( '(' expression')'
      | '[' ( expressions )? ']'
      )?
    ;

actualBindings
    : actualBinding
      ( ',' actualBinding )*
    ;

actualBinding
    : ( noUSIdentOrDigits ':=' )?
      expression
    ;



objectAllocation_
    : 'new' type ( '.' typeNameOrCtorSuffix )?
      ( '(' ( actualBindings )? ')' )?
    ;

HavocRhs_
    : '*'
    ;

constAtomExpression
    : literalExpression
    | thisExpression_
    | freshExpression_
    | allocatedExpression_
    | unchangedExpression_
    | oldExpression_
    | cardinalityExpression_
    | parensExpression
    ;

literalExpression
    : 'false'
    | 'true'
    | 'null'
    | nat
    | dec
    | CHARTOKEN
    | STRINGTOKEN
    ;

nat
    : DIGITS
    | HEXDIGITS
    ;

dec
    : DECIMALDIGITS
    ;

thisExpression_
    : 'this'
    ;

oldExpression_
    : 'old' ( '@' labelName )?
      '(' expression')'
    ;

freshExpression_
    : 'fresh' ( '@' labelName )?
      '(' expression')'
    ;

allocatedExpression_
    : 'allocated' '(' expression')'
    ;

unchangedExpression_
    : 'unchanged' ( '@' labelName )?
      '(' frameExpression
          ( ',' frameExpression)*
      ')'
    ;

cardinalityExpression_
    : '|' expression'|'
    ;

parensExpression
    : '(' ( tupleArgs )? ')'
    ;

tupleArgs
    : ( 'ghost' )?
      actualBinding // argument is true iff the ghost modifier is present
      ( ','
        ( 'ghost' )?
        actualBinding// argument is true iff the ghost modifier is present
      )*
    ;

seqDisplayExpr
    : '[' (expressions )? ']'
    | 'seq' ( genericInstantiation )?
      '(' expression
      ',' expression
      ')'
    ;

setDisplayExpr
    : ( 'iset' | 'multiset' )? '{' (expressions )? '}'
    | 'multiset' '(' expression')'
    ;

mapDisplayExpr
    : ('map' | 'imap') '[' ( mapLiteralExpressions ) ']'
    ;

mapLiteralExpressions
    : expression
      ':='
      expression
      ( ','
        expression
        ':='
        expression
      )*
    ;

endlessExpression
    : ifExpression
    | matchExpression
    | quantifierExpression
    | setComprehensionExpr
    | stmtInExpr expression
    | letExpression
    | mapComprehensionExpr
    ;

ifExpression
    : 'if' ( bindingGuard
           | expression
           )
      'then' expression
      'else' expression
    ;

matchExpression
    : 'match'
      expression
      ( '{' ( caseExpression )* '}'
      | ( caseExpression )*
      )
    ;

caseExpression
    : 'case' attribute* extendedPattern '=>' expression
    ;

casePattern
    : identTypeOptional
    | (IDENT)? '(' ( casePattern ( ',' casePattern )* )? ')'
    ;

singleExtendedPattern
    : possiblyNegatedLiteralExpression
    | identTypeOptional
    | (IDENT)? '(' ( singleExtendedPattern ( ',' singleExtendedPattern )* )? ')'
    ;

extendedPattern
    : ( '|' )? singleExtendedPattern ( '|' singleExtendedPattern )*
    ;

possiblyNegatedLiteralExpression
    : '-' ( nat | dec )
    | literalExpression
    ;

quantifierExpression
    : ( 'forall' | 'exists' )  quantifierDomain '::'
      expression
    ;

setComprehensionExpr
    : ('set' | 'iset' )?
      quantifierDomain
      ( '::' expression )?
    ;

mapComprehensionExpr
    : ( 'map' | 'imap' )
      quantifierDomain
      '::'
      expression
      ( ':=' expression )?
    ;

stmtInExpr
    : assertStmt
    | assumeStmt
    | expectStmt
    | revealStmt
    | calcStmt
    ;

letExpression
    : (
        ( 'ghost' )? 'var' casePattern ( ',' casePattern )*
        ( ':=' | ':-' | attribute* ':|' )
        expression
        ( ',' expression )*
      | ':-'
        expression
      )
      ';'
      expression
    ;

nameSegment
    : IDENT ( genericInstantiation | hashCall )?
    ;

hashCall
    : '#' ( genericInstantiation )?
      '[' expression']'
      '(' ( actualBindings )? ')'
    ;

suffix
    : augmentedDotSuffix_
    | datatypeUpdateSuffix_
    | subsequenceSuffix_
    | slicesByLengthSuffix_
    | sequenceUpdateSuffix_
    | selectionSuffix_
    | argumentListSuffix_
    ;

augmentedDotSuffix_
    : '.' dotSuffix ( genericInstantiation | hashCall )?
    ;

datatypeUpdateSuffix_
    : '.' '(' memberBindingUpdate ( ',' memberBindingUpdate )* ')'
    ;

memberBindingUpdate
    : ( IDENT | DIGITS )
      ':=' expression
    ;

subsequenceSuffix_
    : '[' ( expression)?
      '..' ( expression )?
      ']'
    ;

slicesByLengthSuffix_
    : '[' expression ':'
      (
        expression
        ( ':' expression )*
        ( ':' )?
      )?
      ']'
    ;

sequenceUpdateSuffix_
    : '[' expression
      ':=' expression
      ']'
    ;

selectionSuffix_
    : '[' expression
      ( ',' expression )*
      ']'
    ;

argumentListSuffix_
    : '(' (expressions ) ')'
    ;

expressions
    : expression
      ( ',' expression )*
    ;



quantifierDomain
    : quantifierVarDecl
      ( ',' quantifierVarDecl )*
    ;

quantifierVarDecl
    : identTypeOptional
      ( '<-' expression )?
      attribute*
      ( '|' expression)?
    ;

ident: IDENT
    ;

dotSuffix
    : IDENT | DIGITS | 'requires' | 'reads'
    ;

noUSIdent
    : IDENT
    ;

wildIdent
    : noUSIdent | '_'
    ;

identOrDigits
    : IDENT | DIGITS
    ;

noUSIdentOrDigits
    : noUSIdent | DIGITS
    ;

moduleName
    : noUSIdent
    ;

className
    : noUSIdent    // also traits
    ;

datatypeName
    : noUSIdent
    ;

datatypeMemberName
    : noUSIdentOrDigits
    ;

newtypeName
    : noUSIdent
    ;

iteratorName
    : noUSIdent
    ;

typeVariableName
    : noUSIdent
    ;

methodFunctionName
    : noUSIdentOrDigits
    ;

labelName
    : noUSIdentOrDigits
    ;

attributeName
    : noUSIdent
    ;

exportId
    : noUSIdentOrDigits
    ;

typeNameOrCtorSuffix
    : noUSIdentOrDigits
    ;

moduleQualifiedName
    : moduleName ( '.' moduleName )*
    ;

identType
    : wildIdent ':' type
    ;

fIdentType
    : noUSIdentOrDigits ':' type
    ;

cIdentType
    : noUSIdentOrDigits ( ':' type )?
    ;

gIdentType
    : ( 'ghost' | 'new' | 'nameonly' | 'older' )* identType
      ( ':=' expression )?
    ;

localIdentTypeOptional
    : wildIdent ( ':' type )?
    ;

identTypeOptional
    : wildIdent ( ':' type )?
    ;

typeIdentOptional
    : attribute* ( 'ghost' | 'nameonly' )* ( noUSIdentOrDigits ':' )? type
      ( ':=' expression)?
    ;

formalsOptionalIds
    : '(' ( typeIdentOptional
            ( ',' typeIdentOptional )*
          ) ')'
    ;

attribute : '{:' attributeName expressions? '}';
