# from typing import List

# age = 10
# eye_colour = str("brown")
# hair_colour = str("black")

# senior_students = []


# class Student:
#     def __init__(self, name: str, age: int, eye_colour: str, hair_colour: str) -> None:
#         self._age = age
#         self._eye_colour = eye_colour
#         self._hair_colour = hair_colour
#         self._name = name


# class js_student(Student):
#     def __init__(
#         self,
#         name: str,
#         age: int,
#         eye_colour: str,
#         hair_colour: str,
#         height: float,
#         iq: int,
#     ) -> None:
#         super().__init__(name, age, eye_colour, hair_colour)
#         self._height = height
#         self._iq = iq
#         self.school = str("junior")


# class ss_student(Student):
#     def __init__(
#         self,
#         name: str,
#         age: int,
#         eye_colour: str,
#         hair_colour: str,
#         uni_of_choice: str,
#         grade: str,
#     ) -> None:
#         super().__init__(name, age, eye_colour, hair_colour)
#         self._uni_of_choice = uni_of_choice
#         self._grade = grade
#         self.school = str("senior")


# student_list = []

# student_list.append(js_student("bob", 10, "brown", "black", 1.53, 63))
# student_list.append(js_student("sam", 10, "black", "black", 1.35, 45))
# student_list.append(js_student("jim", 10, "blue", "ginger", 1.72, 78))
# student_list.append(js_student("tim", 11, "brown", "brown", 1.30, 85))
# student_list.append(js_student("tom", 11, "brown", "black", 1.29, 1))


# # student_list.append(ss_student("daniel", 13, "brown", "black", "cambridge", "a"))
# # student_list.append(ss_student("patrick", 12, "brown", "black", "oxford", "a"))
# # student_list.append(ss_student("alex", 14, "blue", "ginger", "oxford", "b"))
# # student_list.append(ss_student("nathan", 13, "black", "brown", "oxford", "a"))
# # student_list.append(ss_student("matthew", 12, "black", "black", "trinity", "f"))


# def print_all_js_names():
#     for student in student_list:
#         if student.school == "junior":
#             print("{}".format(student._name))


# # print_all_js_names()


# def find_oldest_student(input_list: List[Student]) -> Student:
#     for student in input_list:
#         if student.school == "senior":
#             senior_students.append(student)

#     senior_students.sort(key=lambda x: x._name, reverse=True)

#     return senior_students[-1]

# oldest_student_obj = find_oldest_student(student_list)
# print("the oldest student is {} and he is {} years old".format(oldest_student_obj._name, oldest_student_obj._age))
      
