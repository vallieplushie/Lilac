from pylac import .

class Environment:
    """
    Executes the parsed AST
    """

    def __init__(self, main_tree:AstNode):
        self.main_tree = main_tree
        self.global_table : dict[str, AstNode] = {}
        self.call_stack = CallStack()


class StateMonad:
    """
    Environment as a monadic struct5ure. 
    """

    def __init__(self, env=None) -> None:
        if env is None:
            self.env = Environment()
        else:
            self.env = env

    def unwrap(self):
        return self.env

    @staticmethod
    def unit(env):
        """Raises an env to a Monad"""
        return StateMonad(env)
        
    def bind(self, action) -> 'StateMonad':
        """
        Changes the contents of self.env while keeping self.env as reference BUT returns a new wrapper
        """

        res = action.run(self.env)
        if res is None:
            return StateMonad(self.env)
        else:
            return StateMonad(res) 

    def __rshift__(self, action) -> 'StateMonad':
        """bind() with operator >>, returns completely separate monad"""

        res = action.run(copy.deepcopy(self.env))
        if res is None:
            return StateMonad(self.env)
        else:
            return StateMonad(res) 

    def __lshift__(self, action) -> 'StateMonad':
        """Bind with operator <<, mutates env in place"""
        res = action.run(self.env)
        if res is None:
            return StateMonad(self.env)
        else:
            return StateMonad(res)
