import csv
import sys

# Map letter grades to grade point scalers
letter_map = {
    'A': 4,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'D-': 0.7,
    'F': 0
}


def calculate_grade_points(courses: list) -> float:
    """From a list of courses, calculate the total grade points

    Args:
        courses (list): List of courses (Name, Grade, Credit Hours)

    Returns:
        float: Total grade points
    """
    grade_points = 0

    for course in courses:
        grade_points += int(course[2]) * letter_map[course[1]]

    return grade_points


def calculate_credit_hours(courses: list) -> int:
    """From a list of courses, calculate total credit hours

    Args:
        courses (list): List of courses (Name, Grade, Credit Hours)

    Returns:
        int: Total credit hours
    """
    credit_hours = 0

    for course in courses:
        credit_hours += int(course[2])

    return credit_hours


if __name__ == '__main__':
    # CSV column names
    header = ['Class Name', 'Letter Grade', 'Credit Hours']
    courses = []

    # Open CSV from filepath provided in command arguments
    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            # Skip over column names
            if row == header:
                continue

            # Add course array from CSV to the courses array
            courses.append(row)

    # Calculate grade points
    grade_points = calculate_grade_points(courses)

    # Calculate credit hours
    credit_hours = calculate_credit_hours(courses)

    # Calculate GPA and round to 2 decimal places
    gpa = grade_points / credit_hours
    gpa = round(gpa, 2)

    print('GPA:', gpa)
