# web-scraping-challenge

# Project Overview

By using beautiful soup, splinter, flask and MongoDB I scrap different webpages in order to build an application that displays relevant information about NASA mission to mars

# Application Overview

1. I start by scrapping [redplanetscience](https://redplanetscience.com/) in order to get the latest news from the mission to Mars
    - Initial scrap returns only empty results. The page only loads the news content with an onclick event, will use splinter to overcome this
2. Next, the app retrieves the featured image from Mars from [SpaceImages](https://spaceimages-mars.com/)
# Repository Structure
3. Now we retrieve some general facts about Mars from [MarsFacts](https://galaxyfacts-mars.com/)

