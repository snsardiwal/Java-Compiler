import ply.lex as lex
import ply.yacc as yacc
import lexer 
import sys

tokens = lexer.tokens
print("=================================================")
print(tokens)
# tokens = ( 
# 		'err',
# 		'Comment',
# 		'Keyword',
# 		'Seperator',
# 		'Operator',
# 		'Literal',
# 		'Identifier'
# 	)

#parser

start = 'CompilationUnit'

def p_COMPILATIONUNIT(p):
	'''CompilationUnit : PackageDeclaration ImportDeclarations TypeDeclarations
					  | PackageDeclaration ImportDeclarations 
					  | PackageDeclaration TypeDeclarations
					  | ImportDeclarations TypeDeclarations
					  | PackageDeclaration 
					  | ImportDeclarations 
					  | TypeDeclarations 
					  |
	'''
def p_PACKAGEDECLARATION(p):
	'''PackageDeclaration : package Name ';'
	'''
def p_IMPORTDECLARATIONS(p):
	'''ImportDeclarations : ImportDeclaration
						  | ImportDeclaration ImportDeclaration
	'''
def p_TYPEDECLARATIONS(p):
	'''TypeDeclarations : TypeDeclaration
						 | ImportDeclarations ImportDeclaration
	'''
def p_IMPORTDECLARATION(p):
	'''ImportDeclaration : SingleTypeImportDeclaration
						 | TypeImportOnDemandDeclaration
	'''
def p_SINGLETYPEIMPORTDECLARATION(p):
	'''SingleTypeImportDeclaration : import Name ';'
	'''
def p_TYPEIMPORTONDEMANDDECLARATION(p):
	'''TypeImportOnDemandDeclaration : import Name '.' '*' ';'
	'''
def p_TYPEDECLARATION(p):
	'''TypeDeclaration : ClassDeclaration
	'''

## Arraays 
def p_ARRAYINITIALIZER(p):
	'''ArrayInitializer : ArrayInitializer VariableInitializerList ','
						| ArrayInitializer VariableInitializerList
						| ArrayInitializer ','
						|
	'''
def p_VARIABLEINITIALIZERS(p):
	'''VariableInitializerList : VariableInitializer
							  | VariableInitializer CommaVariableInitializers

	'''

def p_CommaVariableInitializers(p):
	''' CommaVariableInitializers : ',' VariableInitializer
								| CommaVariableInitializers ',' VariableInitializer
	'''
## Expressions 
def p_PRIMARY(p):
	'''Primary : PrimaryNoNewArray
			  | ArrayCreationExpression
	'''
def p_PRIMARYNONEWARRAY(p):
	'''PrimaryNoNewArray : Literal
						| ClassLiteral
						| this
						| Name '.' this
						| '(' Expression ')'
						| ClassInstanceCreationExpression
						| FieldAccess
						| ArrayAccess
						| MethodInvocation
						| MethodReference
	'''
def p_CLASSLITERAL(p):
	'''ClassLiteral :  Name SquareStar '.' class
					|  NumericType SquareStar '.' class
					|  boolean SquareStar '.' class
					|	Name  '.' class
					|  NumericType  '.' class
					|  boolean  '.' class
					|  void '.' class 
	'''

def p_SQUARESTAR(p):
	'''SquareStar : '[' ']'
				 | SquareStar  '[' ']'
	'''
def p_CLASSINSTANCECREATIONEXPRESSION(p):
	'''ClassInstanceCreationExpression : UnqualifiedClassInstanceCreationExpression
	   								  | Name '.' UnqualifiedClassInstanceCreationExpression
									  | Primary '.' UnqualifiedClassInstanceCreationExpression
	'''
def p_UNQUALIFIEDCLASSINSTANCECREATIONEXPRESSION(p):
	'''UnqualifiedClassInstanceCreationExpression : new TypeArguments ClassOrInterfaceTypeToInstantiate '(' ArgumentList ')' ClassBody
												| new  ClassOrInterfaceTypeToInstantiate '(' ArgumentList ')' ClassBody
												| new TypeArguments ClassOrInterfaceTypeToInstantiate '(' ')' ClassBody
	''' 
def p_CLASSORINTERFACETYPETOINSTANTIATE(p):
	'''ClassOrInterfaceTypeToInstantiate : Annotations Identifier  AnnoIdenStar TypeArgumentsOrDiamond
										|  Identifier  AnnoIdenStar TypeArgumentsOrDiamond
									    | Annotations Identifier   TypeArgumentsOrDiamond
										| Annotations Identifier  AnnoIdenStar 
										|  Identifier  AnnoIdenStar 
									    | Annotations Identifier   
										| Identifier   TypeArgumentsOrDiamond
										| Identifier
	'''

def p_AnnoIdenStar(p):
	'''AnnoIdenStar : '.' Annotations Identifier
					| '.' Identifier
					| AnnoIdenStar '.' Identifier
					| AnnoIdenStar '.' Annotations Identifier
	'''
def p_TYPEARGUMENTSORDIAMOND(p):
	'''TypeArgumentsOrDiamond : TypeArguments
							 | '<' '>'
	'''
