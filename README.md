# India State-Wise Energy Consumption Analysis

This project is an end-to-end data pipeline assignment that analyzes energy generation capacity across various states in India. The goal is to source, clean, visualize, and derive insights from multiple datasets, culminating in an interactive Power BI dashboard and a predictive analysis.


## 🛠️ Tech Stack & Tools

* **Data Sourcing:** Kaggle, data.gov.in
* **Data Cleaning:** Microsoft Excel (VLOOKUP, Pivot Tables, Formulas) & Python (Pandas)
* **Data Visualization:** Power BI (DAX, Measures, Slicers, Map, Gauge, Bar Charts)
* **Data Analysis:** Python (Matplotlib, Seaborn, Pandas) & Microsoft Excel (CORREL function)

---

## ⚙️ Project Workflow (Data Pipeline)

This project followed a systematic 4-step data pipeline:

### 1. Data Sourcing
* **Energy Dataset:** `Energy_India_2024.csv` (from Kaggle) - Provided state-wise installed capacity for all energy types (Coal, Gas, Nuclear, Hydel, Renewable).
* **Income Dataset:** `perCapitaIncome.csv` (from Kaggle) - Provided state-wise per capita income data for correlation analysis.

### 2. Data Cleaning & Preparation (in Excel)
* **Main Energy File:**
    * Renamed columns for clarity (e.g., `State/Union Territory` to `State`).
    * Used "Find & Replace" to convert `'-'` to `0` for calculations.
    * Checked for duplicates using Pivot Tables.
* **Income File:**
    * Filtered the dataset to isolate the most recent year (2012) for a relevant comparison.
    * Saved this filtered data as `cleaned_income.xlsx`.
* **Data Aggregation:**
    * Combined the two clean datasets into a single `master_dataset.xlsx` using **VLOOKUP** in Excel, matching on the `State` column.
    * Created new "helper columns" (`Total_Generation`, `Total_Renewable`, `Total_Non_Renewable`, `Pct_Renewable`) to simplify Power BI visualizations.

### 3. Data Visualization (in Power BI)
* Loaded the `master_dataset.xlsx` into Power BI.
* **KPIs:** Created card and gauge visuals for key metrics like "Total National Capacity (MW)", "Non-Renewable Share", and "Average Renewable %".
* **Charts:** Built interactive visuals to analyze the data:
    * **Geographic Map:** To show `Total_Generation` by state.
    * **Stacked Bar Chart:** To show the detailed `Energy Mix` (Coal, Gas, Hydel, etc.) for each state.
    * **Slicer:** Added a dropdown slicer to filter the entire dashboard by `State`.

### 4. Mini Predictive Insight (Analysis)
* **Goal:** To determine if there is a relationship between a state's wealth and its energy capacity.
* **Method 2 (Python):** Used Matplotlib/Seaborn to create a **Scatter Plot** and **Heatmap** to visually confirm the correlation.

---

## 💡 Key Insights

* **Top 10 States:** A bar chart was created to identify the top 10 states by total energy generation.
* **Energy Mix:** The stacked bar chart revealed a heavy reliance on `Coal` for many of the top-generating states, while other states (like Himachal Pradesh) showed a high percentage of `Hydel` (renewable) power.
