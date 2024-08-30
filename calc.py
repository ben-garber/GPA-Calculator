import csv
import sys

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
    grade_points = 0
    
    for course in courses:
        grade_points += int(course[2]) * letter_map[course[1]] 
    
    return grade_points

def calculate_credit_hours(courses: list) -> int:
    credit_hours = 0

    for course in courses:
        credit_hours += int(course[2])

    return credit_hours


if __name__ == '__main__':
    header = ['Class Name', 'Letter Grade', 'Credit Hours']
    classes = []

    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            if row == header:
                continue
            classes.append(row)

    grade_points = calculate_grade_points(classes)
    credit_hours = calculate_credit_hours(classes)

    gpa = grade_points / credit_hours
    gpa = round(gpa, 2)

    print('GPA:', gpa)
