%{
#include <bits/stdc++.h>

%}
%start CompilationUnit
%token abstract
%token continue
%token for
%token new
%token switch
%token assert
%token default
%token if
%token package
%token synchronized
%token boolean
%token do
%token goto
%token private
%token this
%token break
%token double
%token implements
%token protected
%token throw
%token byte
%token else
%token import
%token public
%token throws
%token case
%token enum
%token instanceof
%token return
%token transient
%token catch
%token extends
%token int
%token short
%token try
%token char
%token final
%token interface
%token static
%token void
%token class
%token finally
%token long
%token strictfp
%token volatile
%token const
%token float
%token native
%token super
%token while
%token IDENTIFIER
%token IntegerLiteral
%token BooleanLiteral
%token CharacterLiteral
%token StringLiteral
%token NullLiteral
%token FloatingPointLiteral

%%

/* identifier */
QualifiedIdentifierListStar: ',' QualifiedIdentifier
                             |
                             QualifiedIdentifierListStar ',' QualifiedIdentifier
                             ;

Identifier: IDENTIFIER 
            ;

DotIdentifierStar: '.' Identifier
                   |
                   DotIdentifierStar '.' Identifier
                   ;
                    
QualifiedIdentifier: Identifier
                     |
                     Identifier DotIdentifierStar
                     ;

QualifiedIdentifierList: QualifiedIdentifier
                         |
                         QualifiedIdentifier QualifiedIdentifierListStar
                         ;

/* identifier */

/* compilation */

PackageOptional: AnnotationsOptional package QualifiedIdentifier ';'
                 |
                 package QualifiedIdentifier ';'
                 ;

ImportDeclarationStar: ImportDeclaration
                       |
                       ImportDeclarationStar ImportDeclaration
                       ;

TypeDeclarations: TypeDeclaration
                  |
                  TypeDeclarations TypeDeclaration
                  ;

DotStarOptional: '.' '*' 
                 ;

ModifierStar: Modifier
              |
              ModifierStar Modifier
              ;

TypeParametersOptional: TypeParameters
                        ;

ExtendsTypeOptional: extends Type
                     ;

ImplmentsTypeOptional: implements TypeList 
                       ;

ExtendsTypeListOptional: extends TypeList
                         ;

CompilationUnit: PackageOptional ImportDeclarationStar TypeDeclarations
                 |
                 PackageOptional ImportDeclarationStar
                 |
                 PackageOptional TypeDeclarations
                 |
                 PackageOptional
                 |
                 ImportDeclarationStar TypeDeclarations
                 |
                 ImportDeclarationStar
                 |
                 TypeDeclarations
                 |

                 ;

ImportDeclaration: import static Identifier DotIdentifierStar DotStarOptional ';'
                   |
                   import Identifier DotIdentifierStar DotStarOptional ';'
                   |
                   import Identifier DotIdentifierStar ';'
                   |
                   import static Identifier DotIdentifierStar ';'
                   |
                   import static Identifier DotStarOptional ';'
                   |
                   import Identifier DotStarOptional ';'
                   |
                   import Identifier ';'
                   |
                   import static Identifier ';'
                   ;

TypeDeclaration: ClassOrInterfaceDeclaration
                 ;

ClassOrInterfaceDeclaration: ModifierStar ClassDeclaration 
                             |
                             ModifierStar InterfaceDeclaraton
                             |
                             ClassDeclaration 
                             |
                             InterfaceDeclaraton  
                             ;

ClassDeclaration: NormalClassDeclaration
                  |
                  EnumDeclaration 
                  ;

InterfaceDeclaraton: NormalInterfaceDeclaration
                     |
                     AnnotationTypeDeclaration
                     ;

NormalClassDeclaration: class Identifier TypeParametersOptional ExtendsTypeOptional ImplmentsTypeOptional ClassBody
                        |
                        class Identifier TypeParametersOptional ExtendsTypeOptional ClassBody
                        |
                        class Identifier TypeParametersOptional ImplmentsTypeOptional ClassBody
                        |
                        class Identifier TypeParametersOptional ClassBody
                        |
                        class Identifier ExtendsTypeOptional ImplmentsTypeOptional ClassBody
                        |
                        class Identifier ExtendsTypeOptional ClassBody
                        |
                        class Identifier ImplmentsTypeOptional ClassBody
                        |
                        class Identifier ClassBody
                        ;

