import pytest
import os
import shutil
import json
import subprocess

def load_coverage_data(filename):
    """Load coverage data from a JSON file."""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def compare_executed_lines(current_data, reference_data, target_file):
    """Compare executed lines between current and reference coverage data."""

    if target_file in reference_data['files']:
        current_executed = set(current_data['files'][target_file]['executed_lines'])
        reference_executed = set(reference_data['files'][target_file]['executed_lines'])
        
        only_in_current = current_executed - reference_executed
        only_in_reference = reference_executed - current_executed
        
        if only_in_current or only_in_reference:
            print(f"Differences in {target_file}:")
            if only_in_current:
                print(f"  Only in current: {sorted(only_in_current)}")
            if only_in_reference:
                print(f"  Only in reference: {sorted(only_in_reference)}")
            return False
    else:
        print(f"File {target_file} is not present in the reference coverage.")
        return False

    return True


def run_tests_and_coverage():
    # Navigate to the examples directory
    examples_dir = "examples/"
    
    # First command: run pytest with coverage in the examples directory
    pytest_command = f"coverage run -m pytest"
    # Second command: generate the coverage report
    coverage_report_command = "coverage json -o coverage.json"
    
    try:
        # Reset the coverage data
        if os.path.exists(".coverage"):
            os.remove(".coverage")

        if os.path.exists("coverage.json"):
            os.remove("coverage.json")

        if os.path.exists(".pytest_cache"):
            shutil.rmtree(".pytest_cache")

        if os.path.exists("__pycache__"):
            shutil.rmtree("__pycache__")

        
        target_example_files = ["examples/example1.py", "examples/example2.py", "examples/example3.py", "examples/example4.py", "examples/example5.py", "examples/example6.py"]

        generated_test_files = ["examples/test_example1.py", "examples/test_example2.py", "examples/test_example3.py", "examples/test_example4.py", "examples/test_example5.py", "examples/test_example6.py"]

        # Remove the generated test files
        for test_file in generated_test_files:
            if os.path.exists(test_file):
                os.remove(test_file)

        # Run the assignment script for example python files
        for example_file in target_example_files:
            result = subprocess.run(["python", "psym.py", "-t", example_file], check=True)

        # Execute the pytest command within the examples directory
        print('Running pytest with example files')
        result = subprocess.run(pytest_command, shell=True, cwd=examples_dir, check=True)
        
        # Execute the coverage report command in the same directory
        report_result = subprocess.run(coverage_report_command, shell=True, cwd=examples_dir, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        assert os.path.exists("examples/coverage.json"), "Coverage report was not generated"

        print("Coverage report generated successfully")
        
    except subprocess.CalledProcessError as e:
        print("An error occurred while running the commands:")
        print(e.stderr.decode())