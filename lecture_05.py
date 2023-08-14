#to check the sys version
'''
import sys
print (sys.version)
'''

#unconditional transfer statements.
#break
'''
i=1
while i<=100:
    print(i,end=' ')
    if i>=50:
        break
    i+=1
'''

#continue
'''
i=0
while i<100:
    i+=1
    if i==50:
        continue;
    print(i,end=' ')
'''

#functions
'''
#pre defined functions
from math imprt *
print(sqrt(25))
print(pi)


#user defined function
def display():
    print('This is a user defined function')
    print('Defined by user')

#calling a function
if __name__ == '__main__':
    display();
'''

#calling function without arguments and with return values
'''
def sum():
    x=5
    y=10
    z=x+y
    return z
if __name__== '__main__':
    res=sum()
    print('The sun of numbers is: ',res)
'''
#calling function with arguments and without return values
'''
def spy(x):
    sum=0
    prod=1
    while x>0:
        r=x%10
        sum = sum + r
        prod = prod * r
        x=x//10
 
    if sum==prod:
        print('Number is a spy number.')
    else:
        print('Number is not spy number.')
'''

#calling function with arguments and with return values
'''
def spy(x):
    sum=0
    prod=1
    while x>0:
        r=x%10
        sum = sum + r
        prod = prod * r
        x=x//10
    return (sum,prod)
    
if __name__ == '__main__':
    num=int(input('Enter a number: '))
    s,p=spy(num)
    if s==p:
        print('Number is a spy number.')
    else:
        print('Number is not spy number.')
'''

#calling function with default values
'''
def func(name, greet='Good modning'):
    print('Hello'+' '+ name+' '+greet)
func('Suman')
func('Aadil','Good Evening')

#note: When insufficient number of arguments are passed to a function, it uses the default values given in the header of the function.
'''
#calling function with key arguments
'''
def func(name,os,cn,java):
    print(name,os,cn,java)
func('Suman',76,87,98)
func('Aadil',java=88,os=90,cn=60)
'''

#calling function with arbitary arguments
'''
def func(*a):
    for ele in a:
        print(ele,end=' ')
func(10,20,30,40,50,60,70,80,90,100)
'''