import lilac
from error_type import Error
from token import Token
from token_type import Ttype

class Scanner:
    """
    Scanner class which takes care of lexical analysis
    """
    def __init__(self, source:str):
        self.source:str = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

        self.keywords = {
            'true' : Ttype.TRUE,
            'false' : Ttype.FALSE
            }
    
    def scan(self):
        """
        Driving method. Scans the source file, lexing as it goes
        """
        while not self.at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(Ttype.EOF, "", None, self.line))
        self.cleanup_list()
        return self.tokens

    def scan_token(self):
        """
        Scans a single token based on a character
        """
        c = self.advance()
        match c:
            # Single characters
            case '(': self.add_token(Ttype.LEFTPAREN)
            case ')': self.add_token(Ttype.RIGHTPAREN)
            case '[': self.add_token(Ttype.LEFTSQUARE)
            case ']': self.add_token(Ttype.RIGHTSQUARE)
            case ',': self.add_token(Ttype.COMMA)
            case '+': self.add_token(Ttype.PLUS)
            case '-': self.add_token(Ttype.MINUS)
            case '*': self.add_token(Ttype.STAR)
            case '/': self.add_token(Ttype.SLASH)
            case '?': self.add_token(Ttype.QUESTION)
            case '|': self.add_token(Ttype.PIPE)
            case '=': self.add_token(Ttype.EQUAL)

            case '#': self.comment()

            case '"': self.string()
            
            # Default case, also contains number and identifier cases
            case _ : 
                if self.is_digit(c):
                    self.number()
                elif self.is_alpha(c):
                    self.identifier()
                else:
                    lilac.Lilac.error(0, f'Unknown character {c}')
                    sys.exit(65)
                return

    def at_end(self) -> bool:
        """
        Determines whether the scanner is at the end of the file
        """
        return (self.current >= len(self.source))

    def advance(self) -> str:
        """
        Advances by one character in the source, consuming it
        """
        self.current += 1
        return self.source[self.current-1]

    def add_token(self, type, literal:str=None):
        """
        Adds a lexed token to the list
        """
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type, text, literal, self.line))

    def next_match(self, expected) -> bool:
        """
        Checks whether the next character is the expected one
        """
        if self.at_end():
            return False
        if self.source[self.current] != expected:
            return False
        
        self.current += 1
        return True

    def peek(self) -> str:
        """
        Looks at the next character WITHOUT consuming it
        """
        if self.at_end():
            return
        return self.source[self.current]

    def peek_next(self) -> str:
        """
        Looks at the next-next character without consuming it
        """
        if self.current+1 >= len(self.source):
            return
        return self.source[self.current+1]

    def is_digit(self, c) -> bool:
        if c is None:
            return False
        return c >= '0' and c <= '9'

    def number(self):
        """
        Adds a number literal as a token
        """
        # keeps going until digits run out
        while self.is_digit(self.peek()):
            self.advance()
        real = False

        # if the next is a dot and there are numbers after, not an integer
        if self.peek() == '.' and self.is_digit(self.peek_next()):
            real = True
            self.advance()
            while self.is_digit(self.peek()):
                self.advance()
        elif self.peek() == '.' and self.peek_next() is ' ':
            real = True
            self.advance()
        
        if real:
            self.add_token(Ttype.NUMREAL, float(self.source[self.start:self.current]))
        else:
            self.add_token(T.NUMINT, int(self.source[self.start:self.current]))

    def identifier(self):

        while self.alphanum(self.peek()):
            self.advance()

        id = self.source[self.start:self.current]
        type = self.keywords.get(id)
        if type is None:
            type = Ttype.IDENTIFIER

        self.add_token(type)

    def is_alpha(self, c) -> bool:
        """
        Checks whether the current character is in the alphabet (plus _)f
        """
        if c is None:
            return False
        return ((c >= 'a' and c <= 'z') or \
                (c >= 'A' and c <= 'Z') or \
                c == '_')

    def alphanum(self, c) -> bool:
        """
        Checks whether the current character is alphanumeric
        """        
        return self.is_alpha(c) or self.is_digit(c)

    def comment(self):
        """
        skips until a new line
        """
        while not self.next_match('\n'):
            self.advance()
        self.advance()

    def string(self):
        """
        Adds a string literal
        """
        try:
            while peek_next() != '"':
        except IndexError:
            lilac.Lilac.throw(self.line, Error.SyntaxError, 'Unterminated string')

    def block_comment(self):
        while self.source[self.current] != '#' and \
              not self.next_match('#') and \
              self.peek_next() != '#':
            self.advance()
