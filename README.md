# Web Scraping Mission to Mars
I build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 


## Step 1 - Scraping
***
Complete my initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

**NASA Mars News**
Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that I can reference later.

**JPL Mars Space Images - Featured Image**

*Visit the url for the Featured Space Image site.<br/>

*Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.<br/>

*I found the image url to the full size .jpg image.<br/>

*Saved a complete url string for this image.

**Mars Facts**

*Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.<br/>

*Use Pandas to convert the data to a HTML table string.<br/>

**Mars Hemispheres**

*Visit the astrogeology site here to obtain high resolution images for each of Mar's hemispheres.<br/>

*Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.<br/>

*Append the dictionary with the image url string and the hemisphere title to a list.<br/>
<br/>

## Step 2 - MongoDB and Flask Application
***

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

<img
  src="Mission_to_Mars/Image/Displaying Application.png"
  width="550"
  height="600"
/>
