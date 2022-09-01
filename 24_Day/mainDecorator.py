import os
from Decorators import *

oStudent1 = Student("Nitesh")
oStudent2 = Student("Light")

#get student grades
print(oStudent1.grade)
print(oStudent2.grade)
print()

#assingn new grades to the students.
oStudent1.grade = 50
oStudent2.grade = 60

print(oStudent1.grade)
print(oStudent2.grade)
print()