EnumDeclaration: enum Identifier ImplmentsTypeOptional EnumBody 
                 |
                 enum Identifier EnumBody
                 ;

NormalInterfaceDeclaration: interface Identifier TypeParametersOptional ExtendsTypeListOptional InterfaceBody
                            |
                            interface Identifier TypeParametersOptional InterfaceBody
                            |
                            interface Identifier ExtendsTypeListOptional InterfaceBody
                            |
                            interface Identifier InterfaceBody
                            ;

AnnotationTypeDeclaration: '@' interface Identifier AnnotationTypeBody
                            ;

/* compilation */

/* type */

TypeArgumentsOptional: TypeArguments 
                       ;

IdentifierTypeArgumentStar: '.' Identifier TypeArgumentsOptional
                            |
                            '.' Identifier
                            |
                            IdentifierTypeArgumentStar '.' Identifier TypeArgumentsOptional
                            |
                            IdentifierTypeArgumentStar '.' Identifier
                            ;

TypeArgumentListStar: ',' TypeArgument
                      |
                      TypeArgumentListStar ',' TypeArgument
                      ;

ExtendSuperOptional: extends ReferenceType
                     |
                     super ReferenceType
                     ;

Type: BasicType SquareBraceStar
      | 
      BasicType
      |
      ReferenceType SquareBraceStar
      |
      ReferenceType
      ;

BasicType: byte 
           |
           short
           |
           char 
           |
           int 
           |
           long
           |
           float 
           |
           double
           |
           boolean 
           ;

ReferenceType: Identifier TypeArgumentsOptional IdentifierTypeArgumentStar
               |
               Identifier TypeArgumentsOptional
               |
               Identifier IdentifierTypeArgumentStar
               |
               Identifier
               ;

TypeArguments: '<' TypeArgument TypeArgumentListStar '>'
               |
               '<' TypeArgument '>'
               ;

TypeArgument: ReferenceType
              |
              '?' ExtendSuperOptional
              ;

/* type */

/* NonWildcardTypeArguments */

ReferenceTypeListStar: ',' ReferenceType
                       |
                       ReferenceTypeListStar ',' ReferenceType
                       ;

TypeParametersListStar: ',' TypeParameter
                        |
                        TypeParametersListStar ',' TypeParameter

ExtendsBoundOptional: extends Bound
                      ;

AndReferenceTypeStar: '&' ReferenceType
                      |
                      AndReferenceTypeStar '&' ReferenceType
                      ;

NonWildcardTypeArguments: '<' TypeList '>'
                          ;

TypeList: ReferenceType ReferenceTypeListStar
          |
          ReferenceType
          ;                          

TypeArgumentsOrDiamond: "< >"
                        |
                        TypeArguments 
                        ;

NonWildcardTypeArgumentsOrDiamond: "< >"
                                   |
                                   NonWildcardTypeArguments
                                   ;

TypeParameters: '<' TypeParameter TypeParametersListStar '>'
                |
                '<' TypeParameter '>'
                ;

TypeParameter: Identifier ExtendsBoundOptional
               ;     

Bound: ReferenceType AndReferenceTypeStar
       |
       ReferenceType
       ;           

/* NonWildcardTypeArguments */

/* modifier */

AnnotationStar: Annotation
                |
                AnnotationStar Annotation
                ;

AnnotationElementOptional: '(' AnnotationElement2Optional ')'
                           ;

AnnotationElement2Optional: AnnotationElement
                            ;

ElementValuePairListStar: ',' ElementValuePair
                          |
                          ElementValuePairListStar ',' ElementValuePair
                          ;

ElementValuesOptional: ElementValues
                       ;

ElementValueListStar: ',' ElementValue
                      |
                      ElementValueListStar ',' ElementValue
                      ;

Modifier: Annotation
          |
          public
          |
          protected
          |
          private
          |
          static
          |
          abstract
          |
          final 
          |
          native
          |
          synchronized
          |
          transient
          |
          volatile
          |
          strictfp
          ;

