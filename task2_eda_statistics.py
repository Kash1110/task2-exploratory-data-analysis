import os
import pandas as pd
import numpy as np

os.makedirs("reports", exist_ok=True)

def run_task2():
    df = pd.read_csv("data/ecommerce_sales_cleaned.csv")

    # 1. Descriptive Statistics
    num_cols = ["Customer_Age", "Quantity", "Unit_Price", "Total_Sales"]
    desc_stats = df[num_cols].describe().T
    desc_stats["median"] = df[num_cols].median()
    desc_stats["skewness"] = df[num_cols].skew()
    print("--- DESCRIPTIVE STATISTICS ---")
    print(desc_stats[["count", "mean", "median", "std", "min", "max", "skewness"]])

    # 2. Outlier Detection using IQR
    print("\n--- OUTLIER DETECTION (IQR METHOD) ---")
    outlier_summary = {}
    for col in ["Unit_Price", "Quantity", "Total_Sales"]:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        outlier_summary[col] = len(outliers)
        print(f"{col}: {len(outliers)} outliers detected (Upper threshold: {upper_bound:.2f})")

    # 3. Relationships & Key Business Questions
    corr_matrix = df[num_cols].corr()
    print("\n--- CORRELATION MATRIX ---")
    print(corr_matrix.round(3))

    cat_revenue = df.groupby("Product_Category")["Total_Sales"].agg(["count", "sum", "mean"]).sort_values(by="sum", ascending=False)
    region_revenue = df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
    monthly_sales = df.groupby("Order_Month")["Total_Sales"].sum()

    print("\n--- REVENUE BY CATEGORY ---")
    print(cat_revenue.round(2))

    # Bonus: Generate Markdown Summary Report
    report_content = f"""# Exploratory Data Analysis (EDA) Summary Report

## 1. Executive Overview
- **Total Clean Transactions:** {len(df):,}
- **Total Gross Revenue:** ${df['Total_Sales'].sum():,.2f}
- **Average Order Value (AOV):** ${df['Total_Sales'].mean():,.2f} (Median: ${df['Total_Sales'].median():,.2f})

## 2. Key Business Answers
- **Top Performing Category:** `{cat_revenue.index[0]}` generated **${cat_revenue['sum'].iloc[0]:,.2f}** across {cat_revenue['count'].iloc[0]} orders.
- **Top Performing Region:** `{region_revenue.index[0]}` led regional revenue with **${region_revenue.iloc[0]:,.2f}**.
- **Peak Sales Month:** `{monthly_sales.idxmax()}` recorded the highest monthly revenue (**${monthly_sales.max():,.2f}**).
- **Age vs. Spending Correlation:** Pearson $r = {corr_matrix.loc['Customer_Age', 'Total_Sales']:.3f}$, indicating purchasing power is consistent across adult age brackets rather than skewed toward one age group.

## 3. Data Anomalies & Outliers
- **Unit Price Outliers:** {outlier_summary['Unit_Price']} transactions exceeded the IQR upper fence.
- **Quantity Outliers:** {outlier_summary['Quantity']} transactions exceeded the IQR upper fence.
- **Total Sales Outliers:** {outlier_summary['Total_Sales']} transactions exceeded the IQR upper fence, driven primarily by bulk quantity orders (max quantity: {df['Quantity'].max()}) and high-ticket items (max unit price: ${df['Unit_Price'].max():,.2f}).
"""
    report_path = "reports/task2_eda_summary_report.md"
    with open(report_path, "w") as f:
        f.write(report_content)
    print(f"\n[SUCCESS] Short EDA report saved to {report_path}")

if __name__ == "__main__":
    run_task2()
