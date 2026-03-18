class Professor:
    def __init__(self, professor_id, professor_name, rank, course_id):
        self.professor_id = professor_id
        self.professor_name = professor_name
        self.rank = rank
        self.course_id = course_id

    def to_dict(self):
        return {
            "Professor_id": self.professor_id,
            "Professor Name": self.professor_name,
            "Rank": self.rank,
            "Course.id": self.course_id
        }

    def professors_details(self):
        return self.to_dict()

    def add_new_professor(self):
        return f"Professor {self.professor_id} added"

    def delete_professor(self):
        return f"Professor {self.professor_id} deleted"

    def modify_professor_details(self, professor_name=None, rank=None, course_id=None):
        if professor_name is not None:
            self.professor_name = professor_name
        if rank is not None:
            self.rank = rank
        if course_id is not None:
            self.course_id = course_id

    def show_course_details_by_professor(self):
        return {
            "Professor_id": self.professor_id,
            "Professor Name": self.professor_name,
            "Course.id": self.course_id
        }