def p_FIELDACCESS(p):
	'''FieldAccess : Primary '.' Identifier
				   | super '.' Identifier
				   | Name '.' super '.' Identifier 
	'''
def p_ARRAYACCESS(p):
	''' ArrayAccess : Name '[' Expression ']'
					| PrimaryNoNewArray '[' Expression ']'
	'''
def p_METHODINVOCATION(p):
	''' MethodInvocation : Name '('  ArgumentList ')' 
						| Name '('   ')'
						| Name  '.' TypeArguments Identifier '(' ArgumentList ')'
						| Name  '.'  Identifier '(' ArgumentList ')'
						| Name  '.'  Identifier '('  ')'
						| Primary '.' TypeArguments Identifier '(' ArgumentList ')'
						| Primary '.'  Identifier '(' ArgumentList ')'
						| Primary '.' Identifier '(' ')'
						| super '.' TypeArguments Identifier '(' ArgumentList ')'
						| super '.'  Identifier '(' ArgumentList ')'
						| super '.' Identifier '(' ')'
						| Name '.' super '.' TypeArguments Identifier '(' ArgumentList ')'
						| Name '.' super '.'  Identifier '(' ArgumentList ')'
						| Name '.' super '.' Identifier '(' ')'
						
	'''

def p_ArgumentList(p):
	''' ArgumentList :  Expression
					 | ArgumentList ',' Expression 
	'''
def p_METHODREFERENCE(p):
	''' MethodReference : Name ':' ':' TypeArguments Identifier
						| ReferenceType ':' ':' TypeArguments Identifier
						| Primary ':' ':' TypeArguments Identifier
						| super ':' ':' TypeArguments Identifier
						| Name '.' super ':' ':' TypeArguments Identifier
						| ClassType ':' ':' TypeArguments new
						| Name ':' ':'  Identifier
						| ReferenceType ':' ':'  Identifier
						| Primary ':' ':'  Identifier
						| super ':' ':'  Identifier
						| Name '.' super ':' ':'  Identifier
						| ClassType ':' ':'  new
						| ArrayType ':' ':' new
	'''
def p_ARRAYCREATIONEXPRESSION(p):
	'''ArrayCreationExpression : new PrimitiveType DimExprs Dims
							 | new ClassOrInterfaceType DimExprs Dims
							 | new PrimitiveType DimExprs
							 | new ClassOrInterfaceType DimExprs
							 | new PrimitiveType Dims ArrayInitializer
							 | new ClassOrInterfaceType Dims ArrayInitializer
	'''
def p_DIMEXPRS(p):
	'''DimExprs : DimExpr 
			   | DimExpr DimExprs
	'''
def p_DIMEXPR(p):
	'''DimExpr : Annotations '[' Expression ']'
	'''
def p_EXPRESSION(p):
	'''Expression : LambdaExpression
				| AssignmentExpression
	'''
def p_LAMBDAEXPRESSION(p):
	''' LambdaExpression : LambdaParameters '-' '>' LambdaBody
	'''
def p_LAMBDAPARAMETERS(p):
	'''LambdaParameters : Identifier 
						| '(' FormalParameterList ')'
						| '(' ')'
						| '(' InferredFormalParameterList ')' 
	'''

def p_INFERREDFORMALPARAMETERLIST(p):
	'''InferredFormalParameterList : Identifier 
								| Identifier ',' InferredFormalParameterList
	'''
def p_LAMBDABODY(p):
	'''LambdaBody : Expression
				| Block
	'''
def p_ASSIGNMENTEXPRESSION(p):
	'''AssignmentExpression : ConditionalExpression
							| Assignment
	'''
def p_ASSIGNMENT(p): 
	''' Assignment : LeftHandSide AssignmentOperator Expression 
	'''
def p_LEFTHANDSIDE(p):
	'''LeftHandSide : Name
					| FieldAccess
					| ArrayAccess
	'''	
def p_AssignmentOperator(p):
	'''AssignmentOperator : '='
						  | '*' '='
						  | '/' '='
						  | '%' '='
						  | '+' '='
						  | '-' '='
						  | '<' '<' '='
						  | '>' '>' '='
						  | '>' '>' '>' '='
						  | '&' '='
						  | '^' '='
						  | '|' '='
	'''
def p_CONDITIONALEXPRESSION(p):
	'''ConditionalExpression : ConditionalOrExpression
							| ConditionalOrExpression '?' Expression ':' ConditionalExpression
							| ConditionalOrExpression '?' Expression ':' LambdaExpression 
	'''

def p_CONDITIONALOREXPRESSION(p):
	'''ConditionalOrExpression : ConditionalAndExpression
							   | ConditionalAndExpression '&' '&' ConditionalOrExpression

	'''
def p_CONDITIONALANDEXPRESSION(p):
	'''ConditionalAndExpression : InclusiveOrExpression
								| ConditionalAndExpression '&' '&' InclusiveOrExpression
	'''
def p_INCLUSIVEOREXPRESSION(p):
	'''InclusiveOrExpression : ExclusiveOrExpression
							| InclusiveOrExpression '|' ExclusiveOrExpression
	'''

