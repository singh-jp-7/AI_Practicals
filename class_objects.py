class Student(object):
    def __init__(self):
        self.name = None
        self.roll_no = None


class CSE(object):
    def __init__(self):
        self.students =[]

    def add_students(self):
        s = Student()
        s.name = input("Please enter the student name :")
        s.roll_no = input("Please enter the student roll number :")
        self.students.append(s)

    def display_details(self):
        print("**********************")

        for i in self.students:
            print("Name : ", i.name)
            print("Roll number : ", i.roll_no )

        print("*************************")


cse = CSE()

cse.add_students()
cse.display_details()
