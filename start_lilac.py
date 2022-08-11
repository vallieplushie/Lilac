import sys
import os
from pylac import Lilac, Error

if len(sys.argv) > 2:
    print("Incorrect usage")
    sys.exit(64)
elif len(sys.argv) == 2:
    Lilac.interactive = False
    if sys.argv[1][-5:] != 'lilac':
        Lilac.throw(0, Error.Blank, "File must end in .lilac")
    else:
        Lilac.runFile(sys.argv[1])
else:
    Lilac.run_Prompt()
    Lilac.interactive = True

    @staticmethod
    def runFile(source:str):
        with open(source, 'r') as file:
            Lilac.run(file.read())
        if Lilac.hadError:
            sys.exit(65)
