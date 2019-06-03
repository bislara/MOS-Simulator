import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('Dataset.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[1])

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(0.7,1.1) 
plt.xlim(0,1.5) 
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
