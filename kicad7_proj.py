import sys
from config import config
from build import build

EXPECTED_ARGC = 2
ERR_ARG_NUM = f"\
    Takes 1 argument, {len(sys.argv)-1} given.\nArgument must be 'clean', 'config' or 'setup'."

if (EXPECTED_ARGC > len(sys.argv)):
    print(ERR_ARG_NUM)
elif (len(sys.argv) > EXPECTED_ARGC):
    print(ERR_ARG_NUM)
else:
    if sys.argv[1] == 'build':
        build()
    elif sys.argv[1] == 'config':
        config()
    else:
        print("Invalid argument.\nArgument must be 'clean', 'config', or 'setup'.")

        