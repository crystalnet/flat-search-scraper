from selenium.webdriver.common.by import By
from seleniumbase import SB
import pickle
import time
import csv
import json

with SB(uc=False) as sb:
    sb.open("https://www.immobilienscout24.de")

    with open('cookies.pkl', 'rb') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            sb.add_cookie(cookie)

    with open('local_storage.json', 'r', encoding='utf-8') as file:
        local_storage = file.read()
        sb.execute_script(f"var items = JSON.parse(arguments[0]); for (var key in items) {{ window.localStorage.setItem(key, items[key]); }}", local_storage)

    with open('session_storage.json', 'r', encoding='utf-8') as file:
        session_storage = file.read()
        sb.execute_script(f"var items = JSON.parse(arguments[0]); for (var key in items) {{ window.sessionStorage.setItem(key, items[key]); }}", session_storage)

    sb.open("https://www.immobilienscout24.de/Suche/de/baden-wuerttemberg/stuttgart/degerloch/degerloch/wohnung-mit-balkon-mieten?pricetype=rentpermonth&enteredFrom=result_list")

    time.sleep(120)
    properties = sb.find_elements(By.CSS_SELECTOR, ".grid-item.result-list-entry__data-container")

    for property in properties:
            title = property.find_element(By.CSS_SELECTOR, ".result-list-entry__brand-title").text.strip()
            price = property.find_element(By.CSS_SELECTOR, "dl.result-list-entry__primary-criterion dd").text.strip()
            area = property.find_elements(By.CSS_SELECTOR, "dl.result-list-entry__primary-criterion dd")[1].text.strip()
            rooms = property.find_elements(By.CSS_SELECTOR, "dl.result-list-entry__primary-criterion dd")[2].text.strip()
            location = property.find_element(By.CSS_SELECTOR, ".result-list-entry__address").text.strip()

            print(f"Title: {title}")
            print(f"Price: {price}")
            print(f"Area: {area}")
            print(f"Rooms: {rooms}")
            print(f"Location: {location}")
            print("-" * 50)