Annotations: Annotation AnnotationStar
             |
             Annotation
             ;

Annotation: '@' QualifiedIdentifier AnnotationElementOptional
            |
            '@' QualifiedIdentifier
            ;

AnnotationElement: ElementValuePairs
                   |
                   ElementValue 
                   ;

ElementValuePairs: ElementValuePair ElementValuePairListStar
                   |
                   ElementValuePair
                   ;

ElementValuePair: Identifier '=' ElementValue
                  ;

ElementValue: Annotation
              |
              Expression1 
              |
              ElementValueArrayInitializer
              ;

ElementValueArrayInitializer: ElementValuesOptional CommaOptional
                              |
                              ElementValuesOptional
                              |
                              CommaOptional
                              |
                              ElementValueArrayInitializer ElementValuesOptional CommaOptional
                              ;

ElementValues: ElementValue ElementValueListStar
               |
               ElementValue
               ;                         

/* modifier */

/* ClassBody */

ModifierStar: ModifierStar Modifier
              ;

ThrowsQualifiedOptional: throws QualifiedIdentifierList 
                         ;

BlockOrSemicolon: Block
                  |
                  ';'
                  ;

TypeOrVoid: Type 
            |
            void 
            ;

ClassBody: '{' ClassBodyDeclarationStar '}'
           |
           '{' '}'
           ;

VariableDeclaratorListStar: 
                            |
                            VariableDeclaratorListStar ',' VariableDeclarator
                            ;

ClassBodyDeclaration: ';'
                     |
                     ModifierStar MemberDecl
                     |
                     MemberDecl
                     |
                     static Block
                     |
                     Block
                     ;

MemberDecl: MethodOrFieldDecl
            |
            void Identifier VoidMethodDeclaratorRest
            |
            Identifier ConstructorDeclaratorRest
            |
            GenericMethodOrConstructorDecl
            |
            ClassDeclaration
            |
            InterfaceDeclaraton
            ;

MethodOrFieldDecl: Type Identifier MethodOrFieldRest
                   ; 

MethodOrFieldRest: FieldDeclaratorsRest ';'
                   |
                   MethodDeclaratorRest 
                   ;

FieldDeclaratorsRest: VariableDeclaratorRest VariableDeclaratorListStar
                      |
                      VariableDeclaratorRest
                      ;

MethodDeclaratorRest: FormalParameters SquareBraceStar ThrowsQualifiedOptional BlockOrSemicolon
                      |
                      FormalParameters SquareBraceStar BlockOrSemicolon
                      |
                      FormalParameters ThrowsQualifiedOptional BlockOrSemicolon
                      |
                      FormalParameters BlockOrSemicolon
                      ;

VoidMethodDeclaratorRest: FormalParameters ThrowsQualifiedOptional BlockOrSemicolon 
                          |
                          FormalParameters BlockOrSemicolon 
                          ;

ConstructorDeclaratorRest: FormalParameters ThrowsQualifiedOptional Block 
                           |
                           FormalParameters Block 
                           ;

GenericMethodOrConstructorDecl: TypeParameters GenericMethodOrConstructorRest
                                ;

GenericMethodOrConstructorRest: TypeOrVoid Identifier MethodDeclaratorRest
                                |
                                Identifier ConstructorDeclaratorRest
                                ;                                                         

/* ClassBody */

/* InterfaceBody */

InterfaceBodyDeclarationStar: InterfaceBodyDeclaraton 
                              |
                              InterfaceBodyDeclarationStar InterfaceBodyDeclaraton
                              ;

InterfaceBody: '{' InterfaceBodyDeclarationStar '}'
                |
                '{' '}' 
                ;

ConstantDeclaratorListStar: ConstantDeclaratorListStar ',' ConstantDeclarator 
                            | 
                            ',' ConstantDeclarator
                            ;
                
InterfaceBodyDeclaraton: ';'
                         |
                         InterfaceMemberDecl
                         |
                         ModifierStar InterfaceMemberDecl
                         ;

