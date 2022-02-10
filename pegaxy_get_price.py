# importing the requests library
import numpy as np
import pandas as pd
import pegaxy_layers
from datetime import datetime
import time
import requests

import csv
import super_hero

def get_pega():
    now = datetime.now()
    pega = pegaxy_layers.Pega()
    min_hoz, min_hoz_item, min_campona, min_campona_item, min_klin, min_klin_item, min_zan, min_zan_item = pega.get_price()

    row_pega = [now.strftime("%d/%m/%Y %H:%M:%S"),min_hoz, min_campona, min_klin, min_zan]
    # open the file in the write mode
    with open('data\log_pega.csv', 'a', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(row_pega)

    print("Current Floor Hoz    : ", min_hoz_item)
    print("Current Floor Campona: ", min_campona_item)
    print("Current Floor Klin   : ", min_klin_item)
    print("Current Floor Zan    : ", min_zan_item)

 

def get_full_price():
    print("---------------------")
    get_pega()

if __name__ == "__main__":
    # get_full_price()
    while True:
        get_full_price()
        # Sleep 1 minute = 1*60
        time.sleep(5*60)