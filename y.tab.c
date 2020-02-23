/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.0.4"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* Copy the first part of user declarations.  */
#line 1 "parse.yacc" /* yacc.c:339  */

#include <bits/stdc++.h>


#line 71 "y.tab.c" /* yacc.c:339  */

# ifndef YY_NULLPTR
#  if defined __cplusplus && 201103L <= __cplusplus
#   define YY_NULLPTR nullptr
#  else
#   define YY_NULLPTR 0
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif


/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    abstract = 258,
    continue = 259,
    for = 260,
    new = 261,
    switch = 262,
    assert = 263,
    default = 264,
    if = 265,
    package = 266,
    synchronized = 267,
    boolean = 268,
    do = 269,
    goto = 270,
    private = 271,
    this = 272,
    break = 273,
    double = 274,
    implements = 275,
    protected = 276,
    throw = 277,
    byte = 278,
    else = 279,
    import = 280,
    public = 281,
    throws = 282,
    case = 283,
    enum = 284,
    instanceof = 285,
    return = 286,
    transient = 287,
    catch = 288,
    extends = 289,
    int = 290,
    short = 291,
    try = 292,
    char = 293,
    final = 294,
    interface = 295,
    static = 296,
    void = 297,
    class = 298,
    finally = 299,
    long = 300,
    strictfp = 301,
    volatile = 302,
    const = 303,
    float = 304,
    native = 305,
    super = 306,
    while = 307,
    IDENTIFIER = 308,
    IntegerLiteral = 309,
    BooleanLiteral = 310,
    CharacterLiteral = 311,
    StringLiteral = 312,
    NullLiteral = 313,
    FloatingPointLiteral = 314
  };
#endif
/* Tokens.  */
#define abstract 258
#define continue 259
#define for 260
#define new 261
#define switch 262
#define assert 263
#define default 264
#define if 265
#define package 266
#define synchronized 267
#define boolean 268
#define do 269
#define goto 270
#define private 271
#define this 272
#define break 273
#define double 274
#define implements 275
#define protected 276
#define throw 277
#define byte 278
#define else 279
#define import 280
#define public 281
#define throws 282
#define case 283
#define enum 284
#define instanceof 285
#define return 286
#define transient 287
#define catch 288
#define extends 289
#define int 290
#define short 291
#define try 292
#define char 293
#define final 294
#define interface 295
#define static 296
#define void 297
#define class 298
#define finally 299
#define long 300
#define strictfp 301
#define volatile 302
#define const 303
#define float 304
#define native 305
#define super 306
#define while 307
#define IDENTIFIER 308
#define IntegerLiteral 309
#define BooleanLiteral 310
#define CharacterLiteral 311
#define StringLiteral 312
#define NullLiteral 313
#define FloatingPointLiteral 314

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);



/* Copy the second part of user declarations.  */

#line 237 "y.tab.c" /* yacc.c:358  */

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE
# if (defined __GNUC__                                               \
      && (2 < __GNUC__ || (__GNUC__ == 2 && 96 <= __GNUC_MINOR__)))  \
     || defined __SUNPRO_C && 0x5110 <= __SUNPRO_C
#  define YY_ATTRIBUTE(Spec) __attribute__(Spec)
# else
#  define YY_ATTRIBUTE(Spec) /* empty */
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# define YY_ATTRIBUTE_PURE   YY_ATTRIBUTE ((__pure__))
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# define YY_ATTRIBUTE_UNUSED YY_ATTRIBUTE ((__unused__))
#endif

#if !defined _Noreturn \
     && (!defined __STDC_VERSION__ || __STDC_VERSION__ < 201112)
# if defined _MSC_VER && 1200 <= _MSC_VER
#  define _Noreturn __declspec (noreturn)
# else
#  define _Noreturn YY_ATTRIBUTE ((__noreturn__))
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN \
    _Pragma ("GCC diagnostic push") \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")\
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif


#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYSIZE_T yynewbytes;                                            \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / sizeof (*yyptr);                          \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, (Count) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYSIZE_T yyi;                         \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  16
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   1638

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  108
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  184
/* YYNRULES -- Number of rules.  */
#define YYNRULES  400
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  589

