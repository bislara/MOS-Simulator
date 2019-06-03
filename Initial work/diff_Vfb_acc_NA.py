import matplotlib.pyplot as plt
from math import *
from sympy import *
import csv

global Y,deriv,dydx,count
count=0
h=5
global Vgb,Vfb,q,Es,Cox,Po,No,St,NA,ND

#intial values 
x0=0
Vgb=-1
Vfb=0
NA=0
ND=0
St=0.0259
q=1.6*10**(-19)
#Es=1.05*10**(-10)
Es=11.7*8.854*10**(-12)

kox=3.9
Eo=8.854*10**(-12)
Eox=kox*Eo
tox=2*10**(-9)

Ni=1.18*10**16
#Cox=1.668*10**(-2)


#ni=1.26*10**13=sqrt(No*Po)
#PHI(f)=0.59266= PHI(t)*ln(NA/ni)
#2*PHI(f)= 1.1852

Y_list=[]
V_list=[]
Y1_list=[]
V1_list=[]
Y2_list=[]
V2_list=[]

i=0
r=[]

#Vfb=PHI(ms) + Q'o/C'ox

#funct to return the value of funct at a particuar value
def func(Vgb, Y ): 
    global Vfb,q,Es,Cox,Po,No,St,NA,ND
    #print("I am inside func  " , Y)
    try: 
      	  p=Vfb + Y + (sqrt(2*q*Es)/(Cox)) *(sqrt( Po*St*( e**(-Y/St )-1) +( NA-ND  )*Y + No*St*( e**(Y/St )-1) )  ) -Vgb
	  #print("the value of p is ",p)      	
	  return p 
    except ZeroDivisionError:
          print("Error!!!!!!!!!!!", Y)
    	  return 0    

#funct to find derivative in a particular value
def derivFunc( Y ): 
    k= deriv.doit().subs({t:Y})
   # print("I am inside deriv func  ", k)
    if k==0:
	return 1
    else:  
	return k

  
# Function to find the root 
def newtonRaphson( Vgb, Y ): 
    global count
    global Vfb,q,Es,Cox,Po,No,St,NA,ND,h
    if derivFunc(Y)!=0:
    	h = (func(Vgb,Y) )/ (derivFunc(Y)) 
    	print("h is ",h)

    while abs(h) >= 0.001: 
        count=count+1
	try:
      	    h = func(Vgb,Y)/derivFunc(Y)
	    Y = Y - h    
        except ZeroDivisionError:
            print("Error! - derivative zero for x = ", Y)
        # x(i+1) = x(i) - f(x) / f'(x) 
         
      
    #print("The value of the root is : ", 
     #                        "%.4f"% Y)
    print("the no of iterations is ",count) 
    return Y


for i in range(0,15):
	r.append(i/10.0)

#loop for newton Raphson method and using diff intial value for diff Vgb
for Vgb in r:
	NA=5*10**20
	No=(Ni**2)/NA
	Po=NA
	SiF=St*log((NA)/(Ni))
	Vfb=-0.56-SiF
	Cox=Eox/tox
	gm=(sqrt(2*q*Es*NA))/(Cox)
	f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  
	n=0.826+0.026*6
	x0= min(f,n)	
	t= Symbol('t')    
	f=Vfb + t + (sqrt(2*q*Es)/(Cox)) *(sqrt( Po*St*( e**(-t/St )-1) +( NA-ND  )*t + No*St*( e**(t/St )-1) )  ) -Vgb
	deriv= Derivative(f, t)
	val=newtonRaphson(Vgb,x0)  
	#print("the val is : ",val)
	Y_list.append(val)
	V_list.append(Vgb)

#loop for a different value of NA
for Vgb in r:
	Cox=Eox/tox
	NA=5*10**23
	No=(Ni**2)/NA
	Po=NA
	SiF=St*log((NA)/(Ni))
	Vfb=-0.56-SiF
	gm=(sqrt(2*q*Es*NA))/(Cox)
	f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2
	n=0.826+0.026*6
	x0= min(f,n)
	#print("x0 value is ",x0)	
	t= Symbol('t')    
	f=Vfb + t + (sqrt(2*q*Es)/Cox) *(sqrt( Po*St*( e**(-t/St )-1) +( NA-ND  )*t + No*St*( e**(t/St )-1) )  ) -Vgb
	deriv= Derivative(f, t)
	val=newtonRaphson(Vgb,x0)  
	#print("the val is : ",val)
	Y1_list.append(val)
	V1_list.append(Vgb)


for Vgb in r:
	NA=5*10**17
	No=(Ni**2)/NA
	Po=NA
	SiF=St*log((NA)/(Ni))
	Vfb=-0.56-SiF
	Cox=Eox/tox
	gm=(sqrt(2*q*Es*NA))/(Cox)
	f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2
	n=0.826+0.026*6
	x0= min(f,n)
	#print("x0 value is ",x0)	
	t= Symbol('t')    
	f=Vfb + t + (sqrt(2*q*Es)/Cox) *(sqrt( Po*St*( e**(-t/St )-1) +( NA-ND  )*t + No*St*( e**(t/St )-1) )  ) -Vgb
	deriv= Derivative(f, t)
	val=newtonRaphson(Vgb,x0)  
	#print("the val is : ",val)
	Y2_list.append(val)
	V2_list.append(Vgb)


# plotting_graph
plt.ylim(0.5,1.2)
plt.xlim(0,1.5) 

plt.plot(V1_list, Y1_list,color ='g',label="NA=5*10^23")

plt.plot(V_list, Y_list,color ='r',label="NA=5*10^20")

plt.plot(V2_list, Y2_list,color ='b',label="NA=5*10^17")


plt.xlabel('Vgb value') 
plt.ylabel('SHI value')

# show a legend on the plot 
plt.legend() 

plt.title('Vgb VS SHI graph') 
  
plt.show()   

