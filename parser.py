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
	'''title: T COL LINE'''
	p[0] = p[1] + p[2] + p[3]

def p_chapter(p):
	'''chapter: C DECIMAL COL LINE'''
	p[0] = p[1] + p[2] + p[3] + p[4]

def p_section(p):
	''' section: S DECIMAL COL LINE'''
	p[0] = p[1] + p[2] + p[3] + [4]


def p_WORD(p):
	''' WORD: ALPHABET 
		| DECIMAL 
		| FLOAT
	'''
	p[0] = p[1]


#Grammer Rules
def p_DOCUMENT(p):
	''' DOCUMENT: title CHAPTER'''
	p[0] = p[1] + p[2]

def p_CHAPTER(p):
	''' CHAPTER: chapter SECTION chapter
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
	''' SECTION: section BODY SECTION
				| section BODY
	'''
	if(len(p)==3):
		p[0] = p[1] + p[2]
	else:
	    p[0] = p[1] + p[2] + p[3]

def p_BODY(p):
	''' BODY: PARAGRAPH NEWLINE BODY
			| PARAGRAPH NEWLINE
	'''
	if(len(p)==3):
		p[0] = p[1] + p[2]
	else:
		p[0] = p[1] + p[2] + p[3]


def p_PARAGRAPH(p):
	''' PARAGRAPH: LINE LINESEP PARAGRAPH
				| LINE LINESEP
	'''
	if(len(p)==3):
		p[0] = p[1] + p[2]
	else:	
		p[0] = p[1] + p[2] + p[3]


def p_LINE(p):
	''' LINE: WORD WORDSEP LINE
			| WORD
	'''
	if(len(p)==2):
		p[0] = p[1]
	else:	
	    p[0] = p[1] + p[2] + p[3]

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
