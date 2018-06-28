
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@email.com'

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print('Name deleted!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Raj Sen'


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
