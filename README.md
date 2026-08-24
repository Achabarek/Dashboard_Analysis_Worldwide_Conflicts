# Worldwide Conflicts Analysis

## Introduction

This project analyzes worldwide conflict data using Python, Pandas, Altair, and Streamlit.

The analysis combines exploratory data analysis, descriptive analysis, and relationship analysis to investigate
patterns in conflict duration, outcomes, human impact, economic loss, ceasefires, sanctions, UN involvement,
and refugee displacement.

## Dataset

The project uses the **Global War and Conflict Impact Dataset (1950–2024)**, available on Kaggle.

The dataset contains conflict-level information covering the period from 1950 to 2024. 


### Dataset Variables

The dataset contains 30 variables grouped into the following categories:

- **Conflict participants:** `Country_A`, `Country_B`
- **Conflict characteristics:** `Conflict_Type`, `Year`, `Duration_Days`
- **Human impact:** `Military_Deaths_A`, `Military_Deaths_B`, `Civilian_Deaths`, `Refugees_Millions`
- **Economic and demographic factors:** `Economic_Loss_USD_Billions`, `Population_A_Millions`,
`Population_B_Millions`, `GDP_A_Billions`, `GDP_B_Billions`
- **Military activity:** `Weapons_Used`, `Air_Strikes`, `Naval_Battles`
- **International involvement:** `Alliance_A`, `Alliance_B`, `Sanctions`, `UN_Involvement`
- **Conflict resolution:** `Ceasefire`, `Outcome`
- **Geographic and environmental factors:** `Latitude`, `Longitude`, `Terrain_Type`, `Climate_Zone`,
`Temperature_Avg_C`, `Rainfall_mm`
- **Resource factors:** `Resource_Dispute`

The project focuses on some of these variables for the descriptive and relationship analyses presented in the dashboard.

## Analysis Approach

The analysis follows three main stages:

```text
                    Dataset
                       │
                       ▼
             Exploratory Analysis
                       │
                       ▼
      1. Exploratory Data Analysis
         └── Jupyter Notebook
             ├─ Dataset structure
             ├─ Data types
             ├─ Missing values
             ├─ Duplicates
             └─ Distributions
                       │
                       ▼
      2. Descriptive Analysis
         └── What does the dataset contain?
             ├─ Conflicts per year
             ├─ Conflict types
             ├─ Average civilian deaths by conflict type
             ├─ Average economic loss by conflict type
             ├─ Ceasefire counts
             └─ Sanctions counts
                       │
                       ▼
      3. Relationship Analysis
         └── How are variables associated?
             ├─ Ceasefire ↔ Duration
             ├─ Sanctions ↔ Outcome
             ├─ UN involvement ↔ Outcome
             └─ Conflict type ↔ Refugees
                       │
                       ▼
             Streamlit Dashboard
             

### 1. Exploratory Data Analysis

The dataset is initially explored in a Jupyter Notebook to understand its structure, variables, data types, missing values,
duplicates, and distributions before performing further analysis.

### 2. Descriptive Analysis

The Streamlit dashboard summarizes the main characteristics of the conflict data:

- Number of conflicts per year
- Distribution of conflict types
- Average civilian deaths by conflict type
- Average economic loss by conflict type
- Number of conflicts with and without ceasefires
- Number of conflicts with and without sanctions
- Countries with the highest number of conflicts with a ceasefire

### 3. Relationship Analysis

The detailed analysis investigates differences in conflict characteristics and outcomes across groups:

- **Ceasefire ↔ Conflict duration** — comparison of average conflict duration between conflicts with and without a ceasefire
- **Sanctions ↔ Conflict outcome** — comparison of outcome distributions between conflicts with and without sanctions
- **UN involvement ↔ Conflict outcome** — comparison of outcome distributions between conflicts with and without UN involvement
- **Conflict type ↔ Refugee displacement** — comparison of average refugee displacement across conflict types

## Technologies

- Python
- Pandas
- Altair
- Streamlit
- Jupyter Notebook

## Project Structure

```text
worldwide-conflicts-analysis/
│
├── app.py
├── overview.py
├── detailed_analysis.py
├── notebooks/
│   └── conflict_exploration.ipynb
├── data/
│   └── global_conflicts_dataset.csv
├── requirements.txt
├── .gitignore
└── README.md