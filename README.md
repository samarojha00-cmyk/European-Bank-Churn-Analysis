European Bank Customer Churn Analysis
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Microsoft%20Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
Project Overview
This project presents a comprehensive customer churn analysis for a European retail bank using a dataset of 10,000 customers across France, Germany, and Spain.
The goal was to identify which customer segments are most likely to churn, understand the financial impact, and provide actionable recommendations for targeted retention strategies.
---
Problem Statement
Despite having rich customer-level data, banks face challenges in:
Identifying high-risk customer segments
Understanding churn differences by geography and demographics
Quantifying the financial profile of churned customers
---
Tools Used
Tool	Purpose
Microsoft Excel	Data cleaning, derived columns, segmentation
SQL (SQLite / DB Browser)	Churn rate queries, segment analysis
Power BI Desktop	Interactive dashboard, KPI cards, charts
---
Dataset
Source: European Bank Customer Dataset — Unified Mentor Programme
Records: 10,000 customers
Countries: France, Germany, Spain
Target Variable: `Exited` (1 = Churned, 0 = Retained)
Columns
Column	Description
CustomerId	Unique customer identifier
CreditScore	Customer creditworthiness
Geography	France / Spain / Germany
Gender	Male / Female
Age	Customer age
Tenure	Years with the bank
Balance	Account balance
NumOfProducts	Number of bank products
HasCrCard	Credit card ownership
IsActiveMember	Activity indicator
EstimatedSalary	Estimated annual salary
Exited	Churn indicator (target)
---
Project Structure
```
European-Bank-Churn-Analysis/
│
├── Churn_Analysis_Cleaned.csv       # Cleaned dataset with derived columns
├── European_Bank_Customer_Churn_Analysis.pbix   # Power BI dashboard
├── Churn_Research_Paper.docx        # Full research paper
└── README.md                        # Project documentation
```
---
Key Findings
Overall Churn Rate
> **20.4%** — 2,037 out of 10,000 customers exited the bank
By Geography
Country	Churn Rate	Risk Level
Germany	~32%	High
Spain	~17%	Medium
France	~16%	Low
By Age Group
Age Group	Churn Rate	Risk Level
46 - 60	~45%	Very High
30 - 45	~18%	Medium
Under 30	~8%	Low
60+	~11%	Low
By Balance Band
Balance	Churn Rate
High Balance (>100K)	~27%
Zero Balance	~14%
Low Balance	~12%
By Engagement
Member Status	Churn Rate
Inactive Members	~27%
Active Members	~14%
By Gender
Female customers: 55.92% of churned customers
Male customers: 44.08% of churned customers
---
Power BI Dashboard
The interactive dashboard includes:
3 KPI cards: Total Customers, Total Churned, Churn Rate %
Bar chart: Churn by Country
Bar chart: Churn by Age Group
Bar chart: Churn by Balance Band
Donut chart: Churn by Gender
Donut chart: Active vs Inactive Churn
Dynamic slicers: Filter by Geography and Age Group
---
Strategic Recommendations
Germany Retention Programme — Targeted outreach for Germany's ~32% churn rate
Age 46-60 Engagement Strategy — Personalised wealth management and relationship banking
High-Value Customer Protection — Exclusive benefits for high-balance customers
Activation Campaign — Re-engage inactive members before they churn
Gender-Inclusive Products — Address the higher churn rate among female customers
---
Methodology
```
Raw Dataset
    ↓
Phase 1: Data Cleaning (Excel)
    → Remove non-analytical fields
    → Add AgeGroup, BalanceBand, CreditBand, TenureGroup columns
    ↓
Phase 2: SQL Analysis (DB Browser for SQLite)
    → 7 churn analysis queries
    → Segment-level churn rates
    ↓
Phase 3: Power BI Dashboard
    → KPI cards, bar charts, donut charts
    → Interactive slicers
    ↓
Phase 4: Research Paper
    → EDA, insights, recommendations
```
---
Author
Samr Ojha
Project Date: March 2026
Programme: Unified Mentor — Data Analyst Internship
Mentor: The European Central Bank
---
License
This project is for educational purposes as part of the Unified Mentor Data Analyst Programme.
