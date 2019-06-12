#importing modules to main_code
import matplotlib.pyplot as plt
from MOS_3_functions.function import *
from matplotlib.widgets import Slider,Button  # import the Slider widget
import numpy as np


print("Welcome !!!")

global Phi_m,tox,NA,ND,r,count,Qox,Qc


#constants initialize
q=1.6*10**(-19)	        
Eo=8.854*10**(-12)	
ks=11.7			#ks for Si
kox=3.9			#kox for SiO2
Ni=1.15*10**16		#intrinsic concentration in per m^3
Phi_t=0.0259            #Thermal Voltage Phi_t=k*t/q2
tox=2*10**(-9)
#tox=tox*10**(-9)
ND=5*10**23
Eg=0.56			#Eg=EG/2= 1.12/2
NA=10
Qox=10**(-5)
Phi_m=4.1		#for Al
Ea=4.05 		#electron affinity of Silicon
count=0
Vcb=0.4

#for more number of graphs and to distinguish between them 
colour_count=0
colours={1:'b',2:'g',3:'r',4:'c',5:'m',6:'y',7:'k'}

#variable declaration
r=[]	
Y_list={}
V_list={}
Y1_list={}
V1_list={}
Y2_list={}
V2_list={}
Y3_list={}
V3_list={}
Cox_list={}
Cox_val_list={}


Y_list[count]=[]
V_list[count]=[]
Y1_list[count]=[]
V1_list[count]=[]
Y2_list[count]=[]
V2_list[count]=[]
Y3_list[count]=[]
V3_list[count]=[]
Cox_list[count]=[]
Cox_val_list[count]=[]

graph_plot={}
graph_plot1={}
graph_plot2={}
graph_plot3={}
graph_plot4={}

Es=ks*Eo		
Eox=kox*Eo		


# plotting_graph
plt.title="Different graphs"

fig,((ax1, ax2), (ax3, ax4))= plt.subplots(2,2,sharey=False)
plt.subplots_adjust(left=0.05, bottom=0.30,right=0.98,top=0.95)


#labelling and limit of the axes
#1
ax1.set_xlim(-2.75,0.1) 
ax1.set_ylim(0,2.75) 

ax1.set_xlabel('Vgb (in V)') 
ax1.set_ylabel(r'$\psi_S$ (in V)')

ax1.minorticks_on()
ax1.tick_params(direction="in")

#2
ax2.set_xlabel(r'$ \psi_s$ (in V)') 
ax2.set_ylabel('Q (in C/m^2 *10^(-3))')

ax2.set_xlim(-2.75,0.1) 
ax2.set_ylim(0,10) 
ax2.minorticks_on()
ax2.tick_params(direction="in")


#3
ax3.set_xlim(-2.75,0.1) 
ax3.set_ylim(0,10) 

ax3.set_xlabel('Vgb (in V)') 
ax3.set_ylabel('Q (in C/m^2 *10^(-3))')
ax3.minorticks_on()
ax3.tick_params(direction="in")

#4
ax4.set_xlim(-2.85,0) 
ax4.set_ylim(0,3) 

ax4.set_xlabel('Vgb (in V)') 
ax4.set_ylabel('dQ/dVgb (in F/m^2 *10^(-2))')
ax4.minorticks_on()
ax4.tick_params(direction="in")


#2-D variable of graph
graph_plot[count]=[]
graph_plot[count],= plt.plot(V_list[count], Y_list[count],color ='r',label="")	

graph_plot1[count]=[]
graph_plot1[count],= plt.plot(V1_list[count], Y1_list[count],color ='r',label="")	

graph_plot2[count]=[]
graph_plot2[count],= plt.plot(V2_list[count], Y2_list[count],color ='r',label="")	

graph_plot3[count]=[]
graph_plot3[count],= plt.plot(V3_list[count], Y3_list[count],color ='r',label="")	

graph_plot4[count]=[]
graph_plot4[count],= plt.plot(Cox_list[count], Cox_val_list[count],color ='r',label="")	

plt.legend()



