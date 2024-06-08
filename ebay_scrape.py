from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from msedge.selenium_tools import Edge, EdgeOptions
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time
import csv

#----------------------------------------------------------------------------------------------------------------
edge_options = EdgeOptions()
edge_driver_path= "C:/Users/RITIKA VERMA/Desktop/webdriver/msedgedriver.exe"
edge_driver = webdriver.Edge(executable_path=edge_driver_path)

#-----------------------------------------------------------------------------------------------------------------
def ebay_data_scrape(item_to_scrape):

    #getting the ebay home page
    edge_driver.get("https://www.ebay.com/")

    #getting the keyword 
    key_word = WebDriverWait(edge_driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@class= "gh-tb ui-autocomplete-input"]'))
            )
    key_word.send_keys(item_to_scrape)

    #click on the search button
    search_button = WebDriverWait(edge_driver, 10).until(
        EC.element_to_be_clickable((By.ID, "gh-btn"))
    )
    search_button.click()
    print("Clicked on the search button.")

    #finding out the elements to scrape with the respective product link
    list_links =[]
    products = edge_driver.find_elements(By.XPATH, '//div[@class= "s-item__info clearfix"]/a')
    for product in products:
        list_links.append(product.get_attribute("href"))

    return(list_links)
#------------------------------------------------------------------------------------------------------------------

list_links = ebay_data_scrape("Phone")
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
product_data=[]
#Traversing each page one by one through links
for link in list_links:
    edge_driver.get(link)
    time.sleep(5)
    try:
        product_dict={}
        category=[]
        detail=[]
        features_dict = {}

        prod_name = edge_driver.find_element(By.XPATH, '//div[@class= "vim x-item-title"]/h1/span').text
        
        prod_price = edge_driver.find_element(By.XPATH, '//div[@class="x-price-primary"]/span').text
        
        item_num = edge_driver.find_element(By.XPATH, '//div[@class="ux-layout-section__textual-display ux-layout-section__textual-display--itemId"]/span[@class ="ux-textspans ux-textspans--BOLD"]').text
        
        item_specifications_category = edge_driver.find_elements(By.XPATH,'//div[@class="ux-layout-section-evo__row"]/div/dl/dt/div/div/span')
        for item_category in item_specifications_category:
            category.append(item_category.text)

        item_specifications_detail = edge_driver.find_elements(By.XPATH,'//div[@class="ux-layout-section-evo__row"]/div/dl/dd/div/div/span')
        for item_detail in item_specifications_detail:
            detail.append(item_detail.text)

        features_dict = {key: value for key, value in zip(category, detail)}
    except:
        prod_name=''
        prod_price=''
        item_num=''
        features_dict =''

    product_dict["Product Name"] = prod_name
    product_dict["Product Price"] = prod_price
    product_dict["Product ID"]= item_num
    product_dict["Product specifications"]= features_dict

    product_data.append(product_dict)
    
#----------------------------------------------------------------------------------------------------------------------------
#Storing into the CSV file
with open("product_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=product_data[0].keys())
    writer.writeheader()
    for product in product_data:
        writer.writerow(product)

print("Data written to CSV file successfully!")
#----------------------------------------------------------------------------------------------------------------------------








 
