#!/usr/bin/env python
# coding: utf-8

# 1.What will be the output of the following Python statement:
# print 4 - 2 * 2
# ?
# >>> print 9 / 3
# ?
# >>> print 9 % 3
# ?
# >>> print 10 % 3
# ?
# >>> print 10 ** 4
# ?
# >>> print 10 ** 2 * 2
# ?
# Try to guess the result and type it in you shell to prove your guess.
# 

# In[1]:


print(4-2*2)
print(9/3)
print(9%3)
print(10%3)
print(10**4)
print(10**2*2)


# 2.	Create 3 variables, assign numeric values and strings; display them on the screen with and without the print statement.

# In[2]:


a=25
b='Ananth'
c=12.5
print(a,b,c)
a,b,c


# 3.	Program variables have data types such as: Integer; Float and String. After the execution of the following snippet of code what are the data type of the three variables var_one, var_two and var_three?
# 
# var_one = 85
# var_two = 9.81
# var_three =’I am data science’
# 

# In[4]:


var_one = 85
var_two = 9.81
var_three ='I am data science'
print(type(var_one))
print(type(var_two))
print(type(var_three))


# 4.	 1) Write a difference between tuple vs list vs set.
# #Lists
# 
# List is a collection which is ordered- indexable or hashable
# Lists are mutable (changeable) .
# Allows duplicate members
# Brackets used to represent: []
# Lists are like arrays declared in other languages.
# 
# #Tuples
# 
# Collection of items which is ordered. - indexable or hashable
# Tuples are immutable (unchangeable) .
# Brackets used to represent: ()
# Only difference between tuples and lists are that lists can be changed.
# Tuples are faster than lists as they are immutable.
# 
# #Sets
# 
# Collection of Unordered and Unindexed items.- non-indexable or unhashable
# Sets are mutable (changeable).
# Does not take duplicate Values.
# Sets are unordered, so you cannot be sure in which order the items will appear.
# Brackets used to represent: { }.
# Sets are not faster than lists however they have a upper hand when it comes to membership testing.

# 4. 2)  Perform data conversion.
# 	> int to float and vice versa
# 	> str to float and int 
# 	> list to set and vice versa
# 	> list to tuple 
# 	> set to tuple
# 

# In[12]:


# int to float and vice versa

a=10
b=10.5
c=float(a)
d=int(b)
print("Integer to float",c, type(c))
print("Foloat to Integer",d, type(d))


# In[9]:


# str to float and int 

a='135'
b=int(a)
c=float(a)

print("String to float",c, type(c))
print("String to Integer",b, type(b))


# In[14]:


#list to set and vice versa

listofname = ['Ananth','Arun','Siva','Balaji','Balaji']
print("List = ",listofname)
setconversion = set(listofname)
print("Set = ",setconversion)
listconversion = list(setconversion)
print("set to list = ",listconversion)


# In[16]:


#list to tuple 
listofname = ['Ananth','Arun','Siva','Balaji','Balaji']
print("List = ",listofname)
tupleconversion = tuple(listofname)
print('tuple =',tupleconversion)
#set to tuple
newset ={1,2,3,4,5}
newtuple = tuple(newset)
print("set to tuple =", newtuple)


# 5.	Python as a calculator
# You can try the following operators:
# 
# | Operator | Description |
# | :------: | :---------: |
# | +        |Addition|
# | -        |Subtraction|
# | *        |Multiplication|
# | /        |Division|
# | %        |Modulus|
# | **       |Exponent|
# | //       |Floor Division|
# 
# Note : Use int and float data type and perform atleast one case per operator and add your comment on each operator.
# 

# In[25]:


a=205
b=20.50
print(a+b, type(a+b))

print(a-b, type(a-b))

print(a*b, type(a*b))

print(a/b, type(a/b))

print(a%b, type(a%b))

print(a**b, type(a**b))

print(a//b,type(a//b))

#all the above mathematical operators using int and float will return float type result


# mylist = ["Hello",12,"world",11.111,'Me2']
#    Hello
#    [12, 'world']
#    Me2
# 
# Slice mylist to get the above output.
# 

# In[27]:


mylist = ["Hello",12,"world",11.111,'Me2']
print(mylist[0])
print(mylist[1:3])
print(mylist[len(mylist)-1])


# 7.	a=[1,2,3,4], b=['A','B','C']
# 
# a+b ?  perform this operation and comment on the operation.
# 8.	a.append(b)  perform this operation and comment on the operation.
# 9.	a.extend(b)  perform this operation and comment on the operation.
# 

# In[32]:


a=[1,2,3,4]; b=['A','B','C']
print(a+b,type(a+b))
#it will combine both list 
print(a)
print(b)


# In[31]:


print(a.append(b))
print(a)
print(b)
#it will add whole list b at the end of the list a i.e,list of list


# In[33]:


a=[1,2,3,4]; b=['A','B','C']
a.extend(b)
print(a)
print(b)
#it will combine a and b and store the value to a i.e, single list


#    9. What is the difference between “+” ,append ,extend. Brief out.
#     concat operator + will just concat two string/list..etc unless we store it in any variable , it wont automatically store in anywhere
#     append adds an element to a list, and extend concatenates the first list with another list (or another iterable, not necessarily a list.)
# 
# 

# 10.	1) Create a tuple containing a set , list , various data type in it.
#          2)  try to overwrite some element in the tuple list which was created above.
# 

# In[36]:


a=({1,3,5},[1,2,2,3,4,4],1,2.5,True,'data scientist')
a[1][0]=2
print(a)
a[0][1]=2
#sets are not indexable thats y it will throw error
#tuple elements we can't modify


# In[ ]:




