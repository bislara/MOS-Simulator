# importing modules to main_code
from math import *
from sympy import *
import matplotlib.pyplot as plt
from MOS_4_functions.pMOS_funct_Vgs import *  # importing the custom functions
from matplotlib.widgets import Slider, Button, TextBox  	# import the Slider widget
import numpy as np
import csv

global Phi_m, tox, NA, ND, r, count, Qox, Qc, csv_count

print("Welcome !!!")


# constants initialize
q = 1.6*10**(-19)
Eo = 8.854*10**(-12)
ks = 11.7  # ks for Si
kox = 3.9  # kox for SiO2
Ni = 1.15*10**16  # intrinsic concentration in per m^3
Phi_t = 0.0259  # Thermal Voltage Phi_t=k*t/q2
tox = 2*10**(-9)
ND = 5*10**23
Eg = 0.56  # Eg=EG/2= 1.12/2
NA = 0
Qox = 10**(-5)
Phi_m = 4.1
Vgb = 1
Ea = 4.05  # electron affinity of Silicon
count = 0
mu = 400*10**(-4)
w = 10*10**(-6)
l = 10*10**(-6)
Vds = 1
Vsb = 0


# for more number of graphs and to distinguish between them
colour_count = 0
colours = {1: 'b', 2: 'g', 3: 'r', 4: 'c', 5: 'm', 6: 'y', 7: 'k'}
csv_count = 0

# variable declaration
r = []
Y_list = {}
V_list = {}
csv_list = {}

Y_list[count] = []
V_list[count] = []

graph_plot = {}
graph_plot[count] = []

Es = ks*Eo
Eox = kox*Eo

# plotting_graph

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.35, right=0.75)


plt.title('Id Vs Vgs graph for pMOS with Vsb=0')
plt.ylim(0, 3)
plt.xlim(-3.15, 0)
plt.minorticks_on()
plt.tick_params(direction="in")


graph_plot[count] = plt.plot(V_list[count], Y_list[count], color='r', label="")


plt.xlabel('Vgs (V)')
plt.ylabel('Id (mA)')

# plt.legend()


# button function for adding plots
def setValue(val):
    global count, colour_count, colours, Qox, Vds, w, l, mu
    count = count+1

    # initial list declaration
    Y_list[count] = []
    V_list[count] = []
    graph_plot[count] = []

    # initial calculations
    r = []
    Po = (Ni**2)/ND
    No = ND
    Shi_F = Phi_t*log((ND)/(Ni))
    x0 = 2*Shi_F+Phi_t*6  # 6*Phi_t for uniform substrates

    Cox = Eox/tox
    Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
    gm = (sqrt(2*q*Es*ND))/Cox

    # Vcb range
    for i in drange(-3, -0.1, 0.05):
        r.append(i)

    for Vgs in r:
        Id = calculate_Id(w, l, mu, Vgs, Vfb, Vds, Cox, gm,
                          Phi_t, Shi_F, x0, Po, No, NA, ND)
        V_list[count].append(Vgs)
        Y_list[count].append(Id)

    colour_count = colour_count+1

    # redrawing the graphs for different parameter value
    plt.axes()
    plt.title('Id Vs Vgs graph for pMOS with Vsb=0')
    plt.ylim(0, 2.5)
    plt.xlim(-3, 0)
    plt.minorticks_on()
    plt.tick_params(direction="in")

    plt.xlabel('Vgs value (V)')
    plt.ylabel('Id value (mA)')

    graph_plot[count], = plt.plot(
        V_list[count], Y_list[count], color=colours[colour_count], label="Graph: "+str(count))

    plt.legend()


def val_update_Vds(val):
    global tox, ND, Phi_m, count, Qox, Vds, w, l, mu

    if count != 0:
        # initial list declaration
        r = []
        Y_list[count] = []
        V_list[count] = []

        Vds = (slider1.val)
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))
        x0 = 2*Shi_F+Phi_t*6  # 6*Phi_t for uniform substrates

        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/Cox

        # Vcb range
        for i in drange(-3, -0.1, 0.05):
            r.append(i)

        for Vgs in r:
            Id = calculate_Id(w, l, mu, Vgs, Vfb, Vds, Cox,
                              gm, Phi_t, Shi_F, x0, Po, No, NA, ND)
            V_list[count].append(Vgs)
            Y_list[count].append(Id)

        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot


# sliders Update functions of Tox
def val_update_tox(val):
    global tox, ND, Phi_m, count, Qox, Vds, w, l, mu

    if count != 0:
        # initial list declaration
        r = []
        Y_list[count] = []
        V_list[count] = []

        tox = (slider2.val)*10**(-9)
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))
        x0 = 2*Shi_F+Phi_t*6  # 6*Phi_t for uniform substrates

        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/Cox

        # Vcb range
        for i in drange(-3, -0.1, 0.05):
            r.append(i)

        for Vgs in r:
            Id = calculate_Id(w, l, mu, Vgs, Vfb, Vds, Cox,
                              gm, Phi_t, Shi_F, x0, Po, No, NA, ND)
            V_list[count].append(Vgs)
            Y_list[count].append(Id)

        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot


# sliders Update functions of NA
def val_update_ND(val):
    global tox, ND, Phi_m, count, Qox, Vds, mu, w, l

    if count != 0:
        # initial list declaration
        r = []
        Y_list[count] = []
        V_list[count] = []

        ND = (slider3.val)*10**22
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))
        x0 = 2*Shi_F+Phi_t*6  # 6*Phi_t for uniform substrates

        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/Cox

        # Vcb range
        for i in drange(-3, -0.1, 0.05):
            r.append(i)

        for Vgs in r:
            Id = calculate_Id(w, l, mu, Vgs, Vfb, Vds, Cox,
                              gm, Phi_t, Shi_F, x0, Po, No, NA, ND)
            V_list[count].append(Vgs)
            Y_list[count].append(Id)

        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot


# sliders Update functions of Phi_m
def val_update_Phi(val):
    global tox, ND, Phi_m, count, Qox, Vds, mu, w, l

    if count != 0:
        # initial list declaration
        r = []
        Y_list[count] = []
        V_list[count] = []

        Phi_m = (slider4.val)
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))
        x0 = 2*Shi_F+Phi_t*6  # 6*Phi_t for uniform substrates

        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/Cox

        # Vcb range
        for i in drange(-3, -0.1, 0.05):
            r.append(i)

        for Vgs in r:
            Id = calculate_Id(w, l, mu, Vgs, Vfb, Vds, Cox,
                              gm, Phi_t, Shi_F, x0, Po, No, NA, ND)
            V_list[count].append(Vgs)
            Y_list[count].append(Id)

        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot


# sliders Update functions of Qox
def val_update_Qox(val):
    global tox, ND, Phi_m, count, Qox, Vds, mu, w, l

    if count != 0:
        # initial list declaration
        r = []
        Y_list[count] = []
        V_list[count] = []

        Qox = (slider5.val)*10**(-6)
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))
        x0 = 2*Shi_F+Phi_t*6  # 6*Phi_t for uniform substrates

        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/Cox

        # Vcb range
        for i in drange(-3, -0.1, 0.05):
            r.append(i)

        for Vgs in r:
            Id = calculate_Id(w, l, mu, Vgs, Vfb, Vds, Cox,
                              gm, Phi_t, Shi_F, x0, Po, No, NA, ND)
            V_list[count].append(Vgs)
            Y_list[count].append(Id)

        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot


def submit_mu(text):
    global tox, ND, Phi_m, count, Qox, Vds, mu, w, l

    if count != 0:
        # initial list declaration
        r = []
        Y_list[count] = []
        V_list[count] = []

        mu = float(text)*10**(-4)
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))
        x0 = 2*Shi_F+Phi_t*6  # 6*Phi_t for uniform substrates

        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/Cox

        # Vcb range
        for i in drange(-3, -0.1, 0.05):
            r.append(i)

        for Vgs in r:
            Id = calculate_Id(w, l, mu, Vgs, Vfb, Vds, Cox,
                              gm, Phi_t, Shi_F, x0, Po, No, NA, ND)
            V_list[count].append(Vgs)
            Y_list[count].append(Id)

        print("mu is ", mu)
        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot


def submit_w(text):
    global tox, ND, Phi_m, count, Qox, Vds, mu, w, l

    if count != 0:
        # initial list declaration
        r = []
        Y_list[count] = []
        V_list[count] = []

        w = float(text)*10**(-6)
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))
        x0 = 2*Shi_F+Phi_t*6  # 6*Phi_t for uniform substrates

        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/Cox

        # Vcb range
        for i in drange(-3, -0.1, 0.05):
            r.append(i)

        for Vgs in r:
            Id = calculate_Id(w, l, mu, Vgs, Vfb, Vds, Cox,
                              gm, Phi_t, Shi_F, x0, Po, No, NA, ND)
            V_list[count].append(Vgs)
            Y_list[count].append(Id)

        print("mu is ", mu)
        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot


def submit_l(text):
    global tox, ND, Phi_m, count, Qox, Vds, mu, w, l

    if count != 0:
        # initial list declaration
        r = []
        Y_list[count] = []
        V_list[count] = []

        l = float(text)*10**(-6)
        Po = (Ni**2)/ND
        No = ND
        Shi_F = Phi_t*log((ND)/(Ni))
        x0 = 2*Shi_F+Phi_t*6  # 6*Phi_t for uniform substrates

        Cox = Eox/tox
        Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
        gm = (sqrt(2*q*Es*ND))/Cox

        # Vcb range
        for i in drange(-3, -0.1, 0.05):
            r.append(i)

        for Vgs in r:
            Id = calculate_Id(w, l, mu, Vgs, Vfb, Vds, Cox,
                              gm, Phi_t, Shi_F, x0, Po, No, NA, ND)
            V_list[count].append(Vgs)
            Y_list[count].append(Id)

        print("mu is ", mu)
        graph_plot[count].set_ydata(Y_list[count])
        graph_plot[count].set_xdata(V_list[count])
        plt.draw          # redraw the plot


