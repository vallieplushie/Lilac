#from typing import *
import sys

# Lilac imports
import pylac

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
    def runFile(source:str):
        with open(source, 'r') as file:
            Lilac.run(file.read())
        if Lilac.hadError:
            sys.exit(65)
    
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
        scan = pylac.Scanner(source)
        scan.scan()
        for t in scan.tokens:
            print(t)

    @staticmethod
    def throw(line:int, type:pylac.Error, message:str):
        Lilac.report(line, type, message)

    @staticmethod
    def report(line:int, err_type:pylac.Error, message:str):
        """
        Prints and reports an error to the console
        """
        print(f'[Line {line}] {err_type.value}: {message}')
        Lilac.hadError = True
        # don't quit if it's interactive
        if Lilac.interactive:
            Lilac.interactive_mode()
        else:
            sys.exit(64) # need to use the correct exit code here, maybe add different codes in the Error enum
