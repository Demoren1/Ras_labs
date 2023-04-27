import matplotlib.pyplot as plt
from adc import *
import time

x = []
y = []

my_time1 = time.time()

data = []
frequency = 0.01
base_adc(data, frequency)                       #получение данных

my_time2 = time.time()
print(my_time2 - my_time1)


for result in data:                             #вывод полученных данных
    print("value = %g, t = %.3g" % (result[0], result[1]))
    x.append(result[1])
    y.append(result[0])


plt.grid()
plt.plot(x, y)
plt.show()

with open("data.txt", "w") as file:         #запись в файл
    file.write('value time\n')
    for result in data:
        my_string = str(result[0]) + ' ' + str(result[1]) + '\n'
        file.write(my_string)
print("time of experiment %g" % (my_time2 - my_time1))

delta_time = my_time2 - my_time1
discr = len(y) / delta_time
kvant = 3.3 / 256

with open("settings.txt", "w") as settings:
    tmp_str = str(delta_time) + ' '
    settings.write(tmp_str)

    tmp_str = str(frequency) + ' '
    settings.write(tmp_str)

    tmp_str = str(discr) + ' '
    settings.write(tmp_str)

    tmp_str = str(kvant) + ' '
    settings.write(tmp_str)
print("discr = %g, kvant = %g, time = %g, frequency = %g" %(discr, kvant, delta_time, frequency))
