from sre_constants import MIN_REPEAT
import streamlit as st
import requests


class Item():
    def __init__(self):
        # api-endpoint
        self.URL = ""
        # defining a params dict for the parameters to be sent to the API
        self.PARAMS = {'address':"delhi technological university"}

    def refine_data(self, data):
        refined_data = []
        id = []
        fixed_price = []
        link = []
        for i in data['list']:
            id.append(i['id'] )
            fixed_price.append(float(i['fixed_price'])/float(i['count']))
            link_text = "https://market.radiocaca.com/#/market-place/" + str(i['id'])
            link.append(link_text)
        refined_data.append(id)
        refined_data.append(fixed_price)
        refined_data.append(link)
        
        return refined_data

    def get_price(self):
        # sending get request and saving the response as response object
        r = requests.get(url = self.URL, params = self.PARAMS)
        
        # extracting data in json format
        data = r.json()
        refined_data = self.refine_data(data)

        return refined_data

    def get_min_price(self, horse_list):
        min_price = 9999999
        min_item = []
        for i in horse_list:
            if float(i['price']) < min_price:
                min_price = float(i['price'])
                min_item = i

        return min_price, min_item



class Pega(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://api-apollo.pegaxy.io/v1/pegas/prices/floor?category=bloodLine,breedCount,gender,breedType&maxBreedCount=7&minBreedCount=0"

    def refine_data(self, data):
        hoz = []
        campona = []
        klin=[]
        zan=[]

        print("Number of pegas on the market: ", len(data))
        for i in data:
            if i['bloodLine'] == 'Hoz':
                hoz.append(i)
            elif i['bloodLine'] == 'Campona':
                campona.append(i)
            elif i['bloodLine'] == 'Klin':
                klin.append(i)
            elif i['bloodLine'] == 'Zan':
                zan.append(i)
        
        min_hoz, min_hoz_item = self.get_min_price(hoz)
        min_campona, min_campona_item = self.get_min_price(campona)
        min_klin, min_klin_item = self.get_min_price(klin)
        min_zan, min_zan_item = self.get_min_price(zan)
        
        return [min_hoz, min_hoz_item, min_campona, min_campona_item, min_klin, min_klin_item, min_zan, min_zan_item]