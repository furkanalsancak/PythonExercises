
#First look at OOP concepts

'''
class doctors:
    def __init__(self, name, age, dep):
        self.name = name
        self.age = age
        self.dep = dep
    
    def checkDoc(self):
        if self.age >30:
            print("Doctor, you are close to retirement.")
        else:
            print("Doctor, you are young.")

class account_dep:
    def __init__(self, total_doctor, all_salaries):
        self.total_doctor = total_doctor
        self.all_salaries = all_salaries


obj = doctors("Zia", 35, "Emergency")

print(obj.checkDoc())
'''


class student_record:
    def record(self):
        self.studentName = "Furkan"
        self.studentClass = "10th"
        print(self.studentName)
        print(self.studentClass)

class accounting(student_record):
    def getRecord(self):
        self.record()


obj = accounting()
obj.getRecord()
    