/* YYTRANSLATE[YYX] -- Symbol number corresponding to YYX as returned
   by yylex, with out-of-bounds checking.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   339

#define YYTRANSLATE(YYX)                                                \
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, without out-of-bounds checking.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   103,     2,     2,     2,   100,    68,     2,
      69,    70,    63,    97,    60,    98,    61,    99,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,    74,    62,
      65,    71,    66,    67,    64,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,    89,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,    72,    75,    73,   104,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    76,    77,    78,    79,    80,
      81,    82,    83,    84,    85,    86,    87,    88,    90,    91,
      92,    93,    94,    95,    96,   101,   102,   105,   106,   107
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,    67,    67,    69,    72,    75,    77,    80,    83,    90,
      92,    95,    97,   100,   102,   105,   107,   110,   112,   115,
     117,   120,   122,   125,   127,   130,   132,   135,   137,   140,
     142,   145,   148,   151,   153,   156,   161,   163,   166,   172,
     175,   182,   184,   187,   189,   192,   194,   197,   199,   202,
     204,   207,   209,   211,   213,   215,   217,   219,   221,   223,
     226,   229,   231,   238,   240,   243,   245,   247,   249,   252,
     254,   257,   260,   263,   265,   268,   270,   273,   276,   279,
     286,   288,   291,   293,   296,   298,   301,   303,   306,   308,
     311,   313,   316,   318,   320,   322,   324,   326,   328,   330,
     332,   334,   336,   338,   341,   344,   347,   349,   352,   355,
     358,   360,   362,   365,   368,   375,   377,   380,   383,   385,
     388,   390,   393,   396,   398,   401,   403,   405,   407,   412,
     414,   416,   418,   420,   434,   437,   440,   443,   446,   448,
     455,   457,   460,   463,   465,   468,   470,   473,   475,   477,
     479,   481,   484,   487,   489,   492,   495,   498,   501,   504,
     507,   514,   516,   519,   521,   524,   526,   529,   531,   534,
     537,   540,   542,   545,   547,   550,   553,   556,   559,   562,
     564,   567,   573,   575,   578,   580,   583,   585,   588,   590,
     593,   595,   598,   600,   603,   605,   608,   610,   613,   615,
     618,   620,   623,   625,   627,   630,   633,   635,   637,   639,
     641,   643,   645,   647,   649,   651,   653,   655,   657,   659,
     661,   663,   665,   667,   670,   677,   679,   683,   685,   688,
     690,   693,   696,   699,   702,   705,   707,   710,   713,   720,
     722,   725,   727,   730,   732,   735,   738,   740,   743,   745,
     747,   750,   753,   755,   758,   761,   763,   766,   769,   771,
     778,   780,   783,   785,   788,   790,   793,   796,   799,   802,
     804,   806,   808,   811,   814,   816,   818,   820,   822,   824,
     830,   832,   835,   837,   837,   840,   843,   845,   848,   850,
     852,   855,   858,   860,   862,   864,   866,   868,   870,   872,
     874,   876,   878,   880,   883,   886,   893,   895,   898,   900,
     903,   905,   907,   909,   911,   913,   915,   917,   919,   921,
     923,   925,   927,   929,   931,   933,   935,   937,   939,   941,
     944,   946,   948,   950,   953,   955,   957,   959,   961,   963,
     966,   968,   975,   977,   980,   982,   985,   988,   990,   992,
     995,   997,  1000,  1002,  1005,  1007,  1009,  1011,  1013,  1015,
    1017,  1019,  1021,  1023,  1026,  1028,  1030,  1032,  1034,  1036,
    1039,  1042,  1045,  1047,  1050,  1052,  1059,  1061,  1064,  1066,
    1069,  1071,  1074,  1077,  1079,  1081,  1085,  1088,  1090,  1093,
    1095,  1103,  1105,  1113,  1115,  1118,  1120,  1123,  1125,  1142,
    1144
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "abstract", "continue", "for", "new",
  "switch", "assert", "default", "if", "package", "synchronized",
  "boolean", "do", "goto", "private", "this", "break", "double",
  "implements", "protected", "throw", "byte", "else", "import", "public",
  "throws", "case", "enum", "instanceof", "return", "transient", "catch",
  "extends", "int", "short", "try", "char", "final", "interface", "static",
  "void", "class", "finally", "long", "strictfp", "volatile", "const",
  "float", "native", "super", "while", "IDENTIFIER", "IntegerLiteral",
  "BooleanLiteral", "CharacterLiteral", "StringLiteral", "NullLiteral",
  "FloatingPointLiteral", "','", "'.'", "';'", "'*'", "'@'", "'<'", "'>'",
  "'?'", "'&'", "'('", "')'", "'='", "'{'", "'}'", "':'", "'|'", "\"+=\"",
  "\"-=\"", "\"*=\"", "\"/=\"", "\"&=\"", "\"|=\"", "\"^=\"", "\"%=\"",
  "\"<<=\"", "\">>=\"", "\">>>=\"", "\"||\"", "\"&&\"", "'^'", "\"==\"",
  "\"!=\"", "\"<=\"", "\">=\"", "\"<<\"", "\">>\"", "\">>>\"", "'+'",
  "'-'", "'/'", "'%'", "\"++\"", "\"--\"", "'!'", "'~'", "\"[]\"", "\";\"",
  "\"[[]]\"", "$accept", "QualifiedIdentifierListStar", "Identifier",
  "DotIdentifierStar", "QualifiedIdentifier", "QualifiedIdentifierList",
  "PackageOptional", "ImportDeclarationStar", "TypeDeclarations",
  "DotStarOptional", "ModifierStar", "TypeParametersOptional",
  "ExtendsTypeOptional", "ImplmentsTypeOptional",
  "ExtendsTypeListOptional", "CompilationUnit", "ImportDeclaration",
  "TypeDeclaration", "ClassOrInterfaceDeclaration", "ClassDeclaration",
  "InterfaceDeclaraton", "NormalClassDeclaration",
  "NormalInterfaceDeclaration", "AnnotationTypeDeclaration",
  "TypeArgumentsOptional", "IdentifierTypeArgumentStar",
  "TypeArgumentListStar", "ExtendSuperOptional", "Type", "BasicType",
  "ReferenceType", "TypeArguments", "TypeArgument",
  "ReferenceTypeListStar", "TypeParametersListStar",
  "ExtendsBoundOptional", "AndReferenceTypeStar",
  "NonWildcardTypeArguments", "TypeList", "TypeArgumentsOrDiamond",
  "NonWildcardTypeArgumentsOrDiamond", "TypeParameters", "TypeParameter",
  "Bound", "AnnotationStar", "AnnotationElementOptional",
  "AnnotationElement2Optional", "ElementValuePairListStar",
  "ElementValuesOptional", "ElementValueListStar", "Modifier",
  "Annotations", "Annotation", "AnnotationElement", "ElementValuePairs",
  "ElementValuePair", "ElementValue", "ElementValueArrayInitializer",
  "ElementValues", "ThrowsQualifiedOptional", "BlockOrSemicolon",
  "TypeOrVoid", "ClassBody", "VariableDeclaratorListStar",
  "ClassBodyDeclaration", "MemberDecl", "MethodDeclaratorRest",
  "VoidMethodDeclaratorRest", "ConstructorDeclaratorRest",
  "GenericMethodOrConstructorDecl", "GenericMethodOrConstructorRest",
  "InterfaceBodyDeclarationStar", "InterfaceBody",
  "ConstantDeclaratorListStar", "InterfaceBodyDeclaraton",
  "InterfaceMemberDecl", "InterfaceMethodOrFieldDecl",
  "InterfaceMethodOrFieldRest", "ConstantDeclaratorsRest",
  "ConstantDeclaratorRest", "ConstantDeclarator",
  "InterfaceMethodDeclaratorRest", "VoidInterfaceMethodDeclaratorRest",
  "InterfaceGenericMethodDecl", "FormalParameterDeclsOptional",
  "VariableModifierStar", "FormalParameterDeclsListOptional",
  "EqualVariableInitializerOptional", "FormalParameters",
  "FormalParameterDecls", "VariableModifier", "FormalParameterDeclsRest",
  "VariableDeclaratorId", "VariableDeclarators", "VariableDeclarator",
  "VariableDeclaratorRest", "VariableInitializer", "ArrayInitializer",
  "IdentifierColonOptional", "ElseStatementOptional",
  "ColonExpressionOptional", "SwitchBlockStatementGroupsStar",
  "IdentifierOptional", "ExpressionOptional", "CatchesOptional",
  "FinallyOptional", "Block", "BlockStatements", "BlockStatement",
  "LocalVariableDeclarationStatement", "Statement", "StatementExpression",
  "OrQualifiedIdentifierStar", "CatchClauseStar", "SemiResourceStar",
  "Catches", "CatchClause", "CatchType", "Finally",
  "ResourceSpecification", "Resources", "Resource", "CommaStatementStar",
  "ForUpdateOptional", "SwitchBlockStatementGroups",
  "SwitchBlockStatementGroup", "SwitchLabels", "SwitchLabel",
  "EnumConstantName", "ForControl", "ForVarControl", "ForVarCOntrolRest",
  "ForVariableDeclaratorsRest", "ForInit", "ForUpdate",
  "TypeArgumentsOrDiamondOptional",
  "DotIdentifierTypeArgumentsOrDiamondOptionalStar", "Creator",
  "CreatedName", "ClassCreatorRest", "ExplicitGenericInvocation",
  "NonWildcardTypeArgumentsOptional",
  "NonWildcardTypeArgumentsOrDiamondOptional", "InnerCreator", "Selector",
  "AssignmentOptional", "Expression1Rest", "Expression", "InfixOpOne",
  "InfixOpStar", "Expression2Rest", "AssignmentOperator", "Expression1",
  "Expression2", "Selectors", "PostfixOps", "Infixop", "Expression3",
  "PrefixOp", "PostfixOp", "ArgumentsOptional", "IdentifierSuffixOptional",
  "IdentifierSuffix", "SquareBraceStar", "ExpressionListStar",
  "ArgumentsExpressionOptional", "Primary", "Literal", "ParExpression",
  "Arguments", "SuperSuffix", "ExplicitGenericInvocationSuffix",
  "AnnotationTypeElementDeclarationsOptionalStar",
  "AnnotationTypeElementDeclarationsOptional",
  "AnnotationTypeElementDeclarations", "AnnotationTypeElementDeclaration",
  "AnnotationTypeElementRest", "AnnotationMethodOrConstantRest",
  "AnnotationMethodRest", "CommaOptional", "AnnotationsOptional",
  "ClassBodyOptional", "ClassBodyDeclarationStar", "AnnotationTypeBody", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   303,   304,
     305,   306,   307,   308,   309,   310,   311,   312,   313,   314,
      44,    46,    59,    42,    64,    60,    62,    63,    38,    40,
      41,    61,   123,   125,    58,   124,   315,   316,   317,   318,
     319,   320,   321,   322,   323,   324,   325,   326,   327,    94,
     328,   329,   330,   331,   332,   333,   334,    43,    45,    47,
      37,   335,   336,    33,   126,   337,   338,   339
};
# endif

#define YYPACT_NINF -435

#define yypact_value_is_default(Yystate) \
  (!!((Yystate) == (-435)))

#define YYTABLE_NINF -394

#define yytable_value_is_error(Yytable_value) \
  0

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const yytype_int16 yypact[] =
{
      37,   -21,    -7,    73,  -435,    99,  -435,  -435,  -435,   122,
      -7,  -435,  -435,   112,  -435,   215,  -435,   167,    -7,  -435,
     178,   647,  -435,   233,  1493,  -435,  -435,  -435,   181,   185,
      -7,   135,  -435,   180,  -435,  -435,  -435,  -435,  -435,   189,
    -435,  -435,   137,  -435,  -435,  -435,  -435,  -435,  -435,    -7,
    1137,  -435,  -435,  -435,  -435,  -435,  -435,    97,   180,  1137,
     147,   147,   152,   184,   195,  -435,  -435,  -435,  -435,  -435,
    -435,  -435,  1137,  1140,   190,   226,  1137,  -435,  -435,  -435,
    -435,  -435,  -435,  -435,  -435,  -435,  -435,    -7,  -435,    -7,
    -435,  -435,  -435,   119,  -435,  -435,  -435,  -435,  -435,  -435,
    -435,  -435,    64,   199,  -435,   198,    -7,  -435,   180,  1137,
    -435,  -435,   222,    -7,  -435,  -435,   202,  -435,   203,   -44,
     717,  1552,    62,   787,  -435,  -435,  -435,  -435,  -435,    -3,
    -435,   207,  -435,   180,   137,   180,  -435,  -435,  -435,  -435,
     211,   212,    19,  -435,  -435,  -435,  -435,  -435,  -435,  -435,
    -435,  -435,  -435,  -435,  -435,  -435,  1137,  -435,  -435,  1546,
    1522,  -435,    91,   857,   210,   210,    -7,  -435,  -435,   156,
    -435,  -435,  -435,   180,  -435,   204,  1137,   209,  -435,   180,
     217,  -435,  -435,    17,  -435,  -435,  -435,   219,   238,  -435,
    -435,  -435,    -7,   787,  1182,  -435,   147,  -435,  -435,  -435,
    -435,  -435,  -435,  -435,  -435,  -435,  -435,  -435,  -435,  -435,
    -435,  -435,  -435,  -435,  -435,  -435,  -435,  1137,   124,  -435,
    -435,  1137,   128,    -7,   252,  -435,   254,  -435,  -435,   228,
    -435,  -435,  -435,  -435,   230,  -435,  -435,    -7,    -7,    -7,
    -435,   144,    -7,  -435,   220,  -435,  -435,  -435,   226,   227,
    -435,   137,   180,   103,  -435,  -435,  -435,  -435,   259,  -435,
      -7,   224,  1546,   274,  1376,  -435,    -7,   397,  1137,  -435,
    -435,  -435,    62,  -435,   202,  -435,    -7,  -435,  -435,  -435,
      -7,  -435,   172,  -435,  -435,  -435,  -435,    -7,   204,  1415,
    -435,  1376,  -435,   198,  -435,  -435,  -435,  1322,  -435,  -435,
    1137,  -435,  -435,   234,  -435,  -435,  -435,    -7,  -435,   -18,
    -435,  -435,  -435,  -435,  -435,    -7,  -435,  -435,  -435,  -435,
      -7,   231,  -435,  -435,   518,  -435,  -435,  1454,   113,  -435,
    -435,   180,   235,  -435,  -435,  -435,  1277,  -435,     5,   231,
     236,  -435,   280,  -435,   159,  -435,    -7,  -435,   240,  -435,
    1525,   577,  -435,  -435,  -435,  -435,    -7,    -7,  -435,  -435,
      -7,   518,  -435,  -435,  -435,   239,  -435,  -435,   237,   213,
    -435,  -435,   280,   245,  1525,  -435,    -7,  -435,  -435,   231,
    -435,  -435,    -7,  -435,  -435,    -7,   232,   247,  1137,   247,
     247,   577,    -7,  1137,  1137,   248,   247,  -435,   -22,  -435,
    -435,   258,  1137,  -435,   231,     9,    -7,   214,   263,  1137,
    -435,   262,  -435,   164,  -435,  -435,  -435,  -435,   147,   147,
     265,  -435,  -435,   266,   267,  -435,   927,   577,  -435,   278,
     269,   997,   270,  -435,   130,  -435,   577,   577,  -435,  -435,
     280,  -435,   271,  -435,   147,   231,   326,    -7,  -435,  -435,
    1137,  -435,  -435,  -435,   276,   147,  -435,   279,   281,   280,
    -435,   272,  -435,   285,  -435,  1525,   268,  -435,   284,  -435,
    1137,   288,   316,  -435,   247,  -435,  -435,  -435,    49,   157,
     290,   287,   303,   309,  -435,   324,  -435,  -435,   298,  -435,
     280,  -435,   787,   147,  -435,   300,  -435,  -435,  -435,    -7,
     262,  1137,  -435,    -7,    -7,   577,  1137,    47,  1137,  -435,
     577,  -435,   301,    -7,   292,  -435,  -435,  -435,  -435,  -435,
    -435,   324,   303,  -435,  -435,   302,  -435,  -435,    -7,  -435,
    -435,  -435,  -435,  -435,   174,  -435,   304,   293,  1137,  -435,
    -435,    47,  -435,  -435,   306,  -435,  -435,    49,  -435,  -435,
    -435,  -435,  -435,  -435,  1137,  -435,  -435,   319,  1137,  -435,
     -44,   308,  1067,  1454,  -435,  1137,  -435,    -7,  1137,   285,
    1137,  -435,  -435,  -435,  -435,  -435,  1137,   310,   314,   325,
     331,    -7,  -435,  1137,  1137,  -435,  -435,  -435,  -435
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       9,     0,     0,    11,    13,     0,    12,   394,    80,     0,
       0,     4,     5,    82,    13,    19,     1,   104,     0,     5,
       7,    84,   105,    19,     0,    14,    32,    81,     0,    17,
       0,     0,    58,   342,    57,    51,    54,    52,    53,     0,
      55,    56,     0,   364,   368,   366,   367,   369,   365,     0,
       0,   338,   339,   334,   335,   336,   337,     5,   344,     0,
     347,   347,     0,     0,   391,   110,    85,   106,    86,    90,
     112,    89,     0,   280,   282,   286,     0,   306,   354,   355,
      97,   100,    95,    94,    93,   101,    98,     0,    96,     0,
     103,   102,    99,     0,    33,    34,    35,    36,    37,    20,
      92,    10,     0,     0,     6,   260,     0,   358,     0,   352,
     356,   343,     0,     0,   372,   357,    41,    63,     0,     5,
       0,   280,     0,    88,    43,    42,   361,   345,   346,   286,
     349,    49,    50,     0,     0,     0,   359,    83,   392,   113,
     108,   114,   286,   292,   293,   294,   295,   296,   297,   298,
     299,   300,   301,   302,   303,   291,     0,   283,   304,     0,
     289,   305,   286,   192,    21,    21,     0,    18,    31,     0,
      74,   261,   262,     0,   265,   395,   350,     0,   363,   342,
      72,    71,   370,     0,    61,    45,    90,    59,     0,   360,
     374,   375,     0,    88,   280,   290,   347,   327,   318,   319,
     314,   312,   310,   311,   313,   316,   317,   320,   321,   322,
     323,   324,   325,   326,   328,   329,   287,     0,     0,   279,
     307,   193,   333,     0,    27,    22,    23,   376,    73,   266,
     264,   397,   396,   267,   353,   371,   373,     0,     0,     0,
      62,     0,     0,   362,     0,    87,    90,    49,   285,   269,
     276,     0,   342,     0,   275,   340,   341,   309,    67,    65,
       0,     0,     0,    25,   378,    40,     0,   198,     0,    64,
      47,    48,     0,    60,    41,   270,     0,   277,   274,   268,
       0,    78,     0,    28,   140,    39,    24,     0,     0,     0,
     377,   379,   380,   260,   198,   125,   122,     0,   398,   128,
     351,    46,    44,   271,   278,    69,    68,     0,    77,    19,
      26,    38,   384,   385,    37,     0,   382,   381,   263,   127,
       0,     0,   132,   133,     0,   126,   131,   182,     0,    76,
     272,     0,    79,    66,   145,   142,     0,   141,   347,     0,
     163,   130,     0,   121,    41,   120,     0,   137,     0,   203,
       0,   198,   201,   202,    75,   273,     0,     0,   150,   151,
       0,     0,   146,   147,   149,     0,   388,   143,     0,     0,
     387,   129,     0,     0,     0,   162,     0,   198,   139,     0,
     183,   171,     0,   172,   164,   190,     0,     0,     0,     0,
       0,   198,   190,     0,   192,   198,     0,   207,     5,   200,
     204,     0,   224,    70,     0,   347,     0,     0,   155,   181,
     383,   198,   169,     0,     2,   117,   136,   138,   347,   347,
       0,   123,   191,     0,   163,   188,   186,   198,   198,     0,
       0,     0,     0,   163,   200,   198,   198,   198,   209,   148,
       0,   152,     0,   154,   347,     0,   390,     0,   156,   179,
     180,   119,   135,   118,     0,   347,   170,   165,     8,     0,
     177,   167,   205,   176,   217,     0,     0,   252,     0,   212,
       0,     0,   184,   200,     0,   216,   219,   218,     0,     0,
     229,     0,     0,   221,   227,   194,   213,   208,     0,   153,
       0,   160,    88,   347,   144,     0,   175,   163,   173,     0,
     198,   181,   178,     0,     0,   198,   192,   189,   187,   211,
     198,   210,     0,     0,     0,   236,   163,   237,   163,   198,
     222,   231,   196,   195,   159,     0,    90,   157,     0,   166,
       3,   134,   168,   124,   167,   215,     0,     0,     0,   244,
     200,   246,   185,   214,     0,   235,   230,     0,   200,   228,
     223,   197,   158,   174,     0,   123,   254,     0,   241,   250,
       5,     0,     0,   182,   247,     0,   225,     0,   256,   257,
     192,   239,   253,   242,   249,   248,   238,   233,     0,     0,
     259,     0,   198,   241,     0,   226,   200,   255,   240
};

  /* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -435,  -435,    -2,   367,    -1,  -435,  -435,   390,   382,  -435,
    -136,   242,  -435,  -435,  -435,  -435,  -435,  -435,  -321,  -252,
    -224,  -435,  -435,   109,   125,  -435,  -435,  -435,  -154,   -77,
     -46,   -98,   129,  -435,  -435,  -435,  -435,    -5,  -246,  -435,
    -435,  -231,    95,  -435,  -435,  -435,  -435,  -435,  -435,  -435,
    -435,  -435,    15,  -435,  -435,   216,  -121,  -435,  -435,  -350,
     -97,    44,   126,  -145,  -435,  -435,  -435,  -435,    71,  -435,
    -435,  -435,  -435,  -435,  -435,  -435,  -435,  -435,    12,   -74,
    -435,   -25,  -435,  -435,  -435,  -317,  -435,  -110,  -309,   -71,
    -435,  -435,  -370,  -435,   -76,  -435,   -73,  -435,  -435,  -435,
    -435,  -435,    38,  -384,   -54,  -435,  -217,  -107,  -435,  -435,
    -373,  -434,  -435,  -435,  -435,   -43,   -80,  -435,   -70,  -435,
    -435,   -68,  -435,  -137,  -435,  -435,   -92,  -435,  -435,  -435,
    -435,  -435,  -435,  -435,  -435,   158,  -435,  -435,   347,  -160,
    -435,  -435,  -435,  -435,  -435,  -435,  -435,   -15,  -435,  -435,
    -435,  -435,   -17,  -435,  -435,  -435,  -435,   -34,  -435,  -435,
    -155,  -435,  -435,   -49,  -435,  -435,  -435,  -435,  -356,    11,
    -125,   201,  -435,  -435,  -435,   165,  -435,  -435,  -435,  -435,
    -435,  -435,  -435,  -435
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,   458,   119,    20,    58,   415,     3,     4,    15,   103,
      24,   224,   263,   288,   261,     5,     6,    25,    26,    94,
      95,    96,    97,    98,   124,   187,   241,   240,    59,    60,
      61,   125,   185,   180,   282,   281,   332,    62,   118,   171,
     330,   225,   259,   306,    17,    22,    63,   140,    64,   141,
      99,     7,   383,    66,    67,    68,    69,    70,    71,   377,
     452,   346,   232,   463,   298,   325,   417,   371,   341,   326,
     347,   309,   285,   408,   337,   362,   363,   441,   366,   367,
     494,   443,   439,   364,   373,   350,   498,   502,   342,   375,
     384,   456,   457,   420,   421,   460,   448,   449,   351,   511,
     471,   469,   423,   219,   482,   550,   399,   327,   352,   353,
     400,   401,   577,   521,   517,   483,   484,   567,   520,   435,
     479,   480,   580,   572,   507,   539,   540,   541,   561,   466,
     467,   556,   557,   468,   573,   172,   229,   107,   108,   174,
     254,   276,   331,   304,   220,   155,   158,    72,   216,   160,
     161,   156,   121,    74,   163,   222,   217,    75,    76,   257,
     110,   126,   127,   368,   234,   177,    77,    78,    79,   111,
     115,   136,   264,   290,   291,   292,   316,   369,   370,   139,
       9,   233,   267,   265
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
      12,    13,   186,   117,    73,   195,   349,   170,    19,   190,
     432,   131,   132,   230,   283,     8,    12,    28,   429,    57,
      10,   122,   411,   374,   236,   129,   106,   159,   104,   105,
     372,   425,    27,   427,   428,   120,    65,   312,   142,   100,
     436,   310,   162,   122,   334,   322,    11,   116,  -393,   159,
     299,   238,   437,   114,   472,   335,   537,  -332,  -332,  -332,
     135,   -41,     1,   486,   487,   313,   324,  -332,   239,   128,
     418,  -332,   246,   323,   365,   538,   184,   319,   340,  -331,
    -331,  -331,   196,   -41,   358,   164,   142,   165,   381,  -331,
     488,    12,    13,  -331,   176,   440,   444,   278,     1,    16,
     104,     2,    11,  -332,   105,   361,    73,   465,   286,   500,
     130,   179,   359,     2,   130,    11,   478,    11,   512,   175,
     116,   159,   536,   184,   571,  -331,   277,   167,   289,   183,
     249,   297,   535,    18,   534,   315,   444,   542,    65,   194,
     525,   250,   142,   544,   189,   114,   191,   247,   221,   571,
     588,  -330,  -330,  -330,   134,   289,    11,   116,   553,   166,
     416,  -330,   122,   481,   227,  -330,    11,   116,   123,   133,
     345,   355,    11,   336,  -194,   251,    73,    11,   434,   354,
     374,    21,   360,   248,   175,   196,   579,   142,    11,    49,
     244,   269,   270,   271,   453,   170,   382,  -330,   113,   478,
      49,   547,   -41,   134,   272,    11,   109,   345,    65,    11,
     273,   473,   196,   253,   117,   -30,   252,    11,   485,   514,
     413,   258,   228,   183,   122,   454,   184,   515,   340,   255,
     256,     2,   307,   -29,   305,   116,   116,   116,   308,    30,
     274,   117,   349,   101,   275,   501,   102,   196,   554,   109,
     112,   135,   130,   300,   137,   138,   159,   157,   116,   196,
     116,   168,   114,   169,   293,   178,   142,   122,   188,   181,
     116,   192,   193,   196,   303,   223,   231,   237,   116,   235,
     242,   243,   117,   453,   196,   116,   260,   116,   262,   266,
     268,   123,    49,   280,   287,   321,   284,   196,   329,   328,
     340,   424,   548,   356,   100,   258,  -161,   376,   409,   407,
     403,   504,   100,   338,   380,   412,    50,   433,   339,   410,
     438,   446,   344,   447,   451,   348,   116,   462,   464,  -258,
     474,   475,   477,   489,   116,   492,   402,   495,   505,   497,
     510,   499,   175,   501,   379,   503,   506,   519,   116,   398,
     509,   100,   516,  -195,   116,   404,   518,   481,   405,   116,
     524,   528,   545,   543,   552,   586,   558,   559,   142,   459,
     461,   526,   116,   426,    12,   414,   402,   565,   431,   221,
     419,   570,   574,   422,   582,   581,    29,   583,   196,   398,
     422,   584,   142,    14,   450,   490,    23,   142,   314,   302,
     -19,   301,   333,   531,   445,   406,   496,   226,   245,   -19,
     569,   455,   402,   -19,   311,   378,   142,   442,   -19,   527,
     491,   402,   402,   -19,   555,   398,   529,   533,   532,   -19,
     430,   522,   513,   563,   398,   398,   -19,   -19,   294,   -19,
     -19,   549,   523,   -19,   -19,   493,   587,   -19,   546,   564,
     -19,   318,   551,   173,   279,   508,   317,     0,     0,   295,
       0,   -19,   -19,   116,     0,     0,     0,     0,     0,     0,
     296,     0,     0,     0,   142,    73,   116,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   450,     0,     0,     0,
     402,   221,     0,     0,     0,   402,     0,    12,   530,     0,
       0,   419,   455,   398,     0,     0,     0,    65,   398,     0,
       0,   455,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   562,     0,     0,   455,     0,   142,     0,
       0,    32,     0,     0,   142,     0,   560,    34,     0,   568,
       0,    35,   142,   402,     0,    12,   566,     0,     0,     0,
     576,     0,     0,    36,    37,   221,    38,     0,     0,     0,
     343,   348,     0,    40,     0,   578,     0,    41,   402,   402,
       0,    11,     0,     0,     0,     0,     0,     0,     0,    12,
     585,   385,   386,    31,   387,   388,     0,   389,     0,   390,
      32,   391,     0,     0,    33,   392,    34,     0,     0,   393,
      35,     0,     0,     0,     0,     0,     0,     0,   394,     0,
       0,     0,    36,    37,   395,    38,     0,     0,     0,    39,
       0,     0,    40,     0,     0,     0,    41,     0,    42,   396,
      11,    43,    44,    45,    46,    47,    48,     0,     0,   397,
       0,     0,    49,     0,     0,     0,    50,     0,     0,     0,
       0,     0,     0,    31,     0,     0,     0,     0,     0,     0,
      32,     0,     0,     0,    33,     0,    34,     0,     0,     0,
      35,     0,     0,     0,    51,    52,     0,     0,    53,    54,
      55,    56,    36,    37,     0,    38,     0,     0,     0,    39,
       0,     0,    40,     0,     0,     0,    41,     0,    42,     0,
      11,    43,    44,    45,    46,    47,    48,   -88,     0,     0,
       0,     2,    49,     0,     0,     0,    50,     0,     0,     0,
       0,     0,     0,    31,     0,     0,     0,     0,     0,     0,
      32,     0,     0,     0,    33,     0,    34,     0,     0,     0,
      35,     0,     0,     0,    51,    52,     0,     0,    53,    54,
      55,    56,    36,    37,     0,    38,     0,     0,     0,    39,
       0,     0,    40,     0,     0,     0,    41,     0,    42,     0,
      11,    43,    44,    45,    46,    47,    48,     0,     0,     0,
       0,     0,    49,     0,     0,     0,    50,   182,     0,     0,
       0,     0,     0,    31,     0,     0,     0,     0,     0,     0,
      32,     0,     0,     0,    33,     0,    34,     0,     0,     0,
      35,     0,     0,     0,    51,    52,     0,     0,    53,    54,
      55,    56,    36,    37,     0,    38,     0,     0,     0,    39,
       0,     0,    40,     0,     0,     0,    41,     0,    42,     0,
      11,    43,    44,    45,    46,    47,    48,     0,     0,     0,
       0,     2,    49,     0,     0,     0,    50,     0,     0,     0,
       0,     0,     0,    31,     0,     0,     0,     0,     0,     0,
      32,     0,     0,     0,    33,     0,    34,     0,     0,     0,
      35,     0,     0,     0,    51,    52,     0,     0,    53,    54,
      55,    56,    36,    37,     0,    38,     0,     0,     0,    39,
       0,     0,    40,     0,     0,     0,    41,     0,    42,     0,
      11,    43,    44,    45,    46,    47,    48,     0,   218,     0,
       0,     0,    49,     0,     0,     0,    50,     0,     0,     0,
       0,     0,     0,    31,     0,     0,     0,     0,     0,     0,
      32,     0,     0,     0,    33,     0,    34,     0,     0,     0,
      35,     0,     0,     0,    51,    52,     0,     0,    53,    54,
      55,    56,    36,    37,     0,    38,     0,     0,     0,    39,
       0,     0,    40,     0,     0,     0,    41,     0,    42,     0,
      11,    43,    44,    45,    46,    47,    48,     0,     0,     0,
       0,     0,    49,     0,     0,     0,    50,     0,     0,     0,
       0,   470,     0,    31,     0,     0,     0,     0,     0,     0,
      32,     0,     0,     0,    33,     0,    34,     0,     0,     0,
      35,     0,     0,     0,    51,    52,     0,     0,    53,    54,
      55,    56,    36,    37,     0,    38,     0,     0,     0,    39,
       0,     0,    40,     0,     0,     0,    41,     0,    42,     0,
      11,    43,    44,    45,    46,    47,    48,     0,     0,   476,
       0,     0,    49,     0,     0,     0,    50,     0,     0,     0,
       0,     0,     0,    31,     0,     0,     0,     0,     0,     0,
      32,     0,     0,     0,    33,     0,    34,     0,     0,     0,
      35,     0,     0,     0,    51,    52,     0,     0,    53,    54,
      55,    56,    36,    37,     0,    38,     0,     0,     0,    39,
       0,     0,    40,     0,     0,     0,    41,     0,    42,     0,
      11,    43,    44,    45,    46,    47,    48,     0,     0,     0,
       0,     0,    49,     0,     0,     0,    50,     0,     0,     0,
       0,   575,     0,    31,     0,     0,     0,     0,     0,     0,
      32,     0,     0,     0,    33,     0,    34,     0,     0,     0,
      35,     0,     0,     0,    51,    52,     0,     0,    53,    54,
      55,    56,    36,    37,     0,    38,     0,     0,     0,    39,
       0,     0,    40,     0,     0,     0,    41,     0,    42,     0,
      11,    43,    44,    45,    46,    47,    48,     0,     0,     0,
    -111,     0,    49,     0,     0,     0,    50,     0,     0,     0,
    -111,   143,  -281,     0,     0,     0,   144,   145,   146,   147,
     148,   149,   150,   151,   152,   153,   154,     0,     0,     0,
       0,     0,     0,     0,    51,    52,     0,     0,    53,    54,
      55,    56,  -281,  -281,  -281,  -281,  -111,     0,  -281,  -281,
    -281,     0,  -281,   143,     0,     0,  -281,  -281,   144,   145,
     146,   147,   148,   149,   150,   151,   152,   153,   154,  -281,
    -281,  -281,  -281,  -281,  -281,  -281,  -281,  -281,  -281,     0,
      80,  -281,  -281,     0,     0,     0,     0,     0,  -281,    81,
      32,     0,     0,    82,     0,     0,    34,     0,    83,     0,
      35,     0,     0,    84,     0,     0,     0,     0,     0,    85,
       0,     0,    36,    37,     0,    38,    86,    87,    88,   357,
      89,     0,    40,    90,    91,    80,    41,    92,     0,     0,
      11,     0,     0,     0,    81,     0,     0,     0,    82,     0,
       0,    93,   223,    83,     0,     0,     0,     0,    84,     0,
       0,     0,     0,     0,    85,     0,     0,     0,     0,     0,
       0,    86,    87,    88,   320,    89,     0,     0,    90,    91,
       0,     0,    92,     0,     0,    11,     0,     0,     0,   -19,
       0,     0,     0,     0,     0,     0,    93,   223,   -19,   -19,
       0,     0,   -19,     0,     0,   -19,     0,   -19,     0,   -19,
       0,     0,   -19,     0,     0,     0,     0,     0,   -19,     0,
       0,   -19,   -19,     0,   -19,   -19,   -19,   -19,    80,   -19,
       0,   -19,   -19,   -19,     0,   -19,   -19,    81,    32,   -19,
       0,    82,     0,     0,    34,     0,    83,     0,    35,     0,
     -19,    84,     0,     0,     0,     0,     0,    85,     0,     0,
      36,    37,     0,    38,    86,    87,    88,   -19,    89,     0,
      40,    90,    91,     0,    41,    92,   -19,  -163,    11,     0,
     -19,     0,     0,  -163,     0,   -19,     0,  -163,     0,    93,
     -19,     0,     0,     0,     0,     0,   -19,     0,     0,  -163,
    -163,     0,  -163,   -19,   -19,   -19,    80,   -19,     0,  -163,
     -19,   -19,     0,  -163,   -19,    81,     0,    11,     0,    82,
       0,     0,     0,     0,    83,     0,     0,     0,   -19,    84,
       0,     0,     0,     0,     0,    85,     0,     0,     0,     0,
       0,     0,    86,    87,    88,     0,    89,     0,    32,    90,
      91,     0,     0,    92,    34,     0,     0,     0,    35,     0,
       0,     0,     0,     0,     0,     0,     0,    93,     0,    32,
      36,    37,     0,    38,   381,    34,     0,     0,     0,    35,
      40,     0,     0,     0,    41,     0,     0,     0,    11,     0,
       0,    36,    37,     0,    38,   197,     0,   198,   199,     2,
     200,    40,     0,     0,     0,    41,     0,   201,     0,    11,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   202,
     203,   204,   205,   206,   207,   208,   209,   210,   211,   212,
     213,   214,   215,   143,     0,     0,     0,     0,   144,   145,
     146,   147,   148,   149,   150,   151,   152,   153,   154
};

static const yytype_int16 yycheck[] =
{
       2,     2,   123,    49,    21,   159,   327,   105,    10,   134,
     394,    60,    61,   173,   260,     0,    18,    18,   391,    21,
      41,    65,   372,   340,   179,    59,    31,    30,    30,    31,
     339,   387,    17,   389,   390,    50,    21,   289,    72,    24,
     396,   287,    76,    65,    62,   297,    53,    49,    11,    30,
     267,    34,    74,    42,   427,    73,     9,    60,    61,    62,
      62,   105,    25,   436,   437,   289,   297,    70,    51,    58,
     379,    74,   193,   297,    69,    28,   122,   294,    69,    60,
      61,    62,   159,   105,   336,    87,   120,    89,    39,    70,
     440,    93,    93,    74,   109,   404,   405,   252,    25,     0,
     102,    64,    53,   106,   106,   336,   123,   424,   262,   459,
     105,   113,   336,    64,   105,    53,   433,    53,   474,   108,
     122,    30,   506,   169,   558,   106,   251,    63,   264,    67,
       6,   267,   505,    11,   504,   289,   445,   510,   123,   156,
     490,    17,   176,   513,   133,   134,   135,   196,   163,   583,
     584,    60,    61,    62,    51,   291,    53,   159,   528,    40,
     377,    70,    65,    33,   166,    74,    53,   169,    71,    17,
     324,   331,    53,   309,    44,    51,   193,    53,   395,    66,
     497,    69,   336,   217,   173,   262,   570,   221,    53,    65,
     192,   237,   238,   239,   411,   293,   350,   106,    61,   516,
      65,   518,   105,    51,    60,    53,    69,   361,   193,    53,
      66,   428,   289,   218,   260,     0,   218,    53,   435,    62,
     374,   223,    66,    67,    65,    61,   272,    70,    69,   101,
     102,    64,    60,     0,   280,   237,   238,   239,    66,    61,
     242,   287,   563,    62,   249,    71,    61,   324,    74,    69,
      61,   253,   105,   268,    70,    60,    30,    67,   260,   336,
     262,    62,   251,    65,   266,    43,   300,    65,    61,    66,
     272,    60,    60,   350,   276,    65,    72,    60,   280,    70,
      61,    43,   328,   500,   361,   287,    34,   289,    34,    61,
      60,    71,    65,    34,    20,   297,    72,   374,   303,    65,
      69,    69,   519,    68,   289,   307,    70,    27,    71,    70,
     356,   465,   297,   315,    74,    70,    69,    69,   320,   106,
      62,   107,   324,    60,    62,   327,   328,    62,    62,    62,
      52,    62,    62,    62,   336,     9,   351,    61,    70,    60,
      24,    60,   331,    71,   346,    60,    62,    44,   350,   351,
      62,   336,    62,    44,   356,   357,    69,    33,   360,   361,
      62,    61,    70,    62,    62,   582,    62,    74,   402,   418,
     419,   492,   374,   388,   376,   376,   391,    71,   393,   394,
     382,    62,    74,   385,    70,    75,    19,    62,   465,   391,
     392,    60,   426,     3,   409,   444,    14,   431,   289,   274,
       3,   272,   307,   500,   406,   361,   455,   165,   192,    12,
     555,   413,   427,    16,   288,   344,   450,   405,    21,   493,
     445,   436,   437,    26,   534,   427,   497,   503,   501,    32,
     392,   485,   478,   540,   436,   437,    39,    40,    41,    42,
      43,   521,   485,    46,    47,   447,   583,    50,   516,   541,
      53,   293,   522,   106,   253,   470,   291,    -1,    -1,    62,
      -1,    64,    65,   465,    -1,    -1,    -1,    -1,    -1,    -1,
      73,    -1,    -1,    -1,   508,   492,   478,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   501,    -1,    -1,    -1,
     505,   506,    -1,    -1,    -1,   510,    -1,   499,   499,    -1,
      -1,   503,   504,   505,    -1,    -1,    -1,   492,   510,    -1,
      -1,   513,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   538,    -1,    -1,   528,    -1,   562,    -1,
      -1,    13,    -1,    -1,   568,    -1,   538,    19,    -1,   554,
      -1,    23,   576,   558,    -1,   547,   547,    -1,    -1,    -1,
     565,    -1,    -1,    35,    36,   570,    38,    -1,    -1,    -1,
      42,   563,    -1,    45,    -1,   567,    -1,    49,   583,   584,
      -1,    53,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   581,
     581,     4,     5,     6,     7,     8,    -1,    10,    -1,    12,
      13,    14,    -1,    -1,    17,    18,    19,    -1,    -1,    22,
      23,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    31,    -1,
      -1,    -1,    35,    36,    37,    38,    -1,    -1,    -1,    42,
      -1,    -1,    45,    -1,    -1,    -1,    49,    -1,    51,    52,
      53,    54,    55,    56,    57,    58,    59,    -1,    -1,    62,
      -1,    -1,    65,    -1,    -1,    -1,    69,    -1,    -1,    -1,
      -1,    -1,    -1,     6,    -1,    -1,    -1,    -1,    -1,    -1,
      13,    -1,    -1,    -1,    17,    -1,    19,    -1,    -1,    -1,
      23,    -1,    -1,    -1,    97,    98,    -1,    -1,   101,   102,
     103,   104,    35,    36,    -1,    38,    -1,    -1,    -1,    42,
      -1,    -1,    45,    -1,    -1,    -1,    49,    -1,    51,    -1,
      53,    54,    55,    56,    57,    58,    59,    60,    -1,    -1,
      -1,    64,    65,    -1,    -1,    -1,    69,    -1,    -1,    -1,
      -1,    -1,    -1,     6,    -1,    -1,    -1,    -1,    -1,    -1,
      13,    -1,    -1,    -1,    17,    -1,    19,    -1,    -1,    -1,
      23,    -1,    -1,    -1,    97,    98,    -1,    -1,   101,   102,
     103,   104,    35,    36,    -1,    38,    -1,    -1,    -1,    42,
      -1,    -1,    45,    -1,    -1,    -1,    49,    -1,    51,    -1,
      53,    54,    55,    56,    57,    58,    59,    -1,    -1,    -1,
      -1,    -1,    65,    -1,    -1,    -1,    69,    70,    -1,    -1,
      -1,    -1,    -1,     6,    -1,    -1,    -1,    -1,    -1,    -1,
      13,    -1,    -1,    -1,    17,    -1,    19,    -1,    -1,    -1,
      23,    -1,    -1,    -1,    97,    98,    -1,    -1,   101,   102,
     103,   104,    35,    36,    -1,    38,    -1,    -1,    -1,    42,
      -1,    -1,    45,    -1,    -1,    -1,    49,    -1,    51,    -1,
      53,    54,    55,    56,    57,    58,    59,    -1,    -1,    -1,
      -1,    64,    65,    -1,    -1,    -1,    69,    -1,    -1,    -1,
      -1,    -1,    -1,     6,    -1,    -1,    -1,    -1,    -1,    -1,
      13,    -1,    -1,    -1,    17,    -1,    19,    -1,    -1,    -1,
      23,    -1,    -1,    -1,    97,    98,    -1,    -1,   101,   102,
     103,   104,    35,    36,    -1,    38,    -1,    -1,    -1,    42,
      -1,    -1,    45,    -1,    -1,    -1,    49,    -1,    51,    -1,
      53,    54,    55,    56,    57,    58,    59,    -1,    61,    -1,
      -1,    -1,    65,    -1,    -1,    -1,    69,    -1,    -1,    -1,
      -1,    -1,    -1,     6,    -1,    -1,    -1,    -1,    -1,    -1,
      13,    -1,    -1,    -1,    17,    -1,    19,    -1,    -1,    -1,
      23,    -1,    -1,    -1,    97,    98,    -1,    -1,   101,   102,
     103,   104,    35,    36,    -1,    38,    -1,    -1,    -1,    42,
      -1,    -1,    45,    -1,    -1,    -1,    49,    -1,    51,    -1,
      53,    54,    55,    56,    57,    58,    59,    -1,    -1,    -1,
      -1,    -1,    65,    -1,    -1,    -1,    69,    -1,    -1,    -1,
      -1,    74,    -1,     6,    -1,    -1,    -1,    -1,    -1,    -1,
      13,    -1,    -1,    -1,    17,    -1,    19,    -1,    -1,    -1,
      23,    -1,    -1,    -1,    97,    98,    -1,    -1,   101,   102,
     103,   104,    35,    36,    -1,    38,    -1,    -1,    -1,    42,
      -1,    -1,    45,    -1,    -1,    -1,    49,    -1,    51,    -1,
      53,    54,    55,    56,    57,    58,    59,    -1,    -1,    62,
      -1,    -1,    65,    -1,    -1,    -1,    69,    -1,    -1,    -1,
      -1,    -1,    -1,     6,    -1,    -1,    -1,    -1,    -1,    -1,
      13,    -1,    -1,    -1,    17,    -1,    19,    -1,    -1,    -1,
      23,    -1,    -1,    -1,    97,    98,    -1,    -1,   101,   102,
     103,   104,    35,    36,    -1,    38,    -1,    -1,    -1,    42,
      -1,    -1,    45,    -1,    -1,    -1,    49,    -1,    51,    -1,
      53,    54,    55,    56,    57,    58,    59,    -1,    -1,    -1,
      -1,    -1,    65,    -1,    -1,    -1,    69,    -1,    -1,    -1,
      -1,    74,    -1,     6,    -1,    -1,    -1,    -1,    -1,    -1,
      13,    -1,    -1,    -1,    17,    -1,    19,    -1,    -1,    -1,
      23,    -1,    -1,    -1,    97,    98,    -1,    -1,   101,   102,
     103,   104,    35,    36,    -1,    38,    -1,    -1,    -1,    42,
      -1,    -1,    45,    -1,    -1,    -1,    49,    -1,    51,    -1,
      53,    54,    55,    56,    57,    58,    59,    -1,    -1,    -1,
      60,    -1,    65,    -1,    -1,    -1,    69,    -1,    -1,    -1,
      70,    71,    30,    -1,    -1,    -1,    76,    77,    78,    79,
      80,    81,    82,    83,    84,    85,    86,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    97,    98,    -1,    -1,   101,   102,
     103,   104,    60,    61,    62,    63,   106,    -1,    66,    67,
      68,    -1,    70,    71,    -1,    -1,    74,    75,    76,    77,
      78,    79,    80,    81,    82,    83,    84,    85,    86,    87,
      88,    89,    90,    91,    92,    93,    94,    95,    96,    -1,
       3,    99,   100,    -1,    -1,    -1,    -1,    -1,   106,    12,
      13,    -1,    -1,    16,    -1,    -1,    19,    -1,    21,    -1,
      23,    -1,    -1,    26,    -1,    -1,    -1,    -1,    -1,    32,
      -1,    -1,    35,    36,    -1,    38,    39,    40,    41,    42,
      43,    -1,    45,    46,    47,     3,    49,    50,    -1,    -1,
      53,    -1,    -1,    -1,    12,    -1,    -1,    -1,    16,    -1,
      -1,    64,    65,    21,    -1,    -1,    -1,    -1,    26,    -1,
      -1,    -1,    -1,    -1,    32,    -1,    -1,    -1,    -1,    -1,
      -1,    39,    40,    41,    42,    43,    -1,    -1,    46,    47,
      -1,    -1,    50,    -1,    -1,    53,    -1,    -1,    -1,     3,
      -1,    -1,    -1,    -1,    -1,    -1,    64,    65,    12,    13,
      -1,    -1,    16,    -1,    -1,    19,    -1,    21,    -1,    23,
      -1,    -1,    26,    -1,    -1,    -1,    -1,    -1,    32,    -1,
      -1,    35,    36,    -1,    38,    39,    40,    41,     3,    43,
      -1,    45,    46,    47,    -1,    49,    50,    12,    13,    53,
      -1,    16,    -1,    -1,    19,    -1,    21,    -1,    23,    -1,
      64,    26,    -1,    -1,    -1,    -1,    -1,    32,    -1,    -1,
      35,    36,    -1,    38,    39,    40,    41,     3,    43,    -1,
      45,    46,    47,    -1,    49,    50,    12,    13,    53,    -1,
      16,    -1,    -1,    19,    -1,    21,    -1,    23,    -1,    64,
      26,    -1,    -1,    -1,    -1,    -1,    32,    -1,    -1,    35,
      36,    -1,    38,    39,    40,    41,     3,    43,    -1,    45,
      46,    47,    -1,    49,    50,    12,    -1,    53,    -1,    16,
      -1,    -1,    -1,    -1,    21,    -1,    -1,    -1,    64,    26,
      -1,    -1,    -1,    -1,    -1,    32,    -1,    -1,    -1,    -1,
      -1,    -1,    39,    40,    41,    -1,    43,    -1,    13,    46,
      47,    -1,    -1,    50,    19,    -1,    -1,    -1,    23,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    64,    -1,    13,
      35,    36,    -1,    38,    39,    19,    -1,    -1,    -1,    23,
      45,    -1,    -1,    -1,    49,    -1,    -1,    -1,    53,    -1,
      -1,    35,    36,    -1,    38,    63,    -1,    65,    66,    64,
      68,    45,    -1,    -1,    -1,    49,    -1,    75,    -1,    53,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    87,
      88,    89,    90,    91,    92,    93,    94,    95,    96,    97,
      98,    99,   100,    71,    -1,    -1,    -1,    -1,    76,    77,
      78,    79,    80,    81,    82,    83,    84,    85,    86
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const yytype_uint16 yystos[] =
{
       0,    25,    64,   114,   115,   123,   124,   159,   160,   288,
      41,    53,   110,   112,   115,   116,     0,   152,    11,   110,
     111,    69,   153,   116,   118,   125,   126,   160,   112,   111,
      61,     6,    13,    17,    19,    23,    35,    36,    38,    42,
      45,    49,    51,    54,    55,    56,    57,    58,    59,    65,
      69,    97,    98,   101,   102,   103,   104,   110,   112,   136,
     137,   138,   145,   154,   156,   160,   161,   162,   163,   164,
     165,   166,   255,   260,   261,   265,   266,   274,   275,   276,
       3,    12,    16,    21,    26,    32,    39,    40,    41,    43,
      46,    47,    50,    64,   127,   128,   129,   130,   131,   158,
     160,    62,    61,   117,   110,   110,   145,   245,   246,    69,
     268,   277,    61,    61,   277,   278,   110,   138,   146,   110,
     255,   260,    65,    71,   132,   139,   269,   270,   277,   265,
     105,   271,   271,    17,    51,   110,   279,    70,    60,   287,
     155,   157,   265,    71,    76,    77,    78,    79,    80,    81,
      82,    83,    84,    85,    86,   253,   259,    67,   254,    30,
     257,   258,   265,   262,   110,   110,    40,    63,    62,    65,
     139,   147,   243,   246,   247,   277,   255,   273,    43,   110,
     141,    66,    70,    67,   138,   140,   164,   133,    61,   277,
     278,   277,    60,    60,   260,   136,   137,    63,    65,    66,
      68,    75,    87,    88,    89,    90,    91,    92,    93,    94,
      95,    96,    97,    98,    99,   100,   256,   264,    61,   211,
     252,   255,   263,    65,   119,   149,   119,   110,    66,   244,
     247,    72,   170,   289,   272,    70,   268,    60,    34,    51,
     135,   134,    61,    43,   110,   163,   164,   271,   265,     6,
      17,    51,   110,   145,   248,   101,   102,   267,   110,   150,
      34,   122,    34,   120,   280,   291,    61,   290,    60,   138,
     138,   138,    60,    66,   110,   145,   249,   278,   268,   279,
      34,   143,   142,   146,    72,   180,   136,    20,   121,   118,
     281,   282,   283,   110,    41,    62,    73,   118,   172,   214,
     255,   140,   132,   110,   251,   138,   151,    60,    66,   179,
     146,   170,   127,   128,   131,   136,   284,   283,   243,   214,
      42,   110,   127,   128,   149,   173,   177,   215,    65,   145,
     148,   250,   144,   150,    62,    73,   118,   182,   110,   110,
      69,   176,   196,    42,   110,   136,   169,   178,   110,   126,
     193,   206,   216,   217,    66,   247,    68,    42,   127,   128,
     136,   149,   183,   184,   191,    69,   186,   187,   271,   285,
     286,   175,   196,   192,   193,   197,    27,   167,   176,   110,
      74,    39,   136,   160,   198,     4,     5,     7,     8,    10,
      12,    14,    18,    22,    31,    37,    52,    62,   110,   214,
     218,   219,   255,   138,   110,   110,   169,    70,   181,    71,
     106,   167,    70,   136,   112,   113,   214,   174,   196,   110,
     201,   202,   110,   210,    69,   276,   255,   276,   276,   218,
     210,   255,   211,    69,   214,   227,   276,    74,    62,   190,
     196,   185,   186,   189,   196,   110,   107,    60,   204,   205,
     255,    62,   168,   214,    61,   110,   199,   200,   109,   271,
     203,   271,    62,   171,    62,   193,   237,   238,   241,   209,
      74,   208,   218,   214,    52,    62,    62,    62,   193,   228,
     229,    33,   212,   223,   224,   214,   218,   218,   167,    62,
     271,   189,     9,   110,   188,    61,   271,    60,   194,    60,
     167,    71,   195,    60,   136,    70,    62,   232,   255,    62,
      24,   207,   276,   138,    62,    70,    62,   222,    69,    44,
     226,   221,   212,   223,    62,   167,   164,   187,    61,   197,
     112,   168,   204,   202,   200,   218,   211,     9,    28,   233,
     234,   235,   218,    62,   200,    70,   229,   193,   214,   224,
     213,   226,    62,   200,    74,   195,   239,   240,    62,    74,
     110,   236,   255,   215,   234,    71,   112,   225,   255,   171,
      62,   219,   231,   242,    74,    74,   255,   220,   110,   211,
     230,    75,    70,    62,    60,   112,   214,   231,   219
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint16 yyr1[] =
{
       0,   108,   109,   109,   110,   111,   111,   112,   113,   114,
     114,   115,   115,   116,   116,   111,   111,   117,   117,   118,
     118,   119,   119,   120,   120,   121,   121,   122,   122,   123,
     123,   124,   125,   126,   126,   127,   128,   128,   129,   130,
     131,   132,   132,   133,   133,   134,   134,   135,   135,   136,
     136,   137,   137,   137,   137,   137,   137,   137,   137,   138,
     139,   140,   140,   141,   141,   142,   142,   143,   143,   144,
     144,   145,   146,   147,   147,   148,   148,   149,   150,   151,
     152,   152,   153,   153,   154,   154,   155,   155,   156,   156,
     157,   157,   158,   158,   158,   158,   158,   158,   158,   158,
     158,   158,   158,   158,   159,   160,   161,   161,   162,   163,
     164,   164,   164,   165,   166,   118,   118,   167,   168,   168,
     169,   169,   170,   171,   171,   172,   172,   172,   172,   173,
     173,   173,   173,   173,   174,   175,   176,   177,   178,   178,
     179,   179,   180,   181,   181,   182,   182,   183,   183,   183,
     183,   183,   184,   185,   185,   186,   187,   188,   189,   190,
     191,   192,   192,   193,   193,   194,   194,   195,   195,   196,
     197,   198,   198,   199,   199,   200,   201,   202,   203,   204,
     204,   205,   206,   206,   207,   207,   208,   208,   209,   209,
     210,   210,   211,   211,   212,   212,   213,   213,   214,   214,
     215,   215,   216,   216,   216,   217,   218,   218,   218,   218,
     218,   218,   218,   218,   218,   218,   218,   218,   218,   218,
     218,   218,   218,   218,   219,   220,   220,   221,   221,   222,
     222,   223,   224,   225,   226,   227,   227,   228,   229,   230,
     230,   231,   231,   232,   232,   233,   234,   234,   235,   235,
     235,   236,   237,   237,   238,   239,   239,   240,   241,   242,
     243,   243,   244,   244,   245,   245,   246,   247,   248,   249,
     249,   250,   250,   251,   252,   252,   252,   252,   252,   252,
     253,   253,   254,   254,   255,   256,   257,   257,   258,   258,
     258,   255,   259,   259,   259,   259,   259,   259,   259,   259,
     259,   259,   259,   259,   260,   261,   262,   262,   263,   263,
     264,   264,   264,   264,   264,   264,   264,   264,   264,   264,
     264,   264,   264,   264,   264,   264,   264,   264,   264,   264,
     265,   265,   265,   265,   266,   266,   266,   266,   266,   266,
     267,   267,   268,   268,   269,   269,   270,   271,   271,   271,
     272,   272,   273,   273,   274,   274,   274,   274,   274,   274,
     274,   274,   274,   274,   275,   275,   275,   275,   275,   275,
     276,   277,   278,   278,   279,   279,   280,   280,   281,   281,
     282,   282,   283,   284,   284,   284,   284,   285,   285,   286,
     286,   287,   287,   288,   288,   289,   289,   290,   290,   291,
     291
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     0,     3,     1,     0,     3,     2,     2,     0,
       4,     0,     1,     0,     2,     0,     3,     0,     2,     0,
       2,     0,     1,     0,     2,     0,     2,     0,     2,     3,
       2,     6,     1,     2,     2,     1,     1,     1,     6,     5,
       4,     0,     1,     0,     4,     0,     3,     2,     2,     2,
       2,     1,     1,     1,     1,     1,     1,     1,     1,     3,
       4,     1,     2,     0,     3,     0,     3,     0,     2,     0,
       3,     3,     2,     2,     1,     2,     1,     4,     2,     2,
       0,     2,     0,     3,     0,     1,     0,     3,     0,     1,
       0,     3,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     2,     3,     1,     1,     2,     3,
       1,     1,     1,     2,     2,     0,     2,     2,     1,     1,
       1,     1,     3,     0,     3,     1,     2,     2,     1,     3,
       2,     1,     1,     1,     4,     3,     3,     2,     3,     2,
       0,     2,     3,     0,     3,     1,     2,     1,     3,     1,
       1,     1,     3,     2,     1,     2,     3,     2,     4,     3,
       4,     0,     1,     0,     2,     0,     2,     0,     2,     3,
       3,     1,     1,     2,     4,     2,     2,     2,     2,     1,
       1,     0,     0,     2,     0,     2,     0,     2,     0,     2,
       0,     1,     0,     1,     0,     1,     0,     1,     0,     2,
       0,     2,     1,     1,     2,     4,     1,     1,     3,     2,
       4,     4,     3,     3,     5,     5,     3,     3,     3,     3,
       3,     3,     4,     5,     1,     0,     3,     0,     2,     0,
       2,     2,     7,     2,     2,     4,     3,     2,     5,     0,
       3,     0,     1,     0,     2,     2,     1,     2,     3,     3,
       2,     1,     1,     5,     4,     5,     2,     2,     0,     2,
       0,     1,     0,     4,     3,     2,     3,     2,     2,     0,
       1,     0,     1,     3,     3,     2,     2,     3,     4,     1,
       0,     2,     0,     1,     1,     2,     0,     2,     0,     1,
       2,     2,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     2,     2,     0,     2,     0,     2,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       2,     2,     2,     3,     1,     1,     1,     1,     1,     1,
       1,     1,     0,     1,     0,     1,     1,     0,     1,     1,
       0,     3,     0,     2,     1,     1,     2,     2,     2,     2,
       3,     2,     4,     3,     1,     1,     1,     1,     1,     1,
       3,     3,     1,     3,     2,     2,     0,     2,     0,     1,
       1,     2,     2,     4,     1,     1,     1,     1,     1,     5,
       3,     0,     1,     0,     1,     0,     1,     0,     2,     0,
       1
};


#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                  \
do                                                              \
  if (yychar == YYEMPTY)                                        \
    {                                                           \
      yychar = (Token);                                         \
      yylval = (Value);                                         \
      YYPOPSTACK (yylen);                                       \
      yystate = *yyssp;                                         \
      goto yybackup;                                            \
    }                                                           \
  else                                                          \
    {                                                           \
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;                                                  \
    }                                                           \
while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256



/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)

/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Type, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*----------------------------------------.
| Print this symbol's value on YYOUTPUT.  |
`----------------------------------------*/