#button function for adding plots
def setValue(val):
	global count,colour_count,colours,Qox,Vcb
	count=count+1
	
	#initial list declaration
	Y_list[count]=[]
	V_list[count]=[]
	graph_plot[count]=[]
	Y1_list[count]=[]
	V1_list[count]=[]
	graph_plot1[count]=[]
	Y2_list[count]=[]
	V2_list[count]=[]
	graph_plot2[count]=[]
	Y3_list[count]=[]
	V3_list[count]=[]
	graph_plot3[count]=[]
	Cox_list[count]=[]
	Cox_val_list[count]=[]
	graph_plot4[count]=[]
	
	#initial calculations
	r=[]
	Po=(Ni**2)/ND	
	No=ND
	Shi_F=Phi_t*log((ND)/(Ni)) 	
	n=-(2*Shi_F+Phi_t*6+Vcb)	
	Cox=Eox/tox	
	Vfb=+Phi_m-Ea-Eg+Shi_F-Qox/Cox	
	gm=(sqrt(2*q*Es*ND))/(Cox)
	
	# drange funct for creating steps in for loop
	for i in drange(-2.75,-0.2,0.05):
		r.append(i)
	
	for Vgb in r:
		
		f=-(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  
		x0= max(f,n)		#initial value of NewtonRaphson
				
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po,Vcb) 
		Qc = (charge_funct(NA,Phi_t,Es,q,val,Shi_F,ND,Po,No,Vcb))
		dq_dVgb=deriv_funct(val,Qc,NA,Phi_t,Es,q,Shi_F,Vgb,Vfb,ND,Cox,No,Po,Vcb)
			
		V_list[count].append(Vgb)
		Y_list[count].append(abs(val))

		V1_list[count].append(val)
		Y1_list[count].append(abs(Qc)*1000)

		V2_list[count].append(Vgb)
		Y2_list[count].append(abs(Qc)*1000)

		V3_list[count].append(Vgb)
		Y3_list[count].append(dq_dVgb*100)
		
		Cox_list[count].append(Vgb)
		Cox_val_list[count].append(Cox*100)

	colour_count=colour_count+1
	
	#redrawing the graphs for different parameter value
	plt.sca(ax1)	
	graph_plot[count],= plt.plot(V_list[count], Y_list[count],color =colours[colour_count],label="Curve "+str(count))			
	plt.legend()

	plt.sca(ax2)
	graph_plot1[count],= plt.plot(V1_list[count], Y1_list[count],color =colours[colour_count],label="Curve "+str(count))			
	plt.legend()


	plt.sca(ax3)	
	graph_plot2[count],= plt.plot(V2_list[count], Y2_list[count],color =colours[colour_count],label="Curve "+str(count))			
	plt.legend()

	plt.sca(ax4)	
	graph_plot3[count],= plt.plot(V3_list[count], Y3_list[count],color =colours[colour_count],label="Curve "+str(count))
	graph_plot4[count],= plt.plot(Cox_list[count], Cox_val_list[count],color =colours[colour_count],linestyle='--')
			
	plt.legend()


def val_update_Vcb(val):
    global tox,NA,Phi_m,count,Qox,Vcb
	
    if count!=0:

	#initial list declaration
	r=[]
	Y_list[count]=[]
	V_list[count]=[]
	Y1_list[count]=[]
	V1_list[count]=[]
	Y2_list[count]=[]
	V2_list[count]=[]
	Y3_list[count]=[]
	V3_list[count]=[]
	Cox_list[count]=[]
	Cox_val_list[count]=[]

	Vcb=(slider1.val)
	
	Po=(Ni**2)/ND	
	No=ND
	Shi_F=Phi_t*log((ND)/(Ni)) 	
	n=-(2*Shi_F+Phi_t*6+ Vcb)	
	Cox=Eox/tox	
	Vfb=+Phi_m-Ea-Eg+Shi_F-Qox/Cox	
	gm=(sqrt(2*q*Es*ND))/(Cox)
	
	# drange funct for creating steps in for loop
	for i in drange(-2.75,Vfb-0.01,0.05):
		r.append(i)
	
   	for Vgb in r:
		f=-(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= max(f,n)		#initial value of NewtonRaphson
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po,Vcb) 
		Qc = (charge_funct(NA,Phi_t,Es,q,val,Shi_F,ND,Po,No,Vcb))
		dq_dVgb=deriv_funct(val,Qc,NA,Phi_t,Es,q,Shi_F,Vgb,Vfb,ND,Cox,No,Po,Vcb)
		
		V_list[count].append(Vgb)
		Y_list[count].append(abs(val))

		V1_list[count].append(val)
		Y1_list[count].append(abs(Qc)*1000)

		V2_list[count].append(Vgb)
		Y2_list[count].append(abs(Qc)*1000)

		V3_list[count].append(Vgb)
		Y3_list[count].append(dq_dVgb*100)
		
		Cox_list[count].append(Vgb)
		Cox_val_list[count].append(Cox*100)


	#redrawing the graphs for different parameter value
	graph_plot[count].set_ydata(Y_list[count])
	graph_plot[count].set_xdata(V_list[count])
	plt.draw          # redraw the plot
	graph_plot1[count].set_ydata(Y1_list[count])
	graph_plot1[count].set_xdata(V1_list[count])
	plt.draw          # redraw the plot
	graph_plot2[count].set_ydata(Y2_list[count])
	graph_plot2[count].set_xdata(V2_list[count])
	plt.draw          # redraw the plot
	graph_plot3[count].set_ydata(Y3_list[count])
	graph_plot3[count].set_xdata(V3_list[count])
	graph_plot4[count].set_ydata(Cox_val_list[count])
	graph_plot4[count].set_xdata(Cox_list[count])
	plt.draw          # redraw the plot




