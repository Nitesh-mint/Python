#using a property to access data in object.

class Student():
    def __init__(self, name, startingGrade=0):
        self.name = name
        self.grade = startingGrade

    @property 
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, newGrade):
        try:
            newGrade = int(newGrade)
        except (TypeError,ValueError) as e:
            raise type(e) ("New grade: " +  str(newGrade)+",is an invalid type.")
        
        if(newGrade<0) and (newGrade>100):
            raise ValueError("New grade"+ str(newGrade)+",Must be betweeen 0 and 100.")
        self.__grade = newGrade