from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Firefox()

driver.get('https://www.academy.com/p/nike-womens-court-legacy-next-nature-shoes')

# element = driver.find_element(By.CSS_SELECTOR, 'span.productTitle--FWmyK')
element = driver.find_element(By.CSS_SELECTOR, "#pdp240TitleWrapper > h1")
product_name = element.text
product_name_element = driver.find_element(By.CSS_SELECTOR, 'span[data-auid="PDP_ProductName"]')
print(product_name)

price_string = driver.find_element(By.CSS_SELECTOR, '.pricing').text
price = float(price_string.replace('$', ''))
print(price)

selected_color = driver.find_element(By.CSS_SELECTOR, 'span.swatchName--KWu4Q').text
print(selected_color)


reviews_count = driver.find_element(By.CSS_SELECTOR, '.ratingCount').text
reviews_count = int(reviews_count.replace('(', '').replace(')', ''))
print(reviews_count)

reviews_score = driver.find_element(By.CSS_SELECTOR, '.ratingAvg').text
reviews_score = float(reviews_score)
print(reviews_score)


buttons = driver.find_elements(By.CSS_SELECTOR, "#swatch-drawer-content > button")
colors = []
for button in buttons:
    aria_label = button.get_attribute('aria-label').strip()
    # Split the aria-label by newline and take the first part
    color_text = aria_label.split('\n')[0].strip()
    colors.append(color_text)
print(colors)


product_data = {
    "name": product_name,
    "price": price,
    "colour": selected_color,
    "availableColours": colors,
    "reviews_count": reviews_count,
    "reviews_score": reviews_score
}

product_json = json.dumps(product_data)
print(product_json)
with open('product_data.json', 'w') as json_file:
    json.dump(product_data, json_file, indent=4)


driver.quit()