#sliders Update functions of Tox
def val_update_tox(val):
    global tox,NA,Phi_m,count,Qox,Vcb
	
    if count!=0:

	#initial list declaration
	r=[]
	Y_list[count]=[]
	V_list[count]=[]
	Y1_list[count]=[]
	V1_list[count]=[]
	Y2_list[count]=[]
	V2_list[count]=[]
	Y3_list[count]=[]
	V3_list[count]=[]
	Cox_list[count]=[]
	Cox_val_list[count]=[]

	tox=(slider2.val)*10**(-9)
	Po=(Ni**2)/ND	
	No=ND
	Shi_F=Phi_t*log((ND)/(Ni)) 	
	n=-(2*Shi_F+Phi_t*6+ Vcb)	
	Cox=Eox/tox	
	Vfb=+Phi_m-Ea-Eg+Shi_F-Qox/Cox	
	gm=(sqrt(2*q*Es*ND))/(Cox)
		
	# drange funct for creating steps in for loop
	for i in drange(-2.75,Vfb-0.01,0.05):
		r.append(i)
	
   	for Vgb in r:
		f=-(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= max(f,n)		#initial value of NewtonRaphson
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po,Vcb) 
		Qc = (charge_funct(NA,Phi_t,Es,q,val,Shi_F,ND,Po,No,Vcb))
		dq_dVgb=deriv_funct(val,Qc,NA,Phi_t,Es,q,Shi_F,Vgb,Vfb,ND,Cox,No,Po,Vcb)		
		V_list[count].append(Vgb)
		Y_list[count].append(abs(val))

		V1_list[count].append(val)
		Y1_list[count].append(abs(Qc)*1000)

		V2_list[count].append(Vgb)
		Y2_list[count].append(abs(Qc)*1000)

		V3_list[count].append(Vgb)
		Y3_list[count].append(dq_dVgb*100)
		
		Cox_list[count].append(Vgb)
		Cox_val_list[count].append(Cox*100)


	#redrawing the graphs for different parameter value
	graph_plot[count].set_ydata(Y_list[count])
	graph_plot[count].set_xdata(V_list[count])
	plt.draw          # redraw the plot
	graph_plot1[count].set_ydata(Y1_list[count])
	graph_plot1[count].set_xdata(V1_list[count])
	plt.draw          # redraw the plot
	graph_plot2[count].set_ydata(Y2_list[count])
	graph_plot2[count].set_xdata(V2_list[count])
	plt.draw          # redraw the plot
	graph_plot3[count].set_ydata(Y3_list[count])
	graph_plot3[count].set_xdata(V3_list[count])
	graph_plot4[count].set_ydata(Cox_val_list[count])
	graph_plot4[count].set_xdata(Cox_list[count])
	plt.draw          # redraw the plot



