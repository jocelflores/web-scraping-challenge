
#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time

def init_browser():
# path to driver
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

# scraping function

def scrape():
    

    browser = init_browser()
    
    # News; Browser 1
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    
    # define object and parse w/ beautiful soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Parse through html to find most recent title and paragraph
    title = soup.find_all("div", class_ = "content_title")
    headline = title[1]
    headline = headline.find("a")
    news_title = headline.text
    teaser = soup.find_all("div", class_ = "article_teaser_body")
    teaser1 = teaser[0]
    news_p = teaser1.text
    
    #print title and paragraph
    print(f'Title: {news_title}\nText: {news_p}')
    browser.quit()

    # Second Scrape; Visit second site
    browser = init_browser()
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)

    # click through file to find the image
    browser.click_link_by_id('full_image')
    browser.click_link_by_partial_text('more info')
    browser.click_link_by_partial_href('/largesize')
    featured_image_url = browser.url
    print(featured_image_url)


    # Third Scrape; Visit third site
    browser = init_browser()
    url3 = "https://space-facts.com/mars/"
    browser.visit(url3)
    tables = pd.read_html(url3)
    
    #save table as df
    df = tables[0]
    df.head()

    # convert to html and print
    html_table = df.to_html()
    print(html_table)
    browser.quit()

    # Fourth Scrape; Visit fourth site
    browser = init_browser()
    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #set main url and find all image links
    main_url = "https://astrogeology.usgs.gov"
    images_url = soup.find_all("div", class_="item")

    # set list
    url_list = []
    
    for image in images_url:
        hem_url = image.find('a')['href']
        url_list.append(hem_url)

    print(url_list)


    # use links to visit and then find the title; Create dictionary
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    hemisphere_image_urls = []
    url_site3 = browser.find_by_css("a.product-item h3")

    for urls in range(len(url_site3)):

        browser.find_by_css("a.product-item h3").click()
        elm = browser.find_link_by_text("Sample").first
        img_url = elm['href']
        title = browser.find_by_css("h2.title").text
        hemisphere_image_urls.append({'title':title, 'img_url': img_url})
        
        browser.back()

    print(hemisphere_image_urls)
    browser.quit()

    # Create empty dictionary and add all data

    mars_info = [{
        "news_title": news_title, 
        "news_paragraph": news_p,
        "featured_image_url": featured_image_url,
        "mars_facts": html_table,
        "hemisphere_image_urls": hemisphere_image_urls
    }]

    print('complete :)')
    return mars_info




