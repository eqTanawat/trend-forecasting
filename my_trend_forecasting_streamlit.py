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
    sales= "https://scontent.fbkk5-5.fna.fbcdn.net/v/t39.30808-6/353461989_3507298182877887_4439614939122370442_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeHrO1xnVshgOWhvyqXLy88O0dyTUwNf21LR3JNTA1_bUsWH-5eITlNp7avEJbJAxGVX0XBxAQwgY-8ycNksNFJK&_nc_ohc=AuppCf5NmgoAX-WRZPl&_nc_ht=scontent.fbkk5-5.fna&oh=00_AfB8BviF1-gao04wsel0VJYmUtoRftDK56LjBBu6OG3JEg&oe=649204A4"
    lnr = "https://scontent.fbkk5-8.fna.fbcdn.net/v/t39.30808-6/351309529_3507525069521865_6197265728625637096_n.jpg?stp=dst-jpg_p180x540&_nc_cat=106&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeFFh_vCjyDsYLDVOvjgPS7rUN_vMvKeryRQ3-8y8p6vJD-SR0jzDYOa1bLFm4Zdfx_sPNXHZr5-gBjdg1WOurYC&_nc_ohc=2c9mRjahQ9kAX8NNiln&_nc_ht=scontent.fbkk5-8.fna&oh=00_AfBCyhNWIX6ey1_ivwcbOmxoJO3aiN_hvhjUmBTCEF0inA&oe=648B5C5D"
    arima = "https://scontent.fbkk5-8.fna.fbcdn.net/v/t39.30808-6/351500624_3507525299521842_9083148150464627825_n.jpg?stp=dst-jpg_p180x540&_nc_cat=106&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeGhDaIO9gWbV6n85SfWr3jESIhVljZp70ZIiFWWNmnvRsygAVmUFvTVj27pxrt3-XDMAfggZHoGu31gje-AxW9C&_nc_ohc=wFl_0tbDscYAX-Kfs_x&_nc_ht=scontent.fbkk5-8.fna&oh=00_AfDgUqfIqNwws19nDEua8oKVzGIMm6mfCsSyp7ak5AFO-g&oe=648BA88B"
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
