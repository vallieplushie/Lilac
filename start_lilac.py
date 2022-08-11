import sys
import os
from pylac import Lilac

if len(sys.argv) > 2:
    print("Incorrect usage")
    sys.exit(64)
elif len(sys.argv) == 2:
    Lilac.interactive = False
    Lilac.runFile(sys.argv[1])
else:
    Lilac.run_Prompt()
    Lilac.interactive = True
