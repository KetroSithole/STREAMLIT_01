import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Generate sample data
np.random.seed(0)
days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
hours_of_day = list(range(24))

# Generating random accident counts for each day of the week and hour of the day
accidents_data = pd.DataFrame({
    'Day_of_Week': np.random.choice(days_of_week, size=1000),
    'Hour': np.random.choice(hours_of_day, size=1000)
})

# Sidebar
st.sidebar.title('Filter Options')
day_filter = st.sidebar.multiselect(
    'Select Day of the Week', options=days_of_week, default=days_of_week)
hour_filter = st.sidebar.slider(
    'Select Hour of the Day', min_value=0, max_value=23, value=(0, 23))

# Filter data
filtered_data = accidents_data[accidents_data['Day_of_Week'].isin(
    day_filter) & accidents_data['Hour'].between(hour_filter[0], hour_filter[1])]

# Main content
st.title('Car Accidents Dashboard')

# Bar chart for accidents by day of the week
accidents_by_day = filtered_data.groupby(
    'Day_of_Week').size().reset_index(name='Accident Count')
bar_chart_day = alt.Chart(accidents_by_day).mark_bar().encode(
    x='Day_of_Week',
    y='Accident Count',
    tooltip=['Day_of_Week', 'Accident Count']
).properties(
    title='Accidents by Day of the Week'
).interactive()
st.write(bar_chart_day)

# Bar chart for accidents by hour of the day
accidents_by_hour = filtered_data.groupby(
    'Hour').size().reset_index(name='Accident Count')
bar_chart_hour = alt.Chart(accidents_by_hour).mark_bar().encode(
    x='Hour',
    y='Accident Count',
    tooltip=['Hour', 'Accident Count']
).properties(
    title='Accidents by Hour of the Day'
).interactive()
st.write(bar_chart_hour)
