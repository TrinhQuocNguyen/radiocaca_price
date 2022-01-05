import streamlit as st


def make_clickable(link):
    # target _blank to open new window
    # extract clickable text to display for your link
    text = link.split('=')[1]
    return f'<a target="_blank" href="{link}">{text}</a>'

def convert(row):
    #print(row)
    return '<a href="{}">{}</a>'.format(row['link'],  row.name)

class kiss_land():
    def __init__(self, data):
        self.data = data

    def refine_data(self):
        refined_data = []
        id = []
        fixed_price = []
        link = []
        for i in self.data['list']:
            id.append(i['id'] )
            fixed_price.append(i['fixed_price'] )
            link_text = "https://market.radiocaca.com/#/market-place/" + str(i['id'])
            link.append(link_text)
            # e['fixed_price'] = i['fixed_price'] 
            # e['id'] = i['id'] 
            # e['name'] = i['name'] 
            # e['token_id'] = i['token_id'] 
            # link = "https://market.radiocaca.com/#/market-place/" + str(i['id'])
            # e['link'] = link #st.markdown(link,unsafe_allow_html=True)
            # e['link'] = e.apply(convert, axis=1)
        # refined_data['id']=id
        # refined_data['fixed_price']=fixed_price
        # refined_data['link']=link

        refined_data.append(id)
        refined_data.append(fixed_price)
        refined_data.append(link)

        # print(refined_data)
        # return id, fixed_price, link
        return refined_data

