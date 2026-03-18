# main.py
from student import Student
from professor import Professor
from course import Course
from grade import Grades
from login_user import LoginUser
from csv_manager import (
    initialize_student_csv, add_student, read_students, search_stu_by_email,
    delete_student, update_student, sort_stnd_by_marks, sort_stnd_by_email,
    initialize_professor_csv, add_professor, read_professors,
    search_professor_by_id, update_professor, delete_professor,
    initialize_course_csv, add_course, read_courses, search_course_by_id,
    update_course, delete_course, initialize_login_csv, add_user, authenticate_user, change_password,
    read_logins, cal_avg_for_course, cal_median_for_course, report_by_course, report_by_student,
    report_by_professor
)


STUDENT_FILE = "students.csv"
PROFESSOR_FILE = "professors.csv"
COURSE_FILE = "courses.csv"

def student_section():
    initialize_student_csv(STUDENT_FILE)

    student1 = Student(
        "ashik@sjsu.edu",
        "Ashi krish",
        "Chourasia",
        "DATA200",
        "A",
        95
    )

    added = add_student(STUDENT_FILE, student1)

    if added:
        print("Student Added Successfully")
    else:
        print("Student already exists.\nStudent was not added")

    print("\nStudents in file:")
    students = read_students(STUDENT_FILE)
    for s in students:
        print(s)

    print("\nSearching for ashik@sjsu.edu...")
    found = search_stu_by_email(STUDENT_FILE, "ashi@sjsu.edu")
    if found:
        print("Student found:")
        print(found)
    else:
        print("Student not found.")

    print("\nUpdating ashik@sjsu.edu...")
    updated = update_student(
        STUDENT_FILE,
        "ashi@sjsu.edu",
        "ashi krish",
        "Chourasia",
        "DATA200",
        "A+",
        98
    )
    if updated:
        print("Student updated successfully.")
    else:
        print("Student not found.")

    print("\nStudents after update:")
    for s in read_students(STUDENT_FILE):
        print(s)

    print("\nStudents sorted by marks:")
    for s in sort_stnd_by_marks(STUDENT_FILE):
        print(s)

    print("\nStudents sorted by email:")
    for s in sort_stnd_by_email(STUDENT_FILE):
        print(s)

def professor_section():
    print("\n--- Professor Section ---")
    initialize_professor_csv(PROFESSOR_FILE)

    prof1 = Professor("modi@sjsu.edu", "Jimmy Modi", "Principle Professor", "DATA200")

    added_prof = add_professor(PROFESSOR_FILE, prof1)
    if added_prof:
        print("Professor added successfully.")
    else:
        print("Professor not added successfully.")

    print("\nProfessors in file:")
    for p in read_professors(PROFESSOR_FILE):
        print(p)

    print("\nSearching for modi@sjsu.edu...")
    found = search_professor_by_id(PROFESSOR_FILE, "modi@sjsu.edu")
    if found:
        print("Professor found:")
        print(found)
    else:
        print("Professor not found.")

    print("\nUpdating modi@sjsu.edu...")
    updated = update_professor(PROFESSOR_FILE, "modi@sjsu.edu", "Jimmy Modi", "Senior Professor", "DATA200")
    if updated:
        print("Professor updated successfully.")
    else:
        print("Professor not found.")

    print("\nProfessors after update:")
    for p in read_professors(PROFESSOR_FILE):
        print(p)

    # print("\nDeleting modi@sjsu.edu...")
    # deleted = delete_professor(PROFESSOR_FILE, "modi@sjsu.edu")
    # if deleted:
    #     print("Professor deleted successfully.")
    # else:
    #     print("Professor not found.")
    #
    # print("\nProfessors after deletion:")
    # for p in read_professors(PROFESSOR_FILE):
    #     print(p)

