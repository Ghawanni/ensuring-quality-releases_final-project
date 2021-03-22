# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    # options = ChromeOptions()
    # options.add_argument("--headless") 
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    username_field = driver.find_element_by_id("user-name")
    password_field = driver.find_element_by_id("password")
    username_field.send_keys(user)
    password_field.send_keys(password)
    print("Logging user {} in".format(user))
    login_button = driver.find_element_by_id("login-button")
    login_button.click()
    print("login successful")

    inventory_items = driver.find_elements_by_class_name("inventory_item")
    print("getting inventory items")
    for inventory_item in inventory_items:
        item_name = inventory_item.find_element_by_class_name("inventory_item_label").find_element_by_class_name("inventory_item_name").text
        print("Got item name")
        price_bar_element = inventory_item.find_element_by_class_name("pricebar")
        print("Got the price bar")
        add_to_cart_button = price_bar_element.find_element_by_class_name("btn_inventory")
        print("Adding item...")
        add_to_cart_button.click()
        print("item {} added!".format(item_name))

    print("All items added to the cart!")
    print("-----------------------------")
    print("-----------------------------")
    print("Removing Items...")
    for inventory_item in inventory_items:
        item_name = inventory_item.find_element_by_class_name("inventory_item_label").find_element_by_class_name("inventory_item_name").text
        print("Got item name")
        price_bar_element = inventory_item.find_element_by_class_name("pricebar")
        print("Got the price bar")
        add_to_cart_button = price_bar_element.find_element_by_class_name("btn_inventory")
        print("Removing item...")
        add_to_cart_button.click()
        print("item {} removed!".format(item_name))
    
    print("The cart is now empty!")

login('standard_user', 'secret_sauce')

