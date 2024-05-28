import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL: str = ("https://yandex.ru/maps/14/tver/chain/pyatyorochka/6003206/"
            "?ll=35.903639%2C56.859151&sll=35.903639%2C56.859131&z=13")

options = webdriver.ChromeOptions()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                     "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
options.add_argument("headless")
driver = webdriver.Chrome(options=options)
driver.get(URL)

time.sleep(2)
while True:
    last_element = driver.find_elements(By.CLASS_NAME, "search-snippet-view")[-1]
    time.sleep(1)
    last_element.location_once_scrolled_into_view
    try:
        li_elements = driver.find_elements(By.CLASS_NAME, "search-snippet-view")
        driver.find_element(By.CLASS_NAME, "add-business-view__link")
        break
    except Exception as e:
        continue

result: list = []

for li in li_elements:
    result.append(li.text.strip())

driver.quit()

five: list = []
for item in result:
    five.append(item.split("\n"))

with open('fives.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file,
    fieldnames=['Название', 'Рейтинг', 'Время работы', 'Адрес'])
    writer.writeheader()
    for row in five:
        writer.writerow(rowdict={'Название': row[0], 'Рейтинг': row[3], 'Время работы': row[6], 'Адрес': row[7]})