def p_EXCLUSIVEOREXPRESSION(p):
	'''ExclusiveOrExpression : AndExpression
							| ExclusiveOrExpression '^' AndExpression 
	'''
def p_ANDEXPRESSION(p):
	'''AndExpression : EqualityExpression
					| AndExpression '&' EqualityExpression
	'''

def p_EQUALITYEXPRESSION(p):
	'''EqualityExpression : RelationalExpression
						  | EqualityExpression '=' '=' RelationalExpression
						  | EqualityExpression '!' '=' RelationalExpression
	'''

def p_RELATIONALEXPRESSION(p):
	'''RelationalExpression : ShiftExpression
	   						| RelationalExpression '<' ShiftExpression
							| RelationalExpression '>' ShiftExpression
							| RelationalExpression '<' '=' ShiftExpression
							| RelationalExpression '>' '=' ShiftExpression
							| RelationalExpression instanceof ReferenceType
	'''

def p_SHIFTEXPRESSION(p):
	'''ShiftExpression : AdditiveExpression
					  | ShiftExpression '<' '<' AdditiveExpression
					  | ShiftExpression '>' '>' AdditiveExpression
					  | ShiftExpression '>' '>' '>' AdditiveExpression  
	'''

def p_ADDITIVEEXPRESSION(p):
	'''AdditiveExpression : MultiplicativeExpression
						  | AdditiveExpression '+' MultiplicativeExpression
						  | AdditiveExpression '-' MultiplicativeExpression
	'''

def p_MULTIPLICATIVEEXPRESSION(p):
	'''MultiplicativeExpression : UnaryExpression
								| MultiplicativeExpression '*' UnaryExpression
								| MultiplicativeExpression '/' UnaryExpression
								| MultiplicativeExpression '%' UnaryExpression
	'''
def p_UNARYEXPRESSION(p):
	'''UnaryExpression : PreIncrementExpression
					 | PreDecrementExpression
					 | '+' UnaryExpression
					 | '-' UnaryExpression
					 | UnaryExpressionNotPlusMinus
	'''
def p_PREINCREMENTEXPRESSION(p):
	'''PreIncrementExpression : '+' '+' UnaryExpression
	'''
def p_PREDECREMENTEXPRESSION(p):
	'''PreDecrementExpression : '-' '-' UnaryExpression
	'''
def p_UNARYEXPRESSIONNOTPLUSMINUS(p):
	'''UnaryExpressionNotPlusMinus : PostfixExpression 
								| '~' UnaryExpression
								| '!' UnaryExpression
								| CastExpression
	'''
def p_POSTFIXEXPRESSION(p):
	'''PostfixExpression : Primary
						| Name
						| PostIncrementExpression
						| PostDecrementExpression
	'''
def p_POSTINCREMENTEXPRESSION(p):
	'''PostIncrementExpression : PostfixExpression '+' '+'
	'''

def p_POSTDECREMENTEXPRESSION(p):
	'''PostDecrementExpression : PostfixExpression '-' '-'
	'''

def p_CASTEXPRESSION(p): #additionalbound paren 
	'''CastExpression : '(' PrimitiveType ')' UnaryExpression
					| '(' ReferenceType AdditionalBounds  ')' UnaryExpressionNotPlusMinus
					| '(' ReferenceType AdditionalBounds  ')' LambdaExpression
					| '(' ReferenceType ')' UnaryExpressionNotPlusMinus
					| '(' ReferenceType ')' LambdaExpression
	'''

def p_CONSTANTEXPRESSION(p):
	'''ConstantExpression : Expression
	'''
 # Error rule for syntax errors

def p_Identifier(p):
	'''Identifier : IDENTIFIER
	'''

def p_Name(p):
	''' Name : SimpleName
	          | QualifiedName
	'''

def p_SimpleName(p):
	''' SimpleName : Identifier
	'''

def p_QualifiedName(p):
	''' QualifiedName : Name '.' Identifier
	'''

def p_ClassDeclaration(p):
	''' ClassDeclaration : NormalClassDeclaration
	                    | EnumDeclaration
	'''

def p_NormalClassDeclaration(p):
	''' NormalClassDeclaration : Modifiers class Identifier TypeParameters Superclass Superinterfaces ClassBody
							  | class Identifier TypeParameters Superclass Superinterfaces ClassBody
	                          | Modifiers class Identifier TypeParameters Superclass ClassBody
							  | class Identifier TypeParameters Superclass ClassBody
							  | Modifiers class Identifier TypeParameters Superinterfaces ClassBody
							  | class Identifier TypeParameters Superinterfaces ClassBody
							  | Modifiers class Identifier TypeParameters ClassBody
							  | class Identifier TypeParameters ClassBody
							  | Modifiers class Identifier Superclass Superinterfaces ClassBody
							  | class Identifier Superclass Superinterfaces ClassBody
							  | Modifiers class Identifier Superclass ClassBody
							  | class Identifier Superclass ClassBody
							  | Modifiers class Identifier Superinterfaces ClassBody
							  | class Identifier Superinterfaces ClassBody
							  | Modifiers class Identifier ClassBody
							  | class Identifier ClassBody
	'''

