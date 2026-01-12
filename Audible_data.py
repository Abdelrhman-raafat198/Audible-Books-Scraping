#  importing {selenium,  pandas $ time} Libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time


title_list=[]
authors_list=[]
runtime_list=[]
rating_list=[]
price_list=[]


#creating a module from the Options class and enabling Headless mode
chrome_options=Options() 
# chrome_options.add_argument("--headless=new")
# chrome_options.add_argument("--window-size=1920,1080")
# chrome_options.add_argument("--disable-gpu")

#Creating chrome driver to be used with selenium
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=chrome_options))

#Geting "audible books" website link and open it with the driver
website="https://www.audible.com/search"
driver.get(website)
driver.maximize_window()
time.sleep(5)



#pagination
pages=driver.find_elements(By.XPATH,'//ul[contains(@class,"pagingElements ")]/li')
last_page=int(pages[-2].text)
current_page=1

while current_page <= last_page:
    time.sleep(5)
    
    # using try and except to avoid code damage during running 
    try:
        #Starting scraping the tables data
        container=driver.find_element(By.CLASS_NAME, "adbl-impression-container")
        boxes=container.find_elements(By.XPATH,'.//li[contains(@class,"productListItem")]')
        for box in boxes:
            title_list.append(box.find_element(By.XPATH,'.//h3[contains(@class,"bc-heading")]//a').get_attribute("innerText"))
            authors_list.append(box.find_element(By.XPATH,'.//li[contains(@class,"authorLabel")]').text)
            runtime_list.append(box.find_element(By.XPATH,'.//li[contains(@class,"runtimeLabel")]').text)
            rating_list.append(box.find_element(By.XPATH,'.//li[contains(@class,"ratingsLabel")]').text)
            price_list.append(box.find_element(By.XPATH,'.//p[contains(@class,"buybox-regular-price")]').text)

    
    except:
        print(f"there is a problem in page {(current_page-1)}")

    try:
        if current_page<last_page:
            next_page=driver.find_element(By.XPATH,'.//span[contains(@class,"nextButton")]')
            next_page.click()
        else:
            print(f"Data Extracted Successfully for the {current_page} pages")
            break
    except:
        
        print(f"there is a problem in navigation to the next page{current_page}")
        break # stop the code
    print(current_page)# just for tracking
    current_page+=1
    
    
#Converting collected data into a dataframe and then save it in Excel sheet
df=pd.DataFrame({"Titles":title_list,"Authors":authors_list,"Runtime":runtime_list,"Rating":rating_list,"Price":price_list})
df.to_excel(r"C:\Users\hp\Desktop\Python_Web_Scraping\projects\Audible_scraping_project\Audible_Books.xlsx", index=False)

driver.quit()