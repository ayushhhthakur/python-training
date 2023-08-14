#list comprehension
'''
x= [p for p in range(10)]
print (x)

     OR

x=[]
for p in range(10):
    x.append()

print(x)

'''

#s={1,5.2,8j,True,'MIET',1}
#print(s)
'''
s={1,5.2,8j,True,'MIET',False}
print(s)
#accessing the elements in the set using iterations
for ele in s:
    print(ele,end=' ')
'''
'''
s={12,22,31,42,54,56}
#using in  operator to search for an element in the set
print(12 in s)
for i in s:
    print(i)
'''

'''
s={123,23,143,431,31}
print(s)
#adding element into the set
s.add(100)
print(s)
'''

'''
s={123,23,143,431,31}
print(s)
#to add more than one element in the set
s.update([1,2,3,4])
print(s)
'''

'''
s={123,23,143,431,31}
#to print the lenght of the set
print(len(s))
'''

'''
s={1,232,2,24,4.1,23,143,431,31}
print(s)
#to remove an element for the set
s.remove(232) #removes element 232
print(s)
s.remove(4.1) #removes element 4.1
print(s)
#removes the element from the set
s.discard(24)
print(s)
s.discard(100) #though the element is not present in the set, it wont raisse an error
print(s)
s=set((6,2,100,8,9,1))
print(s)
print(s.pop()) #removes last most item from the set
print(s)
s.clear()
print(s)
s={123,12,41,123,31,3}
print(s)
del(s) #del keyword will delete the set completly
print(s)
'''

#iterating through a set:
'''
for letter in set("apple"):
    print(letter,end=" ")
'''

'''
for char in set('aaaa'):
    print(char)
'''
'''
st="Roose"
s=set((st)) #converts string to set hence duplicate chars will be eliminated
print(s)
'''
'''
st="Roose"
s={i for i in st}
print(s)
'''

#creating a set form a list
'''
lst=[1,3,23,24,43]
s={i for i in lst}
print(s)
'''

#creating a dictionary form a list#
'''
lst=[1,3,23,24,43]
d={i:i*i for i in lst}
print(d)
'''

#union
'''
s1={1,2,3,4}
s2={'a','b','c','d'}
s3=s1.union(s2)
print(s1)
print(s2)
print(s3)
'''

#intersection updte
'''
s1={1,2,3,4}
s2={4,5,6,7}
s1.intersection_update(s2)
print(s1)
'''

#difference
#'''
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.difference(s2)
print(s1)
#'''

'''
s1={1,2,3,4,5}
print(s1)
s2={4,5,6,7,8}
print(s2)
print(s1,s2)
print(s2,s1)
#union operator
print(s2|s1) #'|' operator is union
print(s1.union(s2))
print(s2.union(s1))
#intersection operator
print(s1&s2)
print(s1.intersection(s2))
print(s2.intersection(s1))
#difference operator
print(s1-s2)
print(s1.difference(s2))
print(s2.difference(s1))
#symmetric operator
print(s1^s2)
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
'''

'''
a=set('abracadabra')
b=set('alacazam')
print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)
'''


#creating an empty dictionary
'''
dict=[]
print(dict)
'''
'''
dict=dict()
print(dict)
'''
'''
dic={'studid':1001,'studname':'Rohit','branch':'CSE'}
print(dic)
print(dic.keys()) #prints only the keynames
print(dic.values()) #prints only the values
print(dic.items()) #prits both keys and values
print(len(dic)) #prints no of items
print(dic.get('studname')) #prints the value of given key
print(dic)
dic.pop('studname') #remove the item of the given key
print(dic)
dic.popitem() #remove the last most item
print(dic)
'''

'''
marks={}.fromkeys(['maths','English','Sciene'],35)
print(marks)

for i in marks:
    print(i)

for i in marks.values:
    print(i)

for i in marks.items:
    print(i)

for i,j in marks.items:
    print(i)
'''
