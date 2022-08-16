from pylac import *


class Parser:
    """
    Parses a list of Tokens to an AST
    """
    def __init__(self, tokens):
        self.tokens = tokens
        self.tree = AstNode()


    def parse(self):
        """
        Uses an "Operator priority" parsing method
        """

        pass

    def find_lowest_bound(self):
        pass

