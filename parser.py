import ply.lex as lex
import ply.yacc as yacc
import lexer
import sys
tokens = lexer.tokens

/* identifier */
def QualifiedIdentifierListStar(p): 
                             '''QualifiedIdentifierListStar: 
							 |
                             QualifiedIdentifierListStar ',' QualifiedIdentifier
                             '''

Identifier: IDENTIFIER 
            ;

DotIdentifierStar: 
                    |
                    DotIdentifierStar '.' Identifier
                    ;
                    
QualifiedIdentifier: Identifier DotIdentifierStar
                     ;

QualifiedIdentifierList: QualifiedIdentifier QualifiedIdentifierListStar
                         ;

/* identifier */

/* compilation */

PackageOptional: 
                |
                 AnnotationsOptional package QualifiedIdentifier ';'
                ;

ImportDeclarationStar: 
                        |
                        ImportDeclaration
                        ;

TypeDeclarations: 
                 |
                 TypeDeclarations TypeDeclaration
                 ;

DotIdentifierStar: 
                   |
                   DotIdentifierStar '.' Identifier
                   ;

DotStarOptional: 
                 | 
                 '.' '*' 
                 ;

ModifierStar: 
              |
              ModifierStar Modifier
              ;

TypeParametersOptional:
                        |
                        TypeParameters
                        ;

ExtendsTypeOptional: 
                     |
                     extends Type
                     ;

ImplmentsTypeOptional: 
                       |
                       implements TypeList 
                       ;

ExtendsTypeListOptional:
                         |
                         extends TypeList
                         ;

CompilationUnit: PackageOptional ImportDeclarationStar TypeDeclarations
                 |
                 ImportDeclarationStar TypeDeclarations
                 ;

ImportDeclaration: import static Identifier DotIdentifierStar DotStarOptional ';'
                   ;

TypeDeclaration: ClassOrInterfaceDeclaration
                ;

ClassOrInterfaceDeclaration: ModifierStar ClassDeclaration 
                             |
                             ModifierStar InterfaceDeclaraton 
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
                        ;

EnumDeclaration: enum Identifier ImplmentsTypeOptional EnumBody 
                 ;

NormalInterfaceDeclaration: interface Identifier TypeParametersOptional ExtendsTypeListOptional InterfaceBody
                            ;

AnnotationTypeDeclaration: '@' interface Identifier AnnotationTypeBody
                            ;

/* compilation */

/* type */

TypeArgumentsOptional: 
                       |
                       TypeArguments 
                       ;

IdentifierTypeArgumentStar: 
                            |
                            IdentifierTypeArgumentStar '.' Identifier TypeArgumentsOptional
                            ;

TypeArgumentListStar: 
                      |
                      TypeArgumentListStar ',' TypeArgument
                      ;

ExtendSuperOptional: extends ReferenceType
                     |
                     super ReferenceType
                     ;

Type: BasicType SquareBraceStar
      | 
      ReferenceType SquareBraceStar
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
               ;

TypeArguments: '<' TypeArgument TypeArgumentListStar '>'
               ;

TypeArgument: ReferenceType
              |
              '?' ExtendSuperOptional
              ;

/* type */

/* NonWildcardTypeArguments */

ReferenceTypeListStar: 
                       |
                       ReferenceTypeListStar ',' ReferenceType
                       ;

TypeParametersListStar: 
                        |
                        TypeParametersListStar ',' TypeParameter

ExtendsBoundOptional: 
                      |
                      extends Bound
                      ;

AndReferenceTypeStar: 
                      |
                      AndReferenceTypeStar '&' ReferenceType
                      ;

NonWildcardTypeArguments: '<' TypeList '>'
                          ;

TypeList: ReferenceType ReferenceTypeListStar
          ;                          

TypeArgumentsOrDiamond: '<''>'
                        |
                        TypeArguments 
                        ;

NonWildcardTypeArgumentsOrDiamond: '<''>'
                                   |
                                   NonWildcardTypeArguments
                                   ;

TypeParameters: '<' TypeParameter TypeParametersListStar '>'
                ;

TypeParameter: Identifier ExtendsBoundOptional
               ;     

Bound: ReferenceType AndReferenceTypeStar
       ;           

/* NonWildcardTypeArguments */

/* modifier */

AnnotationStar: 
                |
                AnnotationStar Annotation
                ;

AnnotationElementOptional: 
                           |
                           '(' AnnotationElement2Optional ')'
                           ;

AnnotationElement2Optional: 
                            |
                            AnnotationElement
                            ;