#sliders Update functions of NA
def val_update_ND(val):
    global tox,NA,Phi_m,count,Qox,Vcb

    if count!=0:
	#initial list declaration
	Y_list[count]=[]
	V_list[count]=[]
	Y1_list[count]=[]
	V1_list[count]=[]
	Y2_list[count]=[]
	V2_list[count]=[]
	Y3_list[count]=[]
	V3_list[count]=[]
	Cox_list[count]=[]
	Cox_val_list[count]=[]

	r=[]
	ND=(slider3.val)*10**23
	Po=(Ni**2)/ND	
	No=ND
	Shi_F=Phi_t*log((ND)/(Ni)) 	
	n=-(2*Shi_F+Phi_t*6+ Vcb)	
	Cox=Eox/tox	
	Vfb=+Phi_m-Ea-Eg+Shi_F-Qox/Cox	
	gm=(sqrt(2*q*Es*ND))/(Cox)
	
	# drange funct for creating steps in for loop
	for i in drange(-2.75,Vfb-0.01,0.05):
		r.append(i)
	
	for Vgb in r:
		f=-(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= max(f,n)		#initial value of NewtonRaphson
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po,Vcb) 
		Qc = (charge_funct(NA,Phi_t,Es,q,val,Shi_F,ND,Po,No,Vcb))
		dq_dVgb=deriv_funct(val,Qc,NA,Phi_t,Es,q,Shi_F,Vgb,Vfb,ND,Cox,No,Po,Vcb) 
		V_list[count].append(Vgb)
		Y_list[count].append(abs(val))

		V1_list[count].append(val)
		Y1_list[count].append(abs(Qc)*1000)

		V2_list[count].append(Vgb)
		Y2_list[count].append(abs(Qc)*1000)

		V3_list[count].append(Vgb)
		Y3_list[count].append(dq_dVgb*100)

		Cox_list[count].append(Vgb)
		Cox_val_list[count].append(Cox*100)

	#redrawing the graphs for different parameter value
	graph_plot[count].set_ydata(Y_list[count])
	graph_plot[count].set_xdata(V_list[count])
	plt.draw          # redraw the plot
	graph_plot1[count].set_ydata(Y1_list[count])
	graph_plot1[count].set_xdata(V1_list[count])
	plt.draw          # redraw the plot
	graph_plot2[count].set_ydata(Y2_list[count])
	graph_plot2[count].set_xdata(V2_list[count])
	plt.draw          # redraw the plot
	graph_plot3[count].set_ydata(Y3_list[count])
	graph_plot3[count].set_xdata(V3_list[count])
	graph_plot4[count].set_ydata(Cox_val_list[count])
	graph_plot4[count].set_xdata(Cox_list[count])
	plt.draw          # redraw the plot


#sliders Update functions of Phi_m
def val_update_Phi(val):
    global tox,NA,Phi_m,count,Qox,Vcb

    if count!=0:

	#initial list declaration
	Y_list[count]=[]
	V_list[count]=[]
	Y1_list[count]=[]
	V1_list[count]=[]
	Y2_list[count]=[]
	V2_list[count]=[]
	Y3_list[count]=[]
	V3_list[count]=[]
	Cox_list[count]=[]
	Cox_val_list[count]=[]

	r=[]
	Phi_m=slider4.val
	Po=(Ni**2)/ND	
	No=ND
	Shi_F=Phi_t*log((ND)/(Ni)) 	
	n=-(2*Shi_F+Phi_t*6+ Vcb)	
	Cox=Eox/tox	
	Vfb=+Phi_m-Ea-Eg+Shi_F-Qox/Cox	
	gm=(sqrt(2*q*Es*ND))/(Cox)
	
	# drange funct for creating steps in for loop
	for i in drange(-2.75,Vfb-0.01,0.05):
		r.append(i)
	
	for Vgb in r:
		f=-(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= max(f,n)		#initial value of NewtonRaphson
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po,Vcb) 
		Qc = (charge_funct(NA,Phi_t,Es,q,val,Shi_F,ND,Po,No,Vcb)) 
		dq_dVgb=deriv_funct(val,Qc,NA,Phi_t,Es,q,Shi_F,Vgb,Vfb,ND,Cox,No,Po,Vcb)
		V_list[count].append(Vgb)
		Y_list[count].append(abs(val))

		V1_list[count].append(val)
		Y1_list[count].append(abs(Qc)*1000)

		V2_list[count].append(Vgb)
		Y2_list[count].append(abs(Qc)*1000)

		V3_list[count].append(Vgb)
		Y3_list[count].append(dq_dVgb*100)

		Cox_list[count].append(Vgb)
		Cox_val_list[count].append(Cox*100)

	#redrawing the graphs for different parameter value
	graph_plot[count].set_ydata(Y_list[count])
	graph_plot[count].set_xdata(V_list[count])
	plt.draw          # redraw the plot
	graph_plot1[count].set_ydata(Y1_list[count])
	graph_plot1[count].set_xdata(V1_list[count])
	plt.draw          # redraw the plot
	graph_plot2[count].set_ydata(Y2_list[count])
	graph_plot2[count].set_xdata(V2_list[count])
	plt.draw          # redraw the plot
	graph_plot3[count].set_ydata(Y3_list[count])
	graph_plot3[count].set_xdata(V3_list[count])
	graph_plot4[count].set_ydata(Cox_val_list[count])
	graph_plot4[count].set_xdata(Cox_list[count])
	plt.draw          # redraw the plot



