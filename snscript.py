##Elsa M. Johnson
##Some of my old data to play with....
##Basic script to cut and paste into python so data is ready to go. 
##If you want to make this more efficient go for it.
##Here x and y are typically colors or apparent magnitudes, 
##there are other columns that for now can be ignored
## T is the kind of object.
##importing three columns of data and getting rid of bad points:
import csv

x=[]
y=[]
t=[]
with open("emj_data.csv", 'rU') as sdss:
    ms = csv.reader(sdss,delimiter=',',dialect='excel')
    ms.next()
    for row in ms:
	t.append(row[1])
        x.append(row[5])
        y.append(row[7])

x=x[0:870]
y=y[0:870]
t=t[0:870]
xx=[float(i) for i in x]
yy=[float(i) for i in y]
xv=[]
yv=[]
tv=[]
for i,j,k in zip(xx,yy,t):
  if abs(i)<10 and abs(j)<10:
    xv.append(i)
    yv.append(j)
    tv.append(k)
    
#Script to separate color data by kind of object:
# Obviously apply to different types to get info. There are 
#more elegant ways of doing this by using pandas and dataframes.
ls1=[]
ls2=[]
ls3=[]
for i,j,k in zip(xv,yv,tv):
  if k=='1.0':
    ls1.append(i)
    ls2.append(j)
    ls3.append(k)

