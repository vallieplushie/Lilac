# Imports
from . import Ttype

class Grammar:
    """
    Encapsulates all the rules for the grammar of Lilac

    Attributes
    ----------
    built_in_type : List[Ttype]
        A list of tokens which represesnt the built in types
    literal : List[Ttype]
        A list of tokens which represent literal values
    operator_table : dict
        Dictionary which holds all the information for the operator tokens.
        The key is a Ttype and the value is a dictionary with the following maps:
            * 'assoc': Either 'R' or 'L', indicating right or left associativity.
            * 'prec': An int indicating the precedence level. Biger sits lower in the tree.
            * 'left': Boolean lambda expressions which return True if the input type is allowed on the left of the operator.
            * 'right': Boolean lambda expressions which return True if the input type is allowed on the right of the operator.
            * 'allowedl': List of types that match 'left'
            * 'allowedr': List of types that match 'right'
    """

    built_in_type = [Ttype.INT, Ttype.INTS, Ttype.REAL, Ttype.REALS, Ttype.STRING, Ttype.STRINGS, Ttype.BOOL, Ttype.BOOLS]
    literal = [Ttype.IDENTIFIER, Ttype.NUMINT, Ttype.NUMREAL, Ttype.STRINGLIT, Ttype.TRUE, Ttype.FALSE]

    # BIG table holding all the information
    operator_table = {
            Ttype.NEWLINE : {
                'assoc' : 'R',
                'prec'  : 1,
                'left'  : (lambda t: True),  # Anything can go on left or right
                'right' : (lambda t: True)
                },
            Ttype.COLON : {
                'assoc' : 'L',
                'prec'  : 2,
                'left'  : (lambda t: True if t in [Ttype.IDENTIFIER, Ttype.SPACE] else False), 
                'right' : (lambda t: True if t in Grammar.literal + [Ttype.SPACE, Ttype.LAMBDA] else False),
                'allowedl' : [Ttype.IDENTIFIER, Ttype.SPACE],
                'allowedr' : Grammar.literal + [Ttype.SPACE, Ttype.LAMBDA]
                },
            **dict.fromkeys([Ttype.PLUS, Ttype.MINUS], {
                'assoc' : 'L',
                'prec'  : 11,
                'left'  : (lambda t: True if t in [Ttype.IDENTIFIER, Ttype.NUMINT, Ttype.NUMREAL] else False),
                'right' : (lambda t: True if t in [Ttype.IDENTIFIER, Ttype.NUMINT, Ttype.NUMREAL] else False),
                'allowedl' : [Ttype.NUMINT, Ttype.NUMREAL, Ttype.IDENTIFIER, Ttype.SPACE],
                'allowedr' : [Ttype.NUMINT, Ttype.NUMREAL, Ttype.IDENTIFIER, Ttype.SPACE]
                }),
            **dict.fromkeys([Ttype.STAR, Ttype.SLASH], {
                'assoc' : 'L',
                'prec'  : 12,
                'left'  : (lambda t: True if t in [Ttype.IDENTIFIER, Ttype.NUMINT, Ttype.NUMREAL] else False),
                'right' : (lambda t: True if t in [Ttype.IDENTIFIER, Ttype.NUMINT, Ttype.NUMREAL] else False),
                'allowedl' : [Ttype.NUMINT, Ttype.NUMREAL, Ttype.IDENTIFIER, Ttype.SPACE],
                'allowedr' : [Ttype.NUMINT, Ttype.NUMREAL, Ttype.IDENTIFIER, Ttype.SPACE]
                }),
            Ttype.CARET : {
                'assoc' : 'L',
                'prec'  : 13,
                'left'  : (lambda t: True if t in [Ttype.IDENTIFIER, Ttype.NUMINT, Ttype.NUMREAL] else False),
                'right' : (lambda t: True if t in [Ttype.IDENTIFIER, Ttype.NUMINT, Ttype.NUMREAL] else False),
                'allowedl' : [Ttype.NUMINT, Ttype.NUMREAL, Ttype.IDENTIFIER, Ttype.SPACE],
                'allowedr' : [Ttype.NUMINT, Ttype.NUMREAL, Ttype.IDENTIFIER, Ttype.SPACE]
                }
            }