def p_Modifiers(p):
	''' Modifiers : Modifier
	             | Modifiers Modifier
	'''

def p_Modifier(p):
	''' Modifier : public 
				| protected 
				| private 
				| static
	            | abstract 
				| final 
				| native 
				| synchronized
				| transient 
				| volatile
	'''

def p_TypeParameters(p):
	''' TypeParameters : '<' TypeParameterList '>'
	'''

def p_TypeParameterList(p):
	''' TypeParameterList : TypeParameter 
	                     | TypeParameter CommaTypeParameterStar
	'''

def p_CommaTypeParameterStar(p):
	''' CommaTypeParameterStar : ',' TypeParameter
	                          | CommaTypeParameterStar ',' TypeParameter
	'''

def p_Superclass(p):
	''' Superclass : extends ClassType
	'''

def p_Superinterfaces(p):
	''' Superinterfaces : implements InterfaceTypeList
	'''

def p_InterfaceTypeList(p):
	''' InterfaceTypeList : InterfaceType
	                    |  InterfaceType CommaInterfaceTypeStar 
	'''

def p_CommaInterfaceTypeStar(p):
	''' CommaInterfaceTypeStar : ',' InterfaceType
	                          | CommaInterfaceTypeStar ',' InterfaceType   
	'''

def p_ClassBody(p):
	''' ClassBody : ClassBody ClassBodyDeclarationStar
	              | 
	'''

def p_ClassBodyDeclaration(p):
	''' ClassBodyDeclaration : ClassMemberDeclaration
	                           | InstanceInitializer
							   | StaticInitializer
							   | ConstructorDeclaration
	'''

def p_ClassMemberDeclaration(p):
	''' ClassMemberDeclaration : FieldDeclaration
	                          | MethodDeclaration
							  | ClassDeclaration
	'''

def p_FieldDeclaration(p):
	''' FieldDeclaration : Modifiers UnannType VariableDeclaratorList
						| UnannType VariableDeclaratorList
	'''

def p_VariableDeclaratorList(p):
	''' VariableDeclaratorList : VariableDeclarator CommaVariableDeclaratorStar
	                         | VariableDeclarator
	'''

def p_CommaVariableDeclaratorStar(p):
	''' CommaVariableDeclaratorStar : ',' VariableDeclarator
	                               | CommaVariableDeclaratorStar ',' VariableDeclarator
	'''

def p_VariableDeclarator(p):
    ''' VariableDeclarator : VariableDeclaratorId '=' VariableInitializer
	                      | VariableDeclaratorId
	'''

def p_VariableDeclaratorId(p):
	'''
        VariableDeclaratorId :  Identifier Dims
		                    |  Identifier
    '''

def p_VariableInitializer(p):
	'''
       VariableInitializer :  Expression
                           | ArrayInitializer
    '''

def p_UnannType(p):
	'''
       UnannType : UnannPrimitiveType
                | UnannReferenceType
    '''

def p_UnannPrimitiveType(p):
    '''UnannPrimitiveType : NumericType
                         | boolean
	'''

def p_UnannReferenceType(p):
	'''
      UnannReferenceType : UnannClassOrInterfaceType
                   | UnannTypeVariable
                   | UnannArrayType
    '''

def p_UnannClassOrInterfaceType(p):
	'''UnannClassOrInterfaceType : UnannClassType
								| UnannInterfaceType
	'''

def p_UnannClassType(p):
	''' UnannClassType : Identifier TypeArguments
	                  | Identifier
                      | UnannClassOrInterfaceType '.' Annotations Identifier TypeArguments
					  | UnannClassOrInterfaceType '.' Annotations Identifier 
					  | UnannClassOrInterfaceType '.' Identifier TypeArguments
					  | UnannClassOrInterfaceType '.' Identifier
					  '''

def p_UnannInterfaceType(p):
			'''UnannInterfaceType : UnannClassType
			'''

def p_UnannTypeVariable(p):
		'''UnannTypeVariable : Identifier
		'''

def p_UnannArrayType(p):
		'''UnannArrayType : UnannPrimitiveType Dims
					| UnannClassOrInterfaceType Dims
					| UnannTypeVariable Dims
		'''

def p_MethodDeclaration(p):
		'''MethodDeclaration : Modifiers MethodHeader MethodBody
		'''

def p_MethodHeader(p):
		'''MethodHeader : Result MethodDeclarator Throws
		            |  Result MethodDeclarator 
					|  TypeParameters Annotations Result MethodDeclarator Throws
					|  TypeParameters Annotations Result MethodDeclarator 
		'''

def p_Result(p):
		'''Result : UnannType
		      | void
		'''

def p_MethodDeclarator(p):
		'''MethodDeclarator : Identifier '(' FormalParameterList ')' Dims
						| Identifier '(' ')' Dims
						| Identifier '(' FormalParameterList ')' 
						| Identifier '(' ')' 
		'''

def p_FormalParameterList(p):
		'''FormalParameterList : ReceiverParameter
						| FormalParameters ',' LastFormalParameter
						| LastFormalParameter
		'''

