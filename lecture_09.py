#Object Oriented Programming System (OPPs)
#class in python
'''
class student:
    stdno=101
    stdname='Ash'
    fees=120000

    def output(self):
        print('Student ID No: ',self.stdno)
        print('Student Name: ',self.stdname)
        print('Student Fees: ',self.fees)
stud=student() #creates an object stud for the class student
stud.output() #calling the function using object
print(__doc__)
'''

'''
class Employee:

    def accept(self):
        self.eno=int(input('Enter employee number: '))
        self.ena=input('Enter employee name: ')
        self.sal=int(input('Enter employee salary: '))

    def output(self):
        print('ID:{0} NAME:{1} SALARY:{2}'.format(self.eno, self.ena, self.sal))

if __name__=="__main__":
    emp=Employee()
    print(emp) #prints address of emp object
    emp.accept()
    emp.output()
'''

'''
class MyClass:
    #This is my Class
    a=10 #static member of the class

    def func(self):
        print("HEllO")
    
print(MyClass.a) #printing the value of 'a' with class name i.e static
#MyClass.func() #it raises error because functions cant be called with class
mc=MyClass()
mc.func() #calling func with object is possible
print(mc.a) #printing the value of 'a' with object 
'''

#constructor in pyhron
'''
class Employee:
    def __init__(self): #constructor method to initilize members
        self.eno=101 #default constructor
        self.ena='Ash'
        self.sal=12000

    def output(self):
        print('ID:{0} NAME:{1} SALARY:{2}'.format(self.eno, self.ena, self.sal))

emp=Employee() #while createing the object, the constructor function will be called
emp.output()
'''
'''
class one:
    def __init__(self): #default constructor
        print('First constructor')

    def __int__(self,n): #Argumented constructor
        print('Argumented constructor')

#this code will give an error because we cant define more than one constructor in python
o=one()
p=one(5)
'''

'''
class Employee:
    def __init__(self,name,id): #argumented constructor
        self.id=id
        self.name=name

    def display(self):
        print('ID: %d \t Name: %s'%(self.id,self.name))
        print('ID: ',self.id,'\t Name',self.name)
        print('ID: {} \t Name: {}'.format(self.id,self.name))

emp1=Employee("John",101) #createing object with actual parameter
emp2=Employee("David",102)
emp1.display()
emp2.display()
'''

def func(x,y):
    print(type(x))
    print(type(y))
    print("values ",x,y)

func(43,65)
func(23.5,65.3)
func(43,65.3)
func("Ayush","Aditya")
func(10,30j)