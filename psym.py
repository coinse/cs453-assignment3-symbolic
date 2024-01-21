import argparse
import sys


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate test data using \
        symbolic execution.')
    parser.add_argument('-t', '--target', required=True,\
     help="the target file to symbolically execute")
    parser.add_argument('-o', '--output', required=True,\
     help="the output file to store the generated PyTest testcases")
    args = parser.parse_args()

    target = args.target
    output = args.output
    
    # perform the symbolic execution
    # ...

    # generate PyTest unit test cases
    # ...