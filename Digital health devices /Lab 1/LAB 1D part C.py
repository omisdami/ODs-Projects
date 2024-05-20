from pandas import read_csv
import matplotlib.pyplot as plt
for x in range (1,5):
    filepath = f'{x}.csv'
    df= read_csv(filepath)
    #loading datasets of 1st participant
    activitiesx= df.values[:, [4]]
    plt.boxplot(activitiesx)
    plt.xlabel('samples')
    plt.ylabel('Accelerometer')
    plt.title(f"Activity  data for Participant{x}")
    plt.legend('x''y''z')
    plt.show()
    print("Raw Accelerometer  data for Participant x")