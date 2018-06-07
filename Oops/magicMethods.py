class emp:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return(f"Employee('{self.fname}','{self.lname}','{self.pay}')")

    # def __str__(self):
    #     pass


emp_1 = emp('Corey', 'Schafer', 50000)
emp_2 = emp('Test', 'Employee', 60000)

print(emp_1)
