# 🛠️ REST API to MySQL ETL

This project implements an **ETL pipeline in Python** that extracts data from a **REST API**, transforms it, and loads it into a **MySQL database**. 🚀  

The goal is to practice **end-to-end Data Engineering**: API consumption, data transformation, database integration, and logging for monitoring.

---

## 📖 Project Overview

This project focuses on automating the flow of data from external APIs into a structured MySQL database, making it ready for analysis or reporting.

**Key Highlights:**

- **API Integration:** Fetching data from REST endpoints.  
- **Data Transformation:** Cleaning, standardizing, and enriching data.  
- **Database Loading:** Inserting or updating records in MySQL.  
- **Logging & Monitoring:** Track pipeline execution and errors.  
- **Environment Management:** Keep sensitive credentials secure with `.env`.

---

## ⚙️ ETL Process

The pipeline is modular and consists of three main stages:

### 1️⃣ Extract — Fetch Data from API
> Pulls JSON data from REST API endpoints and prepares it for processing.

- Full extraction of available records  
- Handles API authentication and headers  
- Converts JSON responses into Python dictionaries or DataFrames  

---

### 2️⃣ Transform — Prepare Data
> Cleans, standardizes, and enriches the raw data for quality and consistency.

- Remove duplicates and invalid entries  
- Handle missing or null values  
- Convert types and normalize fields  
- Add derived columns or calculated metrics  

---

### 3️⃣ Load — Insert into MySQL
> Loads the transformed data into MySQL tables.

- Connects securely using environment variables (`.env`)  
- Supports full refresh or incremental updates  
- Logs insertions, updates, and any errors

---

## ✨ Features

- Extract data from a **REST API** using HTTP requests.  
- Transform data into the proper format (cleaning, normalization, type conversion).  
- Load data into a **MySQL database**, creating or updating tables.  
- Use **environment variables** to secure sensitive credentials.  
- Detailed logging for monitoring ETL execution.  
---

## 🛠️ Technologies Used
- [![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)  
- [![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)](https://www.mysql.com/)  
- **Pandas** – data manipulation  
- **Requests** – API consumption  
- **SQLAlchemy / mysql-connector-python** – MySQL integration  
- **python-dotenv** – manage environment variables  

---

## 📝 Logging & Monitoring

The pipeline includes **detailed logging** to:

- Track API requests and responses
- Log data transformation steps
- Record successful inserts or updates in MySQL
- Capture and report errors

Logs help ensure **reliability** and simplify **debugging**.

---

## 🧠 Inspiration

This project was inspired by **real-world ETL and API integration workflows**, combining **Python, REST APIs, and MySQL** to simulate an **end-to-end data engineering process**.
