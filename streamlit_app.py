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
def convert_egg(row):
    # print(row)
    return '<a href="{}">{}</a>'.format(row['link_egg'], "Link")
def convert_potion(row):
    # print(row)
    return '<a href="{}">{}</a>'.format(row['link_potion'], "Link")

def convert_dragon(row):
    # print(row)
    return '<a href="{}">{}</a>'.format(row['link_dragon'], "Link")

# update every minute (60*1000)
st_autorefresh(interval= 5* 60 * 1000, key="dataframerefresh")
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

def get_main():
    now = datetime.now()
    st.subheader('Last Update: '+ now.strftime("%d/%m/%Y %H:%M:%S"))
    metamon = layers.Metamon()
    df_metamon = metamon.get_price()

    kiss = layers.Kiss_Land()
    df_kiss = kiss.get_price()

    harvard_n = layers.New_Harvard_N_Land()
    df_harvard_n = harvard_n.get_price()

    musk_usm = layers.Musk_Land()
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

    st.write(df_full.to_html(escape=False), unsafe_allow_html=True)


def get_egg():
    now = datetime.now()
    st.subheader('Last Update: '+ now.strftime("%d/%m/%Y %H:%M:%S"))
    egg = layers.Egg()
    df_egg = egg.get_price()

    potion = layers.Potion()
    df_potion = potion.get_price()

    dragon = layers.Dragon_Fruit_Dog()
    df_dragon = dragon.get_price()

    df_full = pd.DataFrame({
        'EGG' : df_egg[1],
        'link_egg' : df_egg[2],

        'POTION' : df_potion[1],
        'link_potion' : df_potion[2],

        'DRAGON_FRUIT' : df_dragon[1],
        'link_dragon' : df_dragon[2],
    })

    df_full['link_egg'] = df_full.apply(convert_egg, axis=1)
    df_full['link_potion'] = df_full.apply(convert_potion, axis=1)
    df_full['link_dragon'] = df_full.apply(convert_dragon, axis=1)

    st.write(df_full.to_html(escape=False), unsafe_allow_html=True)
   
def get_full_price():
    get_main()
    get_egg()

    

st.dataframe(get_full_price())