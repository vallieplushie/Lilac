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
    BOOL = 'B'
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
    LAMBDA = '=>'

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
    NOT = '!'
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

    PIPE = '|'
    QUESTION = '?'

    EOF = auto()


class Token:
    """
    Representation of a token
    
    ...

    Attributes
    ----------
    type : Ttype
        The type of token which this object represents.
    lexeme : str
        The string in source code that this token represents.
    literal : object
        The value of the token, if it is a number or string
    line : int
        The line number of the token
    """
    def __init__(self, 
            type:Ttype,
            lexeme:str, # How the token appears in text
            literal, # The literal value of the token
            line:int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f'{self.type} {self.lexeme} {self.literal} {self.line}'
