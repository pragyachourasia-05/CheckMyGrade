class Student:
    def __init__(self, email_address, first_name, last_name, course_id, grades, marks):
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
        self.course_id = course_id
        self.grades = grades
        self.marks = marks

    def to_dict(self):
        return {
            "Email_address": self.email_address,
            "First_name": self.first_name,
            "Last_name": self.last_name,
            "Course.id": self.course_id,
            "grades": self.grades,
            "Marks": str(self.marks)
        }

    def display_records(self):
        return self.to_dict()

    def add_new_student(self):
        return f"Student {self.email_address} added"

    def delete_new_student(self):
        return f"Student {self.email_address} deleted"

    def check_my_grades(self):
        return self.grades

    def update_student_record(self, first_name=None, last_name=None, course_id=None, grades=None, marks=None):
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if course_id is not None:
            self.course_id = course_id
        if grades is not None:
            self.grades = grades
        if marks is not None:
            self.marks = marks

    def check_my_marks(self):
        return self.marks