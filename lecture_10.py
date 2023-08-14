#method overloading in python
'''
def add(instanceOf, *args):
    if instanceOf=='int':
        rsult=0
    if instanceOf=='str':
        result=''
    if instanceOf=='Welcome':
        result=''

    print(type(args))
    for i in args:
        result=result+i
    return result

print(add('int',3,4,5))
print(add('srt','I','am','in','Jammu'))
print(add('Welcome','to','python'))
'''

'''
class x:
    def m1(self,a=0,b=0,c=0):
        if a==0 and b==0 and c==0:
            print(" Method is called with no argument")

        elif a!=0 and b==0 and c==0:
            self.a=a
            print(self.a)
            print(" Method is called with single arguent")

        elif a!=0 and b!=0 and c==0:
            self.a=a
            self.b=0
            print(self.a)
            print(self.b)
            print(" Method is called with two arguments")
        else:
            self.a=a
            self.b=b
            self.c=c
            print(self.a)
            print(self.b)
            print(self.c)
            print(" Method is called with three arguments")

xobj=x()
xobj.m1()
xobj.m1(10)
xobj.m1(20,30)
xobj.m1(40,50,60)
'''


#pip install multidispatch

#in backend, dispatcher creates an object which stores different implementation and on runtime, it selects the appropriate method as the type and numbers of parameters passed.

from multipledispatch import dispatch

#passing one parameter
@dispatch(int,int)
def product(first,second):
    result=first*second
    print(result);

#passing two parameters
@dispatch(int,int,int)
def product(first,second,third):
    result=first*second*third
    print(result);

#you can also pass datatype of any value as per requirement
@dispatch(float,float,float)
def product(first,second,third):
    result=first*second*third
    print(result);

#calling product method with 2 agrumnets
product(2,3,2)
product(2.2,3.4,2.3)
product(43,54)