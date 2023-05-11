import numpy as np
import matplotlib.pyplot as plt



volt = []
time = []
volt_dot = []
time_dot = []

time_charge =  0
time_uncharge = 0

file = open("work6/settings.txt")
settings = file.read()
print(settings)
file.close()

settings = [float(x) for x in settings.split()]

counter = 0
with open("work6/data.txt", 'r') as data:
    for line in data:
        splitted = line.split()
        if splitted[0].isalpha():
            continue
        splitted = [float(x)  for x in splitted]
        if len(splitted) < 2:
            break

        volt.append(splitted[0]/256)
        time.append(splitted[1])

        counter += 1

time_charge = time[volt.index(max(volt))]
time_uncharge = time[-1] - time_charge

plt.rcParams['figure.figsize'] = [15, 15]

fig1, v_t = plt.subplots()

v_t.set_xlabel("Время, с")
v_t.set_ylabel("Напряжение, В")
v_t.set_title("Зависимость напряжения от времени")
v_t.text(x = 65, y = 0.6, s = "Время зарядки %g" % time_charge, fontsize = 14)
v_t.text(x = 65, y = 0.5, s = "Время разрядки %g" % time_uncharge, fontsize = 14)

v_t.yaxis.set_minor_locator(plt.MultipleLocator(settings[0] * 5))
v_t.xaxis.set_minor_locator(plt.MultipleLocator(settings[1] * 100))

v_t.scatter(time[: : 10], volt[::10], marker = 'o')
v_t.plot(time, volt, '-', color = 'blue', label = 'V(t)')

v_t .grid(True)
v_t.grid(which='minor', color= 'grey', linestyle=':', linewidth=0.5)

plt.legend()
plt.show()

plt.savefig('mygraph.svg')
plt.savefig('mygraph.png')
