import csv
import os
# ---------- STUDENT ------------
#--------------------------------#
STUDENT_FIELDS = [
    "Email_address",
    "First_name",
    "Last_name",
    "Course.id",
    "grades",
    "Marks"
]

def initialize_student_csv(filename):
    if not os.path.exists(filename):
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=STUDENT_FIELDS)
            writer.writeheader()

def read_students(filename):

    students = []
    if not os.path.exists(filename):
        return students

    with open(filename, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        # check headers
        if reader.fieldnames != STUDENT_FIELDS:
            print("CSV header mismatch. Recreating student file.")
            initialize_student_csv(filename)
            return []

        for row in reader:
            students.append(row)

    return students

def write_students(filename, students):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=STUDENT_FIELDS)
        writer.writeheader()
        for row in students:
            writer.writerow(row)

# def add_student(filename, student):
#     students = read_students(filename)
#     for existing_student in students:
#         if existing_student.get("Email_address", "").lower() == student.email_address.lower():
#             print("Student already exists.")
#             return False
#     students.append(student.to_dict())
#     write_students(filename, students)
#     return True

def add_student(filename, student):
    if not student.email_address or not student.course_id:
        print("Student email and course id must not be null.")
        return False

    students = read_students(filename)
    for existing_student in students:
        if existing_student.get("Email_address", "").lower() == student.email_address.lower():
            print("Student already exists.")
            return False

    students.append(student.to_dict())
    write_students(filename, students)
    return True

def search_stu_by_email(filename, email_address):
    students = read_students(filename)
    for student in students:
        if student.get("Email_address", "").lower() == email_address.lower():
            return student
    return None

def delete_student(filename, email_address):
    students = read_students(filename)
    updated_students = []
    found = False
    for student in students:
        if student["Email_address"].lower() == email_address.lower():
            found = True
            # skip adding -> delete
        else:
            updated_students.append(student)
    if found:
        write_students(filename, updated_students)
        return True
    return False

def update_student(filename, email_address, new_first_name, new_last_name, new_course_id, new_grades, new_marks):
    students = read_students(filename)
    found = False
    for student in students:
        if student["Email_address"].lower() == email_address.lower():
            student["First_name"] = new_first_name
            student["Last_name"] = new_last_name
            student["Course.id"] = new_course_id
            student["grades"] = new_grades
            student["Marks"] = str(new_marks)
            found = True
            break
    if found:
        write_students(filename, students)
        return True
    return False

def sort_stnd_by_marks(filename, reverse=False):
    students = read_students(filename)
    # handle empty and ensure Marks present
    def keyfn(s):
        try:
            return int(s.get("Marks", "0"))
        except ValueError:
            return 0
    return sorted(students, key=lambda student: int(student.get("Marks", 0)), reverse=reverse)

def sort_stnd_by_email(filename, reverse=False):
    students = read_students(filename)
    return sorted(students, key=lambda s: s.get("Email_address","").lower(), reverse=reverse)


# ---------- PROFESSOR ------------#
#----------------------------------#
PROFESSOR_FIELDS = [
    "Professor_id",
    "Professor Name",
    "Rank",
    "Course.id"
]

def initialize_professor_csv(filename):
    if not os.path.exists(filename):
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=PROFESSOR_FIELDS)
            writer.writeheader()

def read_professors(filename):
    professors = []
    if os.path.exists(filename):
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                professors.append(row)
    return professors

def write_professors(filename, professors):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=PROFESSOR_FIELDS)
        writer.writeheader()
        for p in professors:
            writer.writerow(p)

# def add_professor(filename, professor):
#     professors = read_professors(filename)
#     for existing in professors:
#         if existing["Professor_id"].lower() == professor.professor_id.lower():
#             print("Professor already exists.")
#             return False
#     professors.append(professor.to_dict())
#     write_professors(filename, professors)
#     return True

def add_professor(filename, professor):
    if not professor.professor_id or not professor.course_id:
        print("Professor id and course id must not be null.")
        return False

    professors = read_professors(filename)
    for existing in professors:
        if existing.get("Professor_id", "").lower() == professor.professor_id.lower():
            print("Professor already exists.")
            return False

    professors.append(professor.to_dict())
    write_professors(filename, professors)
    return True

def search_professor_by_id(filename, professor_id):
    professors = read_professors(filename)
    for p in professors:
        if p["Professor_id"].lower() == professor_id.lower():
            return p
    return None

def update_professor(filename, professor_id, new_name, new_rank, new_course_id):
    professors = read_professors(filename)
    found = False
    for p in professors:
        if p["Professor_id"].lower() == professor_id.lower():
            p["Professor Name"] = new_name
            p["Rank"] = new_rank
            p["Course.id"] = new_course_id
            found = True
            break
    if found:
        write_professors(filename, professors)
        return True
    return False

