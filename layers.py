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
        r = requests.post(url = self.URL, data = self.data)
        
        # extracting data in json format
        res_data = r.json()
        print(res_data)
        # refined_data = self.refine_data(data)

        return res_data


class Kiss_Land(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=single_price&order=asc&name=&saleType&category=20&tokenType&tokenId=-1"

   
class New_Harvard_N_Land(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=single_price&order=asc&name=&saleType&category=34&tokenType&tokenId=-1"


class Musk_Land(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=single_price&order=asc&name=&saleType&category=7&tokenType&tokenId=-1"

class Musk_Land(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=single_price&order=asc&name=&saleType&category=7&tokenType&tokenId=-1"

class Egg(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=fixed_price&order=asc&name=&saleType&category=17&tokenType&tokenId=-1"

class Potion(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=fixed_price&order=asc&name=&saleType&category=15&tokenType&tokenId=-1"


class Dragon_Fruit_Dog(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=fixed_price&order=asc&name=&saleType&category=26&tokenType&tokenId=-1"

class Yellow_Diamond(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=fixed_price&order=asc&name=&saleType&category=16&tokenType&tokenId=0"

class Purple_Diamond(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=fixed_price&order=asc&name=&saleType&category=16&tokenType&tokenId=1"

class Black_Diamond(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=fixed_price&order=asc&name=&saleType&category=16&tokenType&tokenId=2"

class Ding(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=fixed_price&order=asc&name=&saleType&category=12&tokenType&tokenId=-1"

class SpaceXNaut_Dog(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=fixed_price&order=asc&name=&saleType&category=9&tokenType&tokenId=-1"


class Metamon(Item):
    def __init__(self):
        super().__init__()
        # api-endpoint
        self.URL = "https://market-api.radiocaca.com/nft-sales?pageNo=1&pageSize=20&sortBy=single_price&order=asc&name=&saleType&category=13&tokenType&tokenId=-1"

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
