from pylac import *

class Action:
    """
    Class representing the different Actions for the machine to take

    Actions are functions which all have the same interface. They are be passed to the GlobalEnvironment, which runs them on the stack
    """ 
    
    def execute(self, glob:GlobalEnvironment) -> GlobalEnvironment:
        pass

class AdditionAction(Action):
    def execute(self, glob):
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
        res_node = StackNode(type=Stype.INTEGER, contents=)
        glob.call_stack.push(res_node)



class IncludeAction(Action):
    """Take another file and adds its contents to the global table"""
    
    def __init__(self, source_path:str):

    def execute(self):