def p_FormalParameters(p):
		'''FormalParameters : FormalParameter CommaFormalParameters
						| ReceiverParameter CommaFormalParameters
						| FormalParameter
						| ReceiverParameter
		'''

def p_CommaFormalParameters(p):
		'''CommaFormalParameters : ',' FormalParameter
								| CommaFormalParameters ',' FormalParameter
		'''

def p_FormalParameter(p):
		'''FormalParameter : VariableModifierStar UnannType VariableDeclaratorId
						| UnannType VariableDeclaratorId
		'''
def p_VariableModifier(p):
	''' VariableModifier : Annotation
	                   |  final
	'''

def p_LastFormalParameter(p):
		'''LastFormalParameter : VariableModifierStar UnannType Annotations '.' '.' '.' VariableDeclaratorId
							|   UnannType Annotations '.' '.' '.' VariableDeclaratorId
							|	VariableModifierStar UnannType  '.' '.' '.' VariableDeclaratorId
							|	UnannType '.' '.' '.' VariableDeclaratorId
							|	FormalParameter
		'''

def p_ReceiverParameter(p):
		'''ReceiverParameter : Annotations UnannType Identifier '.' this
							| Annotations UnannType this
		'''

def p_Throws(p):
	'''Throws : throws ExceptionTypeList
	'''

def p_ExceptionTypeList(p):
	'''ExceptionTypeList :	ExceptionType CommaExceptionTypes
						| 	ExceptionType
	'''

def p_CommaExceptionTypes(p):
	'''CommaExceptionTypes : ',' ExceptionType
							| CommaExceptionTypes ',' ExceptionType
	'''

def p_ExceptionType(p):
	'''	ExceptionType : ClassType
					| TypeVariable
	'''

def p_MethodBody(p):
		'''MethodBody : Block
		  		| ';'
		'''

def p_InstanceInitializer(p):
		'''InstanceInitializer : Block
		'''

def p_StaticInitializer(p):
		'''StaticInitializer : static Block
		'''

def p_ConstructorDeclaration(p):
		'''ConstructorDeclaration : Modifiers ConstructorDeclarator Throws ConstructorBody
								| ConstructorDeclarator Throws ConstructorBody
								| ConstructorDeclarator ConstructorBody
								| Modifiers ConstructorDeclarator ConstructorBody
		'''

def p_ConstructorDeclarator(p):
		'''ConstructorDeclarator : TypeParameters SimpleTypeName '(' FormalParameterList ')'
								| SimpleTypeName '(' FormalParameterList ')'
								| SimpleTypeName '(' ')'
								| TypeParameters SimpleTypeName '(' ')'
		'''

def p_SimpleTypeName(p):
		'''	SimpleTypeName : Identifier
		'''

def p_ConstructorBody(p):
		''' ConstructorBody : ConstructorBody ExplicitConstructorInvocation BlockStatements
							| ConstructorBody BlockStatements
							| ConstructorBody ExplicitConstructorInvocation
							|

		'''

def p_ExplicitConstructorInvocation(p):
		'''	ExplicitConstructorInvocation :  TypeArguments this '(' ArgumentList ')' ';'
										|	this '(' ArgumentList ')' ';'
										|	TypeArguments this '(' ')' ';'
										| 	this '(' ')' ';'
										|	TypeArguments super '(' ArgumentList ')' ';'
										|	super '(' ArgumentList ')' ';'
										|	super '(' ')' ';'
										|	TypeArguments super '(' ')' ';'
										|	Name '.' TypeArguments super '(' ArgumentList ')' ';'
										|	Name '.' TypeArguments super '(' ')' ';'
										|	Name '.' super '(' ArgumentList ')' ';'
										|	Name '.' super '(' ')' ';'
										|	Primary '.' TypeArguments super '(' ArgumentList ')' ';'
										|	Primary '.' TypeArguments super '(' ')' ';'
										|	Primary '.' super '(' ArgumentList ')' ';'
										|	Primary '.' super '(' ')' ';'
		'''

def p_EnumDeclaration(p):
		'''EnumDeclaration : Modifiers enum Identifier Superinterfaces EnumBody
						| 	Modifiers enum Identifier EnumBody
						| 	enum Identifier EnumBody
						| 	enum Identifier Superinterfaces EnumBody
		'''


def p_EnumBody(p):
		'''EnumBody : 
					| EnumBody EnumConstantList ',' EnumBodyDeclarations 
					| EnumBody EnumConstantList ',' 
					| EnumBody EnumConstantList EnumBodyDeclarations 
					| EnumBody EnumConstantList 
					| EnumBody ',' EnumBodyDeclarations  
					| EnumBody ','
					| EnumBody EnumBodyDeclarations 
		'''

def p_EnumConstantList(p):
		'''	EnumConstantList : EnumConstant CommaEnumConstants
						| 	EnumConstant 
		'''

def p_CommaEnumConstants(p):
		'''	CommaEnumConstants : ',' EnumConstant
						|	CommaEnumConstants ',' EnumConstant
		'''

