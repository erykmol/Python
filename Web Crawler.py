
# coding: utf-8

# In[13]:

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

map_ = {} #map of the website as a dictionary
check_list = [] #list of urls already added
def site_map(url):
    check_list.append(url)
    link_set = set() #set in which links will be stored
    response = requests.get(url).text #retrives data from url 
    page_content = BeautifulSoup(response,'lxml') #parsing data through beatifulsoup
    title = page_content.title.string #retrives title from page content
    map_[url] = {"title":title}
    if(page_content.find_all("a")!=None): #checks if there are any occurences with specific tag
        for link in page_content.find_all("a"):
            new_url = link.get('href') #retrives url from page content 
            if(new_url.startswith("/")):
                new_url=urljoin(url,new_url) #joins abosule url with relative url
                if(new_url not in check_list):   
                    site_map(new_url)
                link_set.add(new_url)
            elif("clear" not in new_url):
                if(new_url not in check_list):
                    site_map(new_url)
                link_set.add(new_url)
        map_[url].update({"links":link_set})#adds key along with its value without replacing already existing keys
    return map_ 

