import pytest
from test_psym import *
import os
import shutil
import json
import subprocess

def setup_module(module):
    run_tests_and_coverage()

def test_example1():
    # Load the coverage data
    current_coverage = load_coverage_data('examples/coverage.json')
    reference_coverage = load_coverage_data('reference_coverage.json')

    # Compare the coverage data
    assert compare_executed_lines(current_coverage, reference_coverage, 'example1.py')