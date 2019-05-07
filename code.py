import pandas as pd
#dates=pd.date_range('2019-01-01','2019-07-07',freq='w') #display date week wise
date=pd.date_range('2019-01-01','2019-07-07',freq='m')  #display date month wise
b=pd.Series([81,82,83,96,42,98],index=date)
c=pd.Series(['da','fa','fa','we','oo','s'],index=date)
d=pd.Series([1,2,3,4,5,6],index=date)
dateframe=pd.DataFrame({'midterm':b,'finals':c,'col3':d}) #creating dataframe
e=dateframe.midterm-dateframe.col3
#print(dateframe['col3']) #getting a specific column
f=dateframe.col3+dateframe.midterm
dateframe2=pd.DataFrame({'midterm':b,'finals':c,'col3':d,"difference":e,"multiply":f})
print(dateframe2)
print(dateframe2.iloc[3]) #getting a the coumn values of the index starting from 0
print(dateframe2.iloc[2:4]) #getting a the coumn values of the index starting from 0
print(dateframe2.iloc[2:4].midterm) #getting the values of a specific column of the index
print(dateframe2.iloc[1:3].finals) #getting the values of a specific column of the index
#print(dateframe2.loc['2019-03-31']) #getting the label values
