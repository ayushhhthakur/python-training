#one line if
'''
x=10
y=20
print('x is big') if x>y else print('y is big')
'''

#write a python program to input a nuber between 1 and 7, print its equallent day name in the week.
'''
x=int(input("Enter the day number(1-7): "))
match(x):
    case 1:
        print("The day is Monday")

    case 2:
        print("The day is Tuesday")

    case 3:
        print("The day is Wednesday")

    case 4:
        print("The day is Thrusday")

    case 5:
        print("The day is Friday")

    case 6:
        print("The day is Saturday")

    case 7:
        print("The day is Sunday")

    case _:
        print("Invaild Input")
'''
#write a python program to print numbers 1 to 100
'''
x=0
while(x<100):
    x+=1
    print(x, end=" ")

print('\nThats it...')
'''
#write a python program to print sum of numbers 1 to 100
'''
x=1
s=0
while (x<=100):
    s=s+x
    x+=1
print("Sum of numbers between 1 and 100: ",s)
'''
#write a python program to print sum of only even numbers 1 to 100
'''
i=1
while i<=10:
    if i%2==0:
        print(i, end=" ")
    i+=1

    for sum
i=1
s=0
while (i<=100):
    if i%2==0:
        s=s+i
    i+=1
print("Sum of even numbers between 1 and 100: ",s)
'''

#wap to count the no of digits that are given as input
'''
i = int(input('Enter a number: '))
c = 0
while i>0:
    #r=i%10
    c+=1
    i=i//10
print("Number of digits are %d"%(c))
'''

#to reverse the numbers 
'''
i = int(input('Enter a number: '))
c = 0
while i!=0:
    r=i%10
    c=c*10+r
    i=i//10
print("Reverse of digits is %d"%(c))
'''
#wap to check whether it is a palidrome no or not
'''
i = int(input('Enter a number: '))
c = 0
temp=i
while i!=0:
    r=i%10
    c=c*10+r
    i=i//10
if temp==c:
    print('Number is palidrome')
else:
    print("Number is not paidrome")
'''

#wap to check whether the  number is armstrong number
'''
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
'''
#wap to check whether the  number is spy number
#A spy number is a positive integer if the sum and product of its digits are equal.
'''
num=int(input('Enter a number: '))
sum=0
prod=1
while num>0:
    digit=num%10
    sum+=digit
    prod*=digit
    num=num//10

if sum==prod:
    print('The given number is a spy number.')
else:
    print('The given number is not spy number')
'''