import unittest
import os
import time

from student import Student
from professor import Professor
from course import Course

from csv_manager import (
    initialize_student_csv,
    add_student,
    read_students,
    search_stu_by_email,
    update_student,
    delete_student,
    sort_stnd_by_marks,
    sort_stnd_by_email,

    initialize_professor_csv,
    add_professor,
    read_professors,
    update_professor,
    delete_professor,

    initialize_course_csv,
    add_course,
    read_courses,
    update_course,
    delete_course
)

TEST_STUDENT_FILE = "test_students.csv"
TEST_PROFESSOR_FILE = "test_professors.csv"
TEST_COURSE_FILE = "test_courses.csv"

class TestCheckMyGrade(unittest.TestCase):

    def setUp(self):
        # remove old test files if they exist
        for filename in [TEST_STUDENT_FILE, TEST_PROFESSOR_FILE, TEST_COURSE_FILE]:
            if os.path.exists(filename):
                os.remove(filename)

        initialize_student_csv(TEST_STUDENT_FILE)
        initialize_professor_csv(TEST_PROFESSOR_FILE)
        initialize_course_csv(TEST_COURSE_FILE)

    def tearDown(self):
        # clean up after tests
        for filename in [TEST_STUDENT_FILE, TEST_PROFESSOR_FILE, TEST_COURSE_FILE]:
            if os.path.exists(filename):
                os.remove(filename)

    # ---------------- STUDENT TESTS ----------------

    def test_add_1000_students(self):
        for i in range(1000):
            student = Student(
                f"student{i}@sjsu.edu",
                f"First{i}",
                f"Last{i}",
                "DATA200",
                "A",
                80 + (i % 20)
            )
            added = add_student(TEST_STUDENT_FILE, student)
            self.assertTrue(added)

        students = read_students(TEST_STUDENT_FILE)
        self.assertEqual(len(students), 1000)
        print("Added 1000 student records successfully.")

    def test_modify_student(self):
        student = Student(
            "student1@sjsu.edu",
            "First1",
            "Last1",
            "DATA200",
            "A",
            85
        )
        add_student(TEST_STUDENT_FILE, student)

        updated = update_student(
            TEST_STUDENT_FILE,
            "student1@sjsu.edu",
            "UpdatedFirst",
            "UpdatedLast",
            "DATA201",
            "A+",
            99
        )

        self.assertTrue(updated)

        result = search_stu_by_email(TEST_STUDENT_FILE, "student1@sjsu.edu")
        self.assertIsNotNone(result)
        self.assertEqual(result["First_name"], "UpdatedFirst")
        self.assertEqual(result["Last_name"], "UpdatedLast")
        self.assertEqual(result["Course.id"], "DATA201")
        self.assertEqual(result["grades"], "A+")
        self.assertEqual(result["Marks"], "99")
        print("Student modification test passed.")

    def test_delete_student(self):
        student = Student(
            "student2@sjsu.edu",
            "First2",
            "Last2",
            "DATA200",
            "B",
            75
        )
        add_student(TEST_STUDENT_FILE, student)

        deleted = delete_student(TEST_STUDENT_FILE, "student2@sjsu.edu")
        self.assertTrue(deleted)

        result = search_stu_by_email(TEST_STUDENT_FILE, "student2@sjsu.edu")
        self.assertIsNone(result)
        print("Student deletion test passed.")

    def test_load_and_search_time(self):
        for i in range(1000):
            student = Student(
                f"student{i}@sjsu.edu",
                f"First{i}",
                f"Last{i}",
                "DATA200",
                "A",
                80 + (i % 20)
            )
            add_student(TEST_STUDENT_FILE, student)

        # simulate loading data from previous run
        loaded_students = read_students(TEST_STUDENT_FILE)
        self.assertEqual(len(loaded_students), 1000)

        start = time.perf_counter()
        result = search_stu_by_email(TEST_STUDENT_FILE, "student999@sjsu.edu")
        end = time.perf_counter()

        self.assertIsNotNone(result)
        print(f"Search time for 1000 student records: {end - start:.8f} seconds")

    def test_sort_students_time(self):
        for i in range(1000):
            student = Student(
                f"student{i}@sjsu.edu",
                f"First{i}",
                f"Last{i}",
                "DATA200",
                "A",
                80 + (i % 20)
            )
            add_student(TEST_STUDENT_FILE, student)

        start = time.perf_counter()
        sorted_marks = sort_stnd_by_marks(TEST_STUDENT_FILE)
        end = time.perf_counter()

        self.assertEqual(len(sorted_marks), 1000)
        print(f"Sort by marks time for 1000 students: {end - start:.8f} seconds")

        start = time.perf_counter()
        sorted_email = sort_stnd_by_email(TEST_STUDENT_FILE)
        end = time.perf_counter()

        self.assertEqual(len(sorted_email), 1000)
        print(f"Sort by email time for 1000 students: {end - start:.8f} seconds")

    # ---------------- COURSE TESTS ----------------

    def test_add_modify_delete_course(self):
        course = Course("DATA200", "Data Science", "Intro to DS")
        added = add_course(TEST_COURSE_FILE, course)
        self.assertTrue(added)

        courses = read_courses(TEST_COURSE_FILE)
        self.assertEqual(len(courses), 1)

        updated = update_course(
            TEST_COURSE_FILE,
            "DATA200",
            "Advanced Data Science",
            "Covers ML and Python"
        )
        self.assertTrue(updated)

        courses = read_courses(TEST_COURSE_FILE)
        self.assertEqual(courses[0]["Course_name"], "Advanced Data Science")

        deleted = delete_course(TEST_COURSE_FILE, "DATA200")
        self.assertTrue(deleted)

        courses = read_courses(TEST_COURSE_FILE)
        self.assertEqual(len(courses), 0)

        print("Course add/modify/delete test passed.")

    # ---------------- PROFESSOR TESTS ----------------

    def test_add_modify_delete_professor(self):
        professor = Professor(
            "modi@sjsu.edu",
            "Jimmy Modi",
            "Professor",
            "DATA200"
        )
        added = add_professor(TEST_PROFESSOR_FILE, professor)
        self.assertTrue(added)

        professors = read_professors(TEST_PROFESSOR_FILE)
        self.assertEqual(len(professors), 1)

        updated = update_professor(
            TEST_PROFESSOR_FILE,
            "modi@sjsu.edu",
            "Jimmy Modi",
            "Senior Professor",
            "DATA201"
        )
        self.assertTrue(updated)

        professors = read_professors(TEST_PROFESSOR_FILE)
        self.assertEqual(professors[0]["Rank"], "Senior Professor")

        deleted = delete_professor(TEST_PROFESSOR_FILE, "modi@sjsu.edu")
        self.assertTrue(deleted)

        professors = read_professors(TEST_PROFESSOR_FILE)
        self.assertEqual(len(professors), 0)

        print("Professor add/modify/delete test passed.")

    def test_sort_students_descending(self):
        for i in range(1000):
            student = Student(
                f"student{i}@sjsu.edu",
                f"First{i}",
                f"Last{i}",
                "DATA200",
                "A",
                80 + (i % 20)
            )
            add_student(TEST_STUDENT_FILE, student)

        sorted_marks_desc = sort_stnd_by_marks(TEST_STUDENT_FILE, reverse=True)
        self.assertEqual(len(sorted_marks_desc), 1000)

        first_marks = int(sorted_marks_desc[0]["Marks"])
        last_marks = int(sorted_marks_desc[-1]["Marks"])
        self.assertGreaterEqual(first_marks, last_marks)

        sorted_email_desc = sort_stnd_by_email(TEST_STUDENT_FILE, reverse=True)
        self.assertEqual(len(sorted_email_desc), 1000)

        first_email = sorted_email_desc[0]["Email_address"]
        last_email = sorted_email_desc[-1]["Email_address"]
        self.assertGreaterEqual(first_email, last_email)

        print("Descending sort test passed.")

    ###Delete
    def test_delete_student_with_1000_records(self):
        for i in range(1000):
            student = Student(
                f"student{i}@sjsu.edu",
                f"First{i}",
                f"Last{i}",
                "DATA200",
                "A",
                80 + (i % 20)
            )
            add_student(TEST_STUDENT_FILE, student)

        deleted = delete_student(TEST_STUDENT_FILE, "student500@sjsu.edu")
        self.assertTrue(deleted)

        students = read_students(TEST_STUDENT_FILE)
        self.assertEqual(len(students), 999)

        result = search_stu_by_email(TEST_STUDENT_FILE, "student500@sjsu.edu")
        self.assertIsNone(result)

        print("Deletion test with 1000 records passed.")

if __name__ == "__main__":
    unittest.main()