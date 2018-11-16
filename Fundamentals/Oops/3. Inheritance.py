
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang='Python'):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) #also correct
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in employees:
            self.employees.remove(emp)

    def print_emp(self):
        for i in self.employees:
            print('-->', i.fullname())


# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'Employee', 60000)


dev_1 = Developer('Corey', 'Schafer', 50000, 'Java')
dev_2 = Developer('Test', 'Employee', 60000)

mng_1 = Manager('Rey', 'Schifler', 90000, [dev_1])
# print(mng_1.email)
# mng_1.print_emp()


print(isinstance(mng_1, Manager))
print(issubclass(Manager, Employee))


# print(dev_1.prog_lang)
# print(dev_1.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)
# print(dev_2.email)

# print(help(Developer))
