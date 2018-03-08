
# coding: utf-8

# In[1]:


## python for loop
# for loop iterates over the items of the sequence - strings or lists

words = ['foo', 'bar', 'baz']
for word in words:
    print(word)


# In[2]:


# concurrent modification of sequence - use slice to make a copy of the sequence

for word in words[:]:
    words.insert(0, 'test')   


# In[4]:


print(words) 


# In[5]:


## range function
# returns iterable object, meaning when iterated upon, returns successive items of the desired sequence
print(range(10))


# In[7]:


# functions and constructs which takes iterable object as argument - for statement and list() are examples:
# meaning iterables till the supply is exhausted

for i in range(10):
    print(i, end=',')
    


# In[10]:


# step and start in range function
for i in range(1, 10, 2):
    print(i, end=',')


# In[11]:


# passing range return iterable object to list constructor
print(list(range(6)))


# In[12]:


# iterate over indices of a list
for i in range(len(words)):
    print(i, words[i])


# In[2]:


# using else clause with loops
# in case of exhaustion for loop.. and when condition becomes false, while loop..else is executed but not when loop terminates because of break statement

# prime numbers

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")


# In[1]:


# continue - continues with next iteration of the loop

for n in range(10):
    if n % 2 == 0: 
        print(n, "is an even number")
        continue
    print(n, "is not an even number")    


# In[ ]:


# using pass
while True:
    pass


# In[13]:


# understanding scope of python variables
counter = 2
def test():
    counter = 3
    print(counter)
    
print(counter)    
    

if __name__ == "__main__":
      test()
print(counter) 

