def calculate_grade(marks):
    """Determine grade based on marks using if-elif-else"""
    if not isinstance(marks, int):
        raise ValueError("Marks must be an integer")
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")
    
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

def check_attendance(attendance):
    """Check attendance eligibility using if-else"""
    if not isinstance(attendance, float):
        raise ValueError("Attendance must be a float")
    if attendance < 0 or attendance > 100:
        raise ValueError("Attendance must be between 0 and 100")
    
    if attendance >= 75.0:
        return "Eligible"
    else:
        return "Not Eligible"

def check_assignments(assignments_completed):
    """Check assignment completion status using if"""
    if not isinstance(assignments_completed, int):
        raise ValueError("Assignments completed must be an integer")
    if assignments_completed < 0 or assignments_completed > 10:
        raise ValueError("Assignments completed must be between 0 and 10")
    
    if assignments_completed == 10:
        return "Complete"
    return "Incomplete"

def determine_final_status(grade, attendance_status, assignment_status):
    """Determine final status using nested if"""
    if attendance_status == "Eligible":
        if assignment_status == "Complete":
            if grade in ['A', 'B', 'C']:
                return "Passed with Good Standing"
            elif grade == 'D':
                return "Passed with Warning"
            else:
                return "Failed - Poor Performance"
        else:
            return "Failed - Incomplete Assignments"
    else:
        return "Failed - Poor Attendance"

if __name__ == "__main__":
    print("Student Grade and Status Calculator")
    print("=" * 35)
    
    # Input Section
    try:
        marks = int(input("Enter marks (0-100): "))
        attendance = float(input("Enter attendance percentage (0-100): "))
        assignments_completed = int(input("Enter completed assignments (0-10): "))
        
        # Processing Section
        grade = calculate_grade(marks)
        attendance_status = check_attendance(attendance)
        assignment_status = check_assignments(assignments_completed)
        final_status = determine_final_status(grade, attendance_status, assignment_status)
        
        # Output Section
        print("\nStudent Status Report")
        print("-" * 35)
        print(f"Grade: {grade}")
        print(f"Attendance Status: {attendance_status}")
        print(f"Assignment Status: {assignment_status}")
        print(f"Final Result: {final_status}")
        print("=" * 35)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 