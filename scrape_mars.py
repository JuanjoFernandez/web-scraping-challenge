def scrape():

    # Dependencies and libraries
    import requests
    import pandas as pd

    from bs4 import BeautifulSoup
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # # Scrapping redplanet science
    url = 'https://redplanetscience.com'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

    # Looking at the browser inspector this line contains the title:
    # <div class="content_title">NASA's Mars 2020 Heads Into the Test Chamber</div>
    # And this line contains the teaser of the article
    # <div class="article_teaser_body">In this time-...</div>

    # Saving the results
    title = soup.find('div', class_='content_title').text
    teaser = soup.find('div', class_='article_teaser_body').text

    # # Scrapping spaceimages-mars.com
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    browser.links.find_by_partial_text('FULL').click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

    # Full size image is at
    # <img class="fancybox-image" src="image/featured/mars2.jpg" alt="">
    image = soup.find('img', class_='fancybox-image')

    # Building the full link
    image_link = 'https://spaceimages-mars.com/' + (image['src'])

    # Scrapping Mars facts
    url = 'https://galaxyfacts-mars.com/'  

    tables = pd.read_html(url, skiprows=1)
    mars_facts = tables[0]

    # Dropping columns, renaming and indexing
    mars_facts = mars_facts.drop(columns=[2])
    mars_facts = mars_facts.rename(columns={0: 'Fact', 1: 'Information'})

    #Saving to html table
    facts_table = mars_facts.to_html(index = False)

    #Replacing the \n
    facts_table = facts_table.replace('\n', '')
    facts_table


    # # Scrapping mars hemispheres
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # Hemisphere list
    hemi_list = ['Cerberus', 'Schiaparelli', 'Syrtis', 'Valles']

    # For loop to iterate through all the hemisphere's pages

    # List to store results
    hemi_img = []

    for _ in hemi_list:

        # Clicking the corresponding link
        browser.links.find_by_partial_text(_).click()
        html = browser.html
        
        # Scrapping the hemisphere page
        soup = BeautifulSoup(html, 'html.parser')
        img_url = soup.find('div', class_='downloads')
        links_list = []
        
        # Retrieving image link
        for link in img_url.ul.find_all('a'):
            links_list.append(link.get('href'))
        img_link = 'https://marshemispheres.com/' + links_list[0]
        
        # Retrieving and formatting title
        title = soup.find('h2', class_='title').get_text()
        title = title.replace(' Enhanced', '')

        # Saving the results as a dictionary and appending to list
        res_dict = {'title': title, 'img_url': img_link}
        hemi_img.append(res_dict)
        
        # Resetting for next iteration
        browser.links.find_by_partial_text('Back').click()    
        
    browser.quit()


    # # Creating the final dictionary to return

    scrapped_data = {
        'latest_news': title,
        'teaser': teaser,
        'featured_image': image_link,
        'mars_facts': facts_table,
        'hemisphere_images': hemi_img
    }

    return scrapped_data