InterfaceMemberDecl: InterfaceMethodOrFieldDecl
                     |
                     void Identifier VoidInterfaceMethodDeclaratorRest 
                     |
                     InterfaceGenericMethodDecl
                     |
                     ClassDeclaration
                     |
                     InterfaceDeclaraton
                     ;

InterfaceMethodOrFieldDecl: Type Identifier InterfaceMethodOrFieldRest
                            ;

InterfaceMethodOrFieldRest: ConstantDeclaratorsRest ';'
                            |
                            InterfaceMethodDeclaratorRest
                            ;

ConstantDeclaratorsRest: ConstantDeclaratorRest ConstantDeclaratorListStar  
                          |
                          ConstantDeclaratorRest
                         ;

ConstantDeclaratorRest: SquareBraceStar '=' VariableInitializer
                        |
                        '=' VariableInitializer
                        ;

ConstantDeclarator: Identifier ConstantDeclaratorRest
                    ;

InterfaceMethodDeclaratorRest: FormalParameters SquareBraceStar ThrowsQualifiedOptional ';'
                                |
                                FormalParameters ThrowsQualifiedOptional ';'
                                |
                                FormalParameters SquareBraceStar  ';'
                                
                                |
                                FormalParameters
                                |

                                ;

VoidInterfaceMethodDeclaratorRest: FormalParameters ThrowsQualifiedOptional ';'
                                   ;

InterfaceGenericMethodDecl: TypeParameters TypeOrVoid Identifier InterfaceMethodDeclaratorRest
                            ;                                                                  

/* InterfaceBody */

/* Formal Parameters*/

FormalParameterDeclsOptional: 
                              |
                              FormalParameterDecls
                              ;

VariableModifierStar: 
                      |
                      VariableModifierStar VariableModifier
                      ;

FormalParameterDeclsListOptional: 
                                  |
                                  ',' FormalParameterDecls
                                  ;

EqualVariableInitializerOptional: 
                                  |
                                  '=' VariableInitializer
                                  ;

FormalParameters: '(' FormalParameterDeclsOptional ')'
                  |
                  '(' ')'
                  ;

FormalParameterDecls: VariableModifierStar Type FormalParameterDeclsRest
                      |
                      Type FormalParameterDeclsRest
                      ;
                    
VariableModifier: final 
                  |
                  Annotation
                  ;

FormalParameterDeclsRest: VariableDeclaratorId FormalParameterDeclsListOptional
                          |
                          VariableDeclaratorId
                          |
                          '.''.''.' VariableDeclaratorId
                          ; 

VariableDeclaratorId: Identifier SquareBraceStar
                      |
                      Identifier
                      ;

VariableDeclarators: VariableDeclarator VariableDeclaratorListStar
                     |
                     VariableDeclarator
                     ;       

VariableDeclarator: Identifier VariableDeclaratorRest
                    ;

VariableDeclaratorRest: SquareBraceStar EqualVariableInitializerOptional
                        |
                        SquareBraceStar
                        |
                        EqualVariableInitializerOptional
                        |

                        ;                                                                                                   

VariableInitializer: ArrayInitializer 
                     |
                     Expression 
                     ;

VariableInitializerListStar: ',' VariableInitializer
                             |
                             VariableInitializerListStar ',' VariableInitializer
                             ;
VariableInitializerUtil : 
                          |
                          VariableInitializer  VariableInitializerListStar  CommaOptional 
                          |
                          VariableInitializer  VariableInitializerListStar
                          |
                          VariableInitializer CommaOptional
                          |
                          VariableInitializer
                          ;

ArrayInitializerUtil: VariableInitializerUtil;
                      |
                      ArrayInitializerUtil VariableInitializerUtil; 
                      ;

ArrayInitializer:  
                  |
                  ArrayInitializerUtil 
                  ;             

/* Formal Parameters*/

/* Block */

IdentifierColonOptional: Identifier ':'
                         ;

ElseStatementOptional: else Statement
                       ;

ColonExpressionOptional: ':' Expression
                         ;

SwitchBlockStatementGroupsStar: SwitchBlockStatementGroups
                                |
                                SwitchBlockStatementGroupsStar SwitchBlockStatementGroups
                                ;

