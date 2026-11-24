# Exploratory Data Analysis (EDA) Summary Report

## 1. Executive Overview
- **Total Clean Transactions:** 1,000
- **Total Gross Revenue:** $684,447.73
- **Average Order Value (AOV):** $684.45 (Median: $545.30)

## 2. Key Business Answers
- **Top Performing Category:** `Beauty` generated **$228,858.09** across 338 orders.
- **Top Performing Region:** `North` led regional revenue with **$196,035.15**.
- **Peak Sales Month:** `2025-01` recorded the highest monthly revenue (**$64,057.68**).
- **Age vs. Spending Correlation:** Pearson $r = 0.045$, indicating purchasing power is consistent across adult age brackets rather than skewed toward one age group.

## 3. Data Anomalies & Outliers
- **Unit Price Outliers:** 1 transactions exceeded the IQR upper fence.
- **Quantity Outliers:** 1 transactions exceeded the IQR upper fence.
- **Total Sales Outliers:** 14 transactions exceeded the IQR upper fence, driven primarily by bulk quantity orders (max quantity: 50) and high-ticket items (max unit price: $4,999.99).
