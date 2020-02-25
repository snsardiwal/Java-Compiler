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

start = 'Name'

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

def p_ClassBodyeclarationStar(p):
	''' ClassBodyeclarationStar : ClassBodyeclarationStar ClassBodyeclaration
	'''

def p_ClassBodyeclaration(p):
	''' ClassBodyeclaration : ClassMemberDeclaration
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
		'''FormalParameter : Modifiers UnannType VariableDeclaratorId
						| UnannType VariableDeclaratorId
		'''

def p_LastFormalParameter(p):
		'''LastFormalParameter :	Modifiers UnannType Annotations '.' '.' '.' VariableDeclaratorId
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
										|	ExpressionName '.' TypeArguments super '(' ArgumentList ')' ';'
										|	ExpressionName '.' TypeArguments super '(' ')' ';'
										|	ExpressionName '.' super '(' ArgumentList ')' ';'
										|	ExpressionName '.' super '(' ')' ';'
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
