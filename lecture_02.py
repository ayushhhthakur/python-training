#04-04-2023
#LECTURE NO 2

#code 1
#studname=input('Enter your name: ')
#studid=input('Enter your id: ')
#print(studname,studid)

#code 2
'''
x=input('Enter first number: ')  #x=int(input('Enter first number: '))  
y=input('Enter second number: ') #y=int(input('Enter second number: '))
print(type(x))
print(type(y))
x=int(x)
y=int(y)
z=x+y
print(x,y,z)
#print(x + '\t' y + '\t' z) cant concartinate int and str
print(x, '\t', y, '\t', z)
print('\nFirst number:%d \t Second Number:%d \t Addition:%d' %(x,y,z))
'''

#spliting numbers using split functon and comas
'''
x,y,z=input('Enter any three numbers: ').split(',')
x=int(x)
y=int(y)
z=int(z)
print('Addition of values', x+y+z)
'''

#spliting string using split function
'''
s1,s2,s3,s4=input('Enter the college name: ').split()
print(s1,s2,s3,s4)
#back slah constants
'''

#using positional arguments
'''
x=int(input('Enter first number: '))  
y=int(input('Enter second number: '))
z=x+y
print('\nFirst Number:%d \t Second Number:%d \t Addition:%d' %(x,y,z))
print('\nFirst Value {} \t Second Value {} \t Addition:{}'.format(x,y,z))
print('\nFirst Value {2} \t Second Value {0} \t Addition:{1}'.format(y,x,z))
print('\nFirst Value {1} \t Second Value {0} \t Addition:{2}'.format(x,y,z))
'''

#comments in python
'''
#this is a comment line
x=int(input('Enter first number: '))  
y=int(input('Enter second number: '))
z=x+y
print('\nFirst Number:%d \t Second Number:%d \t Addition:%d' %(x,y,z))
print(__doc__)
'''

#write a python program to input radius, find the area and circumference of a circle and print
'''
r=float(input("Enter the radius: "))
a=3.14*r*r
c=2*3.14*r
print('Radius: %.2f \t Area: %.2f \t Circumference: %.2f'%(r,a,c))
'''

#input student id, name, marks in os, marks in cn, marks in java. Calculate total marks, percentage makrs and print all
'''
name=input('Enter the Name: ')
id=int(input('Enter the Student ID: '))
os,cn,java=input('Enter the makrs in OS, CN and Java: ').split()
totmarks=int(os)+int(cn)+int(java)
totper= totmarks/300 * 100
print('Marks in OS:{} \n Marks in CN:{} \n Marks in Java:{} \n Total Marks:{} \n Percentage:{}'.format(os,cn,java,totmarks,totper))
'''

#binary, octal and hexadecimal arithmaticd
'''
print(0b01000001)
print(0xff)
print(0xff+0b01000001)
print(0b01000001+0b01000001)
print(0o7+0b01000001)
print(0b01000010-0b01000001)
print(ord('a'))
print(ord('A'))
print(ord('b'))
print(ord('B'))
print(ord('c'))
print(ord('C'))
print(ord('abc'))
'''

#python program that check whether an integer is even or odd using bit manipulation
'''
def is_even(num):
    return num & 1 == 0

num = int(input('Enter any number: '))
if is_even(num):
    print(f"{num} is even")
else:
    print(f"{num} is odd")
*******************************************************************************************************************************
Explanantion
In this is_even function, we perform a bitwise AND operation (&) between the given number num and the number 1. If the last bit of num is 0, then the result of this operation will laso be 0, incicating that num is even. Otherwise, if the last bit of the num is 1, then the operation will be 1, indicating that num is odd.
So, if the returent value for is_even function is true then the input num is even. Otherwise, it is odd.
*******************************************************************************************************************************
'''

#python program that adds 1 to an intger using bit manipulation
'''
def add_one(num):
    mask = 1
    while num & mask == mask:
        num =num ^ mask
        mask <<= 1

        num = num ^ mask
        return num

num = 43
num = add_one(num)
print(f"The new value of num is {num}")

*******************************************************************************************************************************
Explanantion
In the add one function, we first create a mask variable with the value 1. We then enter a while loop that checks whether the least significant bit of mum is 1 by performing a bitwise AND operation (4) between num and the

If the least significant bit is 1, we toggle it to 0 by performing a bitwise XOR operation (") between num and the mark. We then shift the mask one bit to the left using the left shift operator (<<).

We repeat this process until we encounter a bit in num that is 0. At this point, we toggle the first 0 bit to 1 by performing another bitwise XOR operation between num and the mask. This has the effect of adding 1 to num.

Finally, we return the updated value of num. if we call the add one function with the input value of num.
So, if we call the add_one function with the input value og num as 42 the function will add 1 to it and return 43.
*******************************************************************************************************************************
'''


#conditional statements
#swapping two numbers
'''
n1=int(input('Enter first number '))
n2=int(input('Enter second number '))
if n1>n2:
    print(n1,'is greater')
else:
    print(n2,'is greater')

x=int(input('Enter a number: '))
if x>0:
    print(x,'is positive')
else:
    print(x,'is negative')
'''


#greates of two numbers
'''
n1=int(input('Enter first number '))
n2=int(input('Enter second number '))
n3=int(input('Enter third number '))
if n1>n2:
    big=n1
else:
    big=n2
if n3>big:
    big=n3

print('boggest among three numbers is',big)   
'''

#using if elif statement for grades
'''
name=input('Enter the Name: ')
id=int(input('Enter the Student ID: '))
os,cn,java=input('Enter the makrs in OS, CN and Java: ').split()
totmarks=int(os)+int(cn)+int(java)
totper= totmarks/300 * 100
print('Marks in OS:{} \n Marks in CN:{} \n Marks in Java:{} \n Total Marks:{} \n Percentage:{}'.format(os,cn,java,totmarks,totper))
if totper>=90:
    print("Grade is A")
elif totper>=80 and totper<90:
    print("Grade is B")
elif totper>=60 and totper<80:
    print('Grade is C')
else:
    print('Grade is F')
'''

#python program that check if two integers have oppositve signs using bit maipulation
'''
def opposite_signs(num1,num2):
    return (num1 ^ num2)
'''