#sliders Update functions of Qox
def val_update_Qox(val):
    global tox,NA,Phi_m,count,Qox,Vcb

    if count!=0:

	#initial list declaration
	Y_list[count]=[]
	V_list[count]=[]
	Y1_list[count]=[]
	V1_list[count]=[]
	Y2_list[count]=[]
	V2_list[count]=[]
	Y3_list[count]=[]
	V3_list[count]=[]
	Cox_list[count]=[]
	Cox_val_list[count]=[]

	r=[]
	Qox=(slider5.val)*10**(-6)
	Po=(Ni**2)/ND	
	No=ND
	Shi_F=Phi_t*log((ND)/(Ni)) 	
	n=-(2*Shi_F+Phi_t*6+ Vcb)	
	Cox=Eox/tox	
	Vfb=+Phi_m-Ea-Eg+Shi_F-Qox/Cox	
	gm=(sqrt(2*q*Es*ND))/(Cox)
	
	# drange funct for creating steps in for loop
	for i in drange(-2.75,Vfb-0.01,0.05):
		r.append(i)
	
	for Vgb in r:
		f=-(-gm/2 + sqrt((gm)**2)/4 + Vgb - Vfb )**2  	
		x0= max(f,n)				#initial value of NewtonRaphson
		val=newtonRaphson(Vgb,x0,Vfb,NA,ND,Phi_t,q,Es,Cox,No,Po,Vcb) 
		Qc = (charge_funct(NA,Phi_t,Es,q,val,Shi_F,ND,Po,No,Vcb)) 
		dq_dVgb=deriv_funct(val,Qc,NA,Phi_t,Es,q,Shi_F,Vgb,Vfb,ND,Cox,No,Po,Vcb)
		V_list[count].append(Vgb)
		Y_list[count].append(abs(val))

		V1_list[count].append(val)
		Y1_list[count].append(abs(Qc)*1000)

		V2_list[count].append(Vgb)
		Y2_list[count].append(abs(Qc)*1000)

		V3_list[count].append(Vgb)
		Y3_list[count].append(dq_dVgb*100)

		Cox_list[count].append(Vgb)
		Cox_val_list[count].append(Cox*100)

	#redrawing the graphs for different parameter value
	graph_plot[count].set_ydata(Y_list[count])
	graph_plot[count].set_xdata(V_list[count])
	plt.draw          # redraw the plot
	graph_plot1[count].set_ydata(Y1_list[count])
	graph_plot1[count].set_xdata(V1_list[count])
	plt.draw          # redraw the plot
	graph_plot2[count].set_ydata(Y2_list[count])
	graph_plot2[count].set_xdata(V2_list[count])
	plt.draw          # redraw the plot
	graph_plot3[count].set_ydata(Y3_list[count])
	graph_plot3[count].set_xdata(V3_list[count])
	graph_plot4[count].set_ydata(Cox_val_list[count])
	graph_plot4[count].set_xdata(Cox_list[count])
	plt.draw          # redraw the plot


#button_declaration
axButton = plt.axes([0.83,0.10, 0.06, 0.06])		#xloc,yloc,width,heights
btn = Button(axButton, ' ADD ')
	

#button on click callback function
btn.on_clicked(setValue)



#Sliders declaration
axSlider1= plt.axes([0.1,0.21,0.55,0.02])		#xloc,yloc,width,height
slider1 = Slider(axSlider1,'Vcb', valmin=0.01, valmax=1.5,valinit=Vcb,valfmt='Vcb is '+'-'+'%1.2f'+'in V',color="blue")


axSlider2= plt.axes([0.1,0.17,0.55,0.02])		#xloc,yloc,width,height
slider2 = Slider(ax=axSlider2,label='Tox',valmin=1,valmax=8,valinit=tox*10**(9),valfmt='tox is '+'%1.2f'+ ' in nm',color="green")


axSlider3= plt.axes([0.1,0.13,0.55,0.02])		#xloc,yloc,width,height
slider3 = Slider(axSlider3,'ND', valmin=1, valmax=20,valinit=ND/(10**23),valfmt='ND is '+'%1.2f'+ ' in 10**23 m^-3')


axSlider4= plt.axes([0.1,0.09,0.55,0.02])		#xloc,yloc,width,height
slider4 = Slider(axSlider4,r'$\phi_m$', valmin=3.5, valmax=4.5,valinit=Phi_m,valfmt= r'$\phi_m$ is '+'%1.2f',color="red")


axSlider5= plt.axes([0.1,0.04,0.55,0.02])		#xloc,yloc,width,height
slider5 = Slider(axSlider5,'Qox', valmin=0.01, valmax=100,valinit=Qox*10**6,valfmt='Qox is '+'%1.2f'+'*10^(-6)',color="yellow")


#sliders on change function call
slider1.on_changed(val_update_Vcb)
slider2.on_changed(val_update_tox)
slider3.on_changed(val_update_ND)
slider4.on_changed(val_update_Phi)
slider5.on_changed(val_update_Qox)

plt.show()


print("Thank you for using the tool \n")

