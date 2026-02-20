# 🧹 Sales Data Cleaning Project (Task 1)

## 📌 Project Overview

This project focuses on cleaning and preprocessing a sales transaction
dataset using Python and Pandas in VS Code. The raw dataset was cleaned
and transformed into an analysis-ready format.

## 🗂️ Dataset Used

-   File Name: sales_data.csv
-   Type: Sales Transaction Dataset
-   Format: CSV

## 🛠️ Tools & Technologies

-   Python
-   Pandas
-   VS Code

## 🔄 Data Cleaning Steps Performed

1.  Loaded the dataset using Pandas
2.  Handled missing values by removing null CustomerID records
3.  Removed duplicate rows
4.  Filtered invalid data (Quantity \> 0 and UnitPrice \> 0)
5.  Converted InvoiceDate into datetime format
6.  Created new columns:
    -   Revenue (Quantity × UnitPrice)
    -   OrderYear
    -   OrderMonth

## 📂 Project Files

-   task1_data_cleaning.py (Python script)
-   sales_data.csv (Raw dataset)
-   sales_cleaned.csv (Cleaned dataset)
-   README.md (Project documentation)

## ▶️ How to Run in VS Code

1.  Open the project folder in VS Code\
2.  Open terminal\
3.  Install required libraries: pip install pandas openpyxl\
4.  Run the script: python task1_data_cleaning.py

## ✅ Output

The script generates a cleaned dataset file: sales_cleaned.csv

## 🎓 Academic Note

This task demonstrates practical data cleaning and preprocessing skills
using Python for Data Science projects.

## 👩‍💻 Author

Yashaswini Data Science Student
