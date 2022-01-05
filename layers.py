import streamlit as st
import requests

def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split('=')[1]
    return f'<a target="_blank" href="{link}">{text}</a>'

def convert(row):
    #print(row)
    return '<a href="{}">{}</a>'.format(row['link'],  row.name)

class kiss_land():
    def __init__(self):
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=single_price&order=asc&name=&saleType&category=20&tokenType&tokenId=-1"
        # defining a params dict for the parameters to be sent to the API
        self.PARAMS = {'address':"delhi technological university"}

    def refine_data(self, data):
        refined_data = []
        id = []
        fixed_price = []
        link = []
        for i in data['list']:
            id.append(i['id'] )
            fixed_price.append(i['fixed_price'] )
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

class new_harvard_n_land():
    def __init__(self):
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=single_price&order=asc&name=&saleType&category=34&tokenType&tokenId=-1"
        # defining a params dict for the parameters to be sent to the API
        self.PARAMS = {'address':"delhi technological university"}

    def refine_data(self, data):
        refined_data = []
        id = []
        fixed_price = []
        link = []
        for i in data['list']:
            id.append(i['id'] )
            fixed_price.append(i['fixed_price'] )
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

class musk_land():
    def __init__(self):
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=single_price&order=asc&name=&saleType&category=7&tokenType&tokenId=-1"
        # defining a params dict for the parameters to be sent to the API
        self.PARAMS = {'address':"delhi technological university"}

    def refine_data(self, data):
        refined_data = []
        id = []
        fixed_price = []
        link = []
        for i in data['list']:
            id.append(i['id'] )
            fixed_price.append(i['fixed_price'] )
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


class metamon():
    def __init__(self):
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=single_price&order=asc&name=&saleType&category=13&tokenType&tokenId=-1"
        # defining a params dict for the parameters to be sent to the API
        self.PARAMS = {'address':"delhi technological university"}

    def refine_data(self, data):
        refined_data = []
        id = []
        fixed_price = []
        link = []
        level = []
        score = []
        for i in data['list']:
            id.append(i['id'] )
            fixed_price.append(i['fixed_price'] )
            link_text = "https://market.radiocaca.com/#/market-place/" + str(i['id'])
            link.append(link_text)
            URL = "https://market-api.radiocaca.com/nft-sales/" + str(i['id'])
            r = requests.get(url = URL)
            data_metamon = r.json()
            level.append(data_metamon['data']['properties'][2]['value'])
            score.append(data_metamon['data']['properties'][4]['value'])
        
        refined_data.append(id)
        refined_data.append(fixed_price)
        refined_data.append(link)
        refined_data.append(level)
        refined_data.append(score)
        
        return refined_data

    def get_price(self):
        # sending get request and saving the response as response object
        r = requests.get(url = self.URL, params = self.PARAMS)
        
        # extracting data in json format
        data = r.json()
        refined_data = self.refine_data(data)

        return refined_data        