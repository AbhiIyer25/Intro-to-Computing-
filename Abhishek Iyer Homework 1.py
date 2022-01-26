#!/usr/bin/env python
# coding: utf-8

# Question 1:

# In[44]:


numbers = list(range(30, 61, 5))
print(type(numbers))
print(numbers)

print(numbers[::-1])

numbers.append(65)
print(numbers[::-1])


# Question 2:

# In[52]:


list1 = []
for number in range(0, 21):
    list1.append(number)
print(list1)

list1.remove(list1[0])
print(list1)

print("length:", len(list1))
print("maximum:", max(list1))
print("minimum:", min(list1))

print("sum:", sum(list1))


# Question 3:

# In[53]:


weather = {'sunny': 'play', 'rainy': 'watch TV', 'cloudy': 'walk'}
print(type(weather))
print(weather)

for keys, values in weather.items():
    print(keys, values, ",", end=' ')
print(" ") #adds a space after the for loop so the next command can start on the next line

for keys, values in weather.items():
    print("When", keys, "let us", values)

weather.update({'snowy': 'ski'})
print(weather)






