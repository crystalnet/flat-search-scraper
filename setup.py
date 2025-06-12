from seleniumbase import SB
import pickle
import time

with SB(uc=True) as sb:
    sb.open("https://www.immobilienscout24.de/Suche/de/baden-wuerttemberg/stuttgart/degerloch/degerloch/wohnung-mit-balkon-mieten?pricetype=rentpermonth&enteredFrom=result_list")

    time.sleep(30)
    cookies = sb.get_cookies()
    with open('cookies.pkl', 'wb') as file:
        pickle.dump(cookies, file)

    local_storage = sb.execute_script("return JSON.stringify(window.localStorage);")
    with open('local_storage.json', 'w', encoding='utf-8') as file:  
        file.write(local_storage)

    session_storage = sb.execute_script("return JSON.stringify(window.sessionStorage);")
    with open('session_storage.json', 'w', encoding='utf-8') as file:  
        file.write(session_storage)