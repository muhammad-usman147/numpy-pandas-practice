#generators, lambda, sets, decorators
'''
you can call numpy(numerical Python) as an array
it is use in data scince, numpy is very fast as compare to normal python code
anything 
'''
import numpy as np
#ls=[x for x in range(0,10)]

#alist=np.array(ls)
#print(alist*2) #this is called vectorized operations using numpy and also 
#casting as converting list into array using numpy
#a=np.arange(10)  #making array using arange 
#print(a)
#--------
#l1=[1,2,3,4]
#l2=[5,6,9,8]
#print(l1-l2) #you cannot subtract list
#print(l1+l2) #this is a concatinating is list
#l1=np.array(l1)
#l2=np.array(l2)
#1d array is vector
#2d array is matrix
#0d array is scalar
'''
print(l1+l2) #this is adding array
print(l1-l2)#this is subtracting array
print(l1.ndim) #vector is 1 in .ndim
 '''
#-----
'''
d2=np.array([[1,2,3,4],[4,5,6,7],[8,9,10,11]]) #this is a matrix having 3 rows and 4 colums
print(d2) #outputing matrix
print(d2.ndim) #2 is represents  matrix in ndim 
'''
#---=
'''
d2=np.array([[[1,2,3],[4,5,6],[7,8,9],[2,4,5]],[[4,5,6],[3,7,8],[9,8,7],[4,6,7]]]) #this is a matrix having 3 rows and 4 colums
#print(d2.ndim) #3 represents 3 dimension
#print(d2)  #this is a 3 3 direction array
 
d2array=np.arange(100).reshape(10,10) #creating value from 0 10 99 with 10 rows and 10 column
#.reshape(10,10 ) is 10 rows and 10 column
#print(d2array)
vector=d2array.reshape(10,10) #converting 2d into 1d/vector
print(vector)
'''
#----

#multiplying matrix/ mirror multiplication
#m1=np.arange(25).reshape(5,5)
#m2=np.arange(25).reshape(5,5)
#print(m1.shape) #showing shape in rows and columns
#print(m1*m2) #it is also called element wise multiplicaton and mirror multiplication
#in matrix multiplication, order is mandatory
#exp (5,5) matrix cannot be multiply by (4,4)

#m1=np.arange(25).reshape(5,5)
#m2=np.arange(16).reshape(4,4)
#print(m1*m2)
#this will generate an error, because of different rows

#----
#dot multiplication of different matrixs
#m1=np.arange(16).reshape(4,4)


#m2=np.arange(20).reshape(5,4)
#print(m2@m1) #this is not mirror multiplication, this is dot multiplication
#but you cannot multipy m1 @ m2
# when the m1 column is matching the m2 row of other matrix(m2)
#print(m2)
#print(m2.size) #this returns the number of elements in a matrix
#print(m2.size)
#print(np.size(m2,0)) #it will give you the total row number
#print(np.size(m2,1)) #it will give you the total column number
#print(np.zeros(50).reshape(5,10) #creating matrix with zero matrix
#print(np.linspace(1,100,10)) #do research on it...?? 
#x=np.ones(100).reshape(10,10)#creating matrix with 100 values and all values are 1
#print(x*100) #multipling all value by 100, exp [[100,100...],...[100,1000...]]
#print(m2)
#print(m2[1:3,3:4]) #this is slicing, it is getting value which is at 4 row and 1st column
#print(m2[1,3])

#----

#a3=np.array([5,3,34]*10) #here it is multiplying the list 10 times, values will be coped bc it's a list
#a3=np.array([5,3,34])*10 #here it is multiplying the value by the, because it is an array
#a4=np.ones((8,4,4)) #3d array #1st value=depth 2nd is row and 3rd is column
a4=np.arange(20).reshape(5,4)
#print(a4)
#print(a4/3+2)
#---
#a4=np.empty((4,5)) #these returns the garbage values and can be zero or non-zero
#print(a4)
#a5=np.ones_like() #this copies shape can data type
#print(a5)
#a6=np.eye(5) #which have the diagonal ones

#a5=np.arange(9,19).reshape(5,2)
#a6=np.arange(10).reshape(5,2)
#x=a5==a6  #it is comparing the values, if any value of a5 becomes equal to a6 then it wil true. else false
a5=np.arange(81).reshape(9,9)
print(a5)
a5[3:7,3:7]=a5[3:7,3:7]*0
print(a5)