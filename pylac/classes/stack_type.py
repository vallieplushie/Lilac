from enum import Enum

class Stype(Enum):
    """
    Hack-y enum holding all the StackNode types

    Use Stype.INTEGER.value in Stype.LITERALTYPE.value
    """
    
    # Not using an actual enum because i need to group these 
    INTEGER = 1
    INTEGERLIST = 2
    REAL = 3
    REALLIST = 4
    STRING = 5
    STRINGLIST = 6
    BOOL = 7
    BOOLLIST = 8

    LITERALTYPE = [
            INTEGER, INTEGERLIST, 
            REAL, REALLIST,
            STRING, STRINGLIST,
            BOOL, BOOLLIST,
            ]
    
