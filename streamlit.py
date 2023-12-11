import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data_day = pd.read_csv('day.csv')

# Assessing data
datetime_columns = ["dteday"]

for column in datetime_columns:
    data_day[column] = pd.to_datetime(data_day[column])

selected_columns = ['season', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'cnt']
daybyYear2011 = data_day[(data_day['yr'] == 0)][selected_columns]
daybyYear2012 = data_day[(data_day['yr'] == 1)][selected_columns]

# Calculate correlation matrix
correlation_matrix = daybyYear2011.corr()

# Streamlit Dashboard
st.title('Bike Sharing Analysis Dashboard')

# Sidebar
st.sidebar.title('Select Options')
option = st.sidebar.selectbox('Select Visualization', ['Line Plot', 'Correlation Heatmap'])

# Display selected visualization
if option == 'Line Plot':
    st.subheader('Total Pengguna Selama Tahun 2012')
    st.line_chart(daybyYear2011[['cnt', 'cnt']])

elif option == 'Correlation Heatmap':
    st.subheader('Correlation Heatmap')
    st.write(correlation_matrix)

    # Display heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
    st.pyplot()

# Additional insights
st.subheader('Additional Insights')
cnt_correlation = correlation_matrix['cnt'].drop('cnt')
st.write("Korelasi dengan kolom 'cnt':")
st.write(cnt_correlation)
