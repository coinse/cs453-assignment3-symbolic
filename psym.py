import argparse
import sys

from z3 import *

# 1. Implement peer lightweight symbolic execution engine
class IntegerProxy:
    pass


class BoolProxy:
    pass



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate test data using \
        symbolic execution.')
    parser.add_argument('-t', '--target', required=True,\
     help="the target file to symbolically execute")
    args = parser.parse_args()

    target = args.target
    
    # 2. Perform the symbolic execution
    # ...

    # 3. Generate PyTest unit test cases
    # ...