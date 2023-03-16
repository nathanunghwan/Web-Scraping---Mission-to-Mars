from splinter import Browser

# Parses the HTML
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt

# For scraping with Chrome
from webdriver_manager.chrome import ChromeDriverManager


# Setup splinter
# browser = init_browser()
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)

# news_title, news_paragraph = mars_news(browser)
# img_urls_titles = hemisphere(browser)
# # Stroe results in dictionary
# data = {
#     'news_title' : news_title,
#     'news_paragraph' : news_para,
#     'featured_image' : featured_image(browser),
#     'facts' : mars_facts(),
#     'hemispheres' : img_urls_titles
# }
# browser.quit()
# print(data)

# url='https://redplanetscience.com/'
# browser.visit(url)
# browser.is_element_present_by_css('div.list_text', wait_time=1)

# # Convert the browser html to a soup object 
# html= browser.html
# news_soup= soup(html, 'html.parser')

# #Error handling(find the latest title and the paragraph text)
# try:
#     latest_news_elem=news_soup.select_one('div.list_text')
#     latest_news_title=latest_news_elem.find('div', class_='content_title').get_text()
#     news_para = latest_news_elem.find('div', class_='article_teaser_body').get_text()

# except AttributeError:
#     print(None, None)

# print(latest_news_title, news_para)


# url = 'https://spaceimages-mars.com/'
# browser.visit(url)

# # Find and click the full image button
# image_button_elem = browser.find_by_tag('button')[1]
# image_button_elem.click()

# # Convert the browser html to a soup object 
# html = browser.html
# full_img_soup = soup(html, 'html.parser')

# #Error handling(find the relative url)
# try:
#     img_url = full_img_soup.find('img', class_='fancybox-image').get('src')
# except AttributeError:
#     print(None)
# # Absolute path
# featured_img_url = f'https://spaceimages-mars.com/{img_url}'

# print(featured_img_url)

    # Vist URL and use Pandas to scrape the table containing facts  about the planet including Diameter, Mass, etc.
try:
    url = 'https://galaxyfacts-mars.com/'
    df = pd.read_html(url)[0]
except BaseException:
    print(None)
# Set ''Mars - Earth Comparison' as index 
df.set_index('Mars - Earth Comparison', inplace=True)

# Convert back to HTML format
print(df.to_html())
###"None of ['Mars - Earth Comparison'] are in the columns"


    # Visit the marshemispheres site
url = 'https://marshemispheres.com/'
browser.visit(url)

# Create a list to hold the images and titles.
hemisphere_image_urls = []
# Retrieve the image urls and titles for each hemisphere.
for i in range(4):
    # Browse through each article
    browser.links.find_by_partial_text('Hemisphere')[i].click()
    
    # Parse the HTML
    html = browser.html
    hemi_soup = soup(html,'html.parser')
    
    # Scraping
    title = hemi_soup.find('h2', class_='title').text
    img_url = hemi_soup.find('li').a.get('href')
    
    # Store findings into a dictionary and append to list
    hemispheres = {}
    hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'
    hemispheres['title'] = title
    hemisphere_image_urls.append(hemispheres)
    
    # Browse back to repeat
    browser.back()
print(hemisphere_image_urls)  
