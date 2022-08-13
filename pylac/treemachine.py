from pylac import .

class GlobalEnvironment:
    """
    Executes the parsed AST
    """

    def __init__(self, main_tree:AstNode):
        self.main_tree = main_tree
        self.global_table : dict[str, AstNode] = {}
        self.call_stack

    def execute(self, action:Action):
        self = action.execute(self)


clas K