def p_EnumConstant(p):
		''' EnumConstant : EnumConstantModifiers Identifier '(' ArgumentList ')' ClassBody
						| EnumConstantModifiers Identifier '(' ')' ClassBody
						| EnumConstantModifiers Identifier ClassBody
						| EnumConstantModifiers Identifier '(' ArgumentList ')'
						| EnumConstantModifiers Identifier '(' ')'
						| EnumConstantModifiers Identifier
						| Identifier '(' ArgumentList ')' ClassBody
						| Identifier '(' ')' ClassBody
						| Identifier ClassBody
						| Identifier 
						| Identifier '(' ArgumentList ')'
						| Identifier '(' ')'
		'''

def p_EnumConstantModifier(p):
		'''EnumConstantModifier : Annotation
		'''

def p_EnumBodyDeclarations(p):
		''' EnumBodyDeclarations : ';' ClassBodyDeclarationStar
								| ';'
		'''

def p_ClassBodyDeclarationStar(p):
	''' ClassBodyDeclarationStar : ClassBodyDeclaration
							| ClassBodyDeclarationStar ClassBodyDeclaration
	'''
def p_EnumConstantModifiers(p):
		''' EnumConstantModifiers : EnumConstantModifier
								|	EnumConstantModifiers EnumConstantModifier
		'''

def p_Type(p):
	''' Type : PrimitiveType
			  | ReferenceType
	'''

def p_PrimitiveType(p):
	''' PrimitiveType :  NumericType
					  | Annotations NumericType
					  | boolean
					  | Annotations boolean
	'''
def p_Annotations(p):
	''' Annotations : Annotation
					| Annotations Annotation
	'''
def p_NumericType(p):
	''' NumericType : IntegralType
					| FloatingPointType
	'''
def p_IntergralType(p):
	'''IntegralType : byte
					| short
					| int
					| long
					| char
	'''

def p_FloatingPointType(p):
	'''FloatingPointType : float
						| double
	'''

def p_ReferenceType(p):
	'''ReferenceType : ClassOrInterfaceType
					| TypeVariable
					| ArrayType
	'''

def p_ClassOrInterfaceType(p):
	'''ClassOrInterfaceType : Name
	'''

def p_ClassType(p):
	''' ClassType : ClassOrInterfaceType
	'''

def p_InterfaceType(p):
	''' InterfaceType : ClassOrInterfaceType
	'''

def p_TypeVariable(p):
	'''TypeVariable : Identifier
				   | Annotations Identifier
	'''

def p_ArrayType(p):
	'''ArrayType : PrimitiveType '[' ']'
				| Name '[' ']'
				| ArrayType '[' ']'
	'''


def p_Dims(p):
	''' Dims : '[' ']'
			 | '[' ']' sqAnnotations
			 | Annotations '[' ']'
			 | Annotations '[' ']' sqAnnotations
	'''

def p_sqAnnotations(p):
	'''sqAnnotations : '[' ']'
					 | sqAnnotations '[' ']'
					 | sqAnnotations Annotations '[' ']'
	'''

def p_TypeParameter(p):
	'''TypeParameter : Identifier
					 | Identifier TypeBound
					 | TypeParameterModifiers Identifier
					 | TypeParameterModifiers Identifier TypeBound
	'''

def p_TypeParameterModifiers(p):
	'''TypeParameterModifiers : TypeParameterModifier 
							  | TypeParameterModifiers TypeParameterModifier 
	'''

def p_TypeParameterModifier(p):
	'''TypeParameterModifier : Annotation
	'''

def p_TypeBound(p):
	'''TypeBound : extends TypeVariable
				| extends ClassOrInterfaceType
				| extends ClassOrInterfaceType AdditionalBounds
	'''

def p_AdditionalBounds(p):
	'''AdditionalBounds : AdditionalBound
						| AdditionalBounds AdditionalBound
	'''

def p_AdditionalBound(p):
	'''AdditionalBound : '&' InterfaceType
	'''

def p_TypeArguments(p):
	'''TypeArguments : '<' TypeArgumentList '>'
	'''

def p_TypeArgumentList(p):
	'''TypeArgumentList : TypeArgument
						| TypeArgument comTypeArguments
	'''

def p_comTypeArguments(p):
	'''comTypeArguments : ',' TypeArgument
					   | comTypeArguments ',' TypeArgument
	'''

def p_TypeArgument(p):
	'''TypeArgument : ReferenceType
				   | Wildcard
	'''

def p_Wildcard(p):
	'''Wildcard : '?'
				| '?' WildcardBounds
				| Annotations '?'
			    | Annotations '?' WildcardBounds
	'''

def p_WildcardBounds(p):
	'''WildcardBounds : extends ReferenceType
					 | super ReferenceType 
	'''



#Annotations

def p_Annotation(p):
	'''Annotation : NormalAnnotation
				 | MarkerAnnotation
				 | SingleElementAnnotation
	'''
def p_NormalAnnotation(p):
	'''NormalAnnotation : '@' Name '(' ')'
					   | '@' Name '(' ElementValuePairList ')'
	'''

def p_ElementValuePairList(p):
	'''ElementValuePairList : ElementValuePair 
							| ElementValuePair comElementValuePairs
	'''

