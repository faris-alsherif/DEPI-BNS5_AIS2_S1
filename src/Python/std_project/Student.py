class Student:
    _id_counter = 1 #class attribute
    def __init__(self, name):
        self.student_id = Student._id_counter
        Student._id_counter +=1
        self.name = name
        self.grades = {}
        self.enrolled_courses =[]

    def __str__(self):
        return f"Student ID: {self.student_id}, name: {self.name}, Grades: {self.grades}, Courses: {self.enrolled_courses}"

    def __repr__(self) -> str:
        return f"Student ID: {self.student_id}  name:{self.name}, Grades: {self.grades}, Courses: {self.enrolled_courses}"

    def add_grade(self, course_id, grade):
        if not 0<= grade <=100:
            raise ValueError("grade must be between 0 and 100")
        self.grades[course_id] = grade

    def enroll_in_course(self, course):
        if course in self.enrolled_courses:
            raise ValueError("student already enrolled in this course")
        else:
            self.enrolled_courses.append(course)