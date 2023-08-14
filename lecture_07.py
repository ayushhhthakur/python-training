'''
lst=[14,5.2,5,'MIET',False,50,10,30,40]
print(lst)

#subscripting elements
print(lst[3])

#slicing using slicing operator colon (:)
print(lst[1:5]) #print the list from 1st indexed element to 4th indexed element
print(lst[3:]) #print elements from 3rd index to last
print(lst[:5]) #print elements from the begining to <5 position i.e 4th position
print(lst[:]) #print all elements in the list
#negative indexiing
print(lst[-1]) #prins lastmost element from the list
print(lst[-4:-1]) #prints elements from -4 indexed element to -2 indexed element
print(lst[::-1]) #it reverse the list
lst=[[1,2,3,4,5],[11,12,13,14,15],[111,112,113,114,115]] #creating a list within a list
print(lst[1][3])
print(lst[2][1:3])
'''
'''
lst=[] #creates an empty list
while True:
    ele=input('Enter an element to add to the list exit to comeout: ')
    if ele=='exit':
        break


l2=['happy',[5,6,7,8]] #placing a list within list, here [5,6,7,8] is linear list
print(l2[0])
print(l2[1])
print(l2[0][1])
print(l2[1][3])
print(l2[1][1:3])
print(l2[-1])

l3=[1,2,3,4,5,6,7,8]
print(l3[-1])
print(l3[7])
'''
'''
print(lst)
l1=[1,2,'Hello',3.5,4]
print(l1[-1])
print(l1[4])
print(l1[0])
print(l1[-5])

l2=['L','I','V','E','W','I','R','E']
print(l2[7])
print(l2[-1])
print(l2[-5])
print(l2[1:4])
'''
'''
l1=[1,2,'Hello',3.5,4]
print(l1[1:4])

l2=['L','I','V','E','W','I','R','E']
print(l2[4:7])
print(l2[3:1])
print(l2[:])
print(l2[::-1])

l3=['livewire']
print(l3)
print(l3[0])

st='livewire'
print(type(st))
print(st[0])
'''

'''
l1=[10,20,30,40,10]
print(l1)
print(len(l1))
l1.append(50)
print(l1)
print(l1.count(10))
print(l1.index(30))
l2=l1.copy()
print(l2)
l1.insert(2,33)
print(l1)
l1.remove(30)
print(l1)
l1.pop(3)
print(l1)
l3=[80,70,90]
print(l3)
l1.extend(l3)
print(l1)
l3=l1.copy
print(l3)
l1.sort(reverse=True)
print(l1)
l1.reverse()
print(l1)
l1.clear()
print(l1)
l1=['L','I','V','E','W','I','R','E']
print(l1)
del l1[2]
print(l1)
del l1[1:4]
print(l1)
#print(l1+l3)
print(l1*3)
print(len(l1))
del l1
'''

#program to search for an element in list
'''
l1=[10,20,30,40,60,40,40]

n=int(input("Enter the number to search: "))
if n in l1:
    print(n,' is found at ',l1.index(n),' poition')
else:
    print(n,' is not found')
#prints frequency of a number in the list
print(n,' is found',l1.count(n),' times')
'''

#using for loop to search for an element
'''
l1=[1,2,3,4,5,6,8,10]
n=int(input("Enter the number to be searched: "))
f=0
for ele in l1:
    if ele==n:
        f=1
        break

if f==1:
    print(n," is found")
else:
    print(n," not found")
'''

#counting the frequency of a number in the list using for loop
'''
l1=[1,2,3,4,1,5,7,8]
c=0
n=int(input('Enter the number to search: '))
for ele in l1:
    if ele==n:
        c+=1

print(n,' is found',c,' times')
'''

#string functions
'''
#create a new list - list comprehension
l1=[2** x for x in range(10)]
print(l1)
l1=[x for x in range(21,31)]
print(l1)

#code block equallen to above
pow2=[]
for x in range(10):
    pow2.append(2**x)
print(pow2)
l1=[]
for x in range(21,31):
    l1.append(x)
print(l1)
'''