ElementValuePairListStar: 
                          |
                          ElementValuePairListStar ',' ElementValuePair
                          ;

ElementValuesOptional: 
                       |
                       ElementValues
                       ;

ElementValueListStar: 
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
             ;

Annotation: '@' QualifiedIdentifier AnnotationElementOptional
            ;

AnnotationElement: ElementValuePairs
                   |
                   ElementValue 
                   ;

ElementValuePairs: ElementValuePair ElementValuePairListStar
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
                              ;

ElementValues: ElementValue ElementValueListStar 
               ;                         

/* modifier */

/* ClassBody */

ModifierStar: 
              |
              ModifierStar Modifier
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
           ;

VariableDeclaratorListStar: 
                            |
                            VariableDeclaratorListStar ',' VariableDeclarator
                            ;

ClassBodyDeclaration: ';'
                     |
                     ModifierStar MemberDecl
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

MethodOrFieldDecl: Type Identifier MethodOrFieldDecl
                   ; 

MethodOrFieldRest: FieldDeclaratorsRest ';'
                   |
                   MethodDeclaratorRest 
                   ;

FieldDeclaratorsRest: VariableDeclaratorRest VariableDeclaratorListStar
                      ;

MethodDeclaratorRest: FormalParameters SquareBraceStar ThrowsQualifiedOptional BlockOrSemicolon
                      ;

VoidMethodDeclaratorRest: FormalParameters ThrowsQualifiedOptional BlockOrSemicolon 
                          ;

ConstructorDeclaratorRest: FormalParameters ThrowsQualifiedOptional Block 
                           ;

GenericMethodOrConstructorDecl: TypeParameters GenericMethodOrConstructorRest
                                ;

GenericMethodOrConstructorRest: TypeOrVoid Identifier MethodDeclaratorRest
                                |
                                Identifier ConstructorDeclaratorRest
                                ;                                                         

/* ClassBody */

/* InterfaceBody */

InterfaceBodyDeclarationStar: 
                              |
                              InterfaceBodyDeclarationStar InterfaceBodyDeclaraton
                              ;

InterfaceBody: '{' InterfaceBodyDeclarationStar '}'
               ;

ConstantDeclaratorListStar: 
                             |
                             ConstantDeclaratorListStar ',' ConstantDeclarator
                             ;

InterfaceBodyDeclaraton: ';'
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
                         ;

ConstantDeclaratorRest: SquareBraceStar '=' VariableInitializer
                        ;

ConstantDeclarator: Identifier ConstantDeclaratorRest
                    ;

InterfaceMethodDeclaratorRest: FormalParameters SquareBraceStar ThrowsQualifiedOptional ';'
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
                  ;

FormalParameterDecls: VariableModifierStar Type FormalParameterDeclsRest
                      ;
                    
VariableModifier: final 
                  |
                  Annotation
                  ;

FormalParameterDeclsRest: VariableDeclaratorId FormalParameterDeclsListOptional
                          |
                          '.''.''.' VariableDeclaratorId
                          ; 

VariableDeclaratorId: Identifier SquareBraceStar
                      ;

VariableDeclarators: VariableDeclarator VariableDeclaratorListStar
                     ;       

VariableDeclarator: Identifier VariableDeclaratorRest
                    ;

VariableDeclaratorRest: SquareBraceStar EqualVariableInitializerOptional
                        ;                                                                                                   

VariableInitializer: ArrayInitializer 
                     |
                     Expression 
                     ;

ArrayInitializer:  //TODO                    

/* Formal Parameters*/

/* Block */

IdentifierColonOptional: 
                         |
                         Identifier ':'
                         ;

ElseStatementOptional: 
                        |
                        else Statement
                        ;

ColonExpressionOptional: 
                         |
                         ':' Expression
                         ;

SwitchBlockStatementGroupsStar: 
                                |
                                SwitchBlockStatementGroupsStar SwitchBlockStatementGroups
                                ;

IdentifierOptional: 
                    |
                    Identifier
                    ;

ExpressionOptional: 
                    |
                    Expression
                    ;

CatchesOptional: 
                    |
                    Catches
                    ;

FinallyOptional: 
                    |
                    Finally
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
                 ;    

