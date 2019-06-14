from subprocess import call
from matplotlib.widgets import Slider,Button,TextBox  	# import the Slider widget
import numpy as np
import matplotlib.pyplot as plt

print("This is an interactive tool for the simulation of MOS")
#plt.title("Choose which one to plot")

#plt.text(0.5, 0.1, 'Choose which one to plot')


def setValue(val):
	call(['python','3_terminal_MOS/nMOS.py'])

def setValue2(val):
	call(['python','3_terminal_MOS/pMOS.py'])

def setValue3(val):
	call(['python','3_terminal_MOS/SHi_s-Vs-Vcb.py'])

def setValue4(val):
	call(['python','3_terminal_MOS/Shi_s-Vs-Vcb(2).py'])


def setValue5(val):
	call(['python','moscap/nMOS.py'])

def setValue6(val):
	call(['python','moscap/pMOS.py'])

def setValue7(val):
	call(['python','moscap/poison_sol.py'])


#buttons_declaration

title2=plt.axes([0.3,0.5, 0.4, 0.1])
title_btn = Button(title2, ' 3 Terminal MOSFET\n Choose one of these ',color='#afeeee',hovercolor = '#afeeee')


axButton = plt.axes([0.05,0.35, 0.1, 0.06])		#xloc,yloc,width,heights
btn = Button(axButton, ' nMOS ',hovercolor = 'y')
	
axButton2 = plt.axes([0.22,0.35, 0.1, 0.06])		#xloc,yloc,width,heights
btn2 = Button(axButton2, ' pMOS ',hovercolor = 'y')

axButton3 = plt.axes([0.4,0.35, 0.25, 0.06])		#xloc,yloc,width,heights
btn3 = Button(axButton3, r'$\psi_s$ Vs Vcb of nMOS',hovercolor = 'y')

axButton4 = plt.axes([0.7,0.35, 0.25, 0.06])		#xloc,yloc,width,heights
btn4 = Button(axButton4,r'$\psi_s$ Vs Vcb of pMOS',hovercolor = 'y')




title1=plt.axes([0.3,0.85, 0.4, 0.1])
title_btn1 = Button(title1, ' MOSCAP\n Choose one of these ',color='#afeeee',hovercolor = '#afeeee')


axButton5 = plt.axes([0.15,0.7, 0.1, 0.06])		#xloc,yloc,width,heights
btn5 = Button(axButton5, ' nMOS ',hovercolor = 'y')
	
axButton6 = plt.axes([0.35,0.7, 0.1, 0.06])		#xloc,yloc,width,heights
btn6 = Button(axButton6, ' pMOS ',hovercolor = 'y')

axButton7 = plt.axes([0.55,0.7, 0.25, 0.06])		#xloc,yloc,width,heights
btn7 = Button(axButton7, r'$\psi_s$ Vs y ',hovercolor = 'y')



title3=plt.axes([0.3,0.15, 0.4, 0.1])
title_btn3 = Button(title3, ' 4 Terminal MOSFET\n Choose one of these ',color='#afeeee',hovercolor = '#afeeee')

axButton5 = plt.axes([0.15,0.03, 0.1, 0.06])		#xloc,yloc,width,heights
btn5 = Button(axButton5, ' nMOS ',hovercolor = 'y')
	
axButton6 = plt.axes([0.35,0.03, 0.1, 0.06])		#xloc,yloc,width,heights
btn6 = Button(axButton6, ' pMOS ',hovercolor = 'y')

axButton7 = plt.axes([0.55,0.03, 0.25, 0.06])		#xloc,yloc,width,heights
btn7 = Button(axButton7, r'$\psi_s$ Vs y ',hovercolor = 'y')



#button on click callback function
btn.on_clicked(setValue)
btn2.on_clicked(setValue2)
btn3.on_clicked(setValue3)
btn4.on_clicked(setValue4)
btn5.on_clicked(setValue5)
btn6.on_clicked(setValue6)
btn7.on_clicked(setValue7)


plt.show()


