import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt



@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value
        
        
        


global numeric_columns
global non_numeric_columns
try:
    st.write(df)
    numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
    non_numeric_columns = list(df.select_dtypes(['object']).columns)
    non_numeric_columns.append(None)
    print(non_numeric_columns)
except Exception as e:
    print(e)


# Title of the dashboard
st.title ("Covid-19 Dashboard For Ethiopia")



st.image('Courtesy-of-ACM-Capital-Partners-LO.png')

st.caption("Ayoub Djama Waberi")
st.sidebar.title("Descriptive Statistics")



def load_data():
    df=pd.read_csv("ethiopia_covid19_cases_hera.csv")
    
    return df
           



st.markdown("The dashboard will visualize the Covid-19 Situation in Ethiopia")


st.markdown("Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.")
st.markdown("The virus can spread from an infected person’s mouth or nose in small liquid particles when they cough, sneeze, speak, sing or breathe. Another person can then contract the virus when infectious particles that pass through the air are inhaled at short range (this is often called short-range aerosol or short-range airborne transmission) or if infectious particles come into direct contact with the eyes, nose, or mouth (droplet transmission).")
st.markdown("The virus can also spread in poorly ventilated and/or crowded indoor settings, where people tend to spend longer periods of time. This is because aerosols can remain suspended in the air or travel farther than conversational distance (this is often called long-range aerosol or long-range airborne transmission)")
st.markdown("People may also become infected when touching their eyes, nose or mouth after touching surfaces or objects that have been contaminated by the virus.")
st.markdown("This data l got from online, and it summary Covid-19 cases (infections, recoveries, deaths and cumulative cases) at the national level in Ethiopia and it recover only one year from January 1, 2020 to December 31, 2020")




data = load_data()
# st.write(data)
st.markdown("dataset:")
st.write(data)
# Show the dimension of the dataframe
# add a select widget to the side bar


checkbox=st.sidebar.checkbox("Number of rows and columns")
print(checkbox)

if checkbox:
    st.markdown("Data contains:")
    st.write(f'Rows: {data.shape[0]}')
    st.write(f'Columns: {data.shape[1]}')

checkbox=st.sidebar.checkbox("Data column")
print(checkbox)
if checkbox:
    st.markdown("Date columns are:")
    st.write(data.columns)

# summary statistics
checkbox=st.sidebar.checkbox("Summary")
print(checkbox)
if checkbox:
    st.markdown("Summary statistics")
    st.write(data.describe())
    
numeric_columns = data.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns


# create scatterplots
st.sidebar.subheader("Scatter plot setup")
numeric_columns = list(data.select_dtypes(['float', 'int']).columns)
non_numeric_columns = list(data.select_dtypes(['object']).columns)
non_numeric_columns.append(None)
print(non_numeric_columns)



st.markdown('Scatterplot')
x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
plot=alt.Chart(data).mark_circle().encode(x=x_values, y=y_values).interactive()
# display the char
st.altair_chart(plot,use_container_width=True)


st.sidebar.subheader("Histogram Settings")
st.markdown('Histogram')
x = st.sidebar.selectbox('Select target column:', options=numeric_columns)
bin_size = st.sidebar.slider("Number of Bins", min_value=10,
                             max_value=100, value=40)
plot = px.histogram(x=x, data_frame=data)
st.plotly_chart(plot)

df= data.drop(['Country', 'ISO_3', "Date"], axis=1) 
 
st.markdown('Lineplots')
st.line_chart(df,width=1100, height=400)

st.write('This is a area_chart.')
st.area_chart(df)



st.markdown('Boxplot')
plot = px.box(df)
st.plotly_chart(plot)

