# importing the requests library
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import numpy as np
import pandas as pd
import layers
from datetime import datetime
import time
import requests

def convert_kiss(row):
    # print(row)
    return '<a href="{}">{}</a>'.format(row['link_kiss'],  "Link")
def convert_harvard(row):
    # print(row)
    return '<a href="{}">{}</a>'.format(row['link_harvard'], "Link")
def convert_musk(row):
    # print(row)
    return '<a href="{}">{}</a>'.format(row['link_musk'], "Link")
def convert_metamon(row):
    # print(row)
    return '<a href="{}">{}</a>'.format(row['link_metamon'], "Link")


# update every minute (60*1000)
st_autorefresh(interval= 60 * 1000, key="dataframerefresh")

def get_full_price():
    now = datetime.now()
    st.subheader('Last Update: '+ now.strftime("%d/%m/%Y %H:%M:%S"))


    metamon = layers.metamon()
    df_metamon = metamon.get_price()

    kiss = layers.kiss_land()
    df_kiss = kiss.get_price()

    harvard_n = layers.new_harvard_n_land()
    df_harvard_n = harvard_n.get_price()

    musk_usm = layers.musk_land()
    df_musk_usm = musk_usm.get_price()

    df_full = pd.DataFrame({
        'METAMON' : df_metamon[1],
        'link_metamon' : df_metamon[2],
        'Level' : df_metamon[3],
        'Score' : df_metamon[4],

        'KISS_LAND' : df_kiss[1],
        'link_kiss' : df_kiss[2],

        'New_Harvard_N_Land' : df_harvard_n[1],
        'link_harvard' : df_harvard_n[2],

        'MUSK_USM_Land' : df_musk_usm[1],
        'link_musk' : df_musk_usm[2],

    })

    df_full['link_kiss'] = df_full.apply(convert_kiss, axis=1)
    df_full['link_harvard'] = df_full.apply(convert_harvard, axis=1)
    df_full['link_musk'] = df_full.apply(convert_musk, axis=1)
    df_full['link_metamon'] = df_full.apply(convert_metamon, axis=1)

    # df_kiss = get_kiss_land_price()
    # st.write(df_kiss.to_html(escape=False), unsafe_allow_html=True)
    
    # df_metamon = get_kiss_land_price()
    st.write(df_full.to_html(escape=False), unsafe_allow_html=True)
    # st.dataframe(df_full.style.highlight_min(axis=0))
    

st.dataframe(get_full_price())