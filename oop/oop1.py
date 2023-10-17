# oop in python
# Classes and Instances
 
class Employee: 
  # pass # if we want to leave class or function empty , skip

  def __init__(self, first, last, pay):
     # constructor
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@gmail.com'
  
  def fullname(self): 
    return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Hitesh', 'Marwaha', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
print(emp_2)

# emp_1.first = 'Hitesh'
# emp_1.last = 'Marwaha'
# emp_1.email = 'Hitesh.Marwaha@gmail.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@gmail.com'
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)


# full name
print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname())