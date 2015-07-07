#!/usr/bin/env python3.4

import sys
import getopt

def usage():
	print ('How to use...')

try:
    opts, args = getopt.getopt(argv, 'm:p:h', ['miner=', 'params=', 'help'])
except getopt.GetoptError:
    usage()
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        usage()
        sys.exit(2)
    elif opt in ('-m', '--miner'):
        miner_name = arg
    elif opt in ('-p', '--params'):
        params = arg
    else:
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()
