s as pd
otlib.pyplot as plt

ataset

ad_csv('SITTING AT REST ALL.csv')

 a figure with subplots - one for each sensor type
lt.subplots(3, 1, figsize=(20, 15), sharex=True) # Share X-axis (time)

ngs for better visibility
 2.5
= 7

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')


')ed')


['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')



t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')
ad_csv('SITTING AT REST ALL.csv')


t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')
ad_csv('SITTING AT REST ALL.csv')


t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')
ad_csv('SITTING AT REST ALL.csv')


t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')
ad_csv('SITTING AT REST ALL.csv')


t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')
ad_csv('SITTING AT REST ALL.csv')


t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')
ad_csv('SITTING AT REST ALL.csv')


t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered'))
ad_csv('SITTING AT REST ALL.csv')


t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered'))
ad_csv('SITTING AT REST ALL.csv')


t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')
ad_csv('SITTING AT REST ALL.csv')


t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')
ad_csv('SITTING AT REST ALL.csv')


t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')
ad_csv('SITTING AT REST ALL.csv')


t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')
ad_csv('SITTING AT REST ALL.csv')


t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')
ad_csv('SITTING AT REST ALL.csv')


t.subplots(figsize=(14, 8))

ter data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_CAL'], label='Accel X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_CAL'], label='Accel Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_CAL'], label='Accel Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_X_LPF_CAL'], label='Accel X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Y_LPF_CAL'], label='Accel Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Accel_LN_Z_LPF_CAL'], label='Accel Z Filtered')

data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_CAL'], label='Gyro X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_CAL'], label='Gyro Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_CAL'], label='Gyro Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_X_LPF_CAL'], label='Gyro X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Y_LPF_CAL'], label='Gyro Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Gyro_Z_LPF_CAL'], label='Gyro Z Filtered')

er data
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_CAL'], label='Mag X Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_CAL'], label='Mag Y Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_CAL'], label='Mag Z Unfiltered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_X_LPF_CAL'], label='Mag X Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Y_LPF_CAL'], label='Mag Y Filtered')
['Shimmer_89C7_TimestampSync_Unix_CAL'], data['Shimmer_89C7_Mag_Z_LPF_CAL'], label='Mag Z Filtered')
r Y, Z axes)

g the subplots
itle('Accelerometer Data for Sitting at Rest')
itle('Gyroscope Data for Sitting at Rest')
itle('Magnetometer Data for Sitting at Rest')

s:
label('Timestamp')
label('Measurements')
d()
True)

yout()