IdentifierOptional: Identifier
                    ;

ExpressionOptional: Expression
                    ;

CatchesOptional:  Catches
                  ;

FinallyOptional:  Finally
                  ;

Block: 
       |
       Block BlockStatements
       ;

BlockStatements: 
                 |
                 BlockStatements BlockStatement
                 ;

 BlockStatement: LocalVariableDeclarationStatement
                 |
                 ClassOrInterfaceDeclaration
                 |
                 IdentifierColonOptional Statement
                 |
                 Statement 
                 ;    

LocalVariableDeclarationStatement: VariableModifierStar Type VariableDeclarators ';'
                                   |
                                   Type VariableDeclarators ';'
                                   ;

Statement: Block
           |
           ';'
           |
           Identifier ':' Statement
           |
           StatementExpression ';'
           |
           if ParExpression Statement ElseStatementOptional
           |
           if ParExpression Statement
           |
           assert Expression ColonExpressionOptional ';'
           |
           assert Expression ';'
           |
           switch ParExpression SwitchBlockStatementGroupsStar
           |
           switch ParExpression
           |
           while ParExpression Statement
           |
           do Statement while ParExpression ';'
           |
           for '(' ForControl ')' Statement
           |
           break IdentifierOptional ';'
           |
           break';'
           |
           continue IdentifierOptional ';'
           |
           continue ';'
           |
           return ExpressionOptional ';'
           |
           return ';'
           |
           throw Expression ';'
           |
           synchronized ParExpression Block 
           |
           try Block Catches
           |
           try Block CatchesOptional Finally
           |
           try Block Finally
           |
           try ResourceSpecification Block CatchesOptional FinallyOptional
           |
           try ResourceSpecification Block CatchesOptional
           |
           try ResourceSpecification Block FinallyOptional
           |
           try ResourceSpecification Block
           ;

StatementExpression: Expression
                     ;

/*  Block  */

/* Catches */

OrQualifiedIdentifierStar: '|' QualifiedIdentifier
                           |
                           OrQualifiedIdentifierStar '|' QualifiedIdentifier
                           ;


CatchClauseStar: CatchClause
                 |
                 CatchClauseStar CatchClause
                 ;

SemiResourceStar: ';' Resource
                  |
                  SemiResourceStar ';' Resource
                  ;

Catches: CatchClause CatchClauseStar
         |
         CatchClause
         ;

CatchClause: catch '(' VariableModifierStar CatchType Identifier ')' Block 
             |
             catch '(' CatchType Identifier ')' Block 
             ;

CatchType: QualifiedIdentifier OrQualifiedIdentifierStar
           |
           QualifiedIdentifier
           ;

Finally: finally Block
         ;

ResourceSpecification: '(' Resources ';' ')'
                       |
                       '(' Resources ')'
                       ;

Resources: Resource SemiResourceStar
           |
           Resource
           ;                 

Resource: VariableModifierStar ReferenceType VariableDeclaratorId '=' Expression
          |
          ReferenceType VariableDeclaratorId '=' Expression
          ;

/* Catches */

/* SwitchBlockStatementGroupsStar */

CommaStatementStar: 
                    |
                    CommaStatementStar ',' StatementExpression
                    ;

ForUpdateOptional: 
                   |
                   ForUpdate
                   ;

SwitchBlockStatementGroups: 
                            |
                            SwitchBlockStatementGroups SwitchBlockStatementGroup
                            ;

SwitchBlockStatementGroup: SwitchLabels BlockStatements
                           ;

SwitchLabels: SwitchLabel 
              |
              SwitchLabel SwitchLabels  
              ;

SwitchLabel: case Expression ':'
             |
             case EnumConstantName ':'
             |
             default ':'
             ;

EnumConstantName: Identifier
                  ;

ForControl: ForVarControl
            |
            ForInit ';' ExpressionOptional ';' ForUpdateOptional
            ;

ForVarControl: VariableModifierStar Type VariableDeclaratorId ForVarCOntrolRest
               ;

ForVarCOntrolRest: ForVariableDeclaratorsRest ';' ExpressionOptional ';' ForUpdateOptional
                   |
                   ':' Expression
                   ;

