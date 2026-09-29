import matplotlib.pyplot as plt
import numpy as np

days = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
temp = [28, 30, 29, 32, 31, 33, 30]

plt.figure(figsize=(6, 4))
plt.plot(days, temp, marker='o', color='b', linestyle='--')
plt.title("Weekly Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
