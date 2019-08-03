import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b):
    return a * np.sin(x * b)

report = open('data.txt', 'r')
datalines = report.readlines()
datalines.pop(0)

latitude = []
longitude = []

for line in datalines:
    k = ' '.join(line.split()).split()
    latitude.append(float(k[1]))
    longitude.append(float(k[2]))

latitude = np.array(latitude)
longitude = np.array(longitude)
time = np.array([i for i in range(0, len(latitude))])

# plt.plot(time, 51.7*np.sin(time/881), label='sin')
# plt.plot(time, latitude, label='latitude')

lon_period = longitude[4609:10563]
time_period = np.array([i for i in range(0, len(lon_period))])

pol_lon = np.poly1d(np.polyfit(time_period, lon_period, 6))
# print(pol_lon)

arr1 = []

# time2 = np.array([i for i in range(0, 2 * len(latitude))])

for t in time_period:
    arr1.append(pol_lon(t))

arr2 = arr1[1300:]

for t in time_period:
    arr2.append(pol_lon(t))

for t in time_period[0:len(time) - 2 * len(time_period) + 1300]:
    arr2.append(pol_lon(t))

arr3 = []

for t in time:
    arr3.append(51.7*np.sin(t/881))

print(len(arr2))
print(len(time))

# plt.plot(time, longitude, label='longitude')
# plt.plot(time, arr2, label='longitude cut')
# plt.plot(time_period - 1300, pol_lon(time_period), label='fitted_lon')

plt.plot(arr2, arr3)
plt.plot(longitude, latitude)

# period = len(lon_period)

# plt.plot(longitude, latitude, label='both')

# params, params_covariance = curve_fit(func, time, latitude, p0=[100, 1/1000])

# plt.plot(time, func(time, params[0], params[1]), label='fit')
plt.legend()
plt.show()