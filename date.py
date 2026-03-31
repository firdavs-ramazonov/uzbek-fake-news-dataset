import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

dates_data = []
id_counter = 1

for page in range(1, 60):
    url = f"https://factcheck.uz/?cat=46&paged={page}"
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")
        articles = soup.find_all("article")

        if not articles: # Agar sahifada maqola qolmagan bo'lsa to'xtaydi
            break

        for art in articles:
            try:
                link = art.find("a")["href"]
                r = requests.get(link, timeout=10)
                s = BeautifulSoup(r.text, "html.parser")

                # Sanani topishning eng ishonchli usullari:
                # 1. Meta tegdan (eng aniqi)
                date_tag = s.find("meta", property="article:published_time")
                if date_tag:
                    date = date_tag["content"].split("T")[0]
                else:
                    # 2. Agar meta bo'lmasa, time tegidan
                    time_tag = s.find("time", class_="entry-date") or s.find("time")
                    date = time_tag.get_text(strip=True) if time_tag else "no_date"

                dates_data.append({
                    "Id": id_counter,
                    "Sana": date
                })

                print(f"{id_counter} - Sana olindi: {date}")
                id_counter += 1
                time.sleep(0.5) # Tezlikni biroz oshirdik

            except Exception as e:
                print(f"Maqolada xato: {e}")

    except Exception as e:
        print(f"Sahifada xato: {e}")

# CSV ga saqlash
df_dates = pd.DataFrame(dates_data)
df_dates.to_csv("factcheck_dates.csv", index=False, encoding="utf-8-sig")

print(f"\nJarayon tugadi. Jami {len(df_dates)} ta sana saqlandi.")