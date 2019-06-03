import matplotlib.pyplot as plt
from math import *
from sympy import *
global Y,deriv,dydx,count
count=0
h=5

global Vgb,Vfb,q,Es,Cox,Po,No,St,NA,ND

Vgb=-1
Vfb=-1
NA=10**23
ND=10**5
St=0.026
q=1.6*10**(-19)
Es=1.05*10**(-10)
Cox=1.726*10**(-2)
No=10**7
Po=10**22


Y1_list=[]
V1_list=[]

Y_list=[]
V_list=[]

i=0
r=[]
gm=(sqrt(2*q*Es*NA))/(Cox)
for i in range(-100,100):
	r.append(i/100.0)
for Vgb in r: 
        print("gm is ",gm)  
	f=-0.826+ 0.026*6
	Y_list.append(f)
	V_list.append(Vgb)
	
for Vgb in r: 
	
        print("gm is ",gm)  
	f=-(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )
	m=Vfb+f+gm*sqrt(abs(f))
	n=-(0.826)-0.026*6	
        #if Vgb>m:
	#	Y_list.append(f)
	#	V_list.append(Vgb)
	Y1_list.append(max(f,n))
	V1_list.append(Vgb)
	
plt.plot(V1_list, Y1_list,color ='red')
plt.ylim(-1,2) 
plt.xlim(-1,1) 

#plt.plot(V_list, Y_list,color ='r')
plt.xlabel('Vgb value') 
plt.ylabel('SHI value')

plt.title('Vgb Vs SHI graph') 
  
plt.show()   

