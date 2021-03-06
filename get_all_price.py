# importing the requests library
import numpy as np
import pandas as pd
import layers
from datetime import datetime
import time
import requests

import csv
import super_hero

def get_metamon():
    now = datetime.now()
    metamon = layers.Metamon()
    df_metamon = metamon.get_price()

    kiss = layers.Kiss_Land()
    df_kiss = kiss.get_price()

    harvard_n = layers.New_Harvard_N_Land()
    df_harvard_n = harvard_n.get_price()

    musk_usm = layers.Musk_Land()
    df_musk_usm = musk_usm.get_price()

    row_metamon = [now.strftime("%d/%m/%Y %H:%M:%S"),df_metamon[1][0], df_kiss[1][0],df_harvard_n[1][0],df_musk_usm[1][0]]
    # open the file in the write mode
    with open('data\log_metamon.csv', 'a', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(row_metamon)

    # print("Current Metamon, Kiss, Harvard, Musk: ", row_metamon)
    print("### At: "+ str(now.strftime("%d/%m/%Y %H:%M:%S")))
    print("Metamon = " + str(float(df_metamon[1][0]))   + ", Kiss = " + str(df_kiss[1][0]))
    print("Harvard = " + str(df_harvard_n[1][0]) + ", Musk = " + str(df_musk_usm[1][0]))



def get_egg():
    now = datetime.now()
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

    # egg and potion
    row_egg = [now.strftime("%d/%m/%Y %H:%M:%S"), df_egg[1][0], df_potion[1][0], df_y_diamond[1][0], df_p_diamond[1][0], df_b_diamond[1][0]]
    # open the file in the write mode
    with open('data\log_egg.csv', 'a', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(row_egg)

    # print("Current Egg, Potion, Yellow, Purple, Black: ", row_egg)
    print("### At: "+ str(now.strftime("%d/%m/%Y %H:%M:%S")))
    print("Egg = " + str(df_egg[1][0])   + ", Potion = " + str(df_potion[1][0]) + ", Yellow = " + str(df_y_diamond[1][0]))
    print("Purple = " + str(df_p_diamond[1][0]) + ", Black = " + str(df_b_diamond[1][0]))


def get_dragon_fruit():
    now = datetime.now()
    
    dragon = layers.Dragon_Fruit_Dog()
    df_dragon = dragon.get_price()

    ding = layers.Ding()
    df_ding = ding.get_price()
    
    space = layers.SpaceXNaut_Dog()
    df_space = space.get_price()

    bake = layers.Bake_Musk_Mixer()
    df_bake = bake.get_price()

    raca_punk = layers.Raca_Punk()
    df_raca_punk = raca_punk.get_price()

    # dragon fruit, purple diamond, black diamond
    row_dragon_purple_black = [now.strftime("%d/%m/%Y %H:%M:%S"), df_dragon[1][0], df_ding[1][0],df_space[1][0],df_bake[1][0],df_raca_punk[1][0]]
    # open the file in the write mode
    with open('data\log_dragon.csv', 'a', newline='', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(row_dragon_purple_black)

    # print("Current Dragon Fruit, Ding, SpaceX, Bake, Punk: ", row_dragon_purple_black)
    print("### At: "+ str(now.strftime("%d/%m/%Y %H:%M:%S")))
    print("Dragon Fruit = " + str(df_dragon[1][0])   + ", Ding = " + str(df_ding[1][0]))
    print("SpaceX = " + str(df_space[1][0]) + ", Bake = " + str(df_bake[1][0]) + ", Punk = " + str(df_raca_punk[1][0]))    
    

def get_full_price():
    print("---------------------")
    get_metamon()
    get_egg()
    get_dragon_fruit()

if __name__ == "__main__":
    while True:
        get_full_price()
        # Sleep 1 minute = 1*60
        time.sleep(5*60)