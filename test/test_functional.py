import pytest
import re
import inspect
from test.TestUtils import TestUtils
from grade_calculator_and_status_console import *

test_obj = TestUtils()

def test_function_definitions():
    """Test if required functions are defined with proper structures"""
    try:
        with open('grade_calculator_and_status_console.py', 'r') as file:
            content = file.read()
        
        # Check function definitions
        required_functions = {
            'calculate_grade': r'def\s+calculate_grade\s*\(',
            'check_attendance': r'def\s+check_attendance\s*\(',
            'check_assignments': r'def\s+check_assignments\s*\(',
            'determine_final_status': r'def\s+determine_final_status\s*\('
        }
        
        all_funcs_found = True
        for func_name, pattern in required_functions.items():
            if not re.search(pattern, content):
                all_funcs_found = False
                break
        
        test_obj.yakshaAssert("TestFunctionDefinitions", all_funcs_found, "functional")
    except Exception:
        test_obj.yakshaAssert("TestFunctionDefinitions", False, "functional")

def test_conditional_structures():
    """Test if required conditional structures are used"""
    try:
        # Check if-elif-else in grade calculation
        grade_code = inspect.getsource(calculate_grade)
        has_grade_conditionals = ("if" in grade_code and 
                                 "elif" in grade_code and 
                                 "else" in grade_code)
        
        # Check if-else in attendance check
        attendance_code = inspect.getsource(check_attendance)
        has_attendance_conditionals = ("if" in attendance_code and 
                                      "else" in attendance_code)
        
        # Check if in assignments check
        assignments_code = inspect.getsource(check_assignments)
        has_assignments_conditional = "if" in assignments_code
        
        # Check nested if in final status
        status_code = inspect.getsource(determine_final_status)
        has_nested_conditionals = status_code.count("if") >= 2
        
        all_conditionals_present = (has_grade_conditionals and 
                                   has_attendance_conditionals and 
                                   has_assignments_conditional and 
                                   has_nested_conditionals)
        
        test_obj.yakshaAssert("TestConditionalStructures", all_conditionals_present, "functional")
    except Exception:
        test_obj.yakshaAssert("TestConditionalStructures", False, "functional")

def test_calculation_logic():
    """Test if calculation logic is implemented correctly"""
    try:
        # Test grade calculation logic
        grade_correct = (calculate_grade(95) == 'A' and
                        calculate_grade(85) == 'B' and
                        calculate_grade(75) == 'C' and
                        calculate_grade(65) == 'D' and
                        calculate_grade(55) == 'F')
        
        # Test attendance logic
        attendance_correct = (check_attendance(80.0) == "Eligible" and
                             check_attendance(70.0) == "Not Eligible" and
                             check_attendance(75.0) == "Eligible")
        
        # Test assignments logic
        assignments_correct = (check_assignments(10) == "Complete" and
                              check_assignments(9) == "Incomplete" and
                              check_assignments(0) == "Incomplete")
        
        all_logic_correct = grade_correct and attendance_correct and assignments_correct
        
        test_obj.yakshaAssert("TestCalculationLogic", all_logic_correct, "functional")
    except Exception:
        test_obj.yakshaAssert("TestCalculationLogic", False, "functional")

def test_final_status_logic():
    """Test if final status determination logic is correct"""
    try:
        # Test all major status combinations
        good_standing = determine_final_status('A', "Eligible", "Complete") == "Passed with Good Standing"
        warning = determine_final_status('D', "Eligible", "Complete") == "Passed with Warning"
        poor_performance = determine_final_status('F', "Eligible", "Complete") == "Failed - Poor Performance"
        incomplete_assignments = determine_final_status('A', "Eligible", "Incomplete") == "Failed - Incomplete Assignments"
        poor_attendance = determine_final_status('A', "Not Eligible", "Complete") == "Failed - Poor Attendance"
        
        status_logic_correct = (good_standing and warning and 
                               poor_performance and incomplete_assignments and 
                               poor_attendance)
        
        test_obj.yakshaAssert("TestFinalStatusLogic", status_logic_correct, "functional")
    except Exception:
        test_obj.yakshaAssert("TestFinalStatusLogic", False, "functional")