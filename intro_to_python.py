
# coding: utf-8

# In[53]:


##  strings

# Using raw string in print statement
print(r"C:\deep\name")
print("C:\deep\name")

# String slicing
word = "hello, world"
print("printing complete word:", word[:])
print("printing first word:", word[:5])
print("print last word:", word[7:])

# length of the string
print(len(word))

# Avoid newline in first line
print("""Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


# In[54]:


# python strings are immutable
word[0] = 'J'


# In[45]:


## lists

# list indexing and slicing
# slice operation returns a new list
tlist = [1, 2, 3, 4, 5, 6, 7, 8]
print(tlist[:])

# concatenation
tlist2 = [9, 10, 11]
print(tlist[5:] + tlist2)

# append
tlist.append(9)
print(tlist)

# lists are mutable
tlist[0] = 7
print(tlist)

# assignment to slices
tlist[5:] = []
print(tlist)

# length of lists
print(len(tlist))

# nested lists
p = ['a', 'b', 'c']
q = ['d', 'e', 'f']
r = [p, q]
print(r)
print(r[0])
print(r[0][0])





# In[50]:


## multiple assignments in python

# Fibonacci series example
a, b = 0, 1
while (b < 10):
    print(b, end=',')
    a, b = b, a + b