ForVariableDeclaratorsRest: EqualVariableInitializerOptional VariableDeclaratorListStar
                            ;

ForInit: //Doubt

ForUpdate: StatementExpression CommaStatementStar
           ;

/* SwitchBlockStatementGroupsStar */

/* Creator */

TypeArgumentsOrDiamondOptional:
                                |
                                TypeArgumentsOrDiamond
                                ;

DotIdentifierTypeArgumentsOrDiamondOptionalStar: 
                                                 |
                                                 DotIdentifierTypeArgumentsOrDiamondOptionalStar '.' Identifier TypeArgumentsOrDiamondOptional
                                                 ;

Creator: NonWildcardTypeArguments CreatedName ClassCreatorRest
         |
         CreatedName ClassCreatorRest
         ;

CreatedName: Identifier TypeArgumentsOrDiamondOptional DotIdentifierTypeArgumentsOrDiamondOptionalStar
             ;

ClassCreatorRest: Arguments ClassBodyOptional
                  ;

ExplicitGenericInvocation: NonWildcardTypeArguments ExplicitGenericInvocationSuffix
                           ;

NonWildcardTypeArgumentsOptional: 
                                  |
                                  NonWildcardTypeArguments
                                  ;
NonWildcardTypeArgumentsOrDiamondOptional: 
                                           |
                                           NonWildcardTypeArgumentsOrDiamond
                                           ;

InnerCreator: Identifier NonWildcardTypeArgumentsOrDiamondOptional ClassCreatorRest
              ;

Selector: '.' Identifier ArgumentsOptional
          |
          '.' ExplicitGenericInvocation
          |
          '.' this
          |
          '.' super SuperSuffix
          |
          '.' new NonWildcardTypeArgumentsOptional InnerCreator
          |
          ExpressionOptional
          ;
          
/* creator */

/* expressions */
AssignmentOptional: AssignmentOperator Expression1
                    ;

Expression1Rest:  '?' Expression : Expression1
                  ;

InfixOpOne: Infixop Expression3
            ;

InfixOpStar: InfixOpOne
             |
             InfixOpStar InfixOpOne
             ;

Expression2Rest:
                 |
                 InfixOpStar
                 |
                 instanceof Type
                 ;

Expression: Expression1 AssignmentOptional
            |
            Expression1
            ;

AssignmentOperator: '='
                    |
                    "+="
                    |
                    "-="
                    |
                    "*="
                    |
                    "/="
                    |
                    "&="
                    |
                    "|="
                    |
                    "^="
                    |
                    "%="
                    |
                    "<<="
                    |
                    ">>="
                    |
                    ">>>="
                    ;

Expression1: Expression2 Expression1Rest
             |
             Expression2
             ;

Expression2: Expression3 Expression2Rest
             |
             Expression3
             ;

/* expressions */

/*  operators */

Selectors: Selector
           |
           Selectors Selector
           ;

PostfixOps: PostfixOp
            |
            PostfixOps PostfixOp
            ;

Infixop:  "||"
          |
          "&&"
          |
          '|'
          |
          '^'
          |
          '&'
          |
          '^'
          |
          "=="
          |
          "!="
          |
          '<'
          |
          '>'
          |
          "<="
          |
          ">="
          |
          "<<"
          |
          ">>"
          |
          ">>>"
          |
          '+'
          |
          '-'
          |
          '*'
          |
          '/'
          |
          '%'
          ;

Expression3:   PrefixOp Expression3
               |
               Expression Expression3
               |
               Type Expression3
               |
               Primary Selectors PostfixOps
               |
               Primary Selectors
               |
               Primary PostfixOps
               |
               Primary
               ;

PrefixOp: "++"
          |
          "--"
          |
          '!'
          |
          '~'
          |
          '+'
          |
          '-'
          ;

PostfixOp: "++"
           |
           "--"
           ;

/* operators */

/* primary */

ArgumentsOptional: Arguments
                   ;

IdentifierSuffixOptional: IdentifierSuffix
                          ;

IdentifierSuffix: Arguments
                  ;

SquareBraceStar: "[]"
                 |
                 SquareBraceStar "[]"
                 ;

