import pandas as p
from pandas import Series
import math as m
'''
class Function:
    def Writer(self,lister):
        ls=[] #for the highest value
        points=[]
        matrix_array=[]
        #generating the rows and column values of a matrix
        for i in lister:
            for j in range(1,i.size):
                if i.size%j==0: #if the j is divisible by the size of the 
                                #array then use it
                    x=j
                    points.append(x)
            print(points)
            betw=m.ceil(len(points)/2) #taking the middile value of a matrix
            ls.append(str(points[betw])+" "+str(i.size)+"$$ ") 
            matrix=i.reshape(points[betw],int(i.size/points[betw]))
            #here points[betw] is the row  and  i.size/points[betw] is the column 
            #of the respective matrix
            points.clear()
            matrix_array.append(matrix)
        return matrix_array
#DYNAMIC MATRIX GENERATOR
class MainClass:
    def __init__(self,obj):
        self.fobj=obj #object of Function Class
    def main(self):
        ls2=[x for x in range(1,201,3) if x%2==0]
        ls=[x for x in range(1,201,3) if x%2!=0]
        x=np.arange(10,200) #vector created
        ar=np.array(ls)
        ls2=np.array(ls2)
        #converting the x into matrix
        lister=[]
        lister.append(ls2)
        lister.append(x)
        lister.append(ar)
        print(fobj.Writer(lister))
fobj=Function()
obj=MainClass(fobj)
obj.main()
'''
#concatination 2 arrays
#a=np.arange(20).reshape(4,5)
#b=np.arange(21,41).reshape(4,5)
#concat can be done be 2 type   vertical and horizontal
#x=np.concatenate((a,b),axis=0) #this is vertical 
#when axis is 0 then it will add in the rows
#x=np.concatenate((a,b),axis=0) #this is horizontal s
#when axis is 1 then it will add in the columns

#second way to concat the arrays
#x1=np.vstack((a,b)) #when it is horizontal, axis will be 0 it will add in the rows 
#x1=np.hstack((a,b)) #when it is vertical, axis will be 1 it will add in the columns
#print(x1)

#there is another concatination
#print(a)
#print(b)
#x=np.dstack((a,b)) #meaning it is adding in the depth
#print(x)
#this is transposing the array
#x=np.transpose(a)
#print(x)
#boolean indexing
#a=np.array(['a','b','a','c','d','e','a'])
#b=np.random.randn(7,4)
#print(b)
#print(b[a=='a'])
 #here, in the sq brackets the 7 columns of a are the rows of b, which it will return
 #then the true values which it is returning is the column of b
#x=[i for i in range(19)]
#print(int(4.9))