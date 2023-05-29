import csv
import os
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
  
# Set up the Selenium driver to scroll down the page
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
  
# Create a directory to store the downloaded images
if not os.path.exists('4chan_images'):
    os.makedirs('4chan_images')

	
# Navigate to the 4chan board
driver.get('put your 4chan board url')
	
# Parse the HTML response to extract the URLs of all the board pages
soup = BeautifulSoup(driver.page_source, 'html.parser')
post_containers = soup.find_all('div', class_='postContainer')
	
# Open a CSV file to store the image URLs
with open('4chan_image_urls.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Image URL'])
	
# Loop through each post container
for post_container in post_containers:
    # Find all the image links in the post
    file_links = post_container.find_all('a', class_='fileThumb')
	
    # Loop through each image link
    for file_link in file_links:
        image_url = file_link['href']
	
        # Save the image URL to the CSV file
        with open('4chan_image_urls.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([image_url])

		
# Close the Firefox driver
driver.quit()
