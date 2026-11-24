# Task 2: Exploratory Data Analysis (EDA)

A Python statistical analysis repository examining e-commerce transaction features, distributions, correlations, and outliers using Pandas and NumPy.

## Repository Structure
```text
task2-exploratory-data-analysis/
├── data/
│   └── ecommerce_sales_cleaned.csv      # Analysis-ready dataset
├── reports/
│   └── task2_eda_summary_report.md      # Executive summary report of statistical findings (Bonus)
├── src/
│   └── task2_eda_statistics.py          # Descriptive statistics, IQR outlier detection, and business KPI script
├── .gitignore
├── requirements.txt
└── README.md
```

## Key Analytical Operations
1. **Descriptive Statistics:** Computed mean, median, standard deviation, min/max, and skewness across numerical features (`Customer_Age`, `Quantity`, `Unit_Price`, `Total_Sales`).
2. **IQR Outlier Detection:** Flagged statistical anomalies exceeding $Q3 + 1.5 \times IQR$ across pricing, order volume, and gross transaction value.
3. **Variable Relationships:** Evaluated Pearson correlation coefficients to test relationships between customer demographics and spending behavior.
4. **Business KPI Aggregation:** Ranked top product categories, regional revenue leaders, and peak monthly sales trends.
5. **Summary Reporting:** Automated generation of `reports/task2_eda_summary_report.md`.

## Quickstart
```bash
pip install -r requirements.txt
python src/task2_eda_statistics.py
```
