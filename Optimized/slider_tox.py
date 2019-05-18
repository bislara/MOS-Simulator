#importing modules to main_code
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from functions.function import *
from matplotlib.widgets import Slider  # import the Slider widget


#variable declaration
global Vgb_1,Vgb_2,Phi_g,tox,NA,ND,Condition,r

print("Welcome !!!")
print("Enter all the values in the MKS system")

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.15)


#constants initialize
Phi_t=0.0259            #Thermal Voltage Phi_t=k*t/q
q=1.6*10**(-19)	        
Eo=8.854*10**(-12)	
ks=11.7			#ks for Si
kox=3.9			#kox for SiO2
Ni=1.15*10**16		
i=0
plot_type=0
r=[]	
Y_list=[]
V_list=[]

Condition=1
colour_count=1
colours={1:'b',2:'g',3:'r',4:'c',5:'m',6:'y',7:'k'}

tox=2*10**(-9)
NA=5*10**23
Phi_g=0.56
ND=0


Es=ks*Eo		
Eox=kox*Eo		#permittivity

No=(Ni**2)/NA
Po=NA
Shi_F=Phi_t*log((NA)/(Ni)) 	
n=2*Shi_F+Phi_t*6	
Vfb=-0.56-Shi_F


#user input
Vgb_1=float(input("Enter the value of starting value of Vgb :\n"))
Vgb_2=float(input("Enter the value of end value of Vgb :\n"))


#to take 0.1 steps in Vgb
for i in range(int(Vgb_1),int(Vgb_2*10)):
	r.append(i/10.0)


for Vgb in r:
	Cox=Eox/tox
	gm=(sqrt(2*q*Es*NA))/(Cox)
	f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  
	x0= min(f,n)	
	val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
	#print("the val is : ",val)
	Y_list.append(val)
	V_list.append(Vgb)

# plotting_graph
plt.ylim(0,1.2) 
plt.xlim(0,1.5) 

plt.title('Vgb VS SHI graph') 

plt.xlabel('Vgb value') 
plt.ylabel('SHI value')

graph_plot,= plt.plot(V_list, Y_list,color ='r',label="tox=2nm")

axSlider1= plt.axes([0.1,0.04,0.8,0.03])
#slder1 = Slider(axSlider1, 'Slider 1', valmin=0, valmax=100)
slder2 = Slider(			ax=axSlider1,
					label='Slider',
					valmin=1*10**(-9),
					valmax=5*10**(-9),
					valinit=2*10**(-9),
					valfmt='%1.2f',
					color="green")


def val_update(val):
	Y_list=[]
	V_list=[]
	tox=slder2.val
	global Phi_t,q,Eo,ks,kox,Ni,NA,Phi_g,ND,Es,No,Po,Shi_f,n,Vfb,Vgb_1,Vgb_2,r

	Cox=Eox/tox
	#print("Cox is ",Cox)		
	gm=(sqrt(2*q*Es*NA))/(Cox)

   	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
	#	print("the val is : ",val)
		Y_list.append(val)
		V_list.append(Vgb)
	
	graph_plot.set_ydata(Y_list)
	graph_plot.set_xdata(V_list)
	plt.draw          # redraw the plot


slder2.on_changed(val_update)

plt.show()




