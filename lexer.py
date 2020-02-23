import ply.lex as lex
import sys 
#tokens

tokens = ( 
		'err',
		'Comment',
		'Keyword',
		'Seperator',
		'Operator',
		'Literal',
		'Identifier'
	)


t_ignore  = " \t"

def t_Comment(t):
    r'(?://[^\n]*|/\*[^*]*\*+(?:[^/*][^*]*\*+)*/)'
    t.lexer.skip(1)

def t_err(t):
	r'(0)[0-7]*([8-9]+[0-7]*)+ | (0x|0X) | (0b|0B) | /\*(.*[\n]*.*)*[^(\*/)]'
	print("Illegal character '%s'" % t.value)
	t.lexer.skip(1)

t_Keyword = r'''
			abstract|continue|for|new|switch|
			assert|default|if|package|synchronized|
			boolean|double|goto|private|this|
			break|do|implements|protected|throw|
			byte|else|import|public|throws|
			case|enum|instanceof|return|transient|
			catch|extends|int|short|try|
			char|final|interface|static|void|
			class|finally|long|strictfp|volatile|
			const|float|native|super|while
			'''
		


t_Seperator = r'::|@|\.\.\.|\.|,|;|\]|\[|\}|\{|\)|\('
t_Operator = r'>>>=|>>=|<<=|%=|\^=|\|=|&=|/=|\*=|-=|\+=|>>>|>>|<<|%|\^|\||&|/|\*|-|\+|--|\+\+|\|\||&&|!=|<=|>=|==|->|:|\?|~|!|<|>|='



t_Literal = r'''
			(([0-9]|([1-9]([0-9]|_)*[0-9]))+\.([0-9]|([1-9]([0-9]|_)*[0-9]))*((e|E)(\+|-)?([0-9]|([1-9]([0-9]|_)*[0-9]))+)?[fFdD]? |
 	 		\.([0-9]|([1-9]([0-9]|_)*[0-9]))+((e|E)(\+|-)?([0-9]|([1-9]([0-9]|_)*[0-9]))+)?[fFdD]? |
     		([0-9]|([1-9]([0-9]|_)*[0-9]))+((e|E)(\+|-)?([0-9]|([1-9]([0-9]|_)*[0-9]))+)[fFdD]? |
	 		([0-9]|([1-9]([0-9]|_)*[0-9]))+((e|E)(\+|-)?([0-9]|([1-9]([0-9]|_)*[0-9]))+)?[fFdD] |
     		(0(x|X)([0-9a-fA-F]|([0-9a-fA-F]([0-9a-fA-F]|_)*[0-9a-fA-F]))+\.?|0(x|X)([0-9a-fA-F]|([0-9a-fA-F]([0-9a-fA-F]|_)*[0-9a-fA-F]))*\.([0-9a-fA-F]|([0-9a-fA-F]([0-9a-fA-F]|_)*[0-9a-fA-F]))+)(p|P)(\+|-)?([0-9]|([1-9]([0-9]|_)*[0-9]))+[fFdD]?) |
     		#integer
     		(0x|0X)(([0-9a-fA-F]([0-9a-fA-F]|_)*[0-9a-fA-F])|[0-9a-fA-F])[l|L]? |
     		(0b|0B)([0-1]([0-1]|_)*[0-1]|[0-1])[l|L] |
     		((0)((_|[0-7])*[0-7])+[l|L]? |
			([1-9]([0-9]|_)*[0-9]|[0-9])[l|L]?) |
			#Bool and null
			((true) | (false) | (null)) |
			#string
			(\"([^\\\n]|(\\.))*?\") | 
			#char
			((')([^\n\r'\\] | \\b | \\f | \\t | \\n | \\r | \\' | \\\" | \\\\ | \\u[0-9a-fA-F]{4} | \\[0-7]{1,2} | \\[0-3][0-7]{2})('))
			'''

t_Identifier = r'[a-zA-Z\$_][a-zA-Z\$_0-9]*'

precedence = (
	('left','err'),
	('left','Identifier'),
	('left','Literal'),
	('left','Operator'),
	('left','Seperator'),
	('left','Keyword'))

 #Tracking line number
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
#  # Error handling rule

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


file = open(sys.argv[1], "r").readlines()
data = ' '.join(file)
 
# data = "int x = random.nextInt(high - low) + low;"
# print(data)
lexer = lex.lex()
lexer.input(data)

table = {}
while True:
	tok = lexer.token()
	if not tok:
		break
	if tok.value not in table:
		table[tok.value]= [tok.type,1]
	else:
		table[tok.value][1] = table[tok.value][1]+1


for key in table:
	print(key + ','+ str(table[key][0]) + ',' + str(table[key][1]))
