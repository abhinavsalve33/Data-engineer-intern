# Data-engineer-intern
assingnment
# 🚀 Hacker News Data Pipeline for Business Insights

## 📌 Problem Statement
Businesses need real-time insights into trending technologies, startups, and industry discussions. However, this data is scattered across platforms and not structured for direct use.

This project builds an automated data pipeline that collects, cleans, and serves data from Hacker News in a business-friendly format.

---

## 🌐 Data Source
- Website: https://news.ycombinator.com/
- Extracted Fields:
  - Title
  - URL
  - Points (popularity)
  - Author
  - Number of comments

---

## 🛠️ Tech Stack
- Python
- BeautifulSoup
- Requests
- Pandas
- SQLite
- FastAPI

---

## ⚙️ Pipeline Architecture

### 1. Scraper
- Handles pagination across multiple pages
- Extracts structured data
- Manages missing fields (e.g., no comments)
- Handles failures gracefully

### 2. Data Cleaning
- Converts numeric fields (points, comments)
- Removes duplicates
- Standardizes formats

### 3. Storage
- Cleaned data stored in Mysql database

### 4. Automation
- Pipeline designed to run automatically (cron)

### 5. API Layer
- Exposes cleaned data through API endpoints

---

## 📂 Project Structure
