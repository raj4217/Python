class emp:
    no_of_emp = 0
    company = 'HCLT'
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = f'{self.fname}.{self.lname}@{self.company}.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_method(cls, amount):
        cls.raise_amount = amount

    # using classs method as alternative constructor
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = emp('Corey', 'Schafer', 50000)
emp_2 = emp('Test', 'Employee', 60000)

# emp.set_raise_method(1.05)

# emp_1.set_raise_method(1.05) '''setting the class method from a variable will result the same'''

# print(emp.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# #for using alternative constructor
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# m1 = emp.from_string(emp_str_1)
# m2 = emp.from_string(emp_str_2)
# m3 = emp.from_string(emp_str_3)

# print(m1.fname)
# print(m1.lname)
# print(m1.pay)

# for using static method
import datetime
print(emp.is_workday(datetime.date(2018, 6, 4)))
