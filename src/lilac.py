import sys
from typing import *

from error_type import Error
import scanner

class Lilac:
    """
    Main Lilac class, contains the driver code
    """
    hadError:bool = False
    interactive:bool = False

    @staticmethod
    def run_Prompt():
        """
        Runs the interactive prompt
        """
        print('====== Lilac Interactive Prompt ======')
        print('Enter the command "quit" to exit.')
        Lilac.interactive_mode()
    
    @staticmethod
    def interactive_mode():
        """
        Interactive prompt
        """
        while True:
            print('>', end=' ')
            line = input()
            if line == 'quit':
                sys.exit()
            Lilac.run(line)
            Lilac.hadError = False

    @staticmethod
    def run(source:str):
        """
        Runs the source, this will build up all the different parts
        """
        scan = scanner.Scanner(source)
        scan.scan()
        print(scan.tokens)

    @staticmethod
    def throw(line:int, type:Error, message:str):
        Lilac.report(line, type, message)

    @staticmethod
    def report(line:int, err_type:Error, message:str):
        """
        Prints and reports an error to the console
        """
        print(f'[Line {line}] {err_type.value}: {message}')
        Lilac.hadError = True
        if Lilac.interactive:
            Lilac.interactive_mode()
        else:
            sys.exit(64) # need to use the correct exit code here, maybe add different codes in the Error enum
    
if __name__=="__main__":
    if len(sys.argv) > 2:
        print("Incorrect usage")
        sys.exit(64)
    elif len(sys.argv) == 2:
        Lilac.interactive = False
        Lilac.runFile(sys.argv[1])
    else:
        Lilac.run_Prompt()
        Lilac.interactive = True
