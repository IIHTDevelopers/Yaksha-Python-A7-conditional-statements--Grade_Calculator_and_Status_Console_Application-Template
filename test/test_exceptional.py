import pytest
from test.TestUtils import TestUtils
from grade_calculator_and_status_console import *

test_obj = TestUtils()

def test_input_validation_exceptions():
    """Test input validation across all calculation functions"""
    try:
        # Type validation
        with pytest.raises(ValueError):
            calculate_grade("90")  # String instead of int
        with pytest.raises(ValueError):
            check_attendance("75")  # String instead of float
        with pytest.raises(ValueError):
            check_assignments("5")  # String instead of int
            
        # Range validation
        with pytest.raises(ValueError):
            calculate_grade(-5)  # Negative marks
        with pytest.raises(ValueError):
            calculate_grade(101)  # Marks above 100
        with pytest.raises(ValueError):
            check_attendance(-10.0)  # Negative attendance
        with pytest.raises(ValueError):
            check_attendance(101.0)  # Attendance above 100
        with pytest.raises(ValueError):
            check_assignments(-1)  # Negative assignments
        with pytest.raises(ValueError):
            check_assignments(11)  # Assignments above 10
            
        test_obj.yakshaAssert("TestInputValidationExceptions", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestInputValidationExceptions", False, "exception")

def test_final_status_invalid_inputs():
    """Test final status determination with invalid inputs"""
    try:
        # Invalid grade still has sensible behavior
        invalid_grade = determine_final_status('X', "Eligible", "Complete") == "Failed - Poor Performance"
        
        # Invalid attendance status has sensible behavior
        invalid_attendance = determine_final_status('A', "Maybe", "Complete") == "Failed - Poor Attendance"
        
        # Invalid assignment status has sensible behavior
        invalid_assignment = determine_final_status('A', "Eligible", "Maybe") == "Failed - Incomplete Assignments"
        
        all_passed = invalid_grade and invalid_attendance and invalid_assignment
        
        test_obj.yakshaAssert("TestFinalStatusInvalidInputs", all_passed, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestFinalStatusInvalidInputs", False, "exception")