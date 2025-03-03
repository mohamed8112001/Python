from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # Open website
    driver.get("https://www.wikipedia.org")

    # Extract all links
    links = driver.find_elements(By.TAG_NAME, "a")

    print("\nExtracted Links:")
    for link in links[:10]:  # Display first 10 links
        print(link.get_attribute("href"))

finally:
    driver.quit()
