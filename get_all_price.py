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

    print("Current Metamon price: ", row_metamon)



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

    print("Current Egg price: ", row_egg)


def get_dragon_fruit():
    now = datetime.now()
    
    dragon = layers.Dragon_Fruit_Dog()
    df_dragon = dragon.get_price()

    # dragon fruit, purple diamond, black diamond
    row_dragon_purple_black = [now.strftime("%d/%m/%Y %H:%M:%S"), df_dragon[1][0]]
    # open the file in the write mode
    with open('data\log_dragon.csv', 'a', newline='', encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(row_dragon_purple_black)

    print("Current Dragon Fruit price: ", row_dragon_purple_black)
    

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