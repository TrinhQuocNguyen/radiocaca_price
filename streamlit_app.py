# importing the requests library
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import numpy as np
import pandas as pd
import layers
from datetime import datetime
import time

def convert(row):
    #print(row)
    return '<a href="{}">{}</a>'.format(row['link'],  row['link'])

import requests


st.header('Kiss Land Price')
# datetime object containing current date and time
now = datetime.now()
st.subheader('Last Update: '+ now.strftime("%d/%m/%Y %H:%M:%S"))

# update every minute (60*1000)
st_autorefresh(interval= 60 * 1000, key="dataframerefresh")

def get_kiss_land_price():
    # api-endpoint
    URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=single_price&order=asc&name=&saleType&category=20&tokenType&tokenId=-1"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'address':"delhi technological university", 'pageNo':2}
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
    
    # extracting data in json format
    data = r.json()

    kiss = layers.kiss_land(data)
    refined_data = kiss.refine_data()
    df = pd.DataFrame({
        'id' : refined_data[0],
        'fixed_price' : refined_data[1],
        'link' : refined_data[2],
    })

    df['link'] = df.apply(convert, axis=1)
    st.write(df.to_html(escape=False), unsafe_allow_html=True)


st.dataframe(get_kiss_land_price())