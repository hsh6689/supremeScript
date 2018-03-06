## Supreme Script.py Version 0.2 by Seonghyun Hong and Shawn Hoang Le ## 

# Definitions:

# Time needed for delay to treat the bot
import time

# We need to use selenium as api for automatation with JS components
from selenium import webdriver as wb
from selenium.common.exceptions import NoSuchElementException

# Opens up google Chrome
# NOTE: You will need to install google chrome driver 
driver = wb.Chrome()

# We start at the shop/all page this time
driver.get("http://www.supremenewyork.com/shop/all")

##### FIRST ITEM #######
item1 = None
##copy and past the item code
link1 = "//img[@ alt='Imq28ur tw8']"

while not item1:
	try:
		item1 = driver.find_element_by_xpath(link1)
	except NoSuchElementException:
		driver.refresh()

#Try to get the href link by "alt"
item1.click()


##### IF YOU ADD MORE ITEMS, ADD A time.sleep(0.3) ######

#########################################################

# Checkout, able to run this script before the 
elem1 = None

while not elem1:
	try:
		elem1 = driver.find_element_by_name('commit')
	except NoSuchElementException:
		driver.refresh()

elem1.click()

driver.get("http://www.supremenewyork.com/checkout")

name_field = driver.find_element_by_id("order_billing_name")
# Replace 'name' with your name
name_field.send_keys('name')

email_field = driver.find_element_by_id("order_email")
# replace 'email' with your email
email_field.send_keys('email')
# replace with your phone number
tel_field = driver.find_element_by_id("order_tel")
tel_field.send_keys('000 000 0000')

address_field = driver.find_element_by_name("order[billing_address]")
# Replace with your billing address1
address_field.send_keys('address1')
# Replae with your billing address2
apt_field = driver.find_element_by_name("order[billing_address_2]")
apt_field.send_keys('address2')

zip_field = driver.find_element_by_id("order_billing_zip")
# Replace with your zip code
zip_field.send_keys("zipcode")

# State
area_field = driver.find_element_by_id("order_billing_state")
for option in area_field.find_elements_by_tag_name('option'):
	    # Replace with your state code
		if option.text == 'NA':
				option.click()
				break

card_field = driver.find_element_by_id("nnaerb")
#Replace with your card number
card_field.send_keys("0000 0000 0000 0000")

month_field = driver.find_element_by_id("credit_card_month")
for option in month_field.find_elements_by_tag_name('option'):
	# Replace with expiration month of your card
	if option.text == 'month':
		option.click()
		break

year_field = driver.find_element_by_id("credit_card_year")
for option in year_field.find_elements_by_tag_name('option'):
	# Replace with expiration year of your card
	if option.text == 'year':
		option.click()
		break

cvv_field = driver.find_element_by_id("orcer")
# Replace with CVV of your card
cvv_field.send_keys("050")

### TO DO: Check Mark ###
#terms_field = driver.find_element_by_name("order[terms]")
#terms_field.click()


time.sleep(4)

process_field = driver.find_element_by_name("commit")
process_field.click()
