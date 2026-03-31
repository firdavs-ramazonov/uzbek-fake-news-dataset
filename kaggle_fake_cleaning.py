import pandas as pd
import re

def clean_text(text):
    if pd.isna(text):
        return ""
    
    # Eng ko'p uchraydigan encoding xatolarini to'g'rilash
    replacements = {
        'â€™': "'", 
        'â€œ': '"', 
        'â€': '"', 
        'â€”': '—', 
        'â€“': '-', 
        'Â': '', 
        'â\x80\x99': "'",
        'â\x80\x9c': '"',
        'â\x80\x9d': '"'
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    # Ortiqcha bo'shliqlarni tozalash
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# 1. CSV faylingizni yuklang (fayl nomini o'zgartiring)
file_name = "fake.csv" 
df = pd.read_csv(file_name)

# 2. Matnli ustunlarni tozalash (masalan, 'Sarlavha' va 'Matn' ustunlari)
# Ustun nomlari sizda qanday bo'lsa, shuni yozing
if 'title' in df.columns:
    df['title'] = df['title'].apply(clean_text)

if 'text' in df.columns:
    df['text'] = df['text'].apply(clean_text)

# 3. Tozalangan ma'lumotni yangi faylga saqlash
output_name = "clean_fake_dataset.csv"
df.to_csv(output_name, index=False, encoding='utf-8-sig')

print(f"Bajarildi! Tozalangan ma'lumotlar '{output_name}' fayliga saqlandi.")