def p_comElementValuePairs(p):
	'''comElementValuePairs : ',' ElementValuePair
							| comElementValuePairs ',' ElementValuePair
	'''

def p_ElementValuePair(p):
	'''ElementValuePair : Identifier '=' ElementValue
	'''

def p_ElementValue(p):
	'''ElementValue : ConditionalExpression
				   | ElementValueArrayInitializer
				   | Annotation
	'''

def p_ElementValueArrayInitializer(p):
	'''ElementValueArrayInitializer : 
							  | ElementValueArrayInitializer ElementValueList
							  | ElementValueArrayInitializer ','
							  | ElementValueArrayInitializer ElementValueList ','
	'''

def p_ElementValueList(p):
	'''ElementValueList : ElementValue
						| ElementValue comElementValues
	'''

def p_comElementValues(p):
	'''comElementValues : ',' ElementValue
					   | comElementValues ',' ElementValue
	'''

def p_MarkerAnnotation(p):
	'''MarkerAnnotation : '@' Name
	'''

def p_SingleElementAnnotation(p):
	'''SingleElementAnnotation : '@' Name '(' ElementValue ')'
	'''



#Blocks and Statements

def p_Block(p):
	'''Block : 
			| Block oneBlockStatements
	'''
def p_oneBlockStatements(p):
	'''oneBlockStatements :
						 | BlockStatements
	'''

def p_BlockStatements(p):
	'''BlockStatements : BlockStatement
					   | BlockStatements BlockStatement
	'''

def p_BlockStatement(p):
	'''BlockStatement : LocalVariableDeclarationStatement
					 | ClassDeclaration
					 | Statement
	'''

def p_LocalVariableDeclarationStatement(p):
	'''LocalVariableDeclarationStatement : LocalVariableDeclaration ';'
	'''

def p_LocalVariableDeclaration(p):
	'''LocalVariableDeclaration : UnannType VariableDeclaratorList
								| VariableModifierStar UnannType VariableDeclaratorList
	'''

def p_VariableModifierStar(p):
	'''VariableModifierStar : VariableModifier
						   | VariableModifierStar VariableModifier
	'''

def p_Statement(p):
	'''Statement : StatementWithoutTrailingSubstatement
				| LabeledStatement
				| IfThenStatement
				| IfThenElseStatement
				| WhileStatement
				| ForStatement
	'''

def p_StatementNoShortIf(p):
	'''StatementNoShortIf : StatementWithoutTrailingSubstatement
						 | LabeledStatementNoShortIf
						 | IfThenElseStatementNoShortIf
						 | WhileStatementNoShortIf
						 | ForStatementNoShortIf
	'''

def p_StatementWithoutTrailingSubstatement(p):
	'''StatementWithoutTrailingSubstatement : Block
											| EmptyStatement
											| ExpressionStatement
											| AssertStatement
											| DoStatement
											| BreakStatement
											| ContinueStatement
											| ReturnStatement
											| SynchronizedStatement
											| ThrowStatement
											| TryStatement
	'''

def p_EmptyStatement(p):
	'''EmptyStatement : ';'
	'''

def p_LabeledStatement(p):
	'''LabeledStatement : Identifier ':' Statement
	'''

def p_LabeledStatementNoShortIf(p):
	'''LabeledStatementNoShortIf : Identifier ':' StatementNoShortIf
	'''

def p_ExpressionStatement(p):
	'''ExpressionStatement : StatementExpression ';'
	'''

def p_StatementExpression(p):
	'''StatementExpression : Assignment
						  | PreIncrementExpression
						  | PreDecrementExpression
						  | PostIncrementExpression
						  | PostDecrementExpression
						  | MethodInvocation
						  | ClassInstanceCreationExpression
	'''

def p_IfThenStatement(p):
	'''IfThenStatement : if '(' Expression ')' Statement
	'''

def p_IfThenElseStatement(p):
	'''IfThenElseStatement : if '(' Expression ')' StatementNoShortIf else Statement
	'''

def p_IfThenElseStatementNoShortIf(p):
	'''IfThenElseStatementNoShortIf : if '(' Expression ')' StatementNoShortIf else StatementNoShortIf
	'''

def p_AssertStatement(p):
	'''AssertStatement : assert Expression ';'
    				|	assert Expression ':' Expression ';'
	'''

def p_EnumConstantName(p):
	'''EnumConstantName : Identifier
	'''

def p_WhileStatement(p):
	'''WhileStatement : while '(' Expression ')' Statement
	'''

def p_WhileStatementNoShortIf(p):
	'''WhileStatementNoShortIf : while '(' Expression ')' StatementNoShortIf
	'''
def p_DoStatement(p):
	'''DoStatement : do Statement while '(' Expression ')' ';'
	'''

def p_ForStatement(p):
	'''ForStatement : BasicForStatement
 				   | EnhancedForStatement
 	'''

def p_ForStatementNoShortIf(p):
	'''ForStatementNoShortIf : BasicForStatementNoShortIf
							| EnhancedForStatementNoShortIf
	'''

