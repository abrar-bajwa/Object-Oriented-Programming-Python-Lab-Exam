
# Task 1

print('Task 1')


from abc import ABC, abstractclassmethod
import abc


class Student(ABC):
    def __init__(self,name,testscore,grade):
        self.__name=name
        self.__testscore=testscore
        self.__grade=grade

    def getName(self):
        return self.__name
    
    def gettestscore(self):
        return self.__testscore

    def setTestscore(self,testscore):
        self.__testscore=testscore
    @abstractclassmethod
    def computeGrade(self):
        pass

    def getGrade(self):
        return self.__grade

    def setGrade(self,grade):
        self.__grade=grade      




class undergraduateStudent(Student):
    def __init__(self,name,testscore,grade):
        super().__init__(name,testscore,grade)

    def computeGrade(self):
        if self.gettestscore()>=60:
            
            self.setGrade("Pass")
        else:
            
            self.setGrade("Fail")

    def __str__(self):
        return "name = {}, TestScore = {}, Grade= {}".format(self.getName(),self.gettestscore(),self.getGrade())

    
class GraduateStudent(Student):
    def __init__(self,name,testscore,grade):
        super().__init__(name,testscore,grade)

    def computeGrade(self):
        if self.gettestscore()>=70:
            
            self.setGrade("Pass")
        else:
            
            self.setGrade("Fail")
    def __str__(self):
        return "name = {}, TestScore = {}, Grade= {}".format(self.getName(),self.gettestscore(),self.getGrade())




name, testScore = input("Enter name and score: ").split(" ")
testScore = float(testScore)
obj = undergraduateStudent(name, testScore, " ")
obj.computeGrade()
print(obj)
name, testScore = input("Enter name and score: ").split(" ")
testScore = float(testScore)
obj = GraduateStudent(name, testScore, "")
obj.computeGrade()
print(obj)


print()
print("Task 2 and 3")
#Task 2 and 3

#Task 2
class StudentList:
    def __init__(self):
        self.__count = 0
        self.__studentList = []

    def searchStudent(self, id):
        try:
            for each in self.__studentList:
                for k, v in each.items():
                    if k == str(id):
                        return v
        except:
            print()

        if k != str(id) or id ==None:
            return notfoundexception("Not found Exception")

    def addStudent(self, id, name, marks):
        if marks=="" or marks==0 or marks==None:
            return studentmarksnotset(marks)
        elif int(marks) < 0:
            return negativemarks(marks)
        elif name and id and marks:
            self.__studentList.append({
                id: {
                    "name": name,
                    "marks": marks
                }
            })
            self.__count += 1
            return "Student Added!"
        
        else:
            return invalidtype(name)


    def printStudents(self):
        for each in self.__studentList:
            for k, v in each.items():
                try:
                    print("Id :", k,"Name :", v["name"], "Marks :",v["marks"],"Grade :",v["grade"])
                except:
                    print("Id :", k,"Name :", v["name"], "Marks :",v["marks"])

    def setMarks(self, id, marks):
        if marks=="" or marks==0 or marks==None:
            return studentmarksnotset(marks)
        elif self.searchStudent(id):
            for each in self.__studentList:
                for k, v in each.items():
                    if k == id:
                        v["marks"] = marks
                        break
            return "Marks Updated"
        
        elif int(marks)<0:
            return negativemarks(marks)
        else:
            return notfoundexception(str(id))


    def computeGrade(self):
        if marks=="" or marks==0 or marks==None:
            return studentmarksnotset(marks)
        for each in self.__studentList:
            for k, v in each.items():
                if int(v["marks"]) != 0:
                    if int(v["marks"]) >=80> 70:
                        v["grade"]="A+"
                    elif int(v["marks"]) >= 70< 80:
                        v["grade"]= "A"
                    elif int(v["marks"]) >= 60< 70:
                        v["grade"]= "B"
                    else:
                        v["grade"]= "Pass"
                else:
                    return studentmarksnotset(v["name"])
        return "Grade Computed!"


# s = StudentList()

# s.addStudent(1,"bajwa",60)
# s.addStudent(10,"farhan",71)

# print(s.searchStudent(10))

# s.printStudents()
# s.computeGrade()
class negativemarks(Exception):
    def __init__(self,marks):
        self.__marks=marks
    def getMarks(self):
        return self.__marks
    def __str__(self):
        return "Exception: Negative marks are entered"


class notfoundexception(Exception):
    def __init__(self,name):
        self.__name=name
    
    def getName(self):
        return self.__name
    
    def __str__(self):
        return "student not found exception"


class studentmarksnotset(Exception):
    def __init__(self,name):
        self.__name=name
    
    def getName(self):
        return self.__name

    def __str__(self):
        return "student marks not set exception"

class invalidtype(Exception):
    def __init__(self,name):
        self.__name=name
    
    def getName(self):
        return self.__name

    def __str__(self):
        return "invalid type exception! other class type is provided other than student class. "    



students = StudentList()
while True:
    print("""
        1. Add Student\n
        2. Set Student Marks\n
        3. Compute student grades\n
        4. Display Student Roaster\n
        5. Search Student\n
        6. Exit\n
    """)
    choice = int(input("Enter Choice: "))

    print()

    if choice == 1:
        id,name,marks = input("Enter id, name , marks. ").split(" ")
        print(students.addStudent(id,name,marks))
    if choice == 2:
        id,marks = input("Enter id, marks. ").split(" ")
        print(students.setMarks(id,marks))
    if choice == 3:
        print(students.computeGrade())
    if choice == 4:
        students.printStudents()
    
    if choice ==5:
        id =input("Enter Id")
        print(students.searchStudent(str(id)))

    if choice ==6:
        exit()
    if 0>=choice or choice>=7:
        print("Invalid Choice!")
