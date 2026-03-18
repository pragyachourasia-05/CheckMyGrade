class Grades:
    GRADE_RANGES = [
        ("A+", 97, 100),
        ("A", 93, 96),
        ("A-", 90, 92),
        ("B+", 87, 89),
        ("B", 83, 86),
        ("B-", 80, 82),
        ("C+", 77, 79),
        ("C", 73, 76),
        ("C-", 70, 72),
        ("D", 60, 69),
        ("F", 0, 59),
    ]

    def __init__(self, grade_id, grade, marks_range):
        if not grade_id or not str(grade_id).strip():
            raise ValueError("grade_id cannot be empty or null.")

        self.grade_id = str(grade_id).strip()
        self.grade = str(grade).strip()
        self.marks_range = marks_range

    @classmethod
    def get_letter_grade(cls, marks):
        try:
            marks = int(marks)
        except (ValueError, TypeError):
            return "N/A"

        for letter, low, high in cls.GRADE_RANGES:
            if low <= marks <= high:
                return letter
        return "F"

    def display_grade_report(self):
        return {
            "Grade_id": self.grade_id,
            "Grade": self.grade,
            "Marks_range": str(self.marks_range),
        }

    def add_grade(self, grades_list):
        for existing in grades_list:
            if existing.get("Grade_id", "").lower() == self.grade_id.lower():
                print(f"Grade '{self.grade_id}' already exists.")
                return False
        grades_list.append(self.to_dict())
        return True

    def delete_grade(self, grades_list):
        for i, g in enumerate(grades_list):
            if g.get("Grade_id", "").lower() == self.grade_id.lower():
                grades_list.pop(i)
                return True
        print(f"Grade '{self.grade_id}' not found.")
        return False

    def modify_grade(self, grades_list, new_grade, new_marks_range):
        for g in grades_list:
            if g.get("Grade_id", "").lower() == self.grade_id.lower():
                g["Grade"] = new_grade
                g["Marks_range"] = str(new_marks_range)
                self.grade = new_grade
                self.marks_range = new_marks_range
                return True
        print(f"Grade '{self.grade_id}' not found.")
        return False

    def to_dict(self):
        return {
            "Grade_id": self.grade_id,
            "Grade": self.grade,
            "Marks_range": str(self.marks_range),
        }

    def __repr__(self):
        return f"Grades(id={self.grade_id!r}, grade={self.grade!r}, range={self.marks_range!r})"