import time
from selenium import webdriver

# Number of random Wikipedia URLs you want
num_urls = 1000

# Initialize the Selenium WebDriver (you'll need to install Selenium)
driver = webdriver.Chrome()  # You should have Chrome WebDriver installed

# Loop to open random Wikipedia pages and extract URLs
for i in range(num_urls):
    # Get a random Wikipedia URL
    url = "https://en.wikipedia.org/wiki/Special:Random"
    
    # Open the URL
    driver.get(url)
    
    # Wait for the page to load (adjust the sleep duration as needed)
    time.sleep(2)
    
    # Extract the current URL (the URL after redirection)
    current_url = driver.current_url
    
    # Print the current URL to the console
    print(current_url)

# Close the Selenium WebDriver when done
driver.quit()