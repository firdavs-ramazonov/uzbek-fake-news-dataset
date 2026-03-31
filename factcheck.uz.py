import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

data = []
id_counter = 1

for page in range(1, 60):  # sahifani ko‘paytirsa bo‘ladi
    url = f"https://factcheck.uz/?cat=46&paged={page}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    articles = soup.find_all("article")

    for art in articles:
        try:
            link = art.find("a")["href"]

            r = requests.get(link)
            s = BeautifulSoup(r.text, "html.parser")

            # Sarlavha
            title = s.find("h1").get_text(strip=True)

            # Matn
            content_div = s.find("div", class_="entry-content")
            content = content_div.get_text(separator="\n").strip()

            # Sana
            date_tag = s.find("time")
            date = date_tag.get_text(strip=True) if date_tag else "no_date"

            # Manba (matndan qidiramiz)
            if "Telegram" in content:
                source = "Telegram"
            elif "Facebook" in content:
                source = "Facebook"
            else:
                source = "factcheck.uz"

            data.append({
                "Id": id_counter,
                "Sarlavha": title,
                "Matn": content,
                "Sana": date,
                "Manba": source
            })

            print(f"{id_counter} - OK")

            id_counter += 1
            time.sleep(1)

        except Exception as e:
            print("Error:", e)

df = pd.DataFrame(data)

# ❗ Dublikatlarni olib tashlash
df.drop_duplicates(subset=["Sarlavha"], inplace=True)

# ❗ Bo‘shlarni olib tashlash
df.dropna(inplace=True)

# CSV
df.to_csv("factcheck_fake_news.csv", index=False, encoding="utf-8-sig")

print("Tugatildi:", len(df))