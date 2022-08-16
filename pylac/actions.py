from pylac import *

class Action:
    """
    Class representing the different Actions for the machine to take

    Actions are functions which all have the same interface. They are be passed to the GlobalEnvironment, which runs them on the stack
    """ 
    
    def execute(self, glob:GlobalEnvironment) -> GlobalEnvironment:
        pass

    def check(self):
        pass


# TODO:
# When am i doing type checking ?!?!?!?
# Need to decide between here and tree generation.

class NumberAction(Action):
    def __init__(self, left, right, operator:str):
        self.operator = operator
        self.left = left
        self.right = right

    def check(self) -> bool:
        super().check()
        if self.left.stype in [Stype.INTEGER, Stype.REAL]:
            l_check = True
        else:
            Lilac.throw(self.left.token.line, Error.OperandTypeError, 
                        f"Operator '{self.operator}' is not defined for operand '{self.left.token.lexeme}', which is of type {self.left.stype}")

        if self.right.stype in [Stype.INTEGER, Stype.REAL]:
            r_check = True
        else:
            Lilac.throw(self.right.token.line, Error.OperandTypeError, 
                        f"Operator '{self.operator}' is not defined for operand '{self.right.token.lexeme}', which is of type {self.right.stype}")
        
        return (r_check and l_check)


class AdditionAction(NumberAction):
    def __init__(self, left, right, operator: str):
        super().__init__(left, right, operator)

    def execute(self, glob):
        super().check()
        node1:StackNode = glob.call_stack.pop()
        node2:StackNode = glob.call_stack.pop()

        if Stype.REFERENCE in node1.type:
            num1 = glob.global_table[node1.contents]
        else:
            num1 = node1.contents

        if Stype.REFERENCE in node2.type:
            num2 = glob.global_table[node2.contents]
        else:
            num2 = node2.contents

        result = num1+num2
        res_node = StackNode(type=Stype.INTEGER)
        glob.call_stack.push(res_node)

class IncludeAction(Action):
    """Take another file and adds its contents to the global table"""
    
    def __init__(self, source_path:str):
        
    def execute(self):