def course_section():
    print("\n--- Course Section ---")
    initialize_course_csv(COURSE_FILE)

    course1 = Course("DATA200", "Data Science", "Provides insight about DS and Python")
    added = add_course(COURSE_FILE, course1)
    if added:
        print("Course added successfully.")
    else:
        print("Course already exists.")

    print("\nCourses in file:")
    for c in read_courses(COURSE_FILE):
        print(c)

    # -------- SEARCH --------
    print("\nSearching for DATA200...")
    found_course = search_course_by_id(COURSE_FILE, "DATA200")

    if found_course:
        print("Course found:")
        print(found_course)
    else:
        print("Course not found.")

    # -------- UPDATE --------
    print("\nUpdating DATA200...")
    updated_course = update_course(
        COURSE_FILE,
        "DATA200",
        "Advanced Data Science",
        "Covers ML, Python, and Data Analysis"
    )

    if updated_course:
        print("Course updated successfully.")
    else:
        print("Course not found.")

    print("\nCourses after update:")
    courses = read_courses(COURSE_FILE)
    for course in courses:
        print(course)

    # -------- DELETE --------
    # print("\nDeleting DATA200...")
    # deleted_course = delete_course(COURSE_FILE, "DATA200")
    #
    # if deleted_course:
    #     print("Course deleted successfully.")
    # else:
    #     print("Course not found.")
    #
    # print("\nCourses after deletion:")
    # courses = read_courses(COURSE_FILE)
    # for course in courses:
    #     print(course)
    course_readd = Course("DATA200", "Data Science", "Provides insight about DS and Python")
    add_course(COURSE_FILE, course_readd)

def login_section():
    print("\n--- Login Section ---")
    LOGIN_FILE = "login.csv"
    initialize_login_csv(LOGIN_FILE)

    user = LoginUser("modi@sjsu.edu", "Welcome12#_", "professor")

    added = add_user(LOGIN_FILE, user)
    if added:
        print("User added successfully.")
    else:
        print("User not added (maybe already exists).")

    print("\nLogin file contents:")
    logins = read_logins(LOGIN_FILE)
    for login in logins:
        print(login)

    print("\nAuthenticating with original password...")
    role = authenticate_user(LOGIN_FILE, "modi@sjsu.edu", "Welcome12#_")
    if role:
        print(f"Authenticated. Role: {role}")
        print("Logout successful.")
    else:
        print("Authentication failed.")

    print("\nChanging password...")
    changed = change_password(LOGIN_FILE, "modi@sjsu.edu", "NewPass123!")
    if changed:
        print("Password changed.")
    else:
        print("Password change failed.")

    print("\nAuthenticating with new password...")
    role = authenticate_user(LOGIN_FILE, "modi@sjsu.edu", "NewPass123!")
    if role:
        print(f"Authenticated after password change. Role: {role}")
    else:
        print("Authentication failed after password change.")

    print("\nLogin file after password change:")
    logins = read_logins(LOGIN_FILE)
    for login in logins:
        print(login)

def cal_and_report_section():
    print("\n--- Calculation and Report Section ---")

    STUDENT_FILE = "students.csv"
    PROFESSOR_FILE = "professors.csv"

    print("\nAverage marks for DATA200:")
    avg = cal_avg_for_course(STUDENT_FILE, "DATA200")
    print(avg)

    print("\nMedian marks for DATA200:")
    median = cal_median_for_course(STUDENT_FILE, "DATA200")
    print(median)

    print("\nReport by course DATA200:")
    course_report = report_by_course(STUDENT_FILE, "DATA200")
    for student in course_report:
        print(student)

    print("\nReport by student ashi@sjsu.edu:")
    student_report = report_by_student(STUDENT_FILE, "ashi@sjsu.edu")
    print(student_report)

    print("\nReport by professor modi@sjsu.edu:")
    professor_report = report_by_professor(PROFESSOR_FILE, STUDENT_FILE, "modi@sjsu.edu")
    for student in professor_report:
        print(student)

def grade_demo():
    print("\n--- Grade Demo ---")

    grade_obj = Grades("G001", "A+", "97-100")

    print("Grade report:")
    print(grade_obj.display_grade_report())

    print("Letter grade from marks 95:")
    print(Grades.get_letter_grade(95))

def main():
    student_section()
    professor_section()
    course_section()
    login_section()
    cal_and_report_section()
    grade_demo()

if __name__ == "__main__":
    main()