#mathematical operators between lists
'''
l1=[2,3,6,8,9]
l2=[1,5,7,4,12]
l3=[x+y for x,y in zip(l1,l2)]
print(l3)
'''

#what will be the outputs
'''
x=1
def func():
    x=20
    print(x)

    def func1():
        x=10
        print(x)
    func1()
func()
print(x)
'''
'''
def A():
    __name__ = 'B'
    def __name__():
        return 'C'
print(A.__name__)
'''
'''
a=1
if a==3 or 4 or 6:
    print("YES")
else:
    print("NO")
'''

'''
name=''
if name:
    print('HI')
else:
    print('Bye')
'''
'''
def computepay(h,r):
    if h>40:
        p=1.5*r*(h-40)+(40*r)
    else:
        p=h*r
    return p

hrs=input('Enter hours: ')
hr=float(hrs)
rhrs=input('Enter rate per hour: ')
rphrs=float(rhrs)
p=computepay(hr,rphrs)
print(p)
'''

'''
total=sum(range(1,100))
print(total)
'''
'''
a=print(5)
print(a)
'''

'''
string= "I am a boy"
b = string.split()
rev = []
for i in b:
    revers =  i[::-1]
    rev.append(revers)
print(" ".join(rev))
'''



#string in python:
#split(): It splits a string or the input at every space and store into a list. if no char is specified in split(), it will split at every space. If a char is given at every such char the string will be spilleted and stored into the list
'''
str='Welcome to MIET JAMMU'
words=str.split()
print(type(words))
print(words)
for word in words:
    print(word)
'''

'''
words=input('Enter a string: ').split()
print(type(words))
print(words)
for word in words:
    print(word)
'''

'''
line ='the quick brown FOX jumps Over The Lazy Dog'
print(line.capitalize())
print(line.title())
print(line.upper())
print(line.lower())
print(line.casefold())
print(line.count('T'))
print(line.expandtabs(100))
'''

'''
st='Welcome to MIET Jammu'
print(st.find('MIET'))
print(st.index('M'))
'''


'''
st='MIET'
print(st.isalpha())

st='MIET123'
print(st.isalpha())

st='MIET@#'
print(st.isalpha())

st='MIET'
print(st.isalnum())

st='123'
print(st.isalnum())

st='MIET123'
print(st.isalnum())
'''

#using for loop to iterate
'''
st1='Hello World'
st2='Python Programming'
print('character at st1[0]: ',st1[0])
print('character at st2[1:5]: ',st2[1:5])
print(st1)
print(st2)
print(st1[5:])
print(st2[:5])
'''
#input a string of more than one word, find the number of palidrome words in it and print (home work)


#input a string, convert each vovels to upper case and print

#tuple
'''
#createing an empty tuple
tpl=()
print(type(tpl))
#creating an emplty tuple using tuple constructor
tpl=tuple()
print(type(tpl))
#creating a tuple by keeping list of emements within paranthesis
tpl=(10,20,30,40,50)
print(type(tpl))
tpl=10,20,30,40,50
print(type(tpl))
tpl=(100)
print(type(tpl))
tpl=(100,)
print(type(tpl))
'''

#slicing and negative indexing in tuple
'''
tpl=(10,20,30,5.3,8j,'miet',True)
print(type(tpl))
print(tpl)
print(tpl[5])
print(tpl[1:5])
print(tpl[-1])
print(tpl[-4:-1])
print(tpl)
'''

#to create a tuple with tuple constructor
'''
thistuple=tuple ((1,2,3,4,5,6)) #duouble parenthesis is required.
print(thistuple)
'''

'''
thistuple=(1,2,3,4,5,6,7)
i=0
n=int(input('Enter a number to search: '))
for x in thistuple:
    if x==n:
        print(n,' is present at',i,' indexed position')

    i+=1
'''

#program to find an element at multiple occurance 
'''
thistuple=(1,2,3,4,5,6,7)
c=0
n=int(input('Enter a number to search: '))
for x in thistuple:
    for y in thistuple:
        if x==y:
            c+=1

    print(x,' is found 'c, ' times')
    c=0
    '''