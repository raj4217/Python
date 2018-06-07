class emp:
    no_of_emp = 0
    company = 'HCLT'
    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        emp.no_of_emp += 1
        self.fullname = f'{fname} {lname}'
        self.email = f'{self.fname}.{self.lname}@{self.company}.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = emp('Corey', 'Schafer', 50000)
emp_2 = emp('Test', 'Employee', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp.no_of_emp)
