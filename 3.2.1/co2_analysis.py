import matplotlib.pyplot as plt
import pandas as pd

co2_data = pd.read_csv("co2_data.csv", header=0)

plt.plot(co2_data['Month'], co2_data['Anomaly'], color='gray')
plt.ylabel('CO2 Levels in ppm')
plt.xlabel('Years')
plt.title('Change in Carbon Dioxide')
plt.show()
