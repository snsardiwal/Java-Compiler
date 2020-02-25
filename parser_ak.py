import ply.lex as lex
import ply.yacc as yacc


tokens = ('KEYWORD','ALPHABET', 'DECIMAL', 'FLOAT'
		  'LS', 'WS',
		  'T','C','S',
		  'COL')


t_KEYWORD = r'Title|Chapter|Section'
t_ALPHABET = r'[a-zA-Z]*'
t_DECIMAL = r'''
     		(0x|0X)(([0-9a-fA-F]([0-9a-fA-F]|_)*[0-9a-fA-F])|[0-9a-fA-F])[l|L]? |
     		(0b|0B)([0-1]([0-1]|_)*[0-1]|[0-1])[l|L] |
     		((0)((_|[0-7])*[0-7])+[l|L]? |
			([1-9]([0-9]|_)*[0-9]|[0-9])[l|L]?)
			'''	
t_FLOAT = r'''
		(([0-9]|([1-9]([0-9]|_)*[0-9]))+\.([0-9]|([1-9]([0-9]|_)*[0-9]))*((e|E)(\+|-)?([0-9]|([1-9]([0-9]|_)*[0-9]))+)?[fFdD]? |
 	 		\.([0-9]|([1-9]([0-9]|_)*[0-9]))+((e|E)(\+|-)?([0-9]|([1-9]([0-9]|_)*[0-9]))+)?[fFdD]? |
     		([0-9]|([1-9]([0-9]|_)*[0-9]))+((e|E)(\+|-)?([0-9]|([1-9]([0-9]|_)*[0-9]))+)[fFdD]? |
	 		([0-9]|([1-9]([0-9]|_)*[0-9]))+((e|E)(\+|-)?([0-9]|([1-9]([0-9]|_)*[0-9]))+)?[fFdD] |
     		(0(x|X)([0-9a-fA-F]|([0-9a-fA-F]([0-9a-fA-F]|_)*[0-9a-fA-F]))+\.?|0(x|X)([0-9a-fA-F]|([0-9a-fA-F]([0-9a-fA-F]|_)*[0-9a-fA-F]))*\.([0-9a-fA-F]|([0-9a-fA-F]([0-9a-fA-F]|_)*[0-9a-fA-F]))+)(p|P)(\+|-)?([0-9]|([1-9]([0-9]|_)*[0-9]))+[fFdD]?)
'''
t_T = r'Title'
t_C = r'Chapter'
t_S = r'Section'
t_COL = r':'

t_LS = r'[\s]*[/.!?]'
t_WS = r'[\s]*|[\s]*[,;]'


lexer = lex.lex(debug=1)

#parser

# start = 'start'

#Terminals
def p_title(p):
	'''title : T COL LINE'''
	p[0] = p[1] + p[2] + p[3]

def p_chapter(p):
	'''chapter : C DECIMAL COL LINE'''
	p[0] = p[1] + p[2] + p[3] + p[4]

def p_section(p):
	''' section : S DECIMAL COL LINE'''
	p[0] = p[1] + p[2] + p[3] + [4]


def p_WORD(p):
	''' WORD : ALPHABET 
		| DECIMAL 
		| FLOAT
	'''
	p[0] = p[1]


#Grammer Rules
def p_DOCUMENT(p):
	''' DOCUMENT : title CHAPTER'''
	p[0] = p[1] + p[2]

def p_CHAPTER(p):
	''' CHAPTER : chapter SECTION chapter
				| chapter BODY SECTION CHAPTER
				| chapter SECTION
	'''
	if(len(p)==3):
		p[0] = p[1] + p[2]
	elif(len(p)==4):
		p[0] = p[1] + p[2] + p[3]
	else:
		p[0] = p[1] + p[2] + p[3] + p[4]

def p_SECTION(p):
	''' SECTION : section BODY SECTION
				| section BODY
	'''
	if(len(p)==3):
		p[0] = p[1] + p[2]
	else:
	    p[0] = p[1] + p[2] + p[3]

def p_BODY(p):
	''' BODY : PARAGRAPH NEWLINE BODY
			| PARAGRAPH NEWLINE
	'''
	if(len(p)==3):
		p[0] = p[1] + p[2]
	else:
		p[0] = p[1] + p[2] + p[3]


def p_PARAGRAPH(p):
	''' PARAGRAPH : LINE LINESEP PARAGRAPH
				| LINE LINESEP
	'''
	if(len(p)==3):
		p[0] = p[1] + p[2]
	else:	
		p[0] = p[1] + p[2] + p[3]


def p_LINE(p):
	''' LINE : WORD WORDSEP LINE
			| WORD
	'''
	if(len(p)==2):
		p[0] = p[1]
	else:	
	    p[0] = p[1] + p[2] + p[3]
######################################
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
	'''ArrayInitializer : ArrayInitializer VariableInitializers ','
						| ArrayInitializer VariableInitializers
						| ArrayInitializer ','
						|
	'''
def p_VARIABLEINITIALIZERS(p):
	'''VariableInitializerList : VariableInitializer
							  | VariableInitializers , VariableInitializer

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
	   								  | ExpressionName '.' UnqualifiedClassInstanceCreationExpression
									  | Primary '.' UnqualifiedClassInstanceCreationExpression
	'''
def p_UNQUALIFIEDCLASSINSTANCECREATIONEXPRESSION(p):
	'''UnqualifiedClassInstanceCreationExpression : new TypeArguments ClassOrInterfaceTypeToInstantiate '(' ArgumentList ')' Classbody
												| new  ClassOrInterfaceTypeToInstantiate '(' ArgumentList ')' Classbody
												| new TypeArguments ClassOrInterfaceTypeToInstantiate '(' ArgumentList ')' Classbody
	''' 
def p_CLASSORINTERFACETYPETOINSTANTIATE(p):
	'''ClassOrInterfaceTypeToInstantiate : Annotations Identifier  AnnoIdenStar TypeArgumentsOrDiamond
										|  Identifier  AnnoIdenStar TypeArgumentsOrDiamond
									    | Annotations Identifier   TypeArgumentsOrDiamond
										|Annotations Identifier  AnnoIdenStar 
										|  Identifier  AnnoIdenStar 
									    | Annotations Identifier   
										| Identifier   TypeArgumentsOrDiamond 
										| Identifier  AnnoIdenStar
										| Identifier
										

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
	''' ArrayAccess : ExpressionName '[' Expression ']'
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
	''' MethodReference : Name ':'':' TypeArguments Identifier
						| ReferenceType ':'':' TypeArguments Identifier
						| Primary ':'':' TypeArguments Identifier
						| super ':'':' TypeArguments Identifier
						| Name '.' super ':'':' TypeArguments Identifier
						| ClassType ':'':' TypeArguments new
						| Name ':'':'  Identifier
						| ReferenceType ':'':'  Identifier
						| Primary ':'':'  Identifier
						| super ':'':'  Identifier
						| Name '.' super ':'':'  Identifier
						| ClassType ':'':'  new
						| ArrayType ':'':' new
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
	''' LambdaExpression : LambdaParameters '-''>' LambdaBody
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
								| ConditionalAndExpression && InclusiveOrExpression
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
					| '(' ReferenceType AdditionalBoundS  ')' UnaryExpressionNotPlusMinus
					| '(' ReferenceType AdditionalBoundS  ')' LambdaExpression
	'''

def p_CONSTANTEXPRESSION(p):
	'''ConstantExpression : Expression
	'''
 # Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


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