LocalVariableDeclarationStatement: VariableModifierStar Type VariableDeclarators ';'
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
           assert Expression ColonExpressionOptional ';'
           |
           switch ParExpression SwitchBlockStatementGroupsStar
           |
           while ParExpression Statement
           |
           do Statement while ParExpression ';'
           |
           for '(' ForControl ')' Statement
           |
           break IdentifierOptional ';'
           |
           continue IdentifierOptional ';'
           |
           return ExpressionOptional ';'
           |
           throw Expression ';'
           |
           synchronized ParExpression Block 
           |
           try Block Catches
           |
           try Block CatchesOptional Finally
           |
           try ResourceSpecification Block CatchesOptional FinallyOptional
           ;

StatementExpression: Expression
                     ;

/*  Block  */

/* Catches */

OrQualifiedIdentifierStar: 
                           |
                           OrQualifiedIdentifierStar '|' QualifiedIdentifier
                           ;


CatchClauseStar: 
                 |
                 CatchClauseStar CatchClause
                 ;

SemiResourceStar: 
                  |
                  ';' Resource
                  ;

Catches: CatchClause CatchClauseStar
         ;

CatchClause: catch '(' VariableModifierStar CatchType Identifier ')' Block 
             ;

CatchType: QualifiedIdentifier OrQualifiedIdentifierStar
           ;

Finally: finally Block
         ;

ResourceSpecification: '(' Resources ';' ')'
                       |
                       '(' Resources ')'
                       ;

Resources: Resource SemiResourceStar
           ;                 

Resource: VariableModifierStar ReferenceType VariableDeclaratorId '=' Expression
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
AssignmentOptional: 
                    |
                    AssignmentOperator Expression1
                    ;

Expression1Rest: 
                  |
                  '?' Expression : Expression1
                  ;

InfixOpOne: Infixop Expression3
            ;

InfixOpStar: 
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
             ;

Expression2: Expression3 Expression2Rest
             ;

/* expressions */

/*  operators */

Selectors: Selectors Selector
           ;

PostfixOps: PostfixOps PostfixOp
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

ArgumentsOptional: 
                   |
                   Arguments
                   ;

IdentifierSuffixOptional: 
                          |
                          IdentifierSuffix
                          ;

IdentifierSuffix: Arguments
                  ;

SquareBraceStar: 
                 |
                 SquareBraceStar 
                 |
                 "[]"
                 ;

ExpressionListStar: 
                    |
                    ExpressionListStar ',' Expression
                    ;

ArgumentsExpressionOptional: 
                             |
                             Expression ExpressionListStar
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
         BasicType SquareBraceStar '.' class
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
            ;

SuperSuffix: Arguments
             |
             '.' Identifier ArgumentsOptional
             ;

ExplicitGenericInvocationSuffix: super SuperSuffix
                                 |
                                 Identifier Arguments
                                 ;

/* primary */

/* enumbody */

AnnotationTypeElementDeclarationsOptionalStar: 
                                               |
                                               AnnotationTypeElementDeclarationsOptionalStar AnnotationTypeElementDeclarationsOptional
                                               ;

AnnotationTypeElementDeclarationsOptional: 
                                           |
                                           AnnotationTypeElementDeclarations
                                           ;

AnnotationTypeElementDeclarations: AnnotationTypeElementDeclaration
                                   |
                                   AnnotationTypeElementDeclarations AnnotationTypeElementDeclaration
                                   ;

AnnotationTypeElementDeclaration: ModifierStar AnnotationTypeElementRest
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

EnumConstantsOptional: 
                       |
                       EnumConstants
                       ;

CommaOptional: 
               |
               ','
               ;

EnumBodyDeclarationsOptional: 
                              |
                              EnumBodyDeclarations
                              ;

AnnotationsOptional: 
                     |
                     Annotations
                     ;

ClassBodyOptional: 
                   |
                   ClassBody
                   ;

ClassBodyDeclarationStar: 
                         |
                         ClassBodyDeclarationStar ClassBodyDeclaration
                         ;

EnumBody: EnumBody EnumConstantsOptional CommaOptional EnumBodyDeclarationsOptional
          ; 

EnumConstants: EnumConstant
               |
               EnumConstants ',' EnumConstant
               ;

EnumConstant: AnnotationsOptional Identifier ArgumentsOptional ClassBodyOptional
              ;

EnumBodyDeclarations: ';' ClassBodyDeclarationStar
                      ;

AnnotationTypeBody: 
                    |
                    AnnotationTypeElementDeclarationsOptionalStar
                    ;



/* enumbody */


 # Build the parser
parser = yacc.yacc()

while True:
  try:
    s = raw_input('dfga dfasdf ')
  except EOFError:
    break
  if not s: continue
  result = parser.parse(s)
  print(result)
