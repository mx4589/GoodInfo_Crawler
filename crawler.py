from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from fake_useragent import UserAgent

def main():
    stock_ids = ["0052", "00851", "1504", "00903", "1234"]
    url_prefix = "https://goodinfo.tw/tw/StockDetail.asp?STOCK_ID="
    option = Options()
    ua = UserAgent()
    user_agent = ua.random
    option.add_argument(f'user-agent={user_agent}')
    option.add_argument("--headless=new")
    driver = webdriver.Edge(options = option)
    
 
    for i in range(len(stock_ids)):
        driver.get(url_prefix + stock_ids[i])
        
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME,"table"))
            )
        finally:
                print("Web Load Success")

        res = driver.page_source

        soup = BeautifulSoup(res,"html.parser")
        
        soup.prettify()
        
        
        
        close_price = soup.select_one(
            "body > table > tbody > tr:nth-child(2) > td:nth-child(3) > table > tbody > tr:nth-child(2) > td > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(1)"
            ).text

        open_price = soup.select_one(
            "body > table > tbody > tr:nth-child(2) > td:nth-child(3) > table > tbody > tr:nth-child(2) > td > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(6)"
        ).text
        
        high_price = soup.select_one(
            "body > table > tbody > tr:nth-child(2) > td:nth-child(3) > table > tbody > tr:nth-child(2) > td > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(7)"
        ).text
        
        low_price = soup.select_one(
            "body > table > tbody > tr:nth-child(2) > td:nth-child(3) > table > tbody > tr:nth-child(2) > td > div > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(8)"
        ).text

        
        print(close_price,open_price,high_price,low_price)
    driver.close()
    
if __name__ == '__main__':
    main()