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
import super_hero




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

    df_full['link_kiss'] = df_full.apply(super_hero.convert_kiss, axis=1)
    df_full['link_harvard'] = df_full.apply(super_hero.convert_harvard, axis=1)
    df_full['link_musk'] = df_full.apply(super_hero.convert_musk, axis=1)
    df_full['link_metamon'] = df_full.apply(super_hero.convert_metamon, axis=1)


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

    y_diamond = layers.Yellow_Diamond()
    df_y_diamond = y_diamond.get_price()

    p_diamond = layers.Purple_Diamond()
    df_p_diamond = p_diamond.get_price()

    b_diamond = layers.Black_Diamond()
    df_b_diamond = b_diamond.get_price()

    dragon = layers.Dragon_Fruit_Dog()
    df_dragon = dragon.get_price()

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


    # egg and potion
    row_dragon_purple_black = [df_dragon[1][0], df_p_diamond[1][0], df_b_diamond[1][0]]
    st.markdown('Dragon Fruit Lowest Price: **'+ str(df_dragon[1][0]) +'**.')
    st.markdown('Purple Diamond Lowest Price: **'+ str(df_p_diamond[1][0]) +'**.')
    st.markdown('Black Diamond Lowest Price: **'+ str(df_b_diamond[1][0]) +'**.')
    # open the file in the write mode
    with open('data\dragon_purple_black.csv', 'a', newline='', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(row_dragon_purple_black)



    df_full = pd.DataFrame({
        'EGG' : df_egg[1],
        'link_egg' : df_egg[2],

        'POTION' : df_potion[1],
        'link_potion' : df_potion[2],

        'YELLOW_DIAMOND' : df_y_diamond[1],
        'link_y_diamond' : df_y_diamond[2],

        'DRAGON_FRUIT' : df_dragon[1],
        'link_dragon' : df_dragon[2],
        
        'PURPLE_DIAMOND' : df_p_diamond[1],
        'link_p_diamond' : df_p_diamond[2],
        
        'BLACK_DIAMOND' : df_b_diamond[1],
        'link_b_diamond' : df_b_diamond[2],

    })

    df_full['link_egg'] = df_full.apply(super_hero.convert_egg, axis=1)
    df_full['link_potion'] = df_full.apply(super_hero.convert_potion, axis=1)
    df_full['link_y_diamond'] = df_full.apply(super_hero.convert_y_diamond, axis=1)
    df_full['link_dragon'] = df_full.apply(super_hero.convert_dragon, axis=1)
    df_full['link_p_diamond'] = df_full.apply(super_hero.convert_p_diamond, axis=1)
    df_full['link_b_diamond'] = df_full.apply(super_hero.convert_b_diamond, axis=1)

    st.write(df_full.to_html(escape=False), unsafe_allow_html=True)


def draw_chart_egg():
    st.subheader('Egg & Potion Graph')
    df = pd.read_csv("data\egg.csv")
    st.line_chart(df)

def draw_chart_dragon_purple_black():
    st.subheader('Dragon_Fruit & Purple Diamon & Black Diamond')
    df = pd.read_csv("data\dragon_purple_black.csv")
    st.line_chart(df)


def get_in_egg_price():
    in_egg = layers.InEgg()
    df_in_egg = in_egg.get_price()

    print(df_in_egg)

def get_full_price():
    # get_in_egg_price()

    get_main()
    draw_chart_metamon()
    get_egg()
    draw_chart_egg() 
    draw_chart_dragon_purple_black()


st.dataframe(get_full_price())