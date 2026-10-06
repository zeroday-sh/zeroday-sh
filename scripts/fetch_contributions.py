import json
from pathlib import Path
import requests
from bs4 import BeautifulSoup

USERNAME = "zeroday-sh"
URL = f"https://github.com/users/{USERNAME}/contributions"

res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")

days = []
for cell in soup.find_all("td", class_="ContributionCalendar-day"):
    date = cell.get("data-date")
    level = cell.get("data-level")
    if date and level is not None:
        days.append({"date": date, "level": int(level)})

Path("data").mkdir(exist_ok=True)
with open("data/contributions.json", "w") as f:
    json.dump(days, f, indent=2)

print(f"Toplam {len(days)} gunluk veri data/contributions.json dosyasina yazildi.")
