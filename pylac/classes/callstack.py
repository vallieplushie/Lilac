"""
Types for the callstack used in executing code
"""

from . import *

class StackNode:
    """
    Generic Node in the lilac callstack
    """

    def __init__(self, type:Stype, next=None) -> None:
        self.type:Stype = type
        self.next = next


class CallStack:
    """
    Abstract stack type, essentially a wrapper around StackNode
    """
    def __init__(self) -> None:
        self.top:StackNode = StackNode()

    def push(self, item:StackNode):
        """Push to the stack"""
        item.next = self.top
        self.top = item

    def pop(self) -> StackNode:
        """Pop from the stack"""
        popped_node = self.top
        self.top = popped_node.next
        del popped_node.next
        return popped_node

    def peek(self) -> StackNode:
        popped_node = self.top
        del popped_node.next
        return popped_node