def delete_professor(filename, professor_id):
    professors = read_professors(filename)
    updated = []
    found = False
    for p in professors:
        if p["Professor_id"].lower() == professor_id.lower():
            found = True
        else:
            updated.append(p)
    if found:
        write_professors(filename, updated)
        return True
    return False

# --------- COURSE section ----------------#
#------------------------------------------#

COURSE_FIELDS = [
    "Course_id",
    "Course_name",
    "Description"
]

def initialize_course_csv(filename):
    if not os.path.exists(filename):
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, COURSE_FIELDS)
            writer.writeheader()
def read_courses(filename):
    courses = []
    if os.path.exists(filename):
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                courses.append(row)
    return courses

def write_courses(filename, courses):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=COURSE_FIELDS)
        writer.writeheader()
        for c in courses:
            writer.writerow(c)

def add_course(filename, course):
    if not course.course_id:
        print("Course id must not be null.")
        return False

    courses = read_courses(filename)
    for existing in courses:
        if existing.get("Course_id", "").lower() == course.course_id.lower():
            print("Course already exists.")
            return False

    courses.append(course.to_dict())
    write_courses(filename, courses)
    return True

def search_course_by_id(filename, course_id):
    courses = read_courses(filename)
    for c in courses:
        if c.get("Course_id","").lower() == course_id.lower():
            return c
    return None

def update_course(filename, course_id, new_course_name, new_description):
    courses = read_courses(filename)
    found = False
    for c in courses:
        if c.get("Course_id","").lower() == course_id.lower():
            c["Course_name"] = new_course_name
            c["Description"] = new_description
            found = True
            break
    if found:
        write_courses(filename, courses)
        return True
    return False

def delete_course(filename, course_id):
    courses = read_courses(filename)
    updated = []
    found = False
    for c in courses:
        if c.get("Course_id","").lower() == course_id.lower():
            found = True
        else:
            updated.append(c)
    if found:
        write_courses(filename, updated)
        return True
    return False

# --- -----LOGIN (encrypted passwords)---- ---#
#-----------# ---------- LOGIN SECTION ----------
from security import TextSecurity

cipher = TextSecurity(4)

LOGIN_FIELDS = [
    "User_id",
    "Password",
    "Role"
]


def initialize_login_csv(filename):
    if not os.path.exists(filename):
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=LOGIN_FIELDS)
            writer.writeheader()


def read_logins(filename):
    logins = []

    if os.path.exists(filename):
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                logins.append(row)

    return logins


def write_logins(filename, logins):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=LOGIN_FIELDS)
        writer.writeheader()
        for login in logins:
            writer.writerow(login)


def add_user(filename, login_user):
    logins = read_logins(filename)

    for existing in logins:
        if existing["User_id"].lower() == login_user.user_id.lower():
            print("User already exists.")
            return False

    encrypted_password = cipher.encrypt(login_user.password)

    row = {
        "User_id": login_user.user_id,
        "Password": encrypted_password,
        "Role": login_user.role
    }

    logins.append(row)
    write_logins(filename, logins)
    return True


def authenticate_user(filename, user_id, password):
    logins = read_logins(filename)

    for row in logins:
        if row["User_id"].lower() == user_id.lower():
            decrypted = cipher.decrypt(row["Password"])

            if decrypted == password:
                return row["Role"]
            else:
                return None

    return None


def change_password(filename, user_id, new_password):
    logins = read_logins(filename)
    found = False

    for row in logins:
        if row["User_id"].lower() == user_id.lower():
            row["Password"] = cipher.encrypt(new_password)
            found = True
            break

    if found:
        write_logins(filename, logins)
        return True

    return False

# ----------Calculations & report ------------#
#----------------------------------------------#

def cal_avg_for_course(filename, course_id):
    students = read_students(filename)

    marks_list = []
    for student in students:
        if student.get("Course.id", "").lower() == course_id.lower():
            marks_list.append(int(student.get("Marks", 0)))

    if not marks_list:
        return 0

    return sum(marks_list) / len(marks_list)


def cal_median_for_course(filename, course_id):
    students = read_students(filename)

    marks_list = []
    for student in students:
        if student.get("Course.id", "").lower() == course_id.lower():
            marks_list.append(int(student.get("Marks", 0)))

    if not marks_list:
        return 0

    marks_list.sort()
    n = len(marks_list)

    if n % 2 == 1:
        return marks_list[n // 2]
    else:
        return (marks_list[n // 2 - 1] + marks_list[n // 2]) / 2


def report_by_course(filename, course_id):
    students = read_students(filename)

    result = []
    for student in students:
        if student.get("Course.id", "").lower() == course_id.lower():
            result.append(student)

    return result


def report_by_student(filename, email_address):
    return search_stu_by_email(filename, email_address)


def report_by_professor(professor_file, student_file, professor_id):
    professor = search_professor_by_id(professor_file, professor_id)

    if not professor:
        return []

    course_id = professor.get("Course.id", "")
    if not course_id:
        return []

    return report_by_course(student_file, course_id)