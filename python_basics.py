#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
print(sys.version)


# In[2]:


x=20
print(type(x))


# In[3]:


y=2.44
print(type(y))


# In[4]:


z='rowida'
print(type(z))


# In[5]:


str1="task number one"
print(str1)



# In[6]:


#slice string by leaving out the start index
print(str1[:6])


# In[7]:


print(str1[3:])


# In[8]:


#negative indexing to start from the end
print(str1[-5:])


# In[9]:


str2=" Rowida Taher"
print(str2.upper())
print(str2.lower())


# In[10]:


#remove Whitespace 
print(str2.strip())


# In[11]:


#replace string with another string
print(str2.replace("o","e"))


# In[12]:


#split string into substrings
print(str2.split(" "))


# In[13]:


#String Concatenation
c=str1 + str2
print(c)
print(c.split(" "))


# In[14]:


#f-strings format
age=22
print(f"{str2} is {age}")


# In[15]:


#placeholder with modifier
print(f"my age is {age:.2f}")


# In[16]:


#count
print(c.count("one"))


# In[17]:


#find
print(c.find("number"))


# In[18]:


print(len(c))


# In[20]:


num=int(input("enter a number: "))
if num%2==0:
    print(f"{num} is Even number")
else:
    print(f"{num} is Odd number")


# In[21]:


num1=1
while num1<=10:
    if num1==5:
        num1+=1
        continue
    print(num1)
    num1+=1


# In[22]:


num3=1
while num3<=10:
    print(num3)
    if num3==5:
        break
    num3+=1
  


# In[26]:


for i in range(10):
    if i==7:
        break
    print(i)



# In[30]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numbers:
    if i%5==0:
        continue
    print(i)


# In[64]:


#list indexed,mutable
grades=["good","excellent","verygood"]
if "verygood" in grades:
    print("yes")
print(grades[:-1])

#replace values of list and insert
grades[0:2]=["G","E","F"]
print(grades)

#insert without replace
classes=["A","B","C"]
classes.insert(2,"GG")
print(classes)

#add in the end of list
classes.append("ss")
print(classes)

#extend list
classes.extend(grades)
print(classes)

#remove last item
classes.pop()
print(classes)

#remove
grades.remove("F")
print(grades)

#del
del grades[0]
print(grades)

#clear list
grades.clear()
print(grades)

#delete list
del grades
print(grades)


# In[81]:


#List comprehension>>create new list from existing list
fruits=["apple","orange","watermelon"]
newlist=[x for x in fruits]
print(newlist)

newlist=[x if x!="watermelon" else 
      "grapes" for x in fruits]
print(newlist)
#sort list
lst=[10,20,30]
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)


# In[87]:


#make copy of list
lst2=fruits.copy()
print(lst2)

lst3=list(fruits)
print(lst3)

lst4=fruits[:]
print(lst4)


# In[103]:


#tuples indexed,immutable
tuple=("a","b","c")
print(tuple)
print(type(tuple))
print(tuple[0])
tuple.index("c")

newtuple=tuple*2
newtuple

tuple[2]="d"



# In[113]:


#sets unindexed,immutable,no duplicate
set={"a","b","c","a"}
set1={1,2,3,4,5}
print(set)
print(type(set))

#add item
set.add("ee")
set

#update or join
set1.update(set)
set1

#remove item or discard()
set1.remove("ee")
set1

#join
set2 = {"a", "b", "c"}
set3 = {1, 2, 3}

#union
union_Set=set2.union(set3)
union_Set




# In[114]:


#function
def print_first_name(name):
    print(f"the first name is {name}")
print_first_name("rowida")


# In[115]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




