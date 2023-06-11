import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Trend forecasting")

    # read the csv as DataFrame
    df1 = pd.read_csv('train-1.csv')
    df2 = pd.read_csv('train-2.csv')
    df3 = pd.read_csv('train-3.csv')
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
    arima= "https://scontent.fbkk5-4.fna.fbcdn.net/v/t1.6435-9/128124717_2804596149814764_4906386206631881031_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeGGCHN9UWBRdfVh0OfUbH-Ed6cKhWM1XSx3pwqFYzVdLM0FjPdAM2s0LtD646TCNbIDwiinUF2OECRBDvnYCD4-&_nc_ohc=ZWj6U-yeLCsAX_u1Iwh&_nc_ht=scontent.fbkk5-4.fna&oh=00_AfA6a70HULl_Wy0alSQkLpzMzZLLM6KrOGnM6D5WVOrHTw&oe=64AD793D"
    st.image(arima)
    
    
if __name__ == "__main__":
    main()
