import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_factcheck_kz_rus(limit_pages=20):
    base_url = "https://factcheck.kz/category/fejk/page/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    all_data = []
    
    print("Factcheck.kz dan ruscha feyklarni yig'ish boshlandi...")

    for page in range(1, limit_pages + 1):
        url = f"{base_url}{page}/"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200: break
                
            soup = BeautifulSoup(response.text, 'html.parser')
            
            links = []
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                if 'factcheck.kz' in href and len(href.split('/')) > 4 and '/category/' not in href:
                    if href not in links: links.append(href)
            
            for link in links:
                try:
                    inner_res = requests.get(link, headers=headers, timeout=10)
                    inner_soup = BeautifulSoup(inner_res.text, 'html.parser')
                    
                    title_ru = inner_soup.find('h1').get_text(strip=True) if inner_soup.find('h1') else "Без заголовка"
                    paragraphs = inner_soup.find_all('p')
                    text_ru = "\n".join([p.get_text(strip=True) for p in paragraphs if len(p.get_text()) > 30])
                    
                    if text_ru:
                        all_data.append({
                            "Id": len(all_data) + 1,
                            "Sarlavha_RU": title_ru,
                            "Matn_RU": text_ru,
                            "Manba": link
                        })
                        print(f"[{len(all_data)}] Yig'ildi: {title_ru[:40]}...")
                    
                    time.sleep(0.1)
                except: continue
        except: break

    df = pd.DataFrame(all_data)
    df.to_csv("factcheck_ruscha_baza.csv", index=False, encoding='utf-8-sig')
    print(f"\nTugadi! {len(all_data)} ta ruscha xabar yig'ildi.")

if __name__ == "__main__":
    scrape_factcheck_kz_rus(limit_pages=30)