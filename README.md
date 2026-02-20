
# ⚡ India State-Wise Energy Consumption Analysis  
### End-to-End Data Pipeline & Power BI Dashboard

This project is a complete **data pipeline and analytics workflow** analyzing state-wise energy generation capacity across India.

The objective was to source, clean, merge, visualize, and analyze real-world datasets, culminating in an interactive Power BI dashboard and a correlation-based predictive insight.

---

## 🎯 Project Objective

This project aims to:

- Analyze installed energy capacity across Indian states
- Compare renewable vs non-renewable energy share
- Identify top energy-generating states
- Explore correlation between state income and energy generation

---

## 🛠️ Tech Stack

**Data Sourcing**
- Kaggle
- data.gov.in  

**Data Cleaning & Preparation**
- Microsoft Excel (VLOOKUP, Pivot Tables, Formulas)
- Python (Pandas)

**Data Visualization**
- Power BI (DAX, Measures, KPIs, Map, Gauge, Bar Charts, Slicers)

**Data Analysis**
- Python (Matplotlib, Seaborn)
- Excel (CORREL function)

---

## ⚙️ End-to-End Data Pipeline

### 1️⃣ Data Sourcing

- **Energy Dataset:** `Energy_India_2024.csv`
  - State-wise installed capacity for:
    - Coal
    - Gas
    - Nuclear
    - Hydel
    - Renewable

- **Income Dataset:** `perCapitaIncome.csv`
  - State-wise per capita income

---

### 2️⃣ Data Cleaning & Preparation (Excel + Python)

**Energy Dataset**
- Renamed columns for clarity
- Converted "-" values to 0 using Find & Replace
- Checked duplicates using Pivot Tables

**Income Dataset**
- Filtered to most recent year (2012)
- Saved as `cleaned_income.xlsx`

**Data Integration**
- Combined datasets using `VLOOKUP` on State column
- Created `master_dataset.xlsx`

**Helper Columns Created**
- `Total_Generation`
- `Total_Renewable`
- `Total_Non_Renewable`
- `Pct_Renewable`

These simplified dashboard calculations in Power BI.

---

### 3️⃣ Data Visualization (Power BI)

Loaded `master_dataset.xlsx` into Power BI.

#### 📊 KPIs
- Total National Capacity (MW)
- Non-Renewable Share
- Average Renewable %

#### 🌍 Interactive Visuals
- Geographic Map → Total generation by state
- Stacked Bar Chart → Detailed energy mix
- Top 10 States Chart → Highest total generation
- Gauge → Renewable percentage
- Slicer → Dynamic state filtering

---

### 4️⃣ Mini Predictive Insight

**Goal:**  
Analyze relationship between economic wealth and energy generation.

**Method:**
- Excel `CORREL` function
- Python Scatter Plot (Matplotlib)
- Correlation Heatmap (Seaborn)

This helped evaluate whether wealthier states tend to generate more energy.

---

## 📊 Key Insights

- Top 10 states contribute a significant share of national generation.
- Heavy reliance on Coal in many high-output states.
- Certain states show strong Hydel (renewable) dominance.
- Preliminary correlation suggests a measurable relationship between income and energy capacity.

---

## 📂 Project Structure

```
/data
    Energy_India_2024.csv
    perCapitaIncome.csv
    master_dataset.xlsx

/powerbi
    Energy_Dashboard.pbix

/python_analysis
    analysis.ipynb

README.md
```

---

## 📈 Business Value

- Identifies renewable dependency across states
- Supports energy planning decisions
- Enables data-driven policy insights
- Provides scalable analytics framework

---

## 🚀 Future Improvements

- Add time-series trend analysis
- Integrate live energy datasets
- Build advanced forecasting models
- Renewable growth prediction analysis
- Policy impact simulation

---

## 👨‍💻 Author

Sameer Kashyap  
Data Analytics Enthusiast | BI Developer | AI & Automation Builder  

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.
