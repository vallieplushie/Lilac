"""
Contains all the types which exist in the Lilac AST
"""


from . import *

class AstNode:
    """
    Generic Node in my AST.

    Attributes
    ----------
    left : AstNode
        The child node to the left of this node.
    right : AstNode
        The child node to the right of this node.
    contents : object
        The contents that this node holds
    [Optional]
    helper : AstHelper
        A helper node which sits alongside this node in the AST, holding information about scope 
    """

    def __init__(self, left, right, contents, helper=None):
        self.left:AstNode = left
        self.right:AstNode = right
        self.contents:object = contents
        
        if helper == None:
            self.helper:AstHelper = AstHelper()
        else:
            self.helper:AstHelper = AstHelper()


class AstHelper:
    """
    Helper Node which holds information about the parent
    """

    def __init__(self) -> None:
        self.parent_type = parent_type
        self.scope = scope


class AstOperator(AstNode):
    """
    Represents an operator
    """
    
    def __init__(self, left, right, contents:Token, helper=None):
        super().__init__(left, right, contents, helper)


class AstLiteral(AstNode):
    """
    Represents a literal or identifier
    """

    def __init__(self, left, right, contents:Token, helper=None):
        super().__init__(left, right, contents, helper)

