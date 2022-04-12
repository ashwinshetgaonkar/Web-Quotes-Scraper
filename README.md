# Web Quotes Scraper


<center><img src= "https://raw.githubusercontent.com/ashwinshetgaonkar/kaggle-kernel-images/main/web%20scraping.png" alt ="web scraping" style='width:600px;'></center><br>



## Context:
* Web scraping or web data extraction is data scraping used for extracting data from websites. The web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser. While web scraping can be done manually by a software user, the term typically refers to automated processes implemented using a bot or web crawler. 
* Web scraping a web page involves fetching it and extracting from it. Fetching is the downloading of a page (which a browser does when a user views a page). Therefore, web crawling is a main component of web scraping, to fetch pages for later processing. Once fetched, then extraction can take place. 
* The content of a page may be parsed, searched, reformatted, its data copied into a spreadsheet or loaded into a database. Web scrapers typically take something out of a page, to make use of it for another purpose somewhere else.
*  An example would be to find and copy names and telephone numbers, or companies and their URLs, or e-mail addresses to a list (contact scraping).


## Objective:
* My objective for doing this project was to learn and implement web scraping on static sites.
* In this I have used requests and BeautifulSoup libraries to perform the web scraping.
* The project involves extracting the names of all topics of quotes and then scraping quotes along with their author name for all topics
  previously scraped.
* Building a wep app using Streamlit that performs the above mentioned tasks.
* To see the code along with the proper documentation check out [scraping_quotes.ipynb](https://github.com/ashwinshetgaonkar/Web-Scraping-Project-1/blob/main/scraping_quotes.ipynb) file.
* Tech stack used : Python,BeautifulSoup,pandas,requests,streamlit.


## Web app working:

* The user needs to select the topic on which he/she wants to see the quotes then the application will display 10 quotes by scraping the web in real time.

* To use the web app bulit using streamlit check out [app.py](https://share.streamlit.io/ashwinshetgaonkar/web-scraping-project-1/main/app.py).