ExpressionListStar: ',' Expression
                    |
                    ExpressionListStar ',' Expression
                    ;

ArgumentsExpressionOptional: Expression ExpressionListStar
                             ;

Primary: Literal
         |
         ParExpression
         |
         this ArgumentsOptional
         |
         super SuperSuffix
         |
         new Creator
         |
         NonWildcardTypeArguments ExplicitGenericInvocationSuffix
         |
         NonWildcardTypeArguments this Arguments 
         |
         QualifiedIdentifier IdentifierSuffixOptional
         |
         QualifiedIdentifier
         |
         BasicType SquareBraceStar '.' class
         |
         BasicType '.' class
         |
         void '.' class 
         ;

Literal: IntegerLiteral
         |
         FloatingPointLiteral
         |
         CharacterLiteral
         |
         StringLiteral
         |
         BooleanLiteral
         |
         NullLiteral
         ;

ParExpression: '(' Expression ')'
                ;
        
Arguments: '(' ArgumentsExpressionOptional ')'
           |
           '(' ')'
           ;

SuperSuffix: Arguments
             |
             '.' Identifier ArgumentsOptional
             |
             '.' Identifier
             ;

ExplicitGenericInvocationSuffix: super SuperSuffix
                                 |
                                 Identifier Arguments
                                 ;

/* primary */

/* enumbody */

AnnotationTypeElementDeclarationsOptionalStar: AnnotationTypeElementDeclarationsOptional
                                               |
                                               AnnotationTypeElementDeclarationsOptionalStar AnnotationTypeElementDeclarationsOptional
                                               ;

AnnotationTypeElementDeclarationsOptional: AnnotationTypeElementDeclarations
                                           ;

AnnotationTypeElementDeclarations: AnnotationTypeElementDeclaration
                                   |
                                   AnnotationTypeElementDeclarations AnnotationTypeElementDeclaration
                                   ;

AnnotationTypeElementDeclaration: ModifierStar AnnotationTypeElementRest
                                  |
                                  AnnotationTypeElementRest
                                  ;

AnnotationTypeElementRest: Type Identifier AnnotationMethodOrConstantRest ";"
                           |
                           ClassDeclaration
                           |
                           InterfaceDeclaraton
                           |
                           EnumDeclaration
                           |
                           AnnotationTypeDeclaration
                           ;

AnnotationMethodOrConstantRest: AnnotationMethodRest 
                                |
                                ConstantDeclaratorsRest
                                ;

AnnotationMethodRest: '(' ')' "[[]]" default ElementValue
                      |
                      '(' ')' "[[]]"
                      ; 

EnumConstantsOptional: EnumConstants
                       ;

CommaOptional: ','
               ;

EnumBodyDeclarationsOptional: EnumBodyDeclarations
                              ;

AnnotationsOptional: Annotations
                     ;

ClassBodyOptional: ClassBody
                   ;

ClassBodyDeclarationStar: ClassBodyDeclarationStar ClassBodyDeclaration
                          ;

EnumBody: 
          |
          EnumBody EnumConstantsOptional CommaOptional EnumBodyDeclarationsOptional
          ; 

EnumConstants: EnumConstant
               |
               EnumConstants ',' EnumConstant
               ;

EnumConstant: AnnotationsOptional Identifier ArgumentsOptional ClassBodyOptional
              |
              AnnotationsOptional Identifier ArgumentsOptional
              |
              AnnotationsOptional Identifier ClassBodyOptional
              |
              AnnotationsOptional Identifier
              |
              Identifier ArgumentsOptional ClassBodyOptional
              |
              Identifier ArgumentsOptional
              |
              Identifier ClassBodyOptional
              |
              Identifier
              ;

EnumBodyDeclarations: ';' ClassBodyDeclarationStar
                      |
                      ';'
                      ;

AnnotationTypeBody: 
                    |
                    AnnotationTypeElementDeclarationsOptionalStar
                    ;



/* enumbody */

%%
main()
{
 return(yyparse());
}
yyerror(s)
char *s;
{
  fprintf(stderr, "%s\n",s);
}
yywrap()
{
  return(1);
}
