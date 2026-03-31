# Uzbek Fake News Dataset

## Project Overview
This repository contains a specialized dataset of **3,000 news items** curated for the purpose of training Machine Learning models to detect "Fake News" in the Uzbek language. This project was developed as part of a 6-week technical internship (120 hours).

## Dataset Composition
The dataset consists of **3,000 unique records** sourced from various platforms to ensure diversity and reliability:
* **Factcheck.uz (71 items):** Real/Verified news scraped using BeautifulSoup.
* **Factcheck.kz (58 items):** Translated Kazakh/Russian fact-check data.
* **Kaggle (2,440 items):** International fake news data translated from English to Uzbek.
* **Telegram (272 items):** Local social media news, transliterated from Cyrillic to Latin.
* **ChatGPT (159 items):** Synthetic data generated for specific misinformation categories.

## Repository Contents
* `factcheck.uz.py and factcheck.kz.py`: Python script used for web scraping (BeautifulSoup).
* `telegram_processing.py`: Script for Telegram data extraction and Cyrillic-to-Latin transliteration.
* `final_dataset_3000.csv`: The finalized dataset containing ID, Title, Text, Date, and Source.

## Technical Skills Applied
* **Web Scraping:** BeautifulSoup & Requests.
* **Data Engineering:** Pandas for cleaning and deduplication.
* **API Integration:** Telethon (Telegram API) and Google Translate API.
* **Scripting:** Python-based transliteration logic.

## Usage
This dataset is intended for Academic Research and Natural Language Processing (NLP) tasks specifically targeting the Uzbek language ecosystem.
