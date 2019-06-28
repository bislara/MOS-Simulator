#If you are using virtualenv, it is fine to install tkinter using sudo apt-get install python-tk(python2), sudo apt-get install python3-tk(python3), and and it will work fine in the virtual environment

from math import *
from sympy import *

from subprocess import call
from matplotlib.widgets import Slider, Button, TextBox  	# import the Slider widget
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

print("This is an interactive tool for the simulation of MOS")

def setValue(val):
    #call(['python', 'terminal_MOS3/nMOS.py'])
    call([r"terminal_MOS3/nMOS"])

def setValue2(val):
#    call(['python', 'terminal_MOS3/pMOS.py'])
    call([r"terminal_MOS3/pMOS"])


def setValue3(val):
#    call(['python', 'terminal_MOS3/SHi_s_Vs_Vcb.py'])
    call([r"terminal_MOS3/SHi_s_Vs_Vcb"])


def setValue4(val):
#    call(['python', 'terminal_MOS3/Shi_s_Vs_Vcb.py'])
    call([r"terminal_MOS3/pMOS_SHIs"])


def setValue5(val):
    #call(['python', 'moscap/nMOS.py'])
    call([r"moscap/nMOS"])

def setValue6(val):
    #call(['python', 'moscap/pMOS.py'])
    call([r"moscap/pMOS"])

def setValue7(val):
    #call(['python', 'moscap/poison_sol.py'])
    call([r"moscap/poison_sol"])


def setValue8(val):
#    call(['python', 'terminal4/nMOS_Vgs.py'])
    call([r"terminal4/nMOS_Vgs"])


def setValue9(val):
#    call(['python', 'terminal4/nMOS_Vds.py'])
    call([r"terminal4/nMOS_Vds"])


def setValue10(val):
#    call(['python', 'terminal4/pMOS_Vgs.py'])
    call([r"terminal4/pMOS_Vgs"])


def setValue11(val):
#    call(['python', 'terminal4/pMOS_Vds.py'])
    call([r"terminal4/pMOS_Vds"])


# buttons_declaration

title2 = plt.axes([0.3, 0.5, 0.4, 0.1])
title_btn = Button(title2, ' 3 Terminal MOSFET\n Choose one of these ',
                   color='#afeeee', hovercolor='#afeeee')


axButton = plt.axes([0.05, 0.35, 0.1, 0.06])  # xloc,yloc,width,heights
btn = Button(axButton, ' nMOS ', hovercolor='y')

axButton2 = plt.axes([0.22, 0.35, 0.1, 0.06])  # xloc,yloc,width,heights
btn2 = Button(axButton2, ' pMOS ', hovercolor='y')

axButton3 = plt.axes([0.4, 0.35, 0.25, 0.06])  # xloc,yloc,width,heights
btn3 = Button(axButton3, r'$\psi_s$ Vs Vcb of nMOS', hovercolor='y')

axButton4 = plt.axes([0.7, 0.35, 0.25, 0.06])  # xloc,yloc,width,heights
btn4 = Button(axButton4, r'$\psi_s$ Vs Vcb of pMOS', hovercolor='y')


title1 = plt.axes([0.3, 0.85, 0.4, 0.1])
title_btn1 = Button(title1, ' MOSCAP\n Choose one of these ',
                    color='#afeeee', hovercolor='#afeeee')


axButton5 = plt.axes([0.15, 0.7, 0.1, 0.06])  # xloc,yloc,width,heights
btn5 = Button(axButton5, ' nMOS ', hovercolor='y')

axButton6 = plt.axes([0.35, 0.7, 0.1, 0.06])  # xloc,yloc,width,heights
btn6 = Button(axButton6, ' pMOS ', hovercolor='y')

axButton7 = plt.axes([0.55, 0.7, 0.25, 0.06])  # xloc,yloc,width,heights
btn7 = Button(axButton7, r'$\psi_s$ Vs y ', hovercolor='y')


title3 = plt.axes([0.3, 0.15, 0.4, 0.1])
title_btn3 = Button(title3, ' 4 Terminal MOSFET\n Choose one of these ',
                    color='#afeeee', hovercolor='#afeeee')

axButton8 = plt.axes([0.02, 0.03, 0.2, 0.06])  # xloc,yloc,width,heights
btn8 = Button(axButton8, ' nMOS Id Vs Vgs ', hovercolor='y')

axButton9 = plt.axes([0.26, 0.03, 0.2, 0.06])  # xloc,yloc,width,heights
btn9 = Button(axButton9, ' nMOS Id Vs Vds ', hovercolor='y')

axButton10 = plt.axes([0.5, 0.03, 0.2, 0.06])  # xloc,yloc,width,heights
btn10 = Button(axButton10, ' pMOS Id Vs Vgs ', hovercolor='y')

axButton11 = plt.axes([0.74, 0.03, 0.2, 0.06])  # xloc,yloc,width,heights
btn11 = Button(axButton11, ' pMOS Id Vs Vds ', hovercolor='y')


# button on click callback function
btn.on_clicked(setValue)
btn2.on_clicked(setValue2)
btn3.on_clicked(setValue3)
btn4.on_clicked(setValue4)
btn5.on_clicked(setValue5)
btn6.on_clicked(setValue6)
btn7.on_clicked(setValue7)
btn8.on_clicked(setValue8)
btn9.on_clicked(setValue9)
btn10.on_clicked(setValue10)
btn11.on_clicked(setValue11)


plt.show()

