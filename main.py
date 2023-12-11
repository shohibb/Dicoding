import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_day = pd.read_csv('day.csv')
data_hour = pd.read_csv('hour.csv')

data_day.isna()
data_hour.isna()

#proses assesing data 
data_day.describe()
data_hour.describe()

print(data_day.duplicated().sum())
print(data_hour.duplicated().sum())

# memperbaiki tabel dateday 
datetime_columns = ["dteday"]

for column in datetime_columns:
  data_day[column] = pd.to_datetime(data_day[column])
  data_hour[column] = pd.to_datetime(data_hour[column])

#dari sini bisa dilihat bahwa tipe data value dari tabel dteday telah berubah dari object ke datetime 
data_day.info()
data_hour.info()

selected_columns = ['season','mnth','holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'cnt']
daybyYear2011 = data_day[(data_day['yr'] == 0) ][selected_columns]
daybyYear2012 = data_day[(data_day['yr'] == 1) ][selected_columns]


correlation_matrix = daybyYear2011.corr()

# Plot garis untuk kolom 'cnt' dengan sumbu x sebagai bulan
daybyYear2011['cnt'].plot(figsize=(12, 6), linestyle='-', color='b')
daybyYear2012['cnt'].plot(figsize=(12, 6), linestyle='-', color='r')
# Atur label dan judul
plt.title('Total Pengguna Selama Tahun 2012')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pengguna')
plt.show()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Total Pengguna Selama Tahun 2012')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pengguna')
plt.show()

cnt_correlation = correlation_matrix['cnt'].drop('cnt')
print("Korelasi dengan kolom 'cnt':")
print(cnt_correlation)


