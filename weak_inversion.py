import matplotlib.pyplot as plt
from math import *
from sympy import *
global Y,deriv,dydx,count
count=0
h=5
global Vgb,Vfb,q,Es,Cox,Po,No,St,NA,ND

# Vgb= int(input("Enter the value of Vgb "))
# Vfb= int(input("Enter the value of Vfb "))
# q= int(input("Enter the value of q "))
# Es= int(input("Enter the value of Es "))
# Cox= int(input("Enter the value of Cox "))
# Po= int(input("Enter the value of Po "))
# No= int(input("Enter the value of No "))
# St= int(input("Enter the value of St "))
# NA= int(input("Enter the value of NA "))
# ND= int(input("Enter the value of ND "))
#x0 = float(input("enter the initial value : "))
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

Y_list=[]
V_list=[]
i=0
r=[]
gm=(sqrt(2*q*Es*NA))/(Cox)
for i in range(-100,100):
	r.append(i/100.0)
for Vgb in r: 
        print("gm is ",gm)  
	f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )
	m=Vfb+f+gm*sqrt(abs(f))
        #if Vgb>m:
	Y_list.append(f)
	V_list.append(Vgb)
	#else :	
	#	Y_list.append(0)
	#	V_list.append(Vgb)
	
#plt.plot(V_list, Y_list,color='green', linestyle='dashed', linewidth = 3, 
 #        marker='o', markerfacecolor='blue', markersize=10)


plt.plot(V_list, Y_list,color ='r')
plt.xlabel('Vgb value') 
plt.ylabel('SHI value')

plt.title('Vgb VS SHI graph') 
  
plt.show()   

