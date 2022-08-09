from enum import Enum, auto

class Ttype(Enum):
    """
    Enum containing all the types for 
    """
    # Data Types
    INT = 'I'
    INTS = 'Is'
    REAL = 'R'
    REALS = 'Rs'
    STRING = 'S'
    STRINGS = 'Ss'
    BOOl = 'B'
    BOOLS = 'Bs'

    # Literals
    IDENTIFIER = auto()
    NUMINT = auto()
    NUMREAL = auto()
    STRINGLIT = auto()
    TRUE = 'true'
    FALSE = 'false'

    # Code Structuring
    LEFTPAREN = '('
    RIGHTPAREN = ')'
    NEWLINE = '\n'
    SPACE = ' ' # maybe unnecessary

    # Assignment
    COLON = ':'
    
    # Arithmetic
    PLUS = '+'
    MINUS = '-'
    SLASH = '/'
    STAR = '*'
    CARET = '^'

    # Boolean
    EQUAL = '='
    NOTEQUAL = '!='
    AND = '&&'
    OR = '||'
    LESS = '<'
    GREATER = '>'
    LESSEQUAL = '<='
    GREATEREQUAL = '>='
    
    # List
    LEFTSQUARE = '['
    RIGHTSQUARE = ']'
    COMMA = ','

    EOF = auto()

