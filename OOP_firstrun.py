# # First Run
# # triangle object with side lengths and returns perimeter
# class Triangle:
#     def __init__(self,a,b,c):
#         self.side_a = a
#         self.side_b = b
#         self.side_c = c
#     def find_per(self):
#         perimiter = self.side_a + self.side_b + self.side_c
#         print("The perimeter of the triangle is: ", perimiter)
    
    
# Tri_1 = Triangle(3,4,5)

# Tri_1.find_per()


class Person:
    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    

# Omar = Person("Omar Elbaz", "19", "Student")

# print(Omar.name)
# print(Omar.age)
# print(Omar.intro)

# # Created Getter and setter methods for my person class but I do not need them, the same can be done when initializing.
#     # def get_age(self):
#     #     return self.age
#     # def get_name(self):
#     #     return self.name
#     # def get_occupation(self):
#     #     return self.occupation
#     # def set_age(self,age):
#     #     self.age = age
#     # def set_occupation(self,occupation):
#     #     self.occupation = occupation
#     # def intro_line(self):
#     #     return (self.name, "is", self.age, "years old and works as a ", self.occupation, ".")



# TASK
    # Create Student class inherits from person
        # Student has the following properties: school name, grad year, major,
        # Student has its own method get_classes which searches the json file for name if name exists returns courses
            # json file has a list of student names, and every student name has a dictionary with the classes they are taking
            # create three students with accompanying courses

    # Step 1 Create a json file with data to be read in the future
import json
 
# Data to be written
# Students with accompanying courses
# dictionary = {
#     "Adham": ["Programming 101", "English Composition 101", "Calculus", "American History"],
#     "Omar": ["Programming 102", "English Composition 102", "Calculus II", "European History"],
#     "Weezy": ["Programming Concepts", "Numerical Analysis", "Calculus III", "Intro to Sociology"],

# }

# with open("sample_one.json", "w") as outfile:
#     json.dump(dictionary, outfile)
# json file has been created but the data is in one line, would like  to see if i can write it as a new line.
# If not I will manually adjust it to be able to read lines

# Student Class

class Student(Person):
    def __init__(self, name: str, age: str,occupation: str,school: str, grad_year: str, major: str):
        super().__init__(name,age,occupation)
        self.school = school
        self.grad_year = grad_year
        self.major = major

    def get_classes(self):
        file = open('./first.json')
        json_object = json.load(file)
        if self.name in json_object:
            return (self.name + " is enrolled in the folowiing courses: ", 
                    json_object[self.name])


        


Adham = Student("Adham", "30", "Student", "Rutgers", "2026", "Computer Science")

print(Adham.get_classes())
# json_data()




Omar = Student("Omar Elbaz","19","Student","Rutgers", "2026", "Computer Science")
print(Omar.school)







