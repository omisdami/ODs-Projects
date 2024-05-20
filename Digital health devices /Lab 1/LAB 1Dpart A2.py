from pandas import read_csv
import matplotlib.pyplot as plt
from matplotlib import pyplot
df1 = read_csv('1.csv')
df2 = read_csv('2.csv')
df3 = read_csv('3.csv')
df4 = read_csv('4.csv')

activities1 = df1.values[:, [4]]
activities2 = df2.values[:, [4]]
activities3 = df3.values[:, [4]]
activities4 = df4.values[:, [4]]

fig, axs = plt.subplots(4)
fig.suptitle('Vertically stacked Activity  data for Participant 1 to 4')
axs[0].plot(activities1)
axs[1].plot(activities2)
axs[2].plot(activities3)
axs[3].plot(activities4)
plt.show()