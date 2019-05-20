#importing modules to main_code
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from functions.function import *
from matplotlib.widgets import Slider  # import the Slider widget


#variable declaration
global Vgb_1,Vgb_2,Phi_m,tox,NA,ND,Condition,r

print("Welcome !!!")
print("Enter all the values in the MKS system")

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)


#user input
Vgb_1=float(input("Enter the value of starting value of Vgb :\n"))
Vgb_2=float(input("Enter the value of end value of Vgb :\n"))
#NA=float(input("Enter the value of NA in per m^3 :"))
#tox=float(input("Enter the value of oxide thickness in nm :"))
#Phi_m=float(input("Enter the value of Phi_m :"))


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
#tox=tox*10**(-9)
NA=5*10**23
Phi_m=0.56
ND=0


Es=ks*Eo		
Eox=kox*Eo		




#to take 0.1 steps in Vgb
for i in range(int(Vgb_1),int(Vgb_2*10)):
	r.append(i/10.0)


for Vgb in r:
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Vfb=-Phi_m-Shi_F
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
plt.legend()

plt.xlabel('Vgb value') 
plt.ylabel('SHI value')

graph_plot,= plt.plot(V_list, Y_list,color ='r',label="tox=2nm")



axSlider1= plt.axes([0.1,0.12,0.6,0.03])

#slder1 = Slider(axSlider1, 'Slider 1', valmin=0, valmax=100)
slider1 = Slider(			ax=axSlider1,
					label='Tox',
					valmin=1*10**(-9),
					valmax=5*10**(-9),
					valinit=tox,
					valfmt='tox is '+'%1.11f'+ ' in m',
					color="green")



axSlider2= plt.axes([0.1,0.05,0.6,0.03])
slider2 = Slider(axSlider2,'NA', valmin=1, valmax=20,valinit=NA/(10**23),valfmt='NA is '+'%1.2f'+ ' in 10**23')


def val_update_tox(val):
	global tox,NA
	Y_list=[]
	V_list=[]
	tox=slider1.val
	print("NA is ",NA)
	print("tox is ",tox)	
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Vfb=-Phi_m-Shi_F

	Cox=Eox/tox		
	gm=(sqrt(2*q*Es*NA))/(Cox)

   	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
	#	print("the val is : ",val)
		Y_list.append(val)
		V_list.append(Vgb)
	#plt.plot(V_list, Y_list,color ='r',label="tox= "+tox)
	
	graph_plot.set_ydata(Y_list)
	#graph_plot.set_xdata(V_list)
	plt.draw          # redraw the plot


def val_update_NA(val):
	global tox,NA,Phi_m
	Y_list=[]
	V_list=[]
	NA=(slider2.val)*10**23
	print("NA is ",NA)
	print("tox is ",tox)	
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Vfb=-Phi_m-Shi_F

	Cox=Eox/tox
	gm=(sqrt(2*q*Es*NA))/(Cox)

   	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
		Y_list.append(val)
		V_list.append(Vgb)
	
	graph_plot.set_ydata(Y_list)
	#graph_plot.set_xdata(V_list)
	plt.draw          # redraw the plot


def val_update_Phi(val):
	global tox,NA,Phi_m
	Y_list=[]
	V_list=[]
	NA=(slider3.val)*10**23
	print("NA is ",NA)
	print("tox is ",tox)	
	Po=NA
	No=(Ni**2)/NA
	Shi_F=Phi_t*log((NA)/(Ni)) 	
	n=2*Shi_F+Phi_t*6	
	Vfb=-Phi_m-Shi_F

	Cox=Eox/tox
	gm=(sqrt(2*q*Es*NA))/(Cox)

   	for Vgb in r:
		f=(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= min(f,n)
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po)  
		Y_list.append(val)
		V_list.append(Vgb)
	
	graph_plot.set_ydata(Y_list)
	#graph_plot.set_xdata(V_list)
	plt.draw          # redraw the plot



slider1.on_changed(val_update_tox)
slider2.on_changed(val_update_NA)
slider3.on_changed(val_update_Phi)

plt.show()


