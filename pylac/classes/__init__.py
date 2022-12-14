"""
The action-less classes for the interpreter.

My file structure separates types from behaviour, in here I keep all the types.
"""

from typing import Type

# Init file for my files
from .stack_type import *
from .error import *
from .token import *
from .grammar import *
from .callstack import *
from .astnode import *
from .semantic_token import *
