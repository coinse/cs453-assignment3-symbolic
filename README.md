## CS453 Assignment 3: Lightweight Symbolic Execution Engine

The aim of this assignment is to implement a lightweight dynamic symbolic execution engine by exploiting the dynamic typing of Python as well as the [Z3 SAT solver](https://github.com/Z3Prover/z3) (we will use the Python wrapper, [z3-solver](https://pypi.org/project/z3-solver/)). You may want to use the [Z3 Python tutorial](https://ericpony.github.io/z3py-tutorial/guide-examples.htm) to get familiar with Z3. The final goal is to achieve as much branch coverage as possible using symbolic execution.

### Peer Lightweight Approach

We will follow the [peer approach outlined by Bruni et al](Bruni2008.pdf). It is an intuitive and straightforward idea as long as we limit our scope to a subset of Python. 

The gist of it is that operator overloading in Python allows you to 
**intercept** operations performed to variables. For example, consider the 
following code snippet:

```python
x = 42
y = x + 2
```

A concrete execution will result in the program state in which `x` is equal to 
42, and `y` to 44. Symbolically, however, all we need to know is that `y` is 
now the value of `x` plus 2. This can be recorded by overloading the addition: 
`x + 2` is actually executed as a call to `x.__add__(2)`. Therefore, if you use 
a symbolic variable that you define, instead of a primitive integer, you can 
record the symbolic state of `y`. The linked article gives a very detailed 
explanation of the approach, and it is necessary that you read it before 
designing your engine. 

There are a few of design decisions you need to make:

- As covered in the class, we need to stop branch exploration when there are no more branch to cover. How will you know that no more "negating the last clause" is needed?
- You need to convert the final symbolic summaries of variables into a form that can be solved by z3-solver. Consult the tutorial for details.

### Objective

The repository contains the skeleton of `psym.py`, which contains code for the following arguments:

```python
$ python psym.py
usage: psym.py [-h] -t TARGET -o OUTPUT

Generate test data using symbolic execution.

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        the target file to symbolically execute
$
```

Each target file can contain multiple Python functions, which are written in the following subset of Python. You should try to symbolically execute all functions, even if one of the functions is called by another.

- A target function will only use integers as its arguments and local variables.
- It can use `if` branches, as well as `for` and `while` loops.
- Arithmetic expressions can use addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), power(`**`), and modulo (`%`).
- Predicates can use comparisons (`>`, `>=`, `<`, `<=`, `==`, `!=`) as well as Boolean operators (`and`, `or`, `not`).
- Note that predicates can include function calls.

The final output of your dynamic symbolic execution engine should be PyTest testcases: for each target `.py` file, generate a corresponding PyTest file, with the name being the prefix `test_` added to the original target file name. For example, if the target file is `example3.py`, then the generated PyTest file should be named `test_example3.py` and should be in the same directory as the target file. 

The PyTest testcases should use the results of dynamic symbolic execution to achieve branch coverage. We will use [coverage.py](https://coverage.readthedocs.io/en/7.4.0/) to measure branch coverage of the generated testcases, which will be part of the grade. Note that you do not need to generate any assertions: achieving branch coverage is enough.
