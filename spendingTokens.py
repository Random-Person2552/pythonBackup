from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://www.shopplaywincodes.com/#/rewards-and-sweepstakes")
button = driver.find_element_by_link_text("CLICK HERE TO SPEND 1 TOKEN TO REDEEM")
button.click()
