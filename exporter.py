import pickle
import json

# Load cookies
with open('cookies.pkl', 'rb') as file:
    cookies = pickle.load(file)

# Load localStorage
with open('local_storage.json', 'r', encoding='utf-8') as file:
    try:
        local_storage = json.load(file)
    except Exception as e:
        print("⚠️ local_storage.json is not valid JSON:", e)
        local_storage = {}

# Load sessionStorage
with open('session_storage.json', 'r', encoding='utf-8') as file:
    try:
        session_storage = json.load(file)
    except Exception as e:
        print("⚠️ session_storage.json is not valid JSON:", e)
        session_storage = {}

# Output
print('\n' + '='*80 + '\n')

# Cookies (manual True/False/null fix)
print("    # Add cookies")
for cookie in cookies:
    fixed = json.dumps(cookie).replace("false", "False").replace("true", "True").replace("null", "None")
    print(f"    sb.add_cookie({fixed})")

# localStorage
print("\n    # Restore localStorage")
print("    sb.execute_script(\"\"\"var items = arguments[0];")
print("    for (var key in items) { window.localStorage.setItem(key, items[key]); }\"\"\",")
print(f"        {json.dumps(local_storage, indent=4)})")

# sessionStorage
print("\n    # Restore sessionStorage")
print("    sb.execute_script(\"\"\"var items = arguments[0];")
print("    for (var key in items) { window.sessionStorage.setItem(key, items[key]); }\"\"\",")
print(f"        {json.dumps(session_storage, indent=4)})")

print("\n    # Now continue with your scraping or navigation logic below...")
print("    sb.refresh()  # Optional: to ensure storage is applied")
print("="*80)
