# Bulldozer Price Prediction - Data Analysis & Machine Learning Project

## Description

This project aims to explore a Kaggle dataset related to bulldozer sales and to build a machine learning regression model to predict bulldozer prices. The dataset includes historical sales data and features that influence pricing. Data can
be downloaded from the following url : https://www.kaggle.com/competitions/bluebook-for-bulldozers/data .

---

## Table of Contents

1. [Dataset](#dataset)
2. [Tools and Technologies](#tools-and-technologies)
3. [Approach](#approach)
4. [Prerequisites](#prerequisites)
5. [How to Run the Project](#how-to-run-the-project)

---

## Dataset

### Key Columns Description

The dataset includes the following important features:

- **SalePrice**: Target variable representing the price of the bulldozer.
- **YearMade**: Year the bulldozer was manufactured.
- **ModelID**: Unique identifier for the bulldozer model.
- **UsageHours**: Number of hours the bulldozer has been used.
- **AuctioneerID**: Identifier for the auctioneer managing the sale.
- **MachineHoursCurrentMeter**: Current hour meter reading of the bulldozer.

For a full list of features and descriptions, refer to the `Data Dictionary.xlsx` file from the 
data folder.

---

## Tools and Technologies

This project uses:

- **Python** (3.x)
- **Jupyter Notebook**: Interactive environment for running code and visualizations
- **Key Libraries**:
  - Pandas: Data manipulation and analysis
  - Matplotlib and Seaborn: Data visualization
  - Scikit-learn: Machine learning modeling and evaluation
- **Secondary Libraries**:
  - joblib

---

## Approach

1. **Problem Definition**
2. **Data**
   - Loading data
3. **Exploratory Data Analysis (EDA):**

   - Analyzing feature distributions
   - Visualizing correlations and relationship between features and the target variable

4. **Feature Engineering:**

   - Creating new features from existing columns

5. **Pre-processing:**
   - Data type adjustments based on data interpretation
   - Categorical data encoding
   - Imputation of missing values or incoherent values
 

6. **Modeling, evaluation and experimentation:**

   - Models tested:
     - Random Forest Regressor
   - Metrics used: Negative Mean Squared Log Error (negative RMSLE)
   - Validation curves
   - Hyperparameter tuning

7. **Feature importance**
   - Identification and visualization of most important features and their relative
   importance
---


## Prerequisites

- Python 3.8 or later
- A virtual Python environment is recommended (via `venv` or `conda`)
- The following libraries must be installed:
  - pandas
  - matplotlib
  - numpy
  - joblib
  - scikit-learn
  - seaborn
- Jupyter Notebook to run the `bulldozers_price_regression.ipynb` file

---

## How to Run the Project

1. Clone the repository:

   ```bash
   git clone git@github.com:Dan-Popescu/Bulldozers_Price_Regression_Notebook.git
   cd Bulldozers_Price_Regression_Notebook
   ```

2. Activate the virtual environment:

   ```bash
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Download data from kaggle (https://www.kaggle.com/competitions/bluebook-for-bulldozers/data) and put it in the data folder
  

6. Launch the notebook:

   ```bash
   jupyter notebook bulldozers_price_regression.ipynb
   ```

7. Follow the steps in the notebook to execute the analysis and models.


