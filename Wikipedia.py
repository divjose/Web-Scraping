
# coding: utf-8

# In[ ]:




# In[2]:

#Input:
#    url: URL of a wikipedia page
#    table_no: Number of the table to scrape
#Output:
#    df is a Pandas data frame that contains a tabular representation of the table
#    The columns are named the same as the table columns
#    Each row of df corresponds to a row in the table


from bs4 import BeautifulSoup
import urllib2
from lxml.html import fromstring 
import re
import csv
import pandas as pd


url= raw_input('Enter the URL')
table_number= raw_input('Enter the table number')
table_no=int(table_number)

def scraping_wikipedia_table(url, table_no):
    wiki=url
    header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
    req = urllib2.Request(wiki,headers=header)
    page = urllib2.urlopen(req)

    soup = BeautifulSoup(page)

    table = soup.find_all('table')[table_no]

    tmp = table.find_all('tr')

    first = tmp[0]
    allRows = tmp[1:-1]

    headers = [header.get_text() for header in first.find_all('th')]
    results = [[data.get_text() for data in row.find_all('td')] for row in allRows]

    rowspan = []

    for no, tr in enumerate(allRows):
        tmp = []
        for td_no, data in enumerate(tr.find_all('td')):
            if data.has_key("rowspan"):
                rowspan.append((no, td_no, int(data["rowspan"]), data.get_text()))


    if rowspan:
        for i in rowspan:
            # tr value of rowspan in present in 1th place in results
            for j in xrange(1, i[2]):
                #- Add value in next tr.
                results[i[0]+j].insert(i[1], i[3])


    df = pd.DataFrame(data=results, columns=headers)
    df

    return df

scraping_wikipedia_table(url, table_no)


# In[ ]:




# In[ ]:



