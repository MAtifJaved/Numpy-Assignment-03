#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Question:1
#Convert a 1D array to a 2D array with 2 rows?
#Desired output::
#array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])


# In[11]:


import numpy as np
arr=np.arange(0,10)
print(arr)
arr.reshape(2,5)


# In[13]:


#Question:2
#How to stack two arrays vertically?
#Desired Output::
#array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
import numpy as np
arr1=np.arange(10).reshape(2,5)
arr2=np.ones(10, dtype=int).reshape(2,5)
print(arr1,arr2)
np.vstack((arr1,arr2))


# In[14]:


#Question:3
#How to stack two arrays horizontally?
#Desired Output::
#array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1], [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
import numpy as np
arr1=np.arange(10).reshape(2,5)
arr2=np.ones(10, dtype=int).reshape(2,5)
print(arr1,arr2)
np.hstack((arr1,arr2))


# In[15]:


#Question:4
#How to convert an array of arrays into a flat 1d array?
#Desired Output::
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
import numpy as np
arr=np.array([[0,1,2,3,4],[5,6,7,8,9]])
print(arr)
arr.flatten()


# In[17]:


#Question:5
#How to Convert higher dimension into one dimension?
#Desired Output::
#array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
import numpy as np
arr=np.arange(15).reshape(1,3,5)
print(arr.ndim,"Dimension")
print(arr)
arr=arr.flatten()
print(arr.ndim,"Dimension")
arr


# In[18]:


#Question:6
#Convert one dimension to higher dimension?
#Desired Output::
#array([[ 0, 1, 2], [ 3, 4, 5], [ 6, 7, 8], [ 9, 10, 11], [12, 13, 14]])
import numpy as np
arr=np.arange(15).reshape(-1,3)
arr


# In[19]:


#Question:7
#Create 5x5 an array and find the square of an array?
import numpy as np
arr=np.arange(25).reshape(5,5)
print(arr)
np.square(arr)


# In[22]:


#Question:8
#Create 5x6 an array and find the mean?
import numpy as np
np.random.seed(432)
arr=np.random.randint(30, size=(5,6))
print(arr)
arr.mean()


# In[23]:


#Question:9
#Find the standard deviation of the previous array in Q8?
import numpy as np
np.random.seed(432)
arr=np.random.randint(30, size=(5,6))
print(arr)
np.std(arr)


# In[24]:


#Question:10
#Find the median of the previous array in Q8?
import numpy as np
np.random.seed(432)
arr=np.random.randint(30, size=(5,6))
print(arr)
np.median(arr)


# In[25]:


#Question:11
#Find the transpose of the previous array in Q8?
import numpy as np
np.random.seed(432)
arr=np.random.randint(30, size=(5,6))
print(arr)
arr.T


# In[36]:


#Question:12
#Create a 4x4 an array and find the sum of diagonal elements?
import numpy as np 
n_array = np.array([[1, 2, 15,12], [13,30, 44, 2], [11,45,45,77],[12,12,13,42]]) 
print("Numpy Matrix is:") 
print(n_array)
# calculating the Trace of a matrix 
trace = np.trace(n_array)   
print("\n The Diagonal Sum of given 4X4 matrix:") 
print(trace) 


# In[37]:


#Question:13
#Find the determinant of the previous array in Q12?
import numpy as np 
n_array = np.array([[1, 2, 15,12], [13,30, 44, 2], [11,45,45,77],[12,12,13,42]])
print(n_array)
np.linalg.det(n_array)


# In[44]:


#Question:14
#Find the 5th and 95th percentile of an array?
import numpy as np
arr=np.arange(10)
print("The Original Array is:-")
print(arr)
print("The 5th Percentile of the Original Array is:-")
print(np.percentile(arr,5))
print("The 95th Percentile of the Original Array is:-")
print(np.percentile(arr,95))


# In[45]:


#Question:15
#How to find if a given array has any null values?
import numpy as np
   
# Returns True/False value elementwise  
b = np.arange(25).reshape(5, 5) 
                 
print("\nIs NaN: \n", np.isnan(b)) 
    
c = [[1,2,3],  
     [np.nan,2,2]] 
print("\nIs NaN: \n", np.isnan(c)) 

