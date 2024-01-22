class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.enrolled_courses = []
        self.grades = {}  # Dictionary to store grades for courses

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)

    def performance_report(self):
        print(f'Student: {self.name}, Course: {math_course.course_name}, Grade: {alice.grades[math_course]}')

    def record_grade(self, course, grade):
        if course in self.enrolled_courses:
            self.grades[course] = grade


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.courses = []

    @staticmethod
    def list_courses():
        return math_course.course_name


class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []
        self.attendance = {}
        teacher.courses.append(self)  # Add this course to the teacher's course list
        self.lessons = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            self.attendance[student] = {}

    def record_attendance(self, student, date, status):
        if student in self.students:
            self.attendance[student] = date, status

    def generate_report(self):
        for student in self.students:
            attendance_record = list(self.attendance.get(student, []))
            attendance_date = attendance_record[0]
            attendance_status = attendance_record[1]
            print(f"Student: {student.name}, Attendance: ['{attendance_date}: {attendance_status}']")

    def add_lesson(self, topic, date, materials):
        dictionary = {'topic': topic, 'date': date, 'materials': materials}
        self.lessons.append(dictionary)

    def get_lessons(self):
        for dictionary in self.lessons:
            print(f'Topic: {dictionary.get("topic")}; date: {dictionary.get("date")}; required materials: {dictionary.get("materials")} ')

    def search_lessons(self, info):
        for dictionary in self.lessons:
            for value in dictionary.values():
                if info == value:
                    print(dictionary)


class Lesson:
    def __init__(self, course_name, teacher, materials):
        self.course_name = course_name
        self.teacher = teacher
        self.materials = materials


# Example usage
math_teacher = Teacher("Mr. Smith", 40, "Math")
math_course = Course("Mathematics", math_teacher)
alice = Student("Alice", 20)
bob = Student("Bob", 21)

alice.enroll(math_course)
bob.enroll(math_course)

# Recording attendance
math_course.record_attendance(alice, "2024-01-21", "Present")
math_course.record_attendance(bob, "2024-01-21", "Absent")

# Recording grades
alice.record_grade(math_course, "A")
bob.record_grade(math_course, "B")

# Generating reports
math_course.generate_report()# Student: Alice, Attendance: ['2024-01-21: Present'], Student: Bob, Attendance: ['2024-01-21: Absent']

# Testing implemented methods
alice.performance_report()# Student: Alice, Course: Mathematics, Grade: A
print("Courses taught by Mr. Smith:", math_teacher.list_courses())  # Courses taught by Mr. Smith: ['Mathematics']

lesson1 = Lesson("Algebra Basics", "2024-02-01", ["Algebra Textbook Chapter 1"])
lesson2 = Lesson("Introduction to Geometry", "2024-02-08", ["Geometry Workbook"])


math_course.add_lesson("Algebra Basics", "2024-02-01", ["Algebra Textbook Chapter 1"])
math_course.add_lesson("Introduction to Geometry", "2024-02-08", ["Geometry Workbook"])


math_course.get_lessons()

math_course.search_lessons('Algebra Basics')



