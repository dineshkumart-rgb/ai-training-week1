import csv
import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("API_KEY")
if api_key:
    print("API_KEY loaded")

with open("employees.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    cols = reader.fieldnames
    rows = list(reader)

high = [r for r in rows if int(r["salary"]) > 50000]

with open("employees.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, indent=4)

with open("high_earners.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(high)

print(f"Rows read: {len(rows)} | High earners: {len(high)}")

url = "https://jsonplaceholder.typicode.com/users"
parsed_users = []

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    users_data = response.json()

    for user in users_data[:3]:
        print(f"{user.get('id')} - {user.get('name')} - {user.get('email')}")

    for user in users_data:
        address = user.get("address") or {}
        geo = address.get("geo") or {}
        company = user.get("company") or {}
        parsed_users.append({
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": address.get("city"),
            "lat": geo.get("lat"),
            "lng": geo.get("lng"),
            "company_name": company.get("name"),
        })

    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(parsed_users, f, indent=4)

except requests.exceptions.Timeout:
    print("Error: request timed out")
except requests.exceptions.ConnectionError:
    print("Error: Unable to connect")
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)

try:
    res_404 = requests.get("https://jsonplaceholder.typicode.com/users/9999", timeout=5)
    if res_404.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        res_404.raise_for_status()
except requests.exceptions.Timeout:
    print("Error: request timed out")
except requests.exceptions.ConnectionError:
    print("Error: Unable to connect")
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)