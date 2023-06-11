import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Trend forecasting")

    # read the csv as DataFrame
    df1 = pd.read_csv('file/train-1.csv')
    df2 = pd.read_csv('file/train-2.csv')
    df3 = pd.read_csv('file/train-3.csv')
    df = df1.append(df2, ignore_index=True).append(df3, ignore_index=True)

    # get image
    # arima_predict = st.image("ARIMA_predict.png", caption="Data with ARIMA prediction")

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
    arima= "https://scontent.fbkk5-5.fna.fbcdn.net/v/t39.30808-6/353461989_3507298182877887_4439614939122370442_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeHrO1xnVshgOWhvyqXLy88O0dyTUwNf21LR3JNTA1_bUsWH-5eITlNp7avEJbJAxGVX0XBxAQwgY-8ycNksNFJK&_nc_ohc=NaeOo-u3aJcAX9qEZEH&_nc_ht=scontent.fbkk5-5.fna&oh=00_AfBIMV0SCufyLRQsSP2xoo-Ro8lTnuuBtzXbUU47ttzHqQ&oe=648A1BA4"
    st.image(arima)
    
    
if __name__ == "__main__":
    main()