def p_BasicForStatement(p):
	'''BasicForStatement : for '(' ';' ';' ')' Statement
						| for '(' ForInit ';' ';' ')' Statement
						| for '(' ';' Expression ';' ')' Statement
						| for '(' ';' ';' ForUpdate ')' Statement
						| for '(' ForInit ';' Expression ';' ')' Statement
						| for '(' ';' Expression ';' ForUpdate ')' Statement
						| for '(' ForInit ';' ';' ForUpdate ')' Statement
						| for '(' ForInit ';' Expression ';' ForUpdate ')' Statement
	'''

def p_BasicForStatementNoShortIf(p):
	'''BasicForStatementNoShortIf : for '(' ';' ';' ')' StatementNoShortIf
								| for '(' ForInit ';' ';' ')' StatementNoShortIf
								| for '(' ';' Expression ';' ')' StatementNoShortIf
								| for '(' ';' ';' ForUpdate ')' StatementNoShortIf
								| for '(' ForInit ';' Expression ';' ')' StatementNoShortIf
								| for '(' ';' Expression ';' ForUpdate ')' StatementNoShortIf
								| for '(' ForInit ';' ';' ForUpdate ')' StatementNoShortIf
								| for '(' ForInit ';' Expression ';' ForUpdate ')' StatementNoShortIf
	'''

def p_ForInit(p):
	'''ForInit : StatementExpressionList
			  | LocalVariableDeclaration
	'''

def p_ForUpdate(p):
	'''ForUpdate : StatementExpressionList
	'''

def p_StatementExpressionList(p):
	'''StatementExpressionList : StatementExpression
							   | StatementExpression comStatementExpressionStar
 	'''
def p_comStatementExpressionStar(p):
	'''comStatementExpressionStar : ',' StatementExpression
								 | comStatementExpressionStar ',' StatementExpression
	'''

def p_EnhancedForStatement(p):
	'''EnhancedForStatement : for '(' UnannType VariableDeclaratorId ':' Expression ')' Statement
							| for '(' VariableModifierStar UnannType VariableDeclaratorId ':' Expression ')' Statement
	'''

def p_EnhancedForStatementNoShortIf(p):
	'''EnhancedForStatementNoShortIf : for '(' UnannType VariableDeclaratorId ':' Expression ')' StatementNoShortIf
							| for '(' VariableModifierStar UnannType VariableDeclaratorId ':' Expression ')' StatementNoShortIf
	'''

def p_BreakStatement(p):
	'''BreakStatement : break ';'
					 | break Identifier ';'
	'''

def p_ContinueStatement(p):
	'''ContinueStatement : continue ';'
						| continue Identifier ';'
	'''

def p_ReturnStatement(p):
	'''ReturnStatement : return ';'
					  | return Expression ';'
	'''

def p_ThrowStatement(p):
	'''ThrowStatement : throw Expression ';'
	'''

def p_SynchronizedStatement(p):
	'''SynchronizedStatement : synchronized '(' Expression ')' Block
	'''

def p_TryStatement(p):
	'''TryStatement : try Block Catches
				   | try Block Finally
				   | try Block Catches Finally
				   | TryWithResourcesStatement
	'''

def p_Catches(p):
	'''Catches : CatchClause
			   | CatchClause CatchClauseStar
	'''

def p_CatchClauseStar(p):
	'''CatchClauseStar : CatchClause
					   | CatchClauseStar CatchClause
	'''

def p_CatchClause(p):
	'''CatchClause : catch '(' CatchFormalParameter ')' Block
	'''

def p_CatchFormalParameter(p):
	'''CatchFormalParameter : CatchType VariableDeclaratorId
							| VariableModifierStar CatchType VariableDeclaratorId
	'''

def p_CatchType(p):
	'''CatchType : UnannClassType
				 | UnannClassType stickClassTypeStar
	'''
def p_stickClassTypeStar(p):
	'''stickClassTypeStar : '|' ClassType
						  | stickClassTypeStar '|' ClassType
	'''

def p_Finally(p):
	'''Finally : finally Block
	'''

def p_TryWithResourcesStatement(p):
	'''TryWithResourcesStatement : try ResourceSpecification Block 
								| try ResourceSpecification Block  Catches
								| try ResourceSpecification Block finally
								| try ResourceSpecification Block  Catches finally
	'''

def p_ResourceSpecification(p):
	'''ResourceSpecification : '(' ResourceList ')'
							| '(' ResourceList ';' ')'
	'''

def p_ResourceList(p):
	'''ResourceList : Resource
					| Resource colResourceStar
	'''

def p_colResourceStar(p):
	'''colResourceStar : ';' Resource
					   | colResourceStar ';' Resource
	'''

def p_Resource(p):
	'''Resource : UnannType VariableDeclaratorId '=' Expression
				| VariableModifierStar UnannType VariableDeclaratorId '=' Expression
 	'''

 # Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


 # Build the parser
parser = yacc.yacc()
args = sys.argv
for x in args:
	if(x.startswith("--inp=")):
		input_file_name = x[6:]
		# print(config_file_name)
	if (x.startswith("--output=")):
		html_name = x[9:]

input_file = open(input_file_name,'r')
input_str = input_file.read()

parser.parse(input_str)