static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  FILE *yyo = yyoutput;
  YYUSE (yyo);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# endif
  YYUSE (yytype);
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyoutput, "%s %s (",
             yytype < YYNTOKENS ? "token" : "nterm", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yytype_int16 *yyssp, YYSTYPE *yyvsp, int yyrule)
{
  unsigned long int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       yystos[yyssp[yyi + 1 - yynrhs]],
                       &(yyvsp[(yyi + 1) - (yynrhs)])
                                              );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
static YYSIZE_T
yystrlen (const char *yystr)
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            /* Fall through.  */
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYSIZE_T *yymsg_alloc, char **yymsg,
                yytype_int16 *yyssp, int yytoken)
{
  YYSIZE_T yysize0 = yytnamerr (YY_NULLPTR, yytname[yytoken]);
  YYSIZE_T yysize = yysize0;
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat. */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Number of reported tokens (one for the "unexpected", one per
     "expected"). */
  int yycount = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[*yyssp];
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYSIZE_T yysize1 = yysize + yytnamerr (YY_NULLPTR, yytname[yyx]);
                  if (! (yysize <= yysize1
                         && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
                    return 2;
                  yysize = yysize1;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    YYSIZE_T yysize1 = yysize + yystrlen (yyformat);
    if (! (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
      return 2;
    yysize = yysize1;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          yyp++;
          yyformat++;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
{
  YYUSE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       'yyss': related to states.
       'yyvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        YYSTYPE *yyvs1 = yyvs;
        yytype_int16 *yyss1 = yyss;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * sizeof (*yyssp),
                    &yyvs1, yysize * sizeof (*yyvsp),
                    &yystacksize);

        yyss = yyss1;
        yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yytype_int16 *yyss1 = yyss;
        union yyalloc *yyptr =
          (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
        if (! yyptr)
          goto yyexhaustedlab;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
                  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
      
#line 2055 "y.tab.c" /* yacc.c:1646  */
      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = (char *) YYSTACK_ALLOC (yymsg_alloc);
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYTERROR;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  return yyresult;
}
#line 1151 "parse.yacc" /* yacc.c:1906  */

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
