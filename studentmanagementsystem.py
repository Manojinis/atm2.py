class Student:
    def __init__(self, id, name, roll_no, age, blood_group, department, contact_no, place):
        self.id = id
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.blood_group = blood_group
        self.department = department
        self.contact_no = contact_no
        self.place = place
    def display_name(self):
        return f"NAME: {self.name}"
    def display_blood_group(self):
        return f"BLOOD_GROUP: {self.blood_group}"
    def display_id_name_age_contact_department(self):
        return f"ID: {self.id}, NAME: {self.name}, AGE: {self.age}, CONTACT_NUMBER: {self.contact_no}, DEPARTMENT: {self.department}"


class College(Student):
    def __init__(self, id, name, roll_no, age, blood_group, department, contact_no, place, college_name, university):
        super().__init__(id, name, roll_no, age, blood_group, department, contact_no, place)
        self.college_name = college_name
        self.university = university
    def college_inform(self):
        student_information = self.display_id_name_age_contact_department()
        return f"{student_information}, COLLEGE: {self.college_name}, UNIVERSITY: {self.university}"
id = input("Enter ID: ")
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
age = int(input("Enter age: "))
blood_group = input("Enter blood group: ")
department = input("Enter department: ")
contact_no = input("Enter contact number: ")
place = input("Enter place: ")
college_name = input("Enter college name: ")
university = input("Enter university name: ")

stud2 = College(id, name, roll_no, age, blood_group, department, contact_no, place, college_name, university)
print("\n--- Student Information ---")
print(stud2.college_inform())
print(stud2.display_name())
print(stud2.display_blood_group())
