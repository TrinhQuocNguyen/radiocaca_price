# importing the requests library
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import numpy as np
import pandas as pd
import layers
from datetime import datetime
import time
import requests

import csv



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

    # metamon and kiss
    row = [df_metamon[1][0], df_kiss[1][0]]
    st.markdown('Metamon Lowest Price: **'+ str(df_metamon[1][0]) +'**.')
    st.markdown('Kiss_Land Lowest Price: **'+ str(df_kiss[1][0]) +'**.')
    # open the file in the write mode
    with open('data\metamon_kiss.csv', 'a', newline='', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(row)

    harvard_n = layers.New_Harvard_N_Land()
    df_harvard_n = harvard_n.get_price()

    musk_usm = layers.Musk_Land()
    df_musk_usm = musk_usm.get_price()

    land = [now.strftime("%d/%m/%Y %H:%M:%S"),df_metamon[1][0], df_kiss[1][0],df_harvard_n[1][0],df_musk_usm[1][0]]
    # open the file in the write mode
    with open('data\land.csv', 'a', newline='', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(land)

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

def draw_chart_metamon():
    st.subheader('Metamon & Kiss Land Graph')
    df = pd.read_csv("data\metamon_kiss.csv")
    st.line_chart(df)

def get_egg():
    now = datetime.now()
    st.subheader('Last Update: '+ now.strftime("%d/%m/%Y %H:%M:%S"))
    egg = layers.Egg()
    df_egg = egg.get_price()

    potion = layers.Potion()
    df_potion = potion.get_price()

    # egg and potion
    row = [df_egg[1][0], df_potion[1][0]]
    st.markdown('Egg Lowest Price: **'+ str(df_egg[1][0]) +'**.')
    st.markdown('Potion Lowest Price: **'+ str(df_potion[1][0]) +'**.')
    # open the file in the write mode
    with open('data\egg.csv', 'a', newline='', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(row)

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


def draw_chart_egg():
    st.subheader('Egg & Potion Graph')
    df = pd.read_csv("data\egg.csv")
    st.line_chart(df)


def get_full_price():

    get_main()
    draw_chart_metamon()
    get_egg()
    draw_chart_egg() 


st.dataframe(get_full_price())