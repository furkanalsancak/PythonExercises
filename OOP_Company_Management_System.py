
class Employee():
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.department = "Computer Science"
        self.salary = salary
        self.leave = 15

    def updating_leave(self, days):
        self.leave = self.leave - days
        return self.leave
    
    def __str__(self):
        return f"This is employee number {self.id} \nname : {self.name} \nposition : {self.position} \nsalary : {self.salary} \nleave : {self.leave}"

Bongo = Employee(1, "Bongokule", "CEO", 1000000)
print(Bongo)
offDays = int(input("How many days would you like to take off? : "))
Bongo = Bongo.updating_leave(offDays)
print(Bongo)