#!/usr/bin/env python
# coding: utf-8

# In[62]:


print("Given grammar is " )
print("S -> aBb/ccA")
print("A -> b/c")
print("B -> a/b")
def S():
    global i
    if s[i] == 'a':
        i += 1
        B()
        if s[i] == 'b':
            i += 1
        else:
            error()
    elif s[i] == 'c':
        i += 1
        if s[i] == 'c':
            i += 1
            A()
        else:
            error()

def A():
    global i
    if s[i] == 'b' or s[i] == 'c':
        i += 1
    else:
        error()

def B():
    global i
    if s[i] == 'a' or s[i] == 'b':
        i += 1
    else:
        error()

def error():
    print("string is invalid")

i = 0
s = input("Enter String to check\n")

S()
if i == len(s):
    print("string is valid")
else:
    print("string is invalid")



# In[ ]:




