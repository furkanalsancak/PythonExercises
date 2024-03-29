class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1


    @property
    def email(self):
        return f"{self.first} {self.last}@email.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    # def from_string(emp_str):
    #     first, last, pay = emp_str.split('-') # my try at this without classmethod. Kinda worked. Not sure
    #     return Employee(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    def __repr__(self):
        return f"Employee('{self.first}','{self.last}','{self.pay}')"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"



emp_1 = Employee('Furkan', 'Alsancak', 50000)
emp_2 = Employee('Hakan', 'Alsancak', 60000)

print(repr(emp_1))
print(str(emp_1))

print(int.__add__(1, 2))
print(str.__add__('a','b'))





# import datetime
# my_date = datetime.date(2016, 7, 11)
# print(Employee.is_workday(my_date))

'''
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
'''

'''
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)
'''


# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_1.fullname())

# emp_1.raise_amount = 1.05
# print(emp_1.__dict__)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(Employee.num_of_emps)


# Employee.set_raise_amt(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)