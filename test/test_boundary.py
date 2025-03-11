import pytest
from test.TestUtils import TestUtils
from grade_calculator_and_status_console import *

test_obj = TestUtils()

def test_grade_and_attendance_boundary():
    """Test grade and attendance calculation with boundary values"""
    try:
        # Grade boundaries
        grade_min = calculate_grade(0) == 'F'
        grade_max = calculate_grade(100) == 'A'
        grade_a_boundary = calculate_grade(90) == 'A'
        grade_b_boundary = calculate_grade(89) == 'B'
        
        # Attendance boundaries
        attendance_min = check_attendance(0.0) == "Not Eligible"
        attendance_max = check_attendance(100.0) == "Eligible"
        attendance_threshold = check_attendance(75.0) == "Eligible"
        attendance_below = check_attendance(74.9) == "Not Eligible"
        
        all_passed = all([grade_min, grade_max, grade_a_boundary, grade_b_boundary,
                          attendance_min, attendance_max, attendance_threshold, attendance_below])
        
        test_obj.yakshaAssert("TestGradeAndAttendanceBoundary", all_passed, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestGradeAndAttendanceBoundary", False, "boundary")

def test_assignments_and_status_boundary():
    """Test assignments and final status with boundary cases"""
    try:
        # Assignment boundaries
        assignment_min = check_assignments(0) == "Incomplete"
        assignment_max = check_assignments(10) == "Complete"
        assignment_below = check_assignments(9) == "Incomplete"
        
        # Final status boundaries
        status_best = determine_final_status('A', "Eligible", "Complete") == "Passed with Good Standing"
        status_worst = determine_final_status('F', "Not Eligible", "Incomplete") == "Failed - Poor Attendance"
        status_warning = determine_final_status('D', "Eligible", "Complete") == "Passed with Warning"
        
        all_passed = all([assignment_min, assignment_max, assignment_below,
                          status_best, status_worst, status_warning])
        
        test_obj.yakshaAssert("TestAssignmentsAndStatusBoundary", all_passed, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestAssignmentsAndStatusBoundary", False, "boundary")