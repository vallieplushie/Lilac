# Imports
from . import Ttype

class Grammar:
    """
    Encapsulates all the rules for the grammar of Lilac

    ...

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

    """

    built_in_type = [Ttype.INT, Ttype.INTS, Ttype.REAL, Ttype.REALS, Ttype.STRING, Ttype.STRINGS, Ttype.BOOL, Ttype.BOOLS]


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
                'right' : (lambda t: True if t in Grammar.literal + Ttype.SPACE else False)
                }
            }
