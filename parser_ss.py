import ply.lex as lex
import ply.yacc as yacc
import lexer


#parser



#Type,Values, and Variables

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
	'''ReferenceType : ClassoOrInterfaceType
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

def p_ArrayType(p):
	'''ArrayType : PrimitiveType '[' ']'
				| Name [ ]
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
					 | super Reference Type 
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
							  |
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
	'''MarkerAnnotation : @ Name
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
	'''BlockStatements : BockStatement
					   | BlockStatements BlockStatement
	'''

def p_BlockStatement(p):
	'''BlockStatement : LocalVariableDeclarationStatement
					 | ClassDeclaration
					 | Statement
	'''

def P_LocalVariableDeclarationStatement(p):
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
	'''EmptyStatement : ;
	'''

def p_LabeledStatement(p):
	'''LabeledStatement : Identifier : Statement
	'''

def p_LabeledStatementNoShortIf(p):
	'''LabeledStatementNoShortIf : Identifier : StatementNoShortIf
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
    					assert Expression ':' Expression ';'
	'''

def p_EnumConstantName(p):
	'''EnumConstantName : Identifier
	'''

def p_WhileStatement(p):
	'''WhileStatement : while '(' Expression ')' Statement
	'''

def p_WhileStatementNoShortIf(p):
	'''WhileStaementNoShortIf : while '(' Expression ')' StatementNoShortIf
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
								| for '(' ForInit ';' Expression ';' ForUpdate')' StatementNoShortIf
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


def p_BreakStatement(p):
	'''BreakStatement : break ';'
					 | break Identifier ';'
	'''

def p_ContinueStatement(p):
	'''ContinueStatement : continue ;
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
								| try ResourceSpecification Block  catches
								| try ResourceSpecification Block finally
								| try ResourceSpecification Block  catches finally
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


# start = 'Type'

 # Build the parser
parser = yacc.yacc(start = 'Type')

while True:
  try:
    s = raw_input('dfga dfasdf ')
  except EOFError:
    break
  if not s: continue
  result = parser.parse(s)
  print(result)
