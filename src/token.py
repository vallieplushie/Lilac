import token_type

class Token:
    def __init__(self, 
            type:token_type.Ttype,
            lexeme:str,
            literal,
            line:int):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f'{self.type} {self.lexeme} {self.literal} {self.line}'
