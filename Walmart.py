
# coding: utf-8

# In[11]:




# In[2]:

#Input:
#    url: URL of a Walmart results page for a search query in Movies department
#Output:
#    df is a Pandas data frame that contains a tabular representation of the results
#    The df must have 9 columns that must have the same name and data type as described above
#    Each row of df corresponds to a movie in the results table


from collections import defaultdict
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd



url=raw_input('Enter the URL')

def scraping_walmart_movies(url):
   
    r= requests.get(url)
    r.content
    soup = BeautifulSoup(r.content)


    g_data = soup.find_all("div", {"class" : "tile-content"})
   

    data=defaultdict(list)

    #One loop to rule them all
    for tile in g_data:
        #the "tile" value in g_data contains what you are looking for...
        #find the product titles
        try:
            title = tile.find("a","js-product-title")
            data['Product Title'].append(title.text)
        except:
            data['Product Title'].append("NA")

        #find the prices
        try:
            price = tile.find('span', 'price price-display').text.strip()
            data['Price'].append(price)
        except:
            data['Price'].append("NA")

        try:
            g_star = tile.find("div",{"class" : "stars stars-small tile-row"}).find('span','visuallyhidden').text.strip()
            data['Stars'].append(g_star)
        except:
            data['Stars'].append("NA")

        try:
            dd_starring = tile.find('dd', {"class" : "media-details-multi-line media-details-artist-dd module"}).text.strip()
            data['Starring'].append(dd_starring)
        except:
            data['Starring'].append("NA")

        try:
            running_time = tile.find('dt',{"class" : "media-details-running-time"})
            run_time = running_time.find_next("dd")
            data['Running Time'].append(run_time.text)   
        except:
                    data['Running Time'].append("NA")

        try:
            dd_format = tile.find('dt',{"class" :"media-details-format"})
            form = dd_format.find_next("dd")
            data['Format'].append(form.text)
        except:
            data['Format'].append("NA")

        try:
            dt_rating = tile.find('dt',{"class": "media-details-rating"})
            rate = dt_rating.find_next("dd")
            data['Rating'].append(rate.text)
        except:
            data['Rating'].append("NA")

        div_shipping =tile.find('div',{"class":"tile-aside-content"}).text.strip()
        check = "Preorder now"
        if check in div_shipping:
            data['Shipping'].append("True")
        else:
            data['Shipping'].append("False")

        div_pickup =tile.find('div',{"class":"tile-aside-content"}).text.strip()
        check = "Preorder now"
        if check in div_shipping:
            data['Store Pick Up'].append("True")
        else:
            data['Store Pick Up'].append("False")



    df = pd.DataFrame(data)
    df
    
    #print df

    return df

scraping_walmart_movies(url)




# In[5]:




# In[2]:




# In[ ]:



