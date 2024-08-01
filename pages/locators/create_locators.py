from selenium.webdriver.common.by import By

# Locators for customer account create
first_name_loc = (By.XPATH, "//input[contains(@id, 'firstname')]")
last_name_loc = (By.XPATH, "//input[contains(@id, 'lastname')]")
email_loc = (By.XPATH, "//input[contains(@id, 'email_address')]")
password_loc = (By.XPATH, "//input[@id='password']")
confirm_password_loc = (By.XPATH, "//input[@id='password-confirmation']")
create_account_button_loc = (By.XPATH, "//button[@title='Create an Account']")

first_name_error_loc = (By.ID, "firstname-error")
last_name_error_loc = (By.ID, "lastname-error")
email_error_loc = (By.ID, "email_address-error")
password_error_loc = (By.ID, "password-error")
confirm_password_error_loc = (By.ID, "password-confirmation-error")

success_message_loc = (By.XPATH, "//div[@class='message-success success message']/div")

# Locators for collection page
sorter_select_loc = (By.ID, 'sorter')
price_loc = (By.CSS_SELECTOR, '.price')
product_name_loc = (By.CSS_SELECTOR, '.product-item-link')
eco_collection_filter_loc = (By.XPATH, "//div[@data-role='title'][contains(.,'Eco Collection')]")
yes_filter_option_loc = (By.XPATH, "//a[@href='https://magento.softwaretestingboard.com/collections/eco-friendly.html?eco_collection=1']")

# Locators for test sales
mens_deals_title_loc = (By.XPATH, "//span[contains(text(), \"Mens's Deals\")]")
gear_deals_title_loc = (By.XPATH, "//strong[@class='title']/span[text()='Gear Deals']")
shop_womens_deals_button_loc = (By.XPATH, "//span[@class='more button' and contains(text(), 'Shop Women’s Deals')]")
shop_luma_gear_button_loc = (By.XPATH, "//span[@class='more icon' and contains(text(), 'Shop Luma Gear')]")
