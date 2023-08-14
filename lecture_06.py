#PYTHON PROGRAM TO ILLUSTRte **kwargs for variable number of keyword argument
'''
def myFun(arg1,**kwargs):
    for key, value in kwargs.items():
        print("%s %s %s"%(arg1, key, value))
myFun("Hi", first="Model Institute", mid="of", last="Engineerning")
'''

#recursive funtion
'''
def fact(x):
    if x==0:
        return 1;
    else:
        return x*fact(x-1)

n=int(input("Enter a number: "))
print("Factorial vslue of {} is {}".format(n,fact(n)))
'''

#lambda function (nameless function)
'''
s=lambda a,b:a+b if a>b else b
print('The sum of {} and {} is: {}'.format(10,20,s(10,20)))
print('The sum of {} and {} is: {}'.format(40,20,s(40,20)))
print('The sum of {} and {} is: {}'.format(200,400,s(200,400)))
print(s('MIET',' JAMMU'))
'''

#python progra to illustrate cube of number showing diff between def() and lambda()
'''
def cube(y):
    return y*y*y

print(cube(5))

lambda_cube=lambda y:y*y*y
print(lambda_cube(5))
'''

#lambda function to find the factorial value of a number
'''
fact=lambda x:1 if x==0 else x*(fact(x-1))

n=int(input("Enter a number: "))
print("Factorial value of {} is {}".format(n,fact(n)))
'''

#wap in python to print even numbers in a list
#Normal Function
'''
def isEven(x):
    if x%2==0:
        return True
    else:
        return False

l=[0,5,10,15,20,25,30]
l1=list()
print(type(l1))
for i in l:
    res=isEven(i)
    if res==True:
        l1.append(i)

print(l1)
'''

#lambda function with filter
'''
lst=[0,5,10,15,20,25,30]
lst1=list(filter(lambda x:x%2==0, lst))
print(lst1)
'''
#lambda map function
'''
l1=[1,2,3,4,5]
l2=[5,10,15,20,25,30]
l3=list(map(lambda x,y: x*y,l1,l2))
print(l3)
l4=list(map(lambda x,y,z: x+y+z,l1,l2,l3))
print(l1)
print(l2)
print(l3)
print(l4)
'''
