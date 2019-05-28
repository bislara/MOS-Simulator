import matplotlib.pyplot as plt

from functions.function import *
from matplotlib.widgets import Slider,Button  # import the Slider widget
from scipy.integrate import odeint
import numpy as np

print("Welcome !!!")
#print("Enter all the values in the MKS system")

global Phi_m,tox,NA,ND,r,count,Qox,Qc,q,Es,Phi_t,Shi_F


#user input
#NA=float(input("Enter the value of NA in per m^3 :"))
#tox=float(input("Enter the value of oxide thickness in nm :"))
#Phi_m=float(input("Enter the value of Phi_m :"))


#constants initialize
q=1.6*10**(-19)	        
Eo=8.854*10**(-12)	
ks=11.7			#ks for Si
kox=3.9			#kox for SiO2
Ni=1.15*10**16		
Phi_t=0.0259            #Thermal Voltage Phi_t=k*t/q

tox=2*10**(-9)
NA=5*10**23
Phi_m=0.56
ND=10
Qox=10**(-5)
Phi_m=0.56

#variable declaration

Es=ks*Eo		
Eox=kox*Eo		

Vgb=1

No=(Ni**2)/NA
Po=NA
Cox=Eox/tox
Qox=10**(-5)
Shi_F=Phi_t*log((NA)/(Ni)) 	
Vfb=-Phi_m-Shi_F-Qox/Cox

gm=(sqrt(2*q*Es*NA))/(Cox)
f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  
n=2*Shi_F+Phi_t*6
x0= min(f,n)
#d=derivFunc(x0,Vgb,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)
x1=func(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)
#val=newtonRaphson(Vgb,x0)  
print("x0 is :",x1,x0)


# function that returns dz/dt
def model(z,t):
   
    dydt = -(sqrt(2*q*Es*NA)/Es)*sqrt(Phi_t*e**(-z/Phi_t)+z-Phi_t+e**((-2*Shi_F)/Phi_t)*(Phi_t*e**(z/Phi_t)-z-Phi_t))
    #dzdt = [dxdt,dydt]
    #print(dydt)
    return dydt

# time pointss
t = np.linspace(0,10**10)

# solve ODE
z = odeint(model,x0,t)
#print(z)

# plot results
plt.plot(t,z,'b-',label=r'$\frac{dx}{dt}=3 \; \exp(-t)$')
#plt.plot(t,z[:,1],'r--',label=r'$\frac{dy}{dt}=-y+3$')
plt.ylabel('response')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()



