from selenium import webdriver
import time

chrome_driver_path = "D:/Users/navee/Documents/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 300

while True:
    cookie.click()
    
    if(time.time() > timeout):
        
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []
        
        for price in all_prices:
            element_text = price.text
            
            if element_text != "":
                cost = int(element_text.split('-')[1].strip().replace(',',""))
                item_prices.append((cost))
        
        cookie_upgrades = {}
        
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
        
        money = driver.find_element_by_xpath('//*[@id="money"]').text
        if "," in money:
            money = money.replace(",","")    
        cookies = int(money)

        affordable_upgrades = {}
        
        for cost,id in cookie_upgrades.items():
            if cost < cookies:
                affordable_upgrades[cost] = id
        
        highest_affordable = max(affordable_upgrades)
        print(f"Buying {affordable_upgrades[highest_affordable]} for {highest_affordable} cookies")
        final_id = affordable_upgrades[highest_affordable]
        
        buy = driver.find_element_by_id(final_id)
        buy.click()
        
        timeout = time.time() + 2
        
        if(time.time() > five_min):
            cps = driver.find_element_by_id("cps").text
            print(cps)
            break

driver.quit()
        
