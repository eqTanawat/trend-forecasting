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
    arima = "https://scontent.fbkk5-1.fna.fbcdn.net/v/t39.30808-6/362972382_3541004906173881_5337573898733412971_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeE9Brv6qjIazemFkAOUcWtRJDsEXZsRZ1okOwRdmxFnWuAQVztNNhayNWWq7GmixyMk3I1UCYs1-kehZfHmmpT4&_nc_ohc=5zFPU-DIajQAX8uW78Y&_nc_ht=scontent.fbkk5-1.fna&oh=00_AfDkhwZN8tvrxSQ1LVWzTFywRTnc4qn0vb1LdFWjsDK-Jg&oe=64CABFFD"
    lnr = "https://scontent.fbkk5-7.fna.fbcdn.net/v/t39.30808-6/362301253_3541005159507189_5498899144795092437_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeF6eU4vFwpWWvNQwKbmxegxm15PdeRtTNObXk915G1M0_1-ej7yEENr1v28_oahJeGNWHgbvR9xubd-dfhH13cW&_nc_ohc=FL8yP820oSsAX8gSOVi&_nc_ht=scontent.fbkk5-7.fna&oh=00_AfA0-kihPFYJl34phQnI-aOFAWe2xPmb3USzplLxI0gidg&oe=64CB113D"
    sales = "https://scontent.fbkk5-6.fna.fbcdn.net/v/t39.30808-6/362667351_3541005572840481_168163173636487475_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeESqQ6tJzKrBfasmiFtUBOLXAJXLcDVyEhcAlctwNXISGHysuiRdhXW02eZhaElEKM7A8zIR3TdJtRJhhPxnQS4&_nc_ohc=thSUktnv8vYAX-W9N6V&_nc_ht=scontent.fbkk5-6.fna&oh=00_AfA3BNF5b76RSYpYFfUY-GQuT4IQHKfe_RAQiMET9l084w&oe=64CB20F1"
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
