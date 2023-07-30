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
        
    As we can that there are more than a thousand stores with each store's data 
are 3-year long, we will focus only a store for this case.
    """)

    # Display Data plotted
    st.subheader("Data plotted")
    st.text("Here we are focusing on the store 622 for the educational purpose")
    sales= "https://www.facebook.com/photo/?fbid=3541003796173992&set=a.1633627773578280"
    lnr = "https://www.facebook.com/photo/?fbid=3541005166173855&set=a.1633627773578280"
    arima = "https://www.facebook.com/photo/?fbid=3541005576173814&set=a.1633627773578280"
    st.image(sales, caption="Sales of store no. 622")
    st.text("""
    We will use this data to predict the future value of sales of the store no.622
    """)
    
    # Display Prediction
    st.subheader("Prediction")
    select = st.selectbox('Select the model to predict', [ "Linear Regression", "ARIMA"])
    if select ==  "Linear Regression":
        st.image(lnr, caption="Sales of store no. 622 with last 95-day prediction using Linear Regression")
        st.text("We will use root mean square error(RMSE) to evaluate the error.")
        st.text("The RMSE = 646.5447165656475")
    elif select == "ARIMA":
        st.image(arima, caption="Sales of store no. 622 with last 95-day prediction using ARIMA")
        st.text("We will use root mean square error(RMSE) to evaluate the error.")
        st.text("The RMSE = 2050.939466743283")
   
    st.info("We can see that in this case, using Linear Regression to predict the sales is more accurate.")

if __name__ == "__main__":
    main()
