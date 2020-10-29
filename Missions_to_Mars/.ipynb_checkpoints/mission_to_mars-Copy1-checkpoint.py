

#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup


# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[4]:


html = browser.html


# In[5]:


soup = BeautifulSoup(html, "html.parser")


# In[6]:


title = soup.find_all("div", class_ = "content_title")
headline = title[1]


# In[7]:


headline = headline.find("a")


# In[8]:


news_title = headline.text


# In[9]:


print(news_title)


# In[10]:


teaser = soup.find_all("div", class_ = "article_teaser_body")
teaser1 = teaser[0]


# In[11]:


news_p = teaser1.text


# In[12]:


print(news_p)


# In[13]:


url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


# In[14]:


browser.visit(url2)


# In[15]:


browser.click_link_by_id('full_image')


# In[16]:


browser.click_link_by_partial_text('more info')


# In[17]:


browser.click_link_by_partial_href('/largesize')


# In[18]:


featured_image_url = browser.url
print(featured_image_url)


# In[19]:


url3 = "https://space-facts.com/mars/"


# In[20]:


browser.visit(url3)


# In[21]:


import pandas as pd


# In[22]:


tables = pd.read_html(url3)


# In[23]:


df = tables[0]
df.head()


# In[24]:


html_table = df.to_html()
print(html_table)


# In[25]:


df.to_html('table.html')


# In[26]:


url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'


# In[27]:


browser.visit(url4)


# In[43]:


html = browser.html
soup = BeautifulSoup(html, "html.parser")

main_url = "https://astrogeology.usgs.gov"
images_url = soup.find_all("div", class_="item")

url_list = []

for image in images_url:
    hem_url = image.find('a')['href']
    url_list.append(hem_url)
    
print(url_list)


# In[54]:


html = browser.html
soup = BeautifulSoup(html, "html.parser")
hemisphere_image_urls = []
for urls in url_list:
    hem_url = main_url + urls
    
    browser.visit(hem_url)
    f_title = soup.find('h2', class_ = "title")
    f2_title = f_title.text
    title = f2_title.split(' Enchanced')[0]
    comp_url = soup.find('li').a['href']
    hemisphere_image_urls.append({'title':title, 'img_url': comp_url})


# In[55]:


print(hemisphere_image_urls)


# In[57]:


mars_info = {}
mars_info["news_title"] = news_title
mars_info["news_paragraph"] = news_p


# In[58]:


mars_info["featured_image_url"] = featured_image_url


# In[59]:


mars_info["mars_facts"] = html_table


# In[60]:


mars_info


# In[ ]:




