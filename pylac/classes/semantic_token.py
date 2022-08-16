from . import *

class SemanticToken:
    """
    Like Token, except wraps it up in semantic information, including its action

    ...

    Attributes
    ----------
    [Required]
    token : Token
        Textual token that this SemanticToken represents
    type : Stype
        Semantic type of this token (Int identifier has Stype of Int, even though it is an identifier, etc.)
    
    [Optional]
    action : Action
        The action associated with this token
    """

    def __init__(self, type:Stype, token:Token=None, action=None) -> None:
        self.token:Token = token
        self.stype:Stype = stype
        self.action = action

    def __str__(self) -> str:
        return f'Token: ({self.token})\nSemanticType: {self.stype}\nAction: {self.action}'


