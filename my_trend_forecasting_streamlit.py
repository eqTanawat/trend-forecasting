import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Trend forecasting")

    # Create a sample DataFrame
    data = {
        'Year': [2010, 2011, 2012, 2013, 2014, 2015],
        'Sales': [50, 70, 80, 65, 90, 120]
    }
    df = pd.DataFrame(data)

    # Display the DataFrame
    df = pd.read_csv('train.csv')

    # Display Data
    st.subheader("Data")
    st.text("Data dowloaded from: ")
    st.info("https://www.kaggle.com/competitions/rossmann-store-sales/data?select=store.csv")
    st.text("\nHere is the data we will use to forecast the trend")
    st.dataframe(df)

    # Display EDA
    st.subheader("Exploratory Data Analysis(EDA)")
    st.text( """
Store - a unique Id for each store
DayOfWeek - 0=Monday, 1=Tuesday, ... , 6=Sunday}
Sales - the turnover for any given day (This is what we are predicting)
Customers - the number of customers on a given day
Open - 0 = closed, 1 = open
StateHoliday -  a = public holiday, b = Easter holiday, 
                c = Christmas, 0 = None
SchoolHoliday - indicates if the (Store, Date) was affected by 
                the closure of public schools


        
    """)

    # st.

    # Create a line chart using Plotly
    # fig_line = px.line(df, x='Year', y='Sales')
    # st.subheader("Line Chart")
    # st.plotly_chart(fig_line)

    # # Create a bar chart using Plotly
    # fig_bar = px.bar(df, x='Year', y='Sales')
    # st.subheader("Bar Chart")
    # st.plotly_chart(fig_bar)

if __name__ == "__main__":
    main()