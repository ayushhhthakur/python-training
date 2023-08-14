#wap to check whether the  number is perfect number (homework)
'''
num = int(input("Enter a number: "))
sum= 0
for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
'''

#wap to input a number, find the factorial value of the number
'''
num=int(input('Enter a number: '))
fact=1
while num>0:
    fact=fact*num
    num-=1
print('Factorial is: ',fact)
'''

#wap to input a number, find whether it is a prime number or not
'''
num=int(input('Enter the number: '))
i=1
c=0
while i<=num:
    if num%i==0:
        c+=1
    i+=1

if c==2:
    print('%d is a prime number'%(num))
else:
    print('%d is not a prime number'%(num))
'''

#find the number of palindrome numbers usig nested loop
'''
i=1
while i<=100:
    n=i
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if i==s:
        print(i,' is palidrome')
    i+=1
'''
#wap to check number is armstrong or not between 1 - 1000
'''
i=1
while i<=1000:
    n=i
    s=0
    while n>0:
        r=n%10
        s=s+(r*r*r)
        n=n//10
    if i==s:
        print(i,' is armstrng number')
    i+=1
'''

#printing pattern using nested loop
'''
for i in range (1,6):
    for j in range (1,i+1):
        print(j, end=' ')
    print()

    OUTPUT
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
'''

#printing pattern using nested loop

'''
for i in range (5,0,-1):
    for j in range (1,i+1):
        print(j, end=' ')
    print()

    OUTPUT
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1
'''

#printing pattern using nested loop
'''
for i in range (1,6):
    for j in range (1,i+1):
        print('*', end=' ')
    print()

    OUTPUT
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
'''

#printing pattern using nested loop
'''
for i in range (5,0,-1):
    for j in range (1,i+1):
        print('*', end=' ')
    print()

    OUTPUT
    * * * * * 
    * * * * 
    * * * 
    * * 
    * 
'''
'''
for i in range (1,6):
    for j in range (1,i+1):
            print('*', end=' ')
    print()

 
        * 
      * * *
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
'''

#wap to check whether a number is perfect number or not
'''
num=int(input('Enter a number: ')) #6
sum=0 #1 , 1+2=3 , 3+3=6 
for i in range (1,num): #1, num-1 
    if num%i==0: #6%1==0, 6%2==0, 6%3==0, 6%4!=0, 6%5!=0
        sum+=i
if num==sum:
    print('The number is perfect number.')
else:
    print('Number is not perfect number.')
'''