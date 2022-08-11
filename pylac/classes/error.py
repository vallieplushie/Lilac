from enum import Enum, auto

class Error(Enum):
    """
    Contains the different types of error, as an enum
    """
    SyntaxError = 'SyntaxError'
    # MismatchedParenthesesError = 'MismatchedParenthesesError'
    ArgumentTypeError = 'ArgumentTypeError'
    NameUndefinedError = 'NameUndefinedError'
    Blank = ''