def setData(val):
    global tox, NA, Phi_m, Qox, csv_count, count, Vds, mu, w, l
    # initial calculations
    r = []
    csv_list[csv_count] = []
    Po = (Ni**2)/ND
    No = ND
    Shi_F = Phi_t*log((ND)/(Ni))
    x0 = 2*Shi_F+Phi_t*6  # 6*Phi_t for uniform substrates

    Cox = Eox/tox
    Vfb = +Phi_m-Ea-Eg+Shi_F-Qox/Cox
    gm = (sqrt(2*q*Es*ND))/Cox

    # Vcb range
    for i in drange(-3, -0.1, 0.05):
        r.append(i)

    list_no = 0
    if csv_count == 0:
        csv_list[csv_count].append([])
        csv_list[csv_count][list_no] = [
            'Vds ='+str(Vds), 'Tox ='+str(tox), 'ND ='+str(ND), 'Phi_m ='+str(Phi_m), 'Qox ='+str(Qox), 'mu ='+str(mu), 'l ='+str(l), 'w ='+str(w)]
        list_no += 1
        csv_list[csv_count].append([])
        csv_list[csv_count][list_no] = ['Vgs ('+str(csv_count)+')', 'Shi_s ('+str(
            csv_count)+')']
        list_no += 1
        for Vgs in r:
            csv_list[csv_count].append([])
            Id = calculate_Id(w, l, mu, Vgs, Vfb, Vds, Cox,
                              gm, Phi_t, Shi_F, x0, Po, No, NA, ND)
            csv_list[csv_count][list_no].append(Vgs)
            csv_list[csv_count][list_no].append(Id)
            list_no += 1

        with open('./Dataset/4terminal/pMOS_Id_Vs_Vgs.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([])
            writer.writerows(csv_list[csv_count])
        print("Written 1st time")
        csv_count += 1

    elif csv_count != 0:
        list_no = 0
        csv_list[csv_count].append([])
        csv_list[csv_count][list_no] = [
            'Vds ='+str(Vds), 'Tox ='+str(tox), 'ND ='+str(ND), 'Phi_m ='+str(Phi_m), 'Qox ='+str(Qox), 'mu ='+str(mu), 'l ='+str(l), 'w ='+str(w)]
        list_no += 1
        csv_list[csv_count].append([])
        csv_list[csv_count][list_no] = ['Vgs ('+str(csv_count)+')', 'Shi_s ('+str(
            csv_count)+')']
        list_no += 1
        for Vgs in r:
            csv_list[csv_count].append([])
            Id = calculate_Id(w, l, mu, Vgs, Vfb, Vds, Cox,
                              gm, Phi_t, Shi_F, x0, Po, No, NA, ND)
            csv_list[csv_count][list_no].append(Vgs)
            csv_list[csv_count][list_no].append(Id)
            list_no += 1

        with open('./Dataset/4terminal/pMOS_Id_Vs_Vgs.csv', 'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([])
            writer.writerows(csv_list[csv_count])
        print("saved data for "+str(csv_count)+" times")
        csv_count += 1

    else:
        print("Sorry couldn't save the data")


# button_declaration
axButton = plt.axes([0.83, 0.15, 0.06, 0.06])  # xloc,yloc,width,heights
btn = Button(axButton, ' ADD ')

axButton1 = plt.axes([0.83, 0.05, 0.08, 0.06])  # xloc,yloc,width,heights
btn1 = Button(axButton1, ' Save Data ')

# button on click callback function
btn.on_clicked(setValue)
btn1.on_clicked(setData)


# Sliders declaration
axSlider1 = plt.axes([0.1, 0.21, 0.55, 0.02])  # xloc,yloc,width,height
slider1 = Slider(axSlider1, 'Vds', valmin=-0.01, valmax=4,
                 valinit=Vds, valfmt='Vds is '+'%1.2f'+' V', color="blue")


axSlider2 = plt.axes([0.1, 0.17, 0.55, 0.02])  # xloc,yloc,width,height
slider2 = Slider(ax=axSlider2, label='Tox', valmin=1, valmax=8,
                 valinit=tox*10**(9), valfmt='tox is '+'%1.2f' + ' nm', color="green")


axSlider3 = plt.axes([0.1, 0.13, 0.55, 0.02])  # xloc,yloc,width,height
slider3 = Slider(axSlider3, 'ND', valmin=1, valmax=100, valinit=ND /
                 (10**22), valfmt='ND is '+'%1.2f' + ' *10**22 m^-3')


axSlider4 = plt.axes([0.1, 0.09, 0.55, 0.02])  # xloc,yloc,width,height
slider4 = Slider(axSlider4, r'$\phi_m$', valmin=3.5, valmax=4.5,
                 valinit=Phi_m, valfmt=r'$\phi_m$ is '+'%1.2f' + ' eV', color="red")


axSlider5 = plt.axes([0.1, 0.04, 0.55, 0.02])  # xloc,yloc,width,height
slider5 = Slider(axSlider5, 'Qox', valmin=1, valmax=1000, valinit=Qox *
                 10**6, valfmt='Qox is '+'%1.2f'+'*10^(-6)' + ' C/m^2', color="yellow")


# sliders on change function call
slider1.on_changed(val_update_Vds)
slider2.on_changed(val_update_tox)
slider3.on_changed(val_update_ND)
slider4.on_changed(val_update_Phi)
slider5.on_changed(val_update_Qox)


# Text Box declaration and on_submit function call

Lbox = plt.axes([0.8, 0.45, 0.17, 0.04])
plt.text(0.25, 0.5, 'L in um\n')
l_box = TextBox(Lbox, '', initial=str(l*10**6))
l_box.on_submit(submit_l)

Wbox = plt.axes([0.8, 0.6, 0.17, 0.04])
plt.text(0.25, 0.5, 'W in um\n')
w_box = TextBox(Wbox, '', initial=str(w*10**6))
w_box.on_submit(submit_w)

MUbox = plt.axes([0.8, 0.75, 0.17, 0.04])
plt.text(0.05, 0.5, r'$\mu $ in cm^2/(V.s)'+'\n')
mu_box = TextBox(MUbox, '', initial=str(mu*10**4))
mu_box.on_submit(submit_mu)


plt.show()


print("Thank you for using the tool \n")
