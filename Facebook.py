
# coding: utf-8

# In[9]:

#Input: dom - DOM of the books page corresponding to an FB account's profile. Eg, DOM of https://www.facebook.com/zuck/books
#Output: An array (Python list) of books listed in the profile page. 
#    Note that this function requires a list as an output not a Pandas data frame
# write a helper function that  reads this input file, converts it to DOM using Pattern and calls the function for parsing facebook.
 
from collections import defaultdict
import csv
from bs4 import BeautifulSoup
import urllib2
import numpy as np

html_text = open("/Users/dynajose/Desktop/DOM_HTML.rtf").read()
dom = BeautifulSoup(html_text) 

def scraping_facebook_books(dom):

    f_data = bookDom.find_all("div", {"class" : "_gx6 _agv"})
    book=[]
    for f_books in f_data:
            books_title = f_books.find("a","_gx7")
            books= books_title.text
            book.append(books)
    print book


scraping_facebook_books(dom)



# In[16]:

#Input: dom - DOM of the groups page corresponding to an FB account's profile. Eg, DOM of https://www.facebook.com/zuck/groups
#Output: A Pandas data frame with one row per group. 
#    It must have three columns - 'Group Name', 'Number of Members', 'Group Description'
#    Note that all information of a group is in the same page (eg. https://www.facebook.com/zuck/groups)
#    You can collect all data from same page even if they are incomplete (such as group description)
#    Ensure that the column names as given above


from collections import defaultdict
import csv
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import re

html_text = open("/Users/dynajose/Desktop/divyaGroup.rtf").read()
dom = BeautifulSoup(html_text) 


def scraping_facebook_groups(dom):
    

    data=defaultdict(list)   

    group_data = bookDom.find_all("div", {"class" :"mtm"})
    #print group_data

    for g_link in group_data:
        try:
            link=g_link.find_all("div",{'class':'mbs fwb'})
            for link_group in link:
                link_text= link_group.find('a')
                variable= link_text.text.strip()
                data['Group Name'].append(variable)
        except:
            data['Group Name'].append("NA")

    for g_description in group_data:
        try:
            g_dec = g_description.find_all("div",{'class':'mbs fcg'})
            for g in g_dec:
                d=g.text.strip()
                data['Number of Members'].append(d)
        except:
                data['Number of Members'].append("NA")


    for g_members in group_data:
        g_number = g_members.find_all("span",{'class':"_538r"})
        for number in g_number:
            try:
                n=number.text.strip()
                data['Group Description'].append(n)
            except:
                data['Group Description'].append("NA")


    df = pd.DataFrame(data)
    df
    
    return df


scraping_facebook_groups(dom)


# In[2]:

#Input: dom - DOM of the music page corresponding to an FB account's profile. Eg, DOM of https://www.facebook.com/zuck/music
#Output: A Pandas data frame with one row per group. 
#    It must have four columns 
#    'Name', 'Type' (eg. Musician/Band or Bands&Musicians) and 'Verified' (boolean: True/False), 'Profile Url'
#    Note that all information of a group is in the same page (eg. https://www.facebook.com/zuck/music)
#    Ensure that the column names as given above

#def scraping_facebook_music(dom):
 #   return None

from collections import defaultdict
import csv
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import re

text = open("/Users/dynajose/Desktop/PlayList.rtf").read()
dom = BeautifulSoup(text) 

def scraping_facebook_music(dom):
    
    data=defaultdict(list)
    musicData=defaultdict(list)

    f_music = dom.find_all("div", {"class" : "_gx6 _agv"})

    for music in f_music:
        try:
            Name_title = music.find("a","_gx7")
            data['Name'].append(Name_title.text)
        except:
            data['Name'].append("NA")

        try:
            type_title = music.find("div","_1fs8 fsm fwn fcg") 
            data['Type'].append(type_title.text)
        except:
            data['Type'].append("NA") 


    for link_music in f_music:
        try:
            variable=link_music.find('a', href=re.compile('^https:'))['href']
            data['Profile URL'].append(variable)
        except:
            data['Profile URL'].append("NA")


    for verified_page in f_music:
        for page in verified_page:
            page_verified = page.find_all('span',{'aria-label':'Verified Page'})
            #print page_verified
            check= "Verified Page"
            for a in page_verified :
                 if check in str(a) :
                        data['Verified Page'].append(True)
                 else :
                        data['Verified Page'].append(False)


    df = pd.DataFrame(data)
    df
    
    return df

scraping_facebook_music(dom)
    


# In[3]:

#Let us now make things little bit more harder. 
#In all previous cases, you only had to collect information from a single page.
# But in reality, you have to collect information and integrate from multiple pages.
# Let us try a simple version of such data integration 

#Input: dom - DOM of the music page corresponding to an FB account's profile. Eg, DOM of https://www.facebook.com/zuck/movies
#Output: A Pandas data frame with one row per group. 
#    It must have following columns - 
#        'Name', 'Type' (eg. Movie), 'Verified', 'Profile Url' - as before
#        'Likes', 'Starring', 'Genre', 'Director', 'Movie URL'

#    The first three columns can be obtained from https://www.facebook.com/zuck/movies
#    Once you get the profile url, obtain the HTML of this url and use this content to obtain the last 5 column data
#    For example, Zuckerberg likes 'The Matrix' (great movie btw). 
#    Then you get its profile url 'https://www.facebook.com/TheMatrixMovie?ref=profile'
#    Get the text of this url using requests package and parse information from the About tab
#    Ensure that the column names as given above




from collections import defaultdict
import csv
from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import re

text = open("/Users/dynajose/Desktop/Movies.rtf").read()
dom = BeautifulSoup(text) 


def scraping_facebook_movies(dom):


    data=defaultdict(list)
    musicdata=defaultdict(list)

    f_movies = dom.find_all("div", {"class" : "_gx6 _agv"})

    for movie in f_movies:
        try:
            Name_title = movie.find("a","_gx7")
            data['Name'].append(Name_title.text)
        except:
            data['Name'].append("NA")

        try:
            type_title = movie.find("div","_1fs8 fsm fwn fcg") 
            data['Type'].append(type_title.text)
        except:
            data['Type'].append("NA") 


    for link_music in f_movies:
        try:
            variable=link_music.find('a', href=re.compile('^https:'))['href']
            data['Profile URL'].append(variable)
        except:
            data['Profile URL'].append("NA")

    check= "Verified Page"
    for a in f_movies :
        if check in str(a) :
            data['Verified'].append(True)
        else :
            data['Verified'].append(False)

    df = pd.DataFrame(data)
    df
    
    return df

scraping_facebook_movies(dom)


# In[59]:



    


# In[59]:




# In